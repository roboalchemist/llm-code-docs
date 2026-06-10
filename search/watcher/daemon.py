"""Watchdog-based filesystem monitor for llm-code-docs.

Monitors the docs directory for markdown file changes and feeds events
into the ChangeQueue for debounced incremental indexing. Designed to
run as a long-lived daemon process.

Features:
    - Watches all .md files under docs/{llms-txt,github-scraped,web-scraped}
    - 5-second debounce for rapid changes (configurable)
    - Survives OpenSearch restarts (reconnects automatically)
    - Graceful shutdown on SIGINT/SIGTERM
    - Background threads for watching and processing
"""

import logging
import os
import signal
import sys
import threading
import time
from pathlib import Path
from typing import Any, Dict, Optional

from watchdog.events import (
    FileCreatedEvent,
    FileDeletedEvent,
    FileModifiedEvent,
    FileMovedEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer

from search import config
from search.watcher.indexer import ChangeEvent, ChangeProcessor, ChangeQueue, ChangeType

logger = logging.getLogger(__name__)


class MarkdownEventHandler(FileSystemEventHandler):
    """Watchdog event handler that filters for markdown files.

    Only processes events for .md files, converting them into ChangeEvent
    objects and placing them on the change queue.

    Args:
        queue: The ChangeQueue to send events to.
        docs_root: Root of the docs directory (used for path validation).
    """

    def __init__(self, queue: ChangeQueue, docs_root: Path):
        super().__init__()
        self.queue = queue
        self.docs_root = docs_root

    def _is_markdown(self, path: str) -> bool:
        """Check if a path is a markdown file."""
        return path.endswith(".md")

    def _is_in_category(self, path: str) -> bool:
        """Check if the path is under a known category directory."""
        try:
            rel = Path(path).relative_to(self.docs_root)
            parts = rel.parts
            if parts and parts[0] in config.CATEGORIES:
                return True
        except ValueError:
            pass
        return False

    def _should_process(self, path: str) -> bool:
        """Check if an event path should be processed."""
        return self._is_markdown(path) and self._is_in_category(path)

    def on_created(self, event):
        """Handle file creation."""
        if event.is_directory or not self._should_process(event.src_path):
            return
        logger.debug(f"File created: {event.src_path}")
        self.queue.put(
            ChangeEvent(Path(event.src_path), ChangeType.CREATED)
        )

    def on_modified(self, event):
        """Handle file modification."""
        if event.is_directory or not self._should_process(event.src_path):
            return
        logger.debug(f"File modified: {event.src_path}")
        self.queue.put(
            ChangeEvent(Path(event.src_path), ChangeType.MODIFIED)
        )

    def on_deleted(self, event):
        """Handle file deletion."""
        if event.is_directory or not self._should_process(event.src_path):
            return
        logger.debug(f"File deleted: {event.src_path}")
        self.queue.put(
            ChangeEvent(Path(event.src_path), ChangeType.DELETED)
        )

    def on_moved(self, event):
        """Handle file moves (treated as delete + create)."""
        if event.is_directory:
            return

        # Source is deleted
        if self._should_process(event.src_path):
            logger.debug(f"File moved from: {event.src_path}")
            self.queue.put(
                ChangeEvent(Path(event.src_path), ChangeType.DELETED)
            )

        # Destination is created (if still a markdown file in docs)
        if self._should_process(event.dest_path):
            logger.debug(f"File moved to: {event.dest_path}")
            self.queue.put(
                ChangeEvent(Path(event.dest_path), ChangeType.CREATED)
            )


class DocsWatcher:
    """Main watcher daemon that orchestrates filesystem monitoring and indexing.

    Combines watchdog Observer (filesystem events) with ChangeProcessor
    (queue consumer + indexer). Handles graceful startup and shutdown.

    Args:
        docs_root: Root directory to watch. Defaults to config.DOCS_ROOT.
        debounce_seconds: Debounce window for rapid changes (default: 5s).
        poll_interval: How often the processor checks the queue (default: 1s).
        on_changes_processed: Optional callback for post-processing hooks.

    Example:
        >>> watcher = DocsWatcher(debounce_seconds=5)
        >>> watcher.start()
        >>> # ... runs until stop() is called or signal received ...
        >>> watcher.stop()
    """

    def __init__(
        self,
        docs_root: Optional[Path] = None,
        debounce_seconds: float = 5.0,
        poll_interval: float = 1.0,
        on_changes_processed=None,
    ):
        self.docs_root = docs_root or config.DOCS_ROOT
        self.debounce_seconds = debounce_seconds
        self.poll_interval = poll_interval

        # Core components
        self.queue = ChangeQueue(debounce_seconds=debounce_seconds)
        self.handler = MarkdownEventHandler(self.queue, self.docs_root)
        self.processor = ChangeProcessor(
            queue=self.queue,
            docs_root=self.docs_root,
            poll_interval=poll_interval,
            on_changes_processed=on_changes_processed,
        )
        self.observer = Observer()

        # State
        self._running = False
        self._shutdown_event = threading.Event()

    def start(self) -> None:
        """Start the watcher daemon.

        Begins filesystem monitoring and change processing.
        Non-blocking: starts background threads and returns immediately.
        """
        if self._running:
            logger.warning("DocsWatcher is already running")
            return

        # Validate docs root exists
        if not self.docs_root.exists():
            raise FileNotFoundError(
                f"Docs root does not exist: {self.docs_root}"
            )

        logger.info(f"Starting DocsWatcher on {self.docs_root}")
        logger.info(f"Debounce: {self.debounce_seconds}s, Poll: {self.poll_interval}s")

        # Schedule observer for docs root (recursive)
        self.observer.schedule(
            self.handler,
            str(self.docs_root),
            recursive=True,
        )

        # Start components
        self.observer.start()
        self.processor.start()
        self._running = True

        logger.info("DocsWatcher started successfully")

    def stop(self) -> None:
        """Stop the watcher daemon gracefully.

        Stops filesystem monitoring, drains remaining events, and
        shuts down the processing thread.
        """
        if not self._running:
            return

        logger.info("Stopping DocsWatcher...")
        self._running = False
        self._shutdown_event.set()

        # Stop observer first (no new events)
        self.observer.stop()
        self.observer.join(timeout=5)

        # Stop processor (processes remaining events)
        self.processor.stop(timeout=10)

        logger.info("DocsWatcher stopped")

    def run_forever(self) -> None:
        """Start the watcher and block until shutdown signal.

        Installs signal handlers for SIGINT and SIGTERM for graceful
        shutdown. This is the primary entry point for running as a
        standalone daemon.
        """
        # Install signal handlers
        original_sigint = signal.getsignal(signal.SIGINT)
        original_sigterm = signal.getsignal(signal.SIGTERM)

        def _signal_handler(signum, frame):
            sig_name = signal.Signals(signum).name
            logger.info(f"Received {sig_name}, shutting down...")
            self.stop()

        signal.signal(signal.SIGINT, _signal_handler)
        signal.signal(signal.SIGTERM, _signal_handler)

        try:
            self.start()

            # Block until shutdown
            while self._running:
                self._shutdown_event.wait(timeout=1.0)
        finally:
            # Restore original handlers
            signal.signal(signal.SIGINT, original_sigint)
            signal.signal(signal.SIGTERM, original_sigterm)

            if self._running:
                self.stop()

    @property
    def is_running(self) -> bool:
        """Whether the watcher is currently running."""
        return self._running

    @property
    def stats(self) -> Dict[str, Any]:
        """Get current watcher statistics."""
        return {
            "running": self._running,
            "docs_root": str(self.docs_root),
            "debounce_seconds": self.debounce_seconds,
            "pending_events": self.queue.pending_count,
            "processor": self.processor.stats,
        }


# =============================================================================
# Module-level convenience functions
# =============================================================================

_watcher: Optional[DocsWatcher] = None


def start_watcher(
    docs_root: Optional[Path] = None,
    debounce_seconds: float = 5.0,
    poll_interval: float = 1.0,
) -> DocsWatcher:
    """Start the global watcher instance.

    Args:
        docs_root: Root directory to watch (default: config.DOCS_ROOT).
        debounce_seconds: Debounce window for rapid changes.
        poll_interval: Queue polling interval.

    Returns:
        The DocsWatcher instance.
    """
    global _watcher
    if _watcher and _watcher.is_running:
        logger.warning("Watcher is already running")
        return _watcher

    _watcher = DocsWatcher(
        docs_root=docs_root,
        debounce_seconds=debounce_seconds,
        poll_interval=poll_interval,
    )
    _watcher.start()
    return _watcher


def stop_watcher() -> None:
    """Stop the global watcher instance."""
    global _watcher
    if _watcher:
        _watcher.stop()
        _watcher = None


# =============================================================================
# CLI Entry Point
# =============================================================================

def main():
    """CLI entry point for running the watcher daemon."""
    import argparse

    parser = argparse.ArgumentParser(
        description="File watcher daemon for llm-code-docs incremental indexing"
    )
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=None,
        help=f"Docs directory to watch (default: {config.DOCS_ROOT})",
    )
    parser.add_argument(
        "--debounce",
        type=float,
        default=5.0,
        help="Debounce seconds for rapid changes (default: 5)",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=1.0,
        help="Queue poll interval in seconds (default: 1)",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging level (default: INFO)",
    )
    args = parser.parse_args()

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    watcher = DocsWatcher(
        docs_root=args.docs_root,
        debounce_seconds=args.debounce,
        poll_interval=args.poll_interval,
    )

    logger.info("Starting file watcher daemon...")
    watcher.run_forever()
    logger.info("File watcher daemon exited")


if __name__ == "__main__":
    main()

"""Change queue processor for incremental indexing.

This module processes filesystem change events, deduplicates them,
and triggers incremental indexing operations against OpenSearch.

The ChangeQueue collects events with debouncing to batch rapid changes.
The ChangeProcessor consumes the queue and performs the actual indexing.
"""

import logging
import threading
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set

logger = logging.getLogger(__name__)


class ChangeType(Enum):
    """Type of filesystem change."""
    CREATED = "created"
    MODIFIED = "modified"
    DELETED = "deleted"


@dataclass
class ChangeEvent:
    """Represents a single filesystem change event.

    Attributes:
        path: Absolute path to the changed file.
        change_type: Type of change (created, modified, deleted).
        timestamp: When the change was detected (monotonic clock).
    """
    path: Path
    change_type: ChangeType
    timestamp: float = field(default_factory=time.monotonic)

    def __repr__(self) -> str:
        return f"ChangeEvent({self.change_type.value}: {self.path.name})"


class ChangeQueue:
    """Thread-safe queue that collects and deduplicates change events.

    Implements a debounce mechanism: events are held for a configurable
    period before being released. If the same file changes again within
    the debounce window, the timer resets. This prevents redundant
    indexing during rapid file saves.

    Args:
        debounce_seconds: How long to wait after the last change before
            processing (default: 5 seconds per issue requirements).

    Example:
        >>> queue = ChangeQueue(debounce_seconds=5)
        >>> queue.put(ChangeEvent(Path("/docs/test.md"), ChangeType.MODIFIED))
        >>> # Wait for debounce...
        >>> events = queue.drain()
        >>> len(events) >= 0  # May be empty if still within debounce window
        True
    """

    def __init__(self, debounce_seconds: float = 5.0):
        self.debounce_seconds = debounce_seconds
        self._lock = threading.Lock()
        self._events: Dict[str, ChangeEvent] = {}
        self._ready_event = threading.Event()

    def put(self, event: ChangeEvent) -> None:
        """Add a change event to the queue.

        If an event for the same path already exists, it is replaced
        with the new event (resetting the debounce timer).

        Args:
            event: The change event to enqueue.
        """
        path_key = str(event.path)
        with self._lock:
            existing = self._events.get(path_key)

            # If file was created then modified, keep as created
            if (
                existing
                and existing.change_type == ChangeType.CREATED
                and event.change_type == ChangeType.MODIFIED
            ):
                event = ChangeEvent(
                    path=event.path,
                    change_type=ChangeType.CREATED,
                    timestamp=event.timestamp,
                )

            # If file was created then deleted, remove from queue entirely
            if (
                existing
                and existing.change_type == ChangeType.CREATED
                and event.change_type == ChangeType.DELETED
            ):
                del self._events[path_key]
                logger.debug(f"Cancelled create+delete for {event.path.name}")
                return

            self._events[path_key] = event
            logger.debug(f"Queued: {event}")

        # Signal that new events are available
        self._ready_event.set()

    def drain(self) -> List[ChangeEvent]:
        """Return all events that have passed the debounce window.

        Events whose timestamp is older than debounce_seconds are
        considered ready. Events still within the debounce window
        are kept in the queue.

        Returns:
            List of ready ChangeEvent objects, deduplicated by path.
        """
        now = time.monotonic()
        ready: List[ChangeEvent] = []

        with self._lock:
            still_pending: Dict[str, ChangeEvent] = {}

            for path_key, event in self._events.items():
                age = now - event.timestamp
                if age >= self.debounce_seconds:
                    ready.append(event)
                else:
                    still_pending[path_key] = event

            self._events = still_pending

            # Reset signal if no pending events remain
            if not self._events:
                self._ready_event.clear()

        return ready

    def wait(self, timeout: Optional[float] = None) -> bool:
        """Wait until events are available or timeout expires.

        Args:
            timeout: Maximum seconds to wait (None = wait forever).

        Returns:
            True if events are available, False if timed out.
        """
        return self._ready_event.wait(timeout=timeout)

    @property
    def pending_count(self) -> int:
        """Number of events currently in the queue."""
        with self._lock:
            return len(self._events)

    def clear(self) -> None:
        """Remove all events from the queue."""
        with self._lock:
            self._events.clear()
            self._ready_event.clear()


class ChangeProcessor:
    """Processes change events by invoking indexing operations.

    Runs in a background thread, periodically draining the change queue
    and batching events into efficient indexing operations. Groups changes
    by type (create/modify vs delete) for batch processing.

    Args:
        queue: The ChangeQueue to consume events from.
        docs_root: Root directory of the documentation tree.
        poll_interval: How often to check for ready events (seconds).
        on_changes_processed: Optional callback invoked after processing
            a batch of changes, receiving a dict of stats.

    Example:
        >>> queue = ChangeQueue()
        >>> processor = ChangeProcessor(queue, Path("/docs"))
        >>> processor.start()
        >>> # ... events are processed in background ...
        >>> processor.stop()
    """

    def __init__(
        self,
        queue: ChangeQueue,
        docs_root: Path,
        poll_interval: float = 1.0,
        on_changes_processed: Optional[Callable[[Dict[str, Any]], None]] = None,
    ):
        self.queue = queue
        self.docs_root = docs_root
        self.poll_interval = poll_interval
        self.on_changes_processed = on_changes_processed

        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

        # Statistics
        self._stats_lock = threading.Lock()
        self._stats: Dict[str, int] = {
            "files_created": 0,
            "files_modified": 0,
            "files_deleted": 0,
            "batches_processed": 0,
            "errors": 0,
        }

    def start(self) -> None:
        """Start the background processing thread."""
        if self._thread and self._thread.is_alive():
            logger.warning("ChangeProcessor is already running")
            return

        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run,
            name="change-processor",
            daemon=True,
        )
        self._thread.start()
        logger.info("ChangeProcessor started")

    def stop(self, timeout: float = 10.0) -> None:
        """Stop the background processing thread.

        Args:
            timeout: Maximum seconds to wait for the thread to finish.
        """
        self._stop_event.set()
        # Wake up the queue wait
        self.queue._ready_event.set()

        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=timeout)
            if self._thread.is_alive():
                logger.warning("ChangeProcessor did not stop within timeout")
        logger.info("ChangeProcessor stopped")

    @property
    def is_running(self) -> bool:
        """Whether the processing thread is currently running."""
        return self._thread is not None and self._thread.is_alive()

    @property
    def stats(self) -> Dict[str, int]:
        """Get current processing statistics."""
        with self._stats_lock:
            return dict(self._stats)

    def _run(self) -> None:
        """Main processing loop."""
        logger.info("ChangeProcessor loop started")

        while not self._stop_event.is_set():
            # Wait for events with timeout so we can check stop_event
            self.queue.wait(timeout=self.poll_interval)

            if self._stop_event.is_set():
                break

            # Drain ready events
            events = self.queue.drain()
            if not events:
                continue

            # Process the batch
            try:
                self._process_batch(events)
            except Exception as e:
                logger.error(f"Error processing change batch: {e}", exc_info=True)
                with self._stats_lock:
                    self._stats["errors"] += 1

        # Process any remaining events on shutdown
        remaining = self.queue.drain()
        if remaining:
            try:
                self._process_batch(remaining)
            except Exception as e:
                logger.error(f"Error processing final batch: {e}", exc_info=True)

        logger.info("ChangeProcessor loop ended")

    def _process_batch(self, events: List[ChangeEvent]) -> None:
        """Process a batch of change events.

        Groups events by type and performs batch operations:
        - Deleted files: Remove from index by path
        - Created/modified files: Re-index with new content

        Args:
            events: List of deduplicated change events.
        """
        created: List[ChangeEvent] = []
        modified: List[ChangeEvent] = []
        deleted: List[ChangeEvent] = []

        for event in events:
            if event.change_type == ChangeType.CREATED:
                created.append(event)
            elif event.change_type == ChangeType.MODIFIED:
                modified.append(event)
            elif event.change_type == ChangeType.DELETED:
                deleted.append(event)

        logger.info(
            f"Processing batch: {len(created)} created, "
            f"{len(modified)} modified, {len(deleted)} deleted"
        )

        batch_stats = {
            "created": len(created),
            "modified": len(modified),
            "deleted": len(deleted),
            "errors": [],
        }

        # Process deletions
        if deleted:
            self._process_deletions(deleted, batch_stats)

        # Process creates and modifications
        if created or modified:
            self._process_upserts(created + modified, batch_stats)

        # Update statistics
        with self._stats_lock:
            self._stats["files_created"] += len(created)
            self._stats["files_modified"] += len(modified)
            self._stats["files_deleted"] += len(deleted)
            self._stats["batches_processed"] += 1
            if batch_stats["errors"]:
                self._stats["errors"] += len(batch_stats["errors"])

        # Invoke callback
        if self.on_changes_processed:
            try:
                self.on_changes_processed(batch_stats)
            except Exception as e:
                logger.warning(f"on_changes_processed callback error: {e}")

        logger.info(f"Batch complete: {batch_stats}")

    def _process_deletions(
        self, events: List[ChangeEvent], batch_stats: Dict[str, Any]
    ) -> None:
        """Delete documents from the index for removed files.

        Args:
            events: List of deletion events.
            batch_stats: Dictionary to accumulate stats into.
        """
        from search.opensearch.client import get_client

        try:
            client = get_client()

            if not client.index_exists():
                logger.warning("Index does not exist, skipping deletions")
                return

            for event in events:
                try:
                    path_str = str(event.path)
                    query = {"term": {"path": path_str}}
                    deleted_count = client.bulk_delete_by_query(query)
                    logger.info(
                        f"Deleted {deleted_count} chunks for {event.path.name}"
                    )
                except Exception as e:
                    error_msg = f"Error deleting {event.path}: {e}"
                    logger.error(error_msg)
                    batch_stats["errors"].append(error_msg)

        except Exception as e:
            error_msg = f"Error connecting to OpenSearch for deletions: {e}"
            logger.error(error_msg)
            batch_stats["errors"].append(error_msg)

    def _process_upserts(
        self, events: List[ChangeEvent], batch_stats: Dict[str, Any]
    ) -> None:
        """Index new or modified files.

        For modified files, deletes existing documents first, then
        re-indexes with fresh content. Uses the OpenSearchIndexBuilder
        pipeline for consistency.

        Args:
            events: List of create/modify events.
            batch_stats: Dictionary to accumulate stats into.
        """
        from search.opensearch.builder import OpenSearchIndexBuilder
        from search.opensearch.client import get_client
        from search.indexer.scanner import DocumentInfo

        try:
            client = get_client()

            if not client.index_exists():
                logger.warning("Index does not exist, skipping upserts")
                return

            # Filter to files that still exist (might have been deleted since event)
            valid_events = [e for e in events if e.path.exists()]

            if not valid_events:
                return

            # Delete existing documents for modified files
            modified_events = [
                e for e in valid_events
                if e.change_type == ChangeType.MODIFIED
            ]
            if modified_events:
                for event in modified_events:
                    try:
                        query = {"term": {"path": str(event.path)}}
                        client.bulk_delete_by_query(query)
                    except Exception as e:
                        logger.warning(
                            f"Error deleting old docs for {event.path.name}: {e}"
                        )

            # Build DocumentInfo objects for indexing
            doc_infos = []
            for event in valid_events:
                doc_info = self._path_to_doc_info(event.path)
                if doc_info:
                    doc_infos.append(doc_info)

            if not doc_infos:
                return

            # Use builder for consistent indexing
            builder = OpenSearchIndexBuilder(client=client)
            result = builder._index_documents(doc_infos)

            chunks_indexed = result.get("chunks", 0)
            logger.info(f"Indexed {chunks_indexed} chunks from {len(doc_infos)} files")

            if result.get("errors"):
                batch_stats["errors"].extend(result["errors"])

            # Refresh index to make changes searchable immediately
            client.refresh_index()

        except Exception as e:
            error_msg = f"Error during upsert processing: {e}"
            logger.error(error_msg)
            batch_stats["errors"].append(error_msg)

    def _path_to_doc_info(self, file_path: Path) -> Optional["DocumentInfo"]:
        """Convert a file path to a DocumentInfo object.

        Derives category and framework from the directory structure:
        docs_root / category / framework / ...

        Args:
            file_path: Absolute path to the markdown file.

        Returns:
            DocumentInfo or None if the path cannot be resolved.
        """
        from search.indexer.scanner import DocumentInfo
        from search import config

        try:
            relative = file_path.relative_to(self.docs_root)
            parts = relative.parts

            if len(parts) < 2:
                logger.warning(f"Path too short to determine category/framework: {file_path}")
                return None

            category = parts[0]
            framework = parts[1]

            if category not in config.CATEGORIES:
                logger.warning(f"Unknown category '{category}' for {file_path}")
                return None

            return DocumentInfo(
                path=file_path,
                relative_path=str(relative),
                filename=file_path.name,
                category=category,
                framework=framework,
            )
        except ValueError:
            logger.warning(f"Path {file_path} is not under docs root {self.docs_root}")
            return None

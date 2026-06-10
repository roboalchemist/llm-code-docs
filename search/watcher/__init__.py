"""File watcher daemon for incremental indexing of llm-code-docs.

This module provides a watchdog-based filesystem monitor that detects
changes to markdown files in the docs directory and triggers incremental
indexing via the OpenSearch index builder.

Components:
    - daemon.py: Watchdog-based filesystem monitor with debouncing
    - indexer.py: Change queue processor that batches and indexes changes
"""

from search.watcher.daemon import DocsWatcher, start_watcher, stop_watcher
from search.watcher.indexer import ChangeEvent, ChangeQueue, ChangeProcessor

__all__ = [
    "DocsWatcher",
    "start_watcher",
    "stop_watcher",
    "ChangeEvent",
    "ChangeQueue",
    "ChangeProcessor",
]

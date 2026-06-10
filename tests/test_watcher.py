"""Tests for the file watcher daemon.

Tests cover:
    - ChangeQueue: debouncing, deduplication, event coalescing
    - ChangeProcessor: batch processing, error handling, statistics
    - MarkdownEventHandler: event filtering, path validation
    - DocsWatcher: integration of all components, lifecycle
    - End-to-end: filesystem changes trigger indexing (mocked)
"""

import os
import shutil
import tempfile
import time
import threading
from pathlib import Path
from unittest.mock import MagicMock, patch, call

import pytest

# Set test environment variables before importing config
os.environ.setdefault("OPENSEARCH_HOST", "localhost")
os.environ.setdefault("OPENSEARCH_PORT", "9200")
os.environ.setdefault("OPENSEARCH_INDEX_NAME", "test_llm_docs")
os.environ.setdefault("OPENSEARCH_PIPELINE_NAME", "test_pipeline")

from search.watcher.indexer import ChangeEvent, ChangeQueue, ChangeProcessor, ChangeType
from search.watcher.daemon import DocsWatcher, MarkdownEventHandler


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def docs_tree(tmp_path):
    """Create a temporary docs directory tree mimicking llm-code-docs structure."""
    docs_root = tmp_path / "docs"
    docs_root.mkdir()

    # Create category directories
    for category in ["llms-txt", "github-scraped", "web-scraped"]:
        cat_dir = docs_root / category
        cat_dir.mkdir()

        # Create a framework directory with a sample file
        fw_dir = cat_dir / "test-framework"
        fw_dir.mkdir()
        (fw_dir / "guide.md").write_text("# Test Guide\n\nSample content.")

    return docs_root


@pytest.fixture
def change_queue():
    """Create a ChangeQueue with a very short debounce for testing."""
    return ChangeQueue(debounce_seconds=0.1)


@pytest.fixture
def fast_queue():
    """Create a ChangeQueue with zero debounce for instant drain."""
    return ChangeQueue(debounce_seconds=0.0)


# =============================================================================
# ChangeQueue Tests
# =============================================================================


class TestChangeQueue:
    """Tests for the ChangeQueue debounce and deduplication logic."""

    def test_put_and_drain_after_debounce(self, change_queue):
        """Events are returned after the debounce window passes."""
        event = ChangeEvent(Path("/docs/test.md"), ChangeType.CREATED)
        change_queue.put(event)

        # Should be empty before debounce
        assert change_queue.drain() == []

        # Wait for debounce
        time.sleep(0.15)

        events = change_queue.drain()
        assert len(events) == 1
        assert events[0].path == Path("/docs/test.md")
        assert events[0].change_type == ChangeType.CREATED

    def test_deduplication_same_file(self, change_queue):
        """Multiple changes to the same file are deduplicated."""
        path = Path("/docs/test.md")

        change_queue.put(ChangeEvent(path, ChangeType.MODIFIED))
        change_queue.put(ChangeEvent(path, ChangeType.MODIFIED))
        change_queue.put(ChangeEvent(path, ChangeType.MODIFIED))

        time.sleep(0.15)
        events = change_queue.drain()

        # Should get exactly one event
        assert len(events) == 1
        assert events[0].change_type == ChangeType.MODIFIED

    def test_different_files_separate(self, fast_queue):
        """Different files produce separate events."""
        fast_queue.put(ChangeEvent(Path("/docs/a.md"), ChangeType.CREATED))
        fast_queue.put(ChangeEvent(Path("/docs/b.md"), ChangeType.MODIFIED))

        events = fast_queue.drain()
        assert len(events) == 2
        paths = {str(e.path) for e in events}
        assert paths == {"/docs/a.md", "/docs/b.md"}

    def test_create_then_modify_stays_created(self, fast_queue):
        """If a file is created then modified, it should remain as CREATED."""
        path = Path("/docs/new.md")

        fast_queue.put(ChangeEvent(path, ChangeType.CREATED))
        fast_queue.put(ChangeEvent(path, ChangeType.MODIFIED))

        events = fast_queue.drain()
        assert len(events) == 1
        assert events[0].change_type == ChangeType.CREATED

    def test_create_then_delete_cancels(self, fast_queue):
        """If a file is created then deleted, it should be removed entirely."""
        path = Path("/docs/temp.md")

        fast_queue.put(ChangeEvent(path, ChangeType.CREATED))
        fast_queue.put(ChangeEvent(path, ChangeType.DELETED))

        events = fast_queue.drain()
        assert len(events) == 0

    def test_pending_count(self, fast_queue):
        """pending_count reflects the number of queued events."""
        assert fast_queue.pending_count == 0

        fast_queue.put(ChangeEvent(Path("/a.md"), ChangeType.CREATED))
        assert fast_queue.pending_count == 1

        fast_queue.put(ChangeEvent(Path("/b.md"), ChangeType.CREATED))
        assert fast_queue.pending_count == 2

        fast_queue.drain()
        assert fast_queue.pending_count == 0

    def test_clear(self, fast_queue):
        """clear() empties the queue."""
        fast_queue.put(ChangeEvent(Path("/a.md"), ChangeType.CREATED))
        fast_queue.put(ChangeEvent(Path("/b.md"), ChangeType.CREATED))
        assert fast_queue.pending_count == 2

        fast_queue.clear()
        assert fast_queue.pending_count == 0
        assert fast_queue.drain() == []

    def test_wait_returns_true_when_events_available(self, fast_queue):
        """wait() returns True when events are available."""
        # Put event in a separate thread
        def add_event():
            time.sleep(0.05)
            fast_queue.put(ChangeEvent(Path("/a.md"), ChangeType.CREATED))

        t = threading.Thread(target=add_event)
        t.start()

        result = fast_queue.wait(timeout=1.0)
        assert result is True
        t.join()

    def test_wait_returns_false_on_timeout(self):
        """wait() returns False when it times out."""
        queue = ChangeQueue(debounce_seconds=0.0)
        result = queue.wait(timeout=0.05)
        assert result is False

    def test_debounce_resets_on_new_event(self):
        """Debounce timer resets when the same file changes again."""
        queue = ChangeQueue(debounce_seconds=0.2)
        path = Path("/docs/test.md")

        queue.put(ChangeEvent(path, ChangeType.MODIFIED))
        time.sleep(0.1)

        # Put another event for same file - resets debounce
        queue.put(ChangeEvent(path, ChangeType.MODIFIED))

        # At 0.15s from last event, should still be pending
        time.sleep(0.1)
        events = queue.drain()
        assert len(events) == 0

        # After full debounce from last event
        time.sleep(0.15)
        events = queue.drain()
        assert len(events) == 1


# =============================================================================
# MarkdownEventHandler Tests
# =============================================================================


class TestMarkdownEventHandler:
    """Tests for the watchdog event handler."""

    def test_filters_markdown_files(self, docs_tree, fast_queue):
        """Only .md files trigger events."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        # Markdown file should be processed
        md_event = MagicMock()
        md_event.is_directory = False
        md_event.src_path = str(docs_tree / "llms-txt" / "test" / "guide.md")
        handler.on_created(md_event)
        assert fast_queue.pending_count == 1

        # Non-markdown file should be ignored
        py_event = MagicMock()
        py_event.is_directory = False
        py_event.src_path = str(docs_tree / "llms-txt" / "test" / "script.py")
        handler.on_created(py_event)
        assert fast_queue.pending_count == 1  # Still 1

    def test_filters_directories(self, docs_tree, fast_queue):
        """Directory events are ignored."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        dir_event = MagicMock()
        dir_event.is_directory = True
        dir_event.src_path = str(docs_tree / "llms-txt" / "new-fw")
        handler.on_created(dir_event)
        assert fast_queue.pending_count == 0

    def test_filters_unknown_categories(self, docs_tree, fast_queue):
        """Files outside known category directories are ignored."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(docs_tree / "unknown-category" / "test" / "file.md")
        handler.on_created(event)
        assert fast_queue.pending_count == 0

    def test_on_created_event(self, docs_tree, fast_queue):
        """on_created produces a CREATED change event."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(docs_tree / "github-scraped" / "fastapi" / "intro.md")
        handler.on_created(event)

        events = fast_queue.drain()
        assert len(events) == 1
        assert events[0].change_type == ChangeType.CREATED

    def test_on_modified_event(self, docs_tree, fast_queue):
        """on_modified produces a MODIFIED change event."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(docs_tree / "llms-txt" / "test-framework" / "guide.md")
        handler.on_modified(event)

        events = fast_queue.drain()
        assert len(events) == 1
        assert events[0].change_type == ChangeType.MODIFIED

    def test_on_deleted_event(self, docs_tree, fast_queue):
        """on_deleted produces a DELETED change event."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(docs_tree / "web-scraped" / "test-framework" / "guide.md")
        handler.on_deleted(event)

        events = fast_queue.drain()
        assert len(events) == 1
        assert events[0].change_type == ChangeType.DELETED

    def test_on_moved_creates_delete_and_create(self, docs_tree, fast_queue):
        """File moves generate a DELETE for source and CREATE for dest."""
        handler = MarkdownEventHandler(fast_queue, docs_tree)

        event = MagicMock()
        event.is_directory = False
        event.src_path = str(docs_tree / "llms-txt" / "old" / "file.md")
        event.dest_path = str(docs_tree / "llms-txt" / "new" / "file.md")
        handler.on_moved(event)

        events = fast_queue.drain()
        assert len(events) == 2
        types = {e.change_type for e in events}
        assert types == {ChangeType.DELETED, ChangeType.CREATED}


# =============================================================================
# ChangeProcessor Tests
# =============================================================================


class TestChangeProcessor:
    """Tests for the background change processor."""

    def test_start_and_stop(self, fast_queue, docs_tree):
        """Processor starts and stops cleanly."""
        processor = ChangeProcessor(fast_queue, docs_tree, poll_interval=0.05)
        processor.start()
        assert processor.is_running is True

        processor.stop(timeout=2.0)
        assert processor.is_running is False

    def test_processes_events_in_background(self, docs_tree):
        """Processor drains events and calls processing methods."""
        queue = ChangeQueue(debounce_seconds=0.05)
        processed_batches = []

        def on_processed(stats):
            processed_batches.append(stats)

        processor = ChangeProcessor(
            queue, docs_tree, poll_interval=0.05, on_changes_processed=on_processed
        )

        with patch.object(processor, '_process_deletions') as mock_del, \
             patch.object(processor, '_process_upserts') as mock_ups:

            processor.start()

            # Add events
            queue.put(ChangeEvent(Path("/docs/a.md"), ChangeType.CREATED))
            queue.put(ChangeEvent(Path("/docs/b.md"), ChangeType.DELETED))

            # Wait for processing
            time.sleep(0.3)
            processor.stop(timeout=2.0)

        # Verify callback was invoked
        assert len(processed_batches) >= 1
        total_created = sum(b.get("created", 0) for b in processed_batches)
        total_deleted = sum(b.get("deleted", 0) for b in processed_batches)
        assert total_created == 1
        assert total_deleted == 1

    def test_statistics_accumulate(self, docs_tree):
        """Stats are accumulated across batches."""
        queue = ChangeQueue(debounce_seconds=0.05)
        processor = ChangeProcessor(queue, docs_tree, poll_interval=0.05)

        with patch.object(processor, '_process_deletions'), \
             patch.object(processor, '_process_upserts'):

            processor.start()

            queue.put(ChangeEvent(Path("/docs/a.md"), ChangeType.CREATED))
            queue.put(ChangeEvent(Path("/docs/b.md"), ChangeType.MODIFIED))
            queue.put(ChangeEvent(Path("/docs/c.md"), ChangeType.DELETED))

            time.sleep(0.3)
            processor.stop(timeout=2.0)

        stats = processor.stats
        assert stats["files_created"] == 1
        assert stats["files_modified"] == 1
        assert stats["files_deleted"] == 1
        assert stats["batches_processed"] >= 1

    def test_path_to_doc_info_valid(self, docs_tree):
        """_path_to_doc_info correctly parses docs structure."""
        queue = ChangeQueue(debounce_seconds=0.0)
        processor = ChangeProcessor(queue, docs_tree)

        file_path = docs_tree / "github-scraped" / "fastapi" / "intro.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("# Test")

        doc_info = processor._path_to_doc_info(file_path)
        assert doc_info is not None
        assert doc_info.category == "github-scraped"
        assert doc_info.framework == "fastapi"
        assert doc_info.filename == "intro.md"

    def test_path_to_doc_info_unknown_category(self, docs_tree):
        """_path_to_doc_info returns None for unknown categories."""
        queue = ChangeQueue(debounce_seconds=0.0)
        processor = ChangeProcessor(queue, docs_tree)

        file_path = docs_tree / "unknown" / "test" / "file.md"
        doc_info = processor._path_to_doc_info(file_path)
        assert doc_info is None

    def test_path_to_doc_info_outside_root(self, docs_tree):
        """_path_to_doc_info returns None for paths outside docs root."""
        queue = ChangeQueue(debounce_seconds=0.0)
        processor = ChangeProcessor(queue, docs_tree)

        file_path = Path("/totally/different/path.md")
        doc_info = processor._path_to_doc_info(file_path)
        assert doc_info is None

    def test_process_deletions_calls_client(self, docs_tree):
        """_process_deletions issues delete queries to OpenSearch client."""
        queue = ChangeQueue(debounce_seconds=0.0)
        processor = ChangeProcessor(queue, docs_tree)

        events = [
            ChangeEvent(Path("/docs/old.md"), ChangeType.DELETED),
        ]
        batch_stats = {"errors": []}

        mock_client = MagicMock()
        mock_client.index_exists.return_value = True
        mock_client.bulk_delete_by_query.return_value = 3

        with patch("search.opensearch.client.get_client", return_value=mock_client):
            processor._process_deletions(events, batch_stats)

        mock_client.bulk_delete_by_query.assert_called_once()
        assert batch_stats["errors"] == []

    def test_process_deletions_handles_missing_index(self, docs_tree):
        """_process_deletions handles the case where index doesn't exist."""
        queue = ChangeQueue(debounce_seconds=0.0)
        processor = ChangeProcessor(queue, docs_tree)

        events = [ChangeEvent(Path("/docs/old.md"), ChangeType.DELETED)]
        batch_stats = {"errors": []}

        mock_client = MagicMock()
        mock_client.index_exists.return_value = False

        with patch("search.opensearch.client.get_client", return_value=mock_client):
            processor._process_deletions(events, batch_stats)

        mock_client.bulk_delete_by_query.assert_not_called()

    def test_error_handling_in_processing(self, docs_tree):
        """Errors during processing are caught and recorded."""
        queue = ChangeQueue(debounce_seconds=0.05)
        processor = ChangeProcessor(queue, docs_tree, poll_interval=0.05)

        with patch.object(processor, '_process_batch', side_effect=RuntimeError("test error")):
            processor.start()

            queue.put(ChangeEvent(Path("/docs/a.md"), ChangeType.CREATED))
            time.sleep(0.3)
            processor.stop(timeout=2.0)

        assert processor.stats["errors"] >= 1


# =============================================================================
# DocsWatcher Tests
# =============================================================================


class TestDocsWatcher:
    """Tests for the main watcher daemon."""

    def test_start_and_stop(self, docs_tree):
        """Watcher starts and stops cleanly."""
        watcher = DocsWatcher(docs_root=docs_tree, debounce_seconds=0.1)
        watcher.start()
        assert watcher.is_running is True

        watcher.stop()
        assert watcher.is_running is False

    def test_start_nonexistent_root_raises(self, tmp_path):
        """Starting with a nonexistent docs root raises FileNotFoundError."""
        watcher = DocsWatcher(docs_root=tmp_path / "nonexistent")
        with pytest.raises(FileNotFoundError):
            watcher.start()

    def test_double_start_is_safe(self, docs_tree):
        """Starting twice doesn't create duplicate watchers."""
        watcher = DocsWatcher(docs_root=docs_tree, debounce_seconds=0.1)
        watcher.start()
        watcher.start()  # Should warn but not crash
        assert watcher.is_running is True
        watcher.stop()

    def test_double_stop_is_safe(self, docs_tree):
        """Stopping twice doesn't crash."""
        watcher = DocsWatcher(docs_root=docs_tree, debounce_seconds=0.1)
        watcher.start()
        watcher.stop()
        watcher.stop()  # Should be no-op

    def test_stats_property(self, docs_tree):
        """stats returns expected structure."""
        watcher = DocsWatcher(docs_root=docs_tree, debounce_seconds=5.0)
        stats = watcher.stats

        assert stats["running"] is False
        assert stats["docs_root"] == str(docs_tree)
        assert stats["debounce_seconds"] == 5.0
        assert "pending_events" in stats
        assert "processor" in stats

    def test_detects_new_file(self, docs_tree):
        """Watcher detects when a new markdown file is created."""
        processed = []

        def on_processed(stats):
            processed.append(stats)

        watcher = DocsWatcher(
            docs_root=docs_tree,
            debounce_seconds=0.1,
            poll_interval=0.05,
            on_changes_processed=on_processed,
        )

        with patch.object(ChangeProcessor, '_process_deletions'), \
             patch.object(ChangeProcessor, '_process_upserts'):

            watcher.start()
            time.sleep(0.2)  # Let observer settle

            # Create a new markdown file
            new_file = docs_tree / "llms-txt" / "test-framework" / "new-doc.md"
            new_file.write_text("# New Document\n\nFresh content.")

            # Wait for detection + debounce + processing
            time.sleep(0.5)
            watcher.stop()

        # Should have detected the creation
        assert len(processed) >= 1
        total_created = sum(p.get("created", 0) for p in processed)
        assert total_created >= 1

    def test_detects_modified_file(self, docs_tree):
        """Watcher detects when an existing markdown file is modified."""
        processed = []

        def on_processed(stats):
            processed.append(stats)

        watcher = DocsWatcher(
            docs_root=docs_tree,
            debounce_seconds=0.1,
            poll_interval=0.05,
            on_changes_processed=on_processed,
        )

        with patch.object(ChangeProcessor, '_process_deletions'), \
             patch.object(ChangeProcessor, '_process_upserts'):

            watcher.start()
            time.sleep(0.2)  # Let observer settle

            # Modify an existing file
            existing_file = docs_tree / "llms-txt" / "test-framework" / "guide.md"
            existing_file.write_text("# Updated Guide\n\nModified content.")

            # Wait for detection + debounce + processing
            time.sleep(0.5)
            watcher.stop()

        # Should have detected the modification
        assert len(processed) >= 1

    def test_detects_deleted_file(self, docs_tree):
        """Watcher detects when a markdown file is deleted."""
        processed = []

        def on_processed(stats):
            processed.append(stats)

        watcher = DocsWatcher(
            docs_root=docs_tree,
            debounce_seconds=0.1,
            poll_interval=0.05,
            on_changes_processed=on_processed,
        )

        with patch.object(ChangeProcessor, '_process_deletions'), \
             patch.object(ChangeProcessor, '_process_upserts'):

            watcher.start()
            time.sleep(0.2)  # Let observer settle

            # Delete a file
            target = docs_tree / "github-scraped" / "test-framework" / "guide.md"
            target.unlink()

            # Wait for detection + debounce + processing
            time.sleep(0.5)
            watcher.stop()

        # Should have detected the deletion
        assert len(processed) >= 1
        total_deleted = sum(p.get("deleted", 0) for p in processed)
        assert total_deleted >= 1

    def test_ignores_non_markdown_files(self, docs_tree):
        """Watcher ignores non-.md file changes."""
        processed = []

        def on_processed(stats):
            processed.append(stats)

        watcher = DocsWatcher(
            docs_root=docs_tree,
            debounce_seconds=0.1,
            poll_interval=0.05,
            on_changes_processed=on_processed,
        )

        with patch.object(ChangeProcessor, '_process_deletions'), \
             patch.object(ChangeProcessor, '_process_upserts'):

            watcher.start()
            time.sleep(0.2)

            # Create a non-markdown file
            txt_file = docs_tree / "llms-txt" / "test-framework" / "notes.txt"
            txt_file.write_text("Just a text file")

            time.sleep(0.3)
            watcher.stop()

        # No events should have been processed
        total_events = sum(
            p.get("created", 0) + p.get("modified", 0) + p.get("deleted", 0)
            for p in processed
        )
        assert total_events == 0

    def test_run_forever_responds_to_signal(self, docs_tree):
        """run_forever exits when stop() is called."""
        watcher = DocsWatcher(docs_root=docs_tree, debounce_seconds=0.1)

        # Stop after a short delay
        def stop_later():
            time.sleep(0.3)
            watcher.stop()

        t = threading.Thread(target=stop_later)
        t.start()

        watcher.run_forever()  # Should return when stop() is called
        t.join(timeout=2.0)

        assert watcher.is_running is False


# =============================================================================
# Module-level convenience function tests
# =============================================================================


class TestModuleFunctions:
    """Tests for start_watcher / stop_watcher convenience functions."""

    def test_start_and_stop_watcher(self, docs_tree):
        """Module-level start/stop functions work correctly."""
        from search.watcher.daemon import start_watcher, stop_watcher

        watcher = start_watcher(
            docs_root=docs_tree,
            debounce_seconds=0.1,
            poll_interval=0.05,
        )
        assert watcher.is_running is True

        stop_watcher()
        assert watcher.is_running is False


# =============================================================================
# Integration-style tests (with mocked OpenSearch)
# =============================================================================


class TestWatcherIntegration:
    """Integration tests that exercise the full pipeline with mocked OpenSearch."""

    def test_new_file_triggers_indexing(self, docs_tree):
        """Creating a new .md file results in indexing operations."""
        indexing_called = threading.Event()

        def track_upserts(self_proc, events, batch_stats):
            indexing_called.set()

        with patch.object(ChangeProcessor, '_process_upserts', track_upserts), \
             patch.object(ChangeProcessor, '_process_deletions'):
            watcher = DocsWatcher(
                docs_root=docs_tree,
                debounce_seconds=0.1,
                poll_interval=0.05,
            )
            watcher.start()
            time.sleep(0.2)

            # Create new file
            new_file = docs_tree / "github-scraped" / "new-lib" / "docs.md"
            new_file.parent.mkdir(parents=True, exist_ok=True)
            new_file.write_text("# New Library\n\nDocumentation content.")

            # Wait for indexing
            indexing_called.wait(timeout=2.0)
            time.sleep(0.1)
            watcher.stop()

        assert indexing_called.is_set()

    def test_delete_file_triggers_removal(self, docs_tree):
        """Deleting a .md file results in removal from the index."""
        deletion_called = threading.Event()

        def track_deletions(self_proc, events, batch_stats):
            deletion_called.set()

        with patch.object(ChangeProcessor, '_process_deletions', track_deletions), \
             patch.object(ChangeProcessor, '_process_upserts'):
            watcher = DocsWatcher(
                docs_root=docs_tree,
                debounce_seconds=0.1,
                poll_interval=0.05,
            )
            watcher.start()
            time.sleep(0.2)

            # Delete existing file
            target = docs_tree / "llms-txt" / "test-framework" / "guide.md"
            target.unlink()

            # Wait for deletion processing
            deletion_called.wait(timeout=2.0)
            time.sleep(0.1)
            watcher.stop()

        assert deletion_called.is_set()

    def test_rapid_changes_debounced(self, docs_tree):
        """Rapid changes to the same file are debounced into one event."""
        batch_counts = []

        def on_processed(stats):
            batch_counts.append(stats)

        watcher = DocsWatcher(
            docs_root=docs_tree,
            debounce_seconds=0.2,
            poll_interval=0.05,
            on_changes_processed=on_processed,
        )

        with patch.object(ChangeProcessor, '_process_deletions'), \
             patch.object(ChangeProcessor, '_process_upserts'):

            watcher.start()
            time.sleep(0.2)

            # Rapid modifications to the same file
            target = docs_tree / "llms-txt" / "test-framework" / "guide.md"
            for i in range(5):
                target.write_text(f"# Version {i}\n\nContent update {i}.")
                time.sleep(0.02)

            # Wait for debounce + processing
            time.sleep(0.6)
            watcher.stop()

        # All 5 rapid edits should be coalesced
        # We expect a small number of batches (ideally 1-2)
        total_modified = sum(
            b.get("modified", 0) + b.get("created", 0) for b in batch_counts
        )
        # Should be much less than 5 due to debouncing
        assert total_modified <= 3, f"Expected debouncing, got {total_modified} events from 5 writes"

    def test_opensearch_connection_failure_handled(self, docs_tree):
        """Watcher survives OpenSearch being unavailable."""
        error_count = []

        def on_processed(stats):
            error_count.append(len(stats.get("errors", [])))

        # Mock OpenSearch client that raises ConnectionError
        mock_client = MagicMock()
        mock_client.index_exists.side_effect = ConnectionError("Connection refused")

        watcher = DocsWatcher(
            docs_root=docs_tree,
            debounce_seconds=0.1,
            poll_interval=0.05,
            on_changes_processed=on_processed,
        )

        with patch("search.opensearch.client.get_client", return_value=mock_client):
            watcher.start()
            time.sleep(0.2)

            # Create a file
            new_file = docs_tree / "llms-txt" / "test-framework" / "new.md"
            new_file.write_text("# Test")

            time.sleep(0.5)
            watcher.stop()

        # Watcher should still be operational (errors are logged, not fatal)
        # The on_processed callback should have been called despite errors
        assert len(error_count) >= 1

"""Checkpoint system for resumable indexing."""

import json
from pathlib import Path
from typing import Dict, List, Set, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class IndexCheckpoint:
    """Manages checkpoints for resumable indexing."""

    def __init__(self, checkpoint_dir: Path):
        self.checkpoint_dir = checkpoint_dir
        self.checkpoint_dir.mkdir(exist_ok=True)
        self.checkpoint_file = checkpoint_dir / "rebuild_checkpoint.json"

    def exists(self) -> bool:
        """Check if a checkpoint exists."""
        return self.checkpoint_file.exists()

    def load(self) -> Dict[str, Any]:
        """Load checkpoint data."""
        if not self.exists():
            return {
                "processed_paths": [],
                "total_documents": 0,
                "total_chunks": 0,
                "started_at": None,
                "last_updated": None,
            }

        try:
            with open(self.checkpoint_file) as f:
                data = json.load(f)
                logger.info(
                    f"Loaded checkpoint: {len(data['processed_paths'])} documents processed"
                )
                return data
        except Exception as e:
            logger.warning(f"Failed to load checkpoint: {e}, starting fresh")
            return {
                "processed_paths": [],
                "total_documents": 0,
                "total_chunks": 0,
                "started_at": None,
                "last_updated": None,
            }

    def save(
        self,
        processed_paths: Set[str],
        total_documents: int,
        total_chunks: int,
    ):
        """Save checkpoint data."""
        now = datetime.utcnow().isoformat()
        data = {
            "processed_paths": list(processed_paths),
            "total_documents": total_documents,
            "total_chunks": total_chunks,
            "started_at": self.load().get("started_at") or now,
            "last_updated": now,
        }

        try:
            # Write to temp file first, then rename (atomic)
            temp_file = self.checkpoint_file.with_suffix(".tmp")
            with open(temp_file, "w") as f:
                json.dump(data, f, indent=2)
            temp_file.rename(self.checkpoint_file)
        except Exception as e:
            logger.error(f"Failed to save checkpoint: {e}")

    def clear(self):
        """Delete checkpoint file."""
        try:
            self.checkpoint_file.unlink(missing_ok=True)
            logger.info("Checkpoint cleared")
        except Exception as e:
            logger.warning(f"Failed to clear checkpoint: {e}")

    def get_processed_paths(self) -> Set[str]:
        """Get set of already processed paths."""
        data = self.load()
        return set(data.get("processed_paths", []))

    def print_status(self):
        """Print checkpoint status."""
        if not self.exists():
            print("No checkpoint found - starting fresh rebuild")
            return

        data = self.load()
        processed = len(data["processed_paths"])
        total_docs = data.get("total_documents", 0)
        total_chunks = data.get("total_chunks", 0)
        started = data.get("started_at", "unknown")
        updated = data.get("last_updated", "unknown")

        print(f"\n{'='*60}")
        print("RESUMING FROM CHECKPOINT")
        print(f"{'='*60}")
        print(f"Started at:         {started}")
        print(f"Last updated:       {updated}")
        print(f"Documents processed: {processed:,} / {total_docs:,}")
        print(f"Chunks indexed:     {total_chunks:,}")
        print(f"{'='*60}\n")

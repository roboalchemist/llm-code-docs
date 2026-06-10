"""LanceDB database connection management."""

import lancedb
from pathlib import Path
from typing import Optional
from search import config
from search.db import schema


class DatabaseConnection:
    """Manages connection to LanceDB database."""

    def __init__(self, db_path: Optional[Path] = None):
        """
        Initialize database connection.

        Args:
            db_path: Path to LanceDB database directory.
                    Defaults to config.LANCEDB_DIR.
        """
        self.db_path = db_path or config.LANCEDB_DIR
        self.db_path.mkdir(parents=True, exist_ok=True)
        self._db = None
        self._documents_table = None
        self._folders_table = None

    @property
    def db(self):
        """Get or create database connection."""
        if self._db is None:
            self._db = lancedb.connect(str(self.db_path))
        return self._db

    @property
    def documents_table(self):
        """Get or create documents table."""
        if self._documents_table is None:
            if "documents" in self.db.table_names():
                self._documents_table = self.db.open_table("documents")
            else:
                # Create new table with schema
                self._documents_table = self.db.create_table(
                    "documents",
                    schema=schema.get_documents_schema(),
                )
        return self._documents_table

    @property
    def folders_table(self):
        """Get or create folders table."""
        if self._folders_table is None:
            if "folders" in self.db.table_names():
                self._folders_table = self.db.open_table("folders")
            else:
                # Create new table with schema
                self._folders_table = self.db.create_table(
                    "folders",
                    schema=schema.get_folders_schema(),
                )
        return self._folders_table

    def drop_tables(self):
        """Drop all tables (for rebuild)."""
        if "documents" in self.db.table_names():
            self.db.drop_table("documents")
            self._documents_table = None
        if "folders" in self.db.table_names():
            self.db.drop_table("folders")
            self._folders_table = None

    def table_exists(self, table_name: str) -> bool:
        """Check if a table exists."""
        return table_name in self.db.table_names()

    def get_stats(self) -> dict:
        """Get database statistics."""
        stats = {
            "tables": self.db.table_names(),
            "db_path": str(self.db_path),
        }

        if "documents" in stats["tables"]:
            docs_count = self.documents_table.count_rows()
            stats["documents_count"] = docs_count

        if "folders" in stats["tables"]:
            folders_count = self.folders_table.count_rows()
            stats["folders_count"] = folders_count

        return stats


# Global connection instance
_connection: Optional[DatabaseConnection] = None


def get_connection() -> DatabaseConnection:
    """Get global database connection instance."""
    global _connection
    if _connection is None:
        _connection = DatabaseConnection()
    return _connection

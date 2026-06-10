"""Document scanner for walking the docs tree."""

from pathlib import Path
from typing import List, Tuple, Optional
from dataclasses import dataclass
from search import config


@dataclass
class DocumentInfo:
    """Information about a discovered document."""

    path: Path
    relative_path: str
    filename: str
    category: str  # llms-txt | github-scraped | web-scraped
    framework: str  # e.g., "gitea", "fastapi"


class DocumentScanner:
    """Scans the docs directory tree for markdown files."""

    def __init__(self, docs_root: Optional[Path] = None):
        """
        Initialize scanner.

        Args:
            docs_root: Root directory containing docs/.
                      Defaults to config.DOCS_ROOT.
        """
        self.docs_root = docs_root or config.DOCS_ROOT

    def scan(self) -> List[DocumentInfo]:
        """
        Scan docs directory for all markdown files.

        Returns:
            List of DocumentInfo objects for all found markdown files.
        """
        documents = []

        for category in config.CATEGORIES:
            category_path = self.docs_root / category
            if not category_path.exists():
                print(f"Warning: Category path not found: {category_path}")
                continue

            # Walk the category directory
            for md_file in category_path.rglob("*.md"):
                doc_info = self._create_document_info(md_file, category)
                if doc_info:
                    documents.append(doc_info)

        return documents

    def _create_document_info(
        self, file_path: Path, category: str
    ) -> Optional[DocumentInfo]:
        """
        Create DocumentInfo from a file path.

        Args:
            file_path: Path to the markdown file.
            category: Category name (llms-txt, github-scraped, web-scraped).

        Returns:
            DocumentInfo object or None if invalid.
        """
        try:
            # Compute relative path from docs root
            relative_path = str(file_path.relative_to(self.docs_root))

            # Extract framework name
            # Path structure: docs/category/framework/...
            parts = file_path.relative_to(self.docs_root / category).parts
            framework = parts[0] if parts else "unknown"

            return DocumentInfo(
                path=file_path,
                relative_path=relative_path,
                filename=file_path.name,
                category=category,
                framework=framework,
            )
        except Exception as e:
            print(f"Warning: Could not process {file_path}: {e}")
            return None

    def scan_framework(self, framework_name: str) -> List[DocumentInfo]:
        """
        Scan files for a specific framework.

        Args:
            framework_name: Name of the framework to scan.

        Returns:
            List of DocumentInfo objects for the framework.
        """
        documents = []

        for category in config.CATEGORIES:
            framework_path = self.docs_root / category / framework_name
            if not framework_path.exists():
                continue

            for md_file in framework_path.rglob("*.md"):
                doc_info = self._create_document_info(md_file, category)
                if doc_info:
                    documents.append(doc_info)

        return documents

    def get_framework_path(self, framework_name: str, category: str) -> Optional[Path]:
        """
        Get the path to a framework's documentation directory.

        Args:
            framework_name: Name of the framework.
            category: Category (llms-txt, github-scraped, web-scraped).

        Returns:
            Path to the framework directory or None if not found.
        """
        framework_path = self.docs_root / category / framework_name
        return framework_path if framework_path.exists() else None

    def count_files(self) -> int:
        """
        Count total number of markdown files.

        Returns:
            Total count of .md files.
        """
        count = 0
        for category in config.CATEGORIES:
            category_path = self.docs_root / category
            if category_path.exists():
                count += len(list(category_path.rglob("*.md")))
        return count


# Global scanner instance
_scanner = None


def get_scanner() -> DocumentScanner:
    """Get global scanner instance."""
    global _scanner
    if _scanner is None:
        _scanner = DocumentScanner()
    return _scanner

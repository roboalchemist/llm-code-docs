"""Result formatting for CLI output."""

from typing import Optional
import pandas as pd

from search.searcher.results import SearchResults


class ResultFormatter:
    """Formats search results for CLI display."""

    def __init__(
        self,
        show_content_preview: bool = True,
        content_preview_length: int = 150,
        show_scores: bool = True,
    ):
        """
        Initialize formatter.

        Args:
            show_content_preview: Whether to show content preview.
            content_preview_length: Length of content preview.
            show_scores: Whether to show relevance scores.
        """
        self.show_content_preview = show_content_preview
        self.content_preview_length = content_preview_length
        self.show_scores = show_scores

    def format_results(self, results: SearchResults) -> str:
        """
        Format complete search results for display.

        Args:
            results: SearchResults object containing documents and folders.

        Returns:
            Formatted string for display.
        """
        lines = []

        # Header
        lines.append(f'Query: "{results.query}"')
        lines.append("")

        # Documents section
        lines.append(self._format_documents_section(results.documents))
        lines.append("")

        # Folders section
        lines.append(self._format_folders_section(results.folders))

        return "\n".join(lines)

    def _format_documents_section(self, documents: pd.DataFrame) -> str:
        """
        Format documents section.

        Args:
            documents: DataFrame of document results.

        Returns:
            Formatted string.
        """
        lines = []

        if documents.empty:
            lines.append("=== Documents (0 matches) ===")
            lines.append("No matching documents found.")
            return "\n".join(lines)

        lines.append(f"=== Documents ({len(documents)} matches) ===")
        lines.append("")

        for idx, (_, row) in enumerate(documents.iterrows(), 1):
            lines.append(self._format_document_row(idx, row))
            lines.append("")

        return "\n".join(lines)

    def _format_document_row(self, index: int, row: pd.Series) -> str:
        """
        Format a single document row.

        Args:
            index: Result index (1-based).
            row: Document row from DataFrame.

        Returns:
            Formatted string.
        """
        lines = []

        # Title line with framework tag
        framework = row.get('framework', 'unknown')
        title = row.get('title', '') or row.get('filename', 'Untitled')
        lines.append(f"{index}. [{framework}] {title}")

        # Path
        relative_path = row.get('relative_path', row.get('path', ''))
        lines.append(f"   Path: {relative_path}")

        # Score
        if self.show_scores:
            final_score = row.get('final_score', row.get('similarity_score', 0))
            lines.append(f"   Score: {final_score:.3f}")

        # Chunk info if applicable
        chunk_count = row.get('chunk_count', 1)
        if chunk_count > 1:
            chunk_id = row.get('chunk_id', 0)
            lines.append(f"   Chunk: {chunk_id + 1}/{chunk_count}")

        # Content preview
        if self.show_content_preview:
            content = str(row.get('content', ''))
            preview = self._truncate_content(content)
            if preview:
                lines.append(f"   Preview: {preview}")

        return "\n".join(lines)

    def _format_folders_section(self, folders: pd.DataFrame) -> str:
        """
        Format folders section.

        Args:
            folders: DataFrame of folder results.

        Returns:
            Formatted string.
        """
        lines = []

        if folders.empty:
            lines.append("=== Frameworks (0 matches) ===")
            lines.append("No matching frameworks found.")
            return "\n".join(lines)

        lines.append(f"=== Frameworks ({len(folders)} matches) ===")
        lines.append("")

        for idx, (_, row) in enumerate(folders.iterrows(), 1):
            lines.append(self._format_folder_row(idx, row))
            lines.append("")

        return "\n".join(lines)

    def _format_folder_row(self, index: int, row: pd.Series) -> str:
        """
        Format a single folder row.

        Args:
            index: Result index (1-based).
            row: Folder row from DataFrame.

        Returns:
            Formatted string.
        """
        lines = []

        # Name and description
        name = row.get('framework_name', 'unknown')
        description = row.get('description', '')
        if description:
            lines.append(f"{index}. {name} - {description[:80]}")
        else:
            lines.append(f"{index}. {name}")

        # Stats
        file_count = row.get('file_count', 0)
        size = row.get('size', 'N/A')
        category = row.get('category', 'unknown')
        lines.append(f"   Files: {file_count} | Size: {size} | Category: {category}")

        # Score
        if self.show_scores:
            final_score = row.get('final_score', row.get('similarity_score', 0))
            lines.append(f"   Score: {final_score:.3f}")

        # Source URL if available
        source_url = row.get('source_url', '')
        if source_url:
            lines.append(f"   URL: {source_url}")

        return "\n".join(lines)

    def _truncate_content(self, content: str) -> str:
        """
        Truncate content for preview.

        Args:
            content: Full content string.

        Returns:
            Truncated content preview.
        """
        if not content:
            return ""

        # Clean up content: remove code blocks, extra whitespace
        import re

        # Remove code blocks
        content = re.sub(r'```[\s\S]*?```', '[code]', content)

        # Remove frontmatter
        content = re.sub(r'^---[\s\S]*?---\n', '', content)

        # Collapse whitespace
        content = re.sub(r'\s+', ' ', content).strip()

        # Truncate
        if len(content) > self.content_preview_length:
            content = content[:self.content_preview_length].rsplit(' ', 1)[0] + "..."

        return content

    def format_stats(self, stats: dict) -> str:
        """
        Format database statistics for display.

        Args:
            stats: Dictionary of database statistics.

        Returns:
            Formatted string.
        """
        lines = []
        lines.append("=== Index Statistics ===")
        lines.append("")

        lines.append(f"Database path: {stats.get('db_path', 'N/A')}")
        lines.append(f"Tables: {', '.join(stats.get('tables', []))}")
        lines.append("")

        if 'documents_count' in stats:
            lines.append(f"Documents indexed: {stats['documents_count']:,}")
        if 'folders_count' in stats:
            lines.append(f"Frameworks indexed: {stats['folders_count']:,}")

        return "\n".join(lines)

    def format_document_detail(self, document: pd.DataFrame) -> str:
        """
        Format detailed view of a single document.

        Args:
            document: DataFrame containing document chunk(s).

        Returns:
            Formatted string.
        """
        if document.empty:
            return "Document not found."

        lines = []
        row = document.iloc[0]

        lines.append("=== Document Details ===")
        lines.append("")
        lines.append(f"Title: {row.get('title', 'Untitled')}")
        lines.append(f"Path: {row.get('path', 'N/A')}")
        lines.append(f"Framework: {row.get('framework', 'unknown')}")
        lines.append(f"Category: {row.get('category', 'unknown')}")
        lines.append(f"File Size: {row.get('file_size', 0):,} bytes")
        lines.append(f"Line Count: {row.get('line_count', 0):,}")
        lines.append(f"Chunks: {len(document)}")

        headings = row.get('headings', [])
        if headings and isinstance(headings, list):
            lines.append("")
            lines.append("Headings:")
            for h in headings[:10]:
                lines.append(f"  - {h}")
            if len(headings) > 10:
                lines.append(f"  ... and {len(headings) - 10} more")

        keywords = row.get('keywords', [])
        if keywords and isinstance(keywords, list):
            lines.append("")
            lines.append(f"Keywords: {', '.join(keywords[:15])}")

        return "\n".join(lines)

    def format_folder_detail(self, folder: pd.DataFrame) -> str:
        """
        Format detailed view of a single folder.

        Args:
            folder: DataFrame containing folder row.

        Returns:
            Formatted string.
        """
        if folder.empty:
            return "Folder not found."

        row = folder.iloc[0]
        lines = []

        lines.append("=== Framework Details ===")
        lines.append("")
        lines.append(f"Name: {row.get('framework_name', 'unknown')}")
        lines.append(f"Description: {row.get('description', 'N/A')}")
        lines.append(f"Category: {row.get('category', 'unknown')}")
        lines.append(f"Path: {row.get('path', 'N/A')}")
        lines.append(f"File Count: {row.get('file_count', 0)}")
        lines.append(f"Size: {row.get('size', 'N/A')}")
        lines.append(f"Status: {row.get('status', 'unknown')}")
        lines.append(f"Source URL: {row.get('source_url', 'N/A')}")

        return "\n".join(lines)


# Global formatter instance
_formatter = None


def get_formatter() -> ResultFormatter:
    """Get global formatter instance."""
    global _formatter
    if _formatter is None:
        _formatter = ResultFormatter()
    return _formatter

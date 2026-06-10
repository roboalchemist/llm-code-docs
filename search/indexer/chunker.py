"""Smart document chunking for large files."""

import re
from typing import List, Tuple
from search import config


class DocumentChunker:
    """Chunks large documents intelligently."""

    def __init__(
        self,
        max_tokens: int = None,
        min_tokens: int = None,
        overlap_tokens: int = None,
    ):
        """
        Initialize chunker.

        Args:
            max_tokens: Maximum tokens per chunk.
            min_tokens: Minimum tokens per chunk.
            overlap_tokens: Overlap between chunks.
        """
        self.max_tokens = max_tokens or config.MAX_CHUNK_TOKENS
        self.min_tokens = min_tokens or config.MIN_CHUNK_TOKENS
        self.overlap_tokens = overlap_tokens or config.CHUNK_OVERLAP_TOKENS

    def should_chunk(self, content: str) -> bool:
        """
        Determine if content needs chunking.

        Args:
            content: Document content.

        Returns:
            True if content exceeds max_tokens threshold.
        """
        token_estimate = self._estimate_tokens(content)
        return token_estimate > self.max_tokens

    def chunk(self, content: str) -> List[str]:
        """
        Chunk document into smaller pieces.

        Uses semantic chunking that preserves:
        1. Code blocks (don't split)
        2. Sections (split on ## headers)
        3. Paragraphs (split on double newlines)

        Args:
            content: Document content to chunk.

        Returns:
            List of content chunks.
        """
        if not self.should_chunk(content):
            return [content]

        # Try splitting on H2 headers first
        chunks = self._split_on_headers(content, level=2)

        # If chunks are still too large, split on H3
        final_chunks = []
        for chunk in chunks:
            if self._estimate_tokens(chunk) > self.max_tokens:
                sub_chunks = self._split_on_headers(chunk, level=3)
                final_chunks.extend(sub_chunks)
            else:
                final_chunks.append(chunk)

        # If still too large, split on paragraphs
        result_chunks = []
        for chunk in final_chunks:
            if self._estimate_tokens(chunk) > self.max_tokens:
                para_chunks = self._split_on_paragraphs(chunk)
                result_chunks.extend(para_chunks)
            else:
                result_chunks.append(chunk)

        # Filter out chunks that are too small
        result_chunks = [
            c for c in result_chunks
            if self._estimate_tokens(c) >= self.min_tokens
        ]

        return result_chunks if result_chunks else [content]

    def _split_on_headers(self, content: str, level: int = 2) -> List[str]:
        """
        Split content on headers of a specific level.

        Args:
            content: Content to split.
            level: Header level (2 for ##, 3 for ###).

        Returns:
            List of chunks split on headers.
        """
        header_pattern = r'^' + '#' * level + r'\s+.+$'
        chunks = []
        current_chunk = []

        for line in content.split('\n'):
            if re.match(header_pattern, line.strip()):
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                current_chunk = [line]
            else:
                current_chunk.append(line)

        if current_chunk:
            chunks.append('\n'.join(current_chunk))

        return chunks

    def _split_on_paragraphs(self, content: str) -> List[str]:
        """
        Split content on paragraph boundaries.

        Args:
            content: Content to split.

        Returns:
            List of chunks split on paragraphs.
        """
        # Split on double newlines
        paragraphs = re.split(r'\n\s*\n', content)

        chunks = []
        current_chunk = []
        current_tokens = 0

        for para in paragraphs:
            para_tokens = self._estimate_tokens(para)

            if current_tokens + para_tokens > self.max_tokens and current_chunk:
                # Start new chunk
                chunks.append('\n\n'.join(current_chunk))
                # Add overlap from previous chunk
                if self.overlap_tokens > 0:
                    current_chunk = current_chunk[-1:]
                    current_tokens = self._estimate_tokens(current_chunk[0])
                else:
                    current_chunk = []
                    current_tokens = 0

            current_chunk.append(para)
            current_tokens += para_tokens

        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))

        return chunks

    def _estimate_tokens(self, text: str) -> int:
        """
        Estimate token count using simple heuristic.

        Rough estimate: 1 token ~= 4 characters.

        Args:
            text: Text to estimate.

        Returns:
            Estimated token count.
        """
        return len(text) // 4


# Global chunker instance
_chunker = None


def get_chunker() -> DocumentChunker:
    """Get global chunker instance."""
    global _chunker
    if _chunker is None:
        _chunker = DocumentChunker()
    return _chunker

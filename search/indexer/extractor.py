"""Metadata extraction from markdown files."""

import re
from pathlib import Path
from typing import List, Optional, Dict, Any
import yaml


class MetadataExtractor:
    """Extracts metadata from markdown files."""

    @staticmethod
    def extract_frontmatter(content: str) -> Optional[Dict[str, Any]]:
        """
        Extract YAML frontmatter from markdown content.

        Args:
            content: Markdown file content.

        Returns:
            Dictionary of frontmatter data or None if not present.
        """
        # Match YAML frontmatter: ---\n...\n---
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(frontmatter_pattern, content, re.DOTALL)

        if match:
            try:
                frontmatter_yaml = match.group(1)
                return yaml.safe_load(frontmatter_yaml)
            except Exception as e:
                print(f"Warning: Failed to parse frontmatter: {e}")
                return None

        return None

    @staticmethod
    def extract_title(content: str, frontmatter: Optional[Dict] = None) -> str:
        """
        Extract document title from frontmatter or first H1.

        Args:
            content: Markdown file content.
            frontmatter: Parsed frontmatter dictionary.

        Returns:
            Document title or empty string if not found.
        """
        # Try frontmatter first
        if frontmatter:
            for key in ['title', 'Title', 'name', 'Name']:
                if key in frontmatter:
                    return str(frontmatter[key])

        # Try first H1 heading
        h1_pattern = r'^#\s+(.+)$'
        for line in content.split('\n'):
            match = re.match(h1_pattern, line.strip())
            if match:
                return match.group(1).strip()

        return ""

    @staticmethod
    def extract_headings(content: str) -> List[str]:
        """
        Extract all H1-H3 headings from content.

        Args:
            content: Markdown file content.

        Returns:
            List of heading text (without the # markers).
        """
        headings = []
        heading_pattern = r'^(#{1,3})\s+(.+)$'

        for line in content.split('\n'):
            match = re.match(heading_pattern, line.strip())
            if match:
                heading_text = match.group(2).strip()
                # Remove markdown links from headings
                heading_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', heading_text)
                headings.append(heading_text)

        return headings

    @staticmethod
    def extract_keywords(content: str) -> List[str]:
        """
        Extract technical keywords from content using simple heuristics.

        Args:
            content: Markdown file content.

        Returns:
            List of extracted keywords.
        """
        keywords = set()

        # Common technical terms patterns
        patterns = [
            r'\b(API|REST|GraphQL|HTTP|HTTPS|JSON|XML|YAML)\b',
            r'\b(database|DB|SQL|NoSQL|PostgreSQL|MySQL|MongoDB)\b',
            r'\b(authentication|auth|OAuth|JWT|token)\b',
            r'\b(configuration|config|settings|options)\b',
            r'\b(deployment|deploy|production|staging)\b',
            r'\b(testing|test|unittest|pytest|jest)\b',
            r'\b(async|await|promise|callback)\b',
            r'\b(CLI|command|terminal|shell)\b',
            r'\b(server|client|frontend|backend)\b',
            r'\b(docker|container|kubernetes|k8s)\b',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            keywords.update(m.lower() for m in matches)

        # Also extract code block languages
        code_lang_pattern = r'```(\w+)'
        languages = re.findall(code_lang_pattern, content)
        keywords.update(lang.lower() for lang in languages if lang)

        return sorted(list(keywords))

    @staticmethod
    def extract_metadata(file_path: Path) -> Dict[str, Any]:
        """
        Extract all metadata from a markdown file.

        Args:
            file_path: Path to the markdown file.

        Returns:
            Dictionary containing extracted metadata.
        """
        try:
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Get file stats
            stat = file_path.stat()
            file_size = stat.st_size
            line_count = content.count('\n') + 1

            # Extract components
            frontmatter = MetadataExtractor.extract_frontmatter(content)
            title = MetadataExtractor.extract_title(content, frontmatter)
            headings = MetadataExtractor.extract_headings(content)
            keywords = MetadataExtractor.extract_keywords(content)

            return {
                'content': content,
                'file_size': file_size,
                'line_count': line_count,
                'title': title,
                'headings': headings,
                'keywords': keywords,
                'frontmatter': frontmatter,
            }

        except Exception as e:
            print(f"Error extracting metadata from {file_path}: {e}")
            return {
                'content': '',
                'file_size': 0,
                'line_count': 0,
                'title': '',
                'headings': [],
                'keywords': [],
                'frontmatter': None,
            }


# Global extractor instance
_extractor = None


def get_extractor() -> MetadataExtractor:
    """Get global extractor instance."""
    global _extractor
    if _extractor is None:
        _extractor = MetadataExtractor()
    return _extractor

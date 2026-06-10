"""Parser for index.yaml file."""

import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
from search import config


class IndexYAMLParser:
    """Parser for the llm-code-docs index.yaml file."""

    def __init__(self, yaml_path: Optional[Path] = None):
        """
        Initialize parser.

        Args:
            yaml_path: Path to index.yaml. Defaults to config.INDEX_YAML.
        """
        self.yaml_path = yaml_path or config.INDEX_YAML
        self._data = None

    @property
    def data(self) -> Dict[str, Any]:
        """Lazy-load and cache the YAML data."""
        if self._data is None:
            with open(self.yaml_path, 'r') as f:
                self._data = yaml.safe_load(f)
        return self._data

    def get_metadata(self) -> Dict[str, Any]:
        """Get the metadata section."""
        return self.data.get('metadata', {})

    def get_llms_txt(self) -> List[Dict[str, Any]]:
        """Get all llms.txt entries."""
        return self.data.get('llms_txt', [])

    def get_github_scraped(self) -> List[Dict[str, Any]]:
        """Get all github-scraped entries."""
        return self.data.get('github_scraped', [])

    def get_web_scraped(self) -> List[Dict[str, Any]]:
        """Get all web-scraped entries."""
        return self.data.get('web_scraped', [])

    def get_all_sources(self) -> List[Dict[str, Any]]:
        """Get all documentation sources across all categories."""
        sources = []

        # Add category to each source
        for source in self.get_llms_txt():
            source['_category'] = 'llms-txt'
            sources.append(source)

        for source in self.get_github_scraped():
            source['_category'] = 'github-scraped'
            sources.append(source)

        for source in self.get_web_scraped():
            source['_category'] = 'web-scraped'
            sources.append(source)

        return sources

    def get_source_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Find a source by its name.

        Args:
            name: The name of the source (framework/tool name).

        Returns:
            Source dict or None if not found.
        """
        for source in self.get_all_sources():
            if source.get('name') == name:
                return source
        return None

    def get_source_by_path(self, path: str) -> Optional[Dict[str, Any]]:
        """
        Find a source by its path.

        Args:
            path: The path to the source documentation.

        Returns:
            Source dict or None if not found.
        """
        for source in self.get_all_sources():
            if source.get('path') == path:
                return source
        return None

    def parse_last_updated(self, date_str: str) -> Optional[datetime]:
        """
        Parse last_updated date string to datetime.

        Args:
            date_str: Date string like "2025-12-15 18:20".

        Returns:
            datetime object or None if parsing fails.
        """
        if not date_str:
            return None

        try:
            # Try common formats
            for fmt in ["%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y-%m-%d %H:%M:%S"]:
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
        except Exception:
            pass

        return None


# Global parser instance
_parser = None


def get_parser() -> IndexYAMLParser:
    """Get global parser instance."""
    global _parser
    if _parser is None:
        _parser = IndexYAMLParser()
    return _parser

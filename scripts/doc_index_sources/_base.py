"""Base classes for doc-index source adapters."""

from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class LibraryDoc:
    """A single library's documentation entry from a platform."""

    name: str  # normalized: lowercase, hyphens
    display_name: str  # original casing
    doc_url: str  # direct URL to docs
    language: str | None = None  # python, rust, go, elixir, etc.
    doc_type: str = "html"  # llms-txt, html, api-spec, cheatsheet
    quality_signals: dict = field(default_factory=dict)  # {stars, downloads, etc.}


class IndexSource:
    """Base class for platform source adapters.

    Each adapter fetches library listings from one documentation platform
    and yields LibraryDoc entries for insertion into the index DB.
    """

    platform: str = ""  # unique identifier, e.g. "devdocs"
    api_url: str = ""  # base URL for the platform API
    description: str = ""

    def fetch(self) -> Iterator[LibraryDoc]:
        """Yield LibraryDoc entries from this platform.

        Subclasses must implement this. Should handle pagination,
        rate limiting, and error recovery internally.
        """
        raise NotImplementedError

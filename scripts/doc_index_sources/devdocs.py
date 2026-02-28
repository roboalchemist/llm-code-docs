"""DevDocs.io adapter — 600+ documentation sets covering major languages/frameworks."""

import re
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


def _infer_language_devdocs(doc_type: str | None, name: str) -> str | None:
    """Best-effort language inference from DevDocs metadata."""
    doc_type = (doc_type or "").lower()
    name_l = name.lower()

    mapping = {
        "python": "python",
        "javascript": "javascript",
        "typescript": "typescript",
        "ruby": "ruby",
        "go": "go",
        "rust": "rust",
        "elixir": "elixir",
        "erlang": "erlang",
        "haskell": "haskell",
        "perl": "perl",
        "php": "php",
        "java": "java",
        "kotlin": "kotlin",
        "swift": "swift",
        "c": "c",
        "cpp": "cpp",
        "css": "css",
        "html": "html",
        "lua": "lua",
        "r": "r",
        "scala": "scala",
        "dart": "dart",
    }

    for key, lang in mapping.items():
        if key in doc_type or key in name_l:
            return lang
    return None


class DevDocsSource(IndexSource):
    """DevDocs.io — 600+ documentation sets covering major languages/frameworks."""

    platform = "devdocs"
    api_url = "https://devdocs.io/docs.json"
    description = "DevDocs.io documentation sets"

    def fetch(self) -> Iterator[LibraryDoc]:
        resp = requests.get(self.api_url, timeout=_TIMEOUT)
        resp.raise_for_status()
        docs = resp.json()

        for doc in docs:
            slug = doc.get("slug", "")
            name = doc.get("name", slug)
            # DevDocs slugs can have version suffixes like "react~18"
            base_slug = slug.split("~")[0]
            doc_type = doc.get("type", "")

            yield LibraryDoc(
                name=_normalize_name(base_slug),
                display_name=name,
                doc_url=f"https://devdocs.io/{slug}/",
                language=_infer_language_devdocs(doc_type, name),
                doc_type="html",
                quality_signals={
                    "slug": slug,
                    "version": doc.get("version", ""),
                    "release": doc.get("release", ""),
                    "mtime": doc.get("mtime", 0),
                },
            )

"""Hackage adapter — Haskell package documentation (15K+ packages)."""

import re
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class HackageSource(IndexSource):
    """Hackage — Haskell package documentation."""

    platform = "hackage"
    api_url = "https://hackage.haskell.org/packages/"
    description = "Hackage Haskell package documentation"

    def fetch(self) -> Iterator[LibraryDoc]:
        # Hackage exposes a simple JSON list of all package names
        resp = requests.get(
            self.api_url,
            headers={"Accept": "application/json"},
            timeout=_TIMEOUT,
        )
        resp.raise_for_status()
        packages = resp.json()

        for pkg in packages:
            # The JSON list returns objects with packageName
            if isinstance(pkg, dict):
                name = pkg.get("packageName", "")
            else:
                name = str(pkg)
            if not name:
                continue

            yield LibraryDoc(
                name=_normalize_name(name),
                display_name=name,
                doc_url=f"https://hackage.haskell.org/package/{name}",
                language="haskell",
                doc_type="html",
                quality_signals={},
            )

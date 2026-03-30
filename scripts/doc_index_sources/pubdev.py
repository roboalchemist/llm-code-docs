"""pub.dev adapter — Dart/Flutter package documentation (76K+ packages)."""

import re
import time
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30
_PAGE_DELAY = 0.5


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class PubDevSource(IndexSource):
    """pub.dev — Dart/Flutter package documentation."""

    platform = "pubdev"
    api_url = "https://pub.dev/api/packages"
    description = "pub.dev Dart/Flutter package documentation"

    def fetch(self) -> Iterator[LibraryDoc]:
        url = self.api_url
        while url:
            resp = requests.get(url, timeout=_TIMEOUT)
            resp.raise_for_status()
            data = resp.json()

            for pkg in data.get("packages", []):
                name = pkg.get("name", "")
                if not name:
                    continue

                yield LibraryDoc(
                    name=_normalize_name(name),
                    display_name=name,
                    doc_url=f"https://pub.dev/documentation/{name}/latest/",
                    language="dart",
                    doc_type="html",
                    quality_signals={},
                )

            next_url = data.get("next_url")
            if next_url:
                # next_url is relative like /api/packages?page=2
                url = f"https://pub.dev{next_url}" if next_url.startswith("/") else next_url
            else:
                url = None

            time.sleep(_PAGE_DELAY)

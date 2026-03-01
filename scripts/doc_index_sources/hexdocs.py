"""HexDocs.pm adapter — Elixir/Erlang package documentation (19K+ packages)."""

import re
import time
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30
_PAGE_DELAY = 0.6  # 100 req/min unauthenticated


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class HexDocsSource(IndexSource):
    """HexDocs.pm — Elixir/Erlang package docs via hex.pm API."""

    platform = "hexdocs"
    api_url = "https://hex.pm/api/packages"
    description = "HexDocs.pm Elixir/Erlang package documentation"

    def fetch(self) -> Iterator[LibraryDoc]:
        page = 1
        while True:
            resp = requests.get(
                self.api_url,
                params={"page": page, "sort": "name"},
                headers={"User-Agent": "doc-index/1.0"},
                timeout=_TIMEOUT,
            )
            resp.raise_for_status()
            packages = resp.json()

            if not packages:
                break

            for pkg in packages:
                name = pkg.get("name", "")
                if not name:
                    continue

                downloads = 0
                if pkg.get("downloads"):
                    downloads = pkg["downloads"].get("all", 0)

                yield LibraryDoc(
                    name=_normalize_name(name),
                    display_name=name,
                    doc_url=f"https://hexdocs.pm/{name}/",
                    language="elixir",
                    doc_type="html",
                    quality_signals={
                        "downloads": downloads,
                        "updated_at": pkg.get("updated_at", ""),
                    },
                )

            page += 1
            time.sleep(_PAGE_DELAY)

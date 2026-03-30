"""devhints.io cheatsheets adapter from rstacruz/cheatsheets GitHub repo."""

import os
import re
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class DevhintsSource(IndexSource):
    """devhints.io cheatsheets from rstacruz/cheatsheets GitHub repo."""

    platform = "devhints"
    api_url = "https://api.github.com/repos/rstacruz/cheatsheets/git/trees/master?recursive=1"
    description = "devhints.io cheatsheets"

    def fetch(self) -> Iterator[LibraryDoc]:
        headers = {}
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"token {token}"

        resp = requests.get(self.api_url, headers=headers, timeout=_TIMEOUT)
        resp.raise_for_status()
        tree = resp.json().get("tree", [])

        for item in tree:
            path = item.get("path", "")
            if not path.endswith(".md") or "/" in path:
                continue
            sheet_name = path.rsplit(".md", 1)[0]
            if sheet_name.startswith("_"):
                continue

            yield LibraryDoc(
                name=_normalize_name(sheet_name),
                display_name=sheet_name,
                doc_url=f"https://devhints.io/{sheet_name}",
                doc_type="cheatsheet",
                quality_signals={"size": item.get("size", 0)},
            )

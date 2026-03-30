"""Dash/Zeal docsets adapter via Kapeli/feeds on GitHub."""

import os
import re
from typing import Iterator

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class DashSource(IndexSource):
    """Dash/Zeal docsets via Kapeli/feeds on GitHub."""

    platform = "dash"
    api_url = "https://api.github.com/repos/Kapeli/feeds/contents"
    description = "Dash/Zeal documentation feeds"

    def fetch(self) -> Iterator[LibraryDoc]:
        headers = {}
        token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"token {token}"

        resp = requests.get(self.api_url, headers=headers, timeout=_TIMEOUT)
        resp.raise_for_status()
        contents = resp.json()

        for item in contents:
            fname = item.get("name", "")
            if not fname.endswith(".xml"):
                continue
            docset_name = fname.rsplit(".xml", 1)[0]

            yield LibraryDoc(
                name=_normalize_name(docset_name),
                display_name=docset_name,
                doc_url=f"https://kapeli.com/dash_resources/docsets/{docset_name}",
                doc_type="html",
                quality_signals={"feed_file": fname},
            )

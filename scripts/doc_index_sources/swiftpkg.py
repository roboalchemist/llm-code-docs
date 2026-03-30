"""Swift Package Index adapter — Swift package documentation (10K+ packages).

Uses the official PackageList GitHub repo (a flat JSON array of repo URLs)
rather than the SPI web API which is behind Cloudflare protection.
"""

import re
from typing import Iterator
from urllib.parse import urlparse

import requests

from ._base import IndexSource, LibraryDoc

_TIMEOUT = 30


def _normalize_name(name: str) -> str:
    """Normalize a library name: lowercase, replace spaces/underscores with hyphens."""
    return re.sub(r"[\s_]+", "-", name.strip().lower())


class SwiftPkgSource(IndexSource):
    """Swift Package Index — Swift package documentation via PackageList repo."""

    platform = "swiftpkg"
    api_url = "https://raw.githubusercontent.com/SwiftPackageIndex/PackageList/main/packages.json"
    description = "Swift Package Index documentation"

    def fetch(self) -> Iterator[LibraryDoc]:
        resp = requests.get(self.api_url, timeout=_TIMEOUT)
        resp.raise_for_status()
        urls = resp.json()  # flat array of GitHub URL strings

        for url in urls:
            if not isinstance(url, str) or not url:
                continue

            # Extract owner/repo from GitHub URL
            parsed = urlparse(url)
            path_parts = parsed.path.strip("/").split("/")
            if len(path_parts) < 2:
                continue

            owner = path_parts[0]
            repo = path_parts[1].replace(".git", "")

            yield LibraryDoc(
                name=_normalize_name(repo),
                display_name=repo,
                doc_url=f"https://swiftpackageindex.com/{owner}/{repo}/documentation",
                language="swift",
                doc_type="html",
                quality_signals={
                    "repo_url": url,
                    "owner": owner,
                },
            )

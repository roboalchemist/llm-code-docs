"""Doc-index source adapters registry."""

from .devdocs import DevDocsSource
from .dash import DashSource
from .devhints import DevhintsSource
from .apisguru import APIsGuruSource
from .hexdocs import HexDocsSource
from .pubdev import PubDevSource
from .hackage import HackageSource
from .swiftpkg import SwiftPkgSource
from .golang import GolangSource
from .readthedocs import ReadTheDocsSource
from .cljdoc import CljdocSource

# Registry of all available source adapters, keyed by platform name.
# Order reflects recommended build sequence (Tier A first = quick wins).
SOURCES: dict[str, type] = {
    # Tier A — single API call each
    "devdocs": DevDocsSource,
    "dash": DashSource,
    "devhints": DevhintsSource,
    "apisguru": APIsGuruSource,
    # Tier B — paginated APIs
    "hexdocs": HexDocsSource,
    "pubdev": PubDevSource,
    "hackage": HackageSource,
    "swiftpkg": SwiftPkgSource,
    "golang": GolangSource,
    "readthedocs": ReadTheDocsSource,
    "cljdoc": CljdocSource,
}

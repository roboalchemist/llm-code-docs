#!/usr/bin/env python3
"""
Extract comprehensive documentation from rTorrent GitHub repositories.

This script extracts from 4 GitHub repos into docs/rtorrent/github/:
  1. rakshasa/rtorrent           -> rakshasa-rtorrent/  (configs, scripts, FAQ, man pages)
  2. rtorrent-community/rtorrent-docs -> rtorrent-community/  (handbook RST -> MD)
  3. rakshasa/rtorrent-doc      -> rakshasa-rtorrent-doc/ (wiki docs)
  4. pyroscope/rtorrent-ps       -> rtorrent-ps/  (extended rTorrent-PS docs)

Converts:
  - doc/faq.xml (DocBook XML) -> faq.md
  - docs/*.rst (Sphinx RST) -> markdown

Total: 63 markdown files + shell scripts + configs (~252 KB)
"""

import sys
from pathlib import Path

# Delegate to the comprehensive extractor
SCRIPT_DIR = Path(__file__).parent
COMPREHENSIVE = SCRIPT_DIR / "rtorrent-comprehensive-extract.py"

if __name__ == "__main__":
    if not COMPREHENSIVE.exists():
        print(f"ERROR: {COMPREHENSIVE} not found", file=sys.stderr)
        sys.exit(1)
    # Run the comprehensive extractor
    import subprocess
    result = subprocess.run([sys.executable, str(COMPREHENSIVE)], cwd=SCRIPT_DIR.parent)
    sys.exit(result.returncode)

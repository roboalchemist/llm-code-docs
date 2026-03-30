#!/usr/bin/env python3
"""
Scrape ruTorrent wiki plugin pages.
"""
import os
import re
import requests
from pathlib import Path
from html import unescape

BASE_URL = "https://raw.githubusercontent.com/wiki/Novik/ruTorrent/{page}.md"
TARGET_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "rutorrent" / "plugins"

# Mapping of wiki page names to filenames
PLUGIN_MAP = {
    # Internal plugins (prefix with internal-)
    "Plugin_cloudflare": "internal-cloudflare.md",
    "Plugin_getdir": "internal-getdir.md",
    "Plugin_noty": "internal-noty.md",
    "Plugin_noty2": "internal-noty2.md",
    "Plugin_task": "internal-task.md",
    # Built-in plugins
    "PluginCheckPort": "check_port.md",
    "PluginChunks": "chunks.md",
    "PluginCookies": "cookies.md",
    "PluginCpuload": "cpuload.md",
    "PluginData": "data.md",
    "PluginDataDir": "data_dir.md",
    "PluginDiskspace": "disk_space.md",
    "PluginEdit": "edit.md",
    "PluginErasedata": "erase_data.md",
    "PluginExtRatio": "ext_ratio.md",
    "PluginExtsearch": "ext_search.md",
    "PluginFeeds": "feeds.md",
    "PluginHTTPRPC": "http_rpc.md",
    "PluginIPad": "ipad.md",
    "PluginLookAt": "look_at.md",
    "PluginRetrackers": "retrackers.md",
    "PluginRPC": "rpc.md",
    "PluginScreenshots": "screenshots.md",
    "PluginSeedingtime": "seeding_time.md",
    "PluginShow_peers_like_wtorrent": "show_peers_like_wtorrent.md",
    "PluginSource": "source.md",
    "PluginSpectrogram": "spectrogram.md",
    "PluginTracklabels": "track_labels.md",
    "PluginTrafic": "trafic.md",
    "PluginUnpack": "unpack.md",
    "PluginUploadETA": "upload_eta.md",
    "PluginXMPP": "xmpp.md",
    # Third-party plugins
    "PluginAutodlirssi": "autodl_irssi.md",
    "PluginChat": "chat.md",
    "PluginHostname": "hostname.md",
    "PluginInstantSearch": "instant_search.md",
    "PluginLogoff": "logoff.md",
    "PluginNFO": "nfo.md",
    "PluginPause": "pause.md",
    "PluginTaddLabel": "tadd_labels.md",
}


def clean_markdown(content):
    """Clean up wiki markdown to standard markdown."""
    # Remove wiki-specific links and convert to regular markdown
    # [PageName](PluginPageName) -> [PageName](../PluginPageName) or just keep as text
    content = re.sub(r'\[([^\]]+)\]\(Plugin([^\)]+)\)', r'[\1]', content)

    # Remove markdownify artifacts
    content = re.sub(r'\\([\[\]`])', r'\1', content)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', r'\n\n', content)

    # Fix bullet points (wiki sometimes uses different formats)
    content = re.sub(r'^ \* ', r'- ', content, flags=re.MULTILINE)

    # Clean up trailing whitespace
    content = '\n'.join(line.rstrip() for line in content.split('\n'))

    return content.strip() + '\n'


def fetch_wiki_page(page_name):
    """Fetch a wiki page from GitHub."""
    url = BASE_URL.format(page=page_name)
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            return resp.text
        else:
            print(f"  Failed to fetch {page_name}: HTTP {resp.status_code}")
            return None
    except Exception as e:
        print(f"  Failed to fetch {page_name}: {e}")
        return None


def main():
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    # Get existing files
    existing = set(f.name for f in TARGET_DIR.glob("*.md"))
    print(f"Existing files: {len(existing)}")

    success_count = 0
    skip_count = 0
    fail_count = 0

    for wiki_name, filename in sorted(PLUGIN_MAP.items()):
        if filename in existing:
            print(f"SKIP: {filename} (already exists)")
            skip_count += 1
            continue

        print(f"FETCH: {wiki_name} -> {filename}")
        content = fetch_wiki_page(wiki_name)

        if content:
            cleaned = clean_markdown(content)
            filepath = TARGET_DIR / filename
            filepath.write_text(cleaned)
            size = len(cleaned)
            print(f"  OK: {size} bytes")
            success_count += 1
        else:
            fail_count += 1

    print(f"\nSummary: {success_count} new, {skip_count} skipped, {fail_count} failed")


if __name__ == "__main__":
    main()
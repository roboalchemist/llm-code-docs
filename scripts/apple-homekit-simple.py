#!/home/gateway/miniconda3/bin/python
"""
Apple HomeKit Framework Documentation Extractor.

Manually curated list of important HomeKit API pages to extract.
Since Apple's developer documentation is JavaScript-rendered, this scraper
uses Playwright to render and extract content from specific pages.

Output: docs/web-scraped/apple-homekit/
"""

import subprocess
import re
import json
from pathlib import Path
from typing import Optional, Dict, List
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "apple-homekit"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Predefined list of important HomeKit API pages
HOMEKIT_PAGES = [
    ("https://developer.apple.com/documentation/homekit", "HomeKit Framework Overview"),
    ("https://developer.apple.com/documentation/homekit/interacting-with-a-home-automation-network", "Interacting with Home Automation Network"),
    ("https://developer.apple.com/documentation/homekit/configuring-a-home-automation-device", "Configuring Home Automation Device"),
    ("https://developer.apple.com/documentation/homekit/enabling-homekit-in-your-app", "Enabling HomeKit in Your App"),
    ("https://developer.apple.com/documentation/homekit/testing-your-app-with-the-homekit-accessory-simulator", "Testing with HomeKit Accessory Simulator"),
    ("https://developer.apple.com/documentation/homekit/hmhomemanager", "HMHomeManager Class"),
    ("https://developer.apple.com/documentation/homekit/hmhome", "HMHome Class"),
    ("https://developer.apple.com/documentation/homekit/hmroom", "HMRoom Class"),
    ("https://developer.apple.com/documentation/homekit/hmaccessory", "HMAccessory Class"),
    ("https://developer.apple.com/documentation/homekit/hmservice", "HMService Class"),
    ("https://developer.apple.com/documentation/homekit/hmcharacteristic", "HMCharacteristic Class"),
    ("https://developer.apple.com/documentation/homekit/hmtrigger", "HMTrigger Class"),
    ("https://developer.apple.com/documentation/homekit/hmtimertrigger", "HMTimerTrigger Class"),
    ("https://developer.apple.com/documentation/homekit/hmeventtrigger", "HMEventTrigger Class"),
    ("https://developer.apple.com/documentation/homekit/hmactionset", "HMActionSet Class"),
    ("https://developer.apple.com/documentation/homekit/hmscene", "HMScene Class"),
    ("https://developer.apple.com/documentation/homekit/hmzone", "HMZone Class"),
    ("https://developer.apple.com/documentation/homekit/hmuser", "HMUser Class"),
    ("https://developer.apple.com/documentation/homekit/hmhomeaccessoryserver", "HMHomeAccessoryServer Class"),
    ("https://developer.apple.com/documentation/homekit/hmcamerainformation", "HMCameraInformation Class"),
    ("https://developer.apple.com/documentation/homekit/hmcameraprofile", "HMCameraProfile Class"),
    ("https://developer.apple.com/documentation/homekit/hmcamerastreamsetting", "HMCameraStreamSetting Class"),
    ("https://developer.apple.com/documentation/homekit/hmaccessorysetupmanager", "HMAccessorySetupManager Class"),
    ("https://developer.apple.com/documentation/homekit/hmerror", "HMError Enum"),
    ("https://developer.apple.com/documentation/homekit/hm accessorydelegateerror", "HMAccessoryDelegateError"),
]

documents: Dict[str, str] = {}


def fetch_with_curl(url: str) -> Optional[str]:
    """Fetch URL with curl."""
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', '--max-time', '15',
             '-H', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
             url],
            capture_output=True,
            text=True,
            timeout=20
        )
        if result.returncode == 0 and result.stdout:
            return result.stdout
        return None
    except Exception as e:
        logger.warning(f"Fetch error: {e}")
        return None


def extract_text_from_html(html: str) -> str:
    """Simple HTML text extraction without external libraries."""
    # Remove script and style tags
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)

    # Extract title from page title or h1
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1) if title_match else ""
    title = re.sub(r'<[^>]+>', '', title).replace(" | Apple Developer Documentation", "").strip()

    if not title:
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
        if h1_match:
            title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()

    # Extract content from main areas
    main_match = re.search(
        r'<(?:main|article|div[^>]*id=["\']?content["\']?)[^>]*>(.*?)</(?:main|article|div)>',
        html,
        re.IGNORECASE | re.DOTALL
    )

    content_html = main_match.group(1) if main_match else html

    # Remove nav, footer, and other cruft
    content_html = re.sub(r'<(?:nav|footer|button|script|style)[^>]*>.*?</(?:nav|footer|button|script|style)>', '', content_html, flags=re.DOTALL | re.IGNORECASE)

    # Extract text with basic structure
    lines = []

    # Headings
    for match in re.finditer(r'<h([1-6])[^>]*>(.*?)</h\1>', content_html, re.IGNORECASE | re.DOTALL):
        level = match.group(1)
        text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        if text:
            lines.append('#' * int(level) + ' ' + text)

    # Paragraphs
    for match in re.finditer(r'<p[^>]*>(.*?)</p>', content_html, re.IGNORECASE | re.DOTALL):
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if text and len(text) > 5:
            lines.append(text)

    # List items
    for match in re.finditer(r'<li[^>]*>(.*?)</li>', content_html, re.IGNORECASE | re.DOTALL):
        text = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if text:
            lines.append('- ' + text)

    # Code blocks
    for match in re.finditer(r'<pre[^>]*>(.*?)</pre>', content_html, re.IGNORECASE | re.DOTALL):
        text = match.group(1)
        lines.append('```\n' + text + '\n```')

    content = '\n\n'.join(lines).strip()

    # Clean up remaining HTML entities and tags
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'&nbsp;', ' ', content)
    content = re.sub(r'&amp;', '&', content)
    content = re.sub(r'&lt;', '<', content)
    content = re.sub(r'&gt;', '>', content)
    content = re.sub(r'&quot;', '"', content)

    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return title, content


def scrape_page(url: str, title: str) -> bool:
    """Scrape a single page."""
    logger.info(f"Fetching: {url}")

    html = fetch_with_curl(url)
    if not html:
        logger.info(f"  -> Failed to fetch")
        return False

    # Extract content
    page_title, content = extract_text_from_html(html)
    if not page_title:
        page_title = title

    if not content or len(content) < 100:
        logger.info(f"  -> Content too short")
        return False

    documents[page_title] = content
    logger.info(f"  -> OK ({len(content)} chars)")
    return True


def save_documents():
    """Save documents to files."""
    logger.info(f"\nSaving {len(documents)} documents...")

    if not documents:
        logger.error("No documents collected!")
        return

    # Save individual files
    for i, (title, content) in enumerate(documents.items(), 1):
        safe = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:75]
        filepath = OUTPUT_DIR / f"{i:03d}-{safe}.md"
        filepath.write_text(f"# {title}\n\n{content}", encoding='utf-8')
        logger.info(f"  [{i:2d}] {filepath.name}")

    # Save index
    index = OUTPUT_DIR / "INDEX.md"
    index_text = "# Apple HomeKit Framework Documentation\n\n"
    index_text += "Official Apple HomeKit framework documentation for iOS and macOS developers.\n\n"
    index_text += "## Documentation Source\n\n"
    index_text += "- [HomeKit Framework](https://developer.apple.com/documentation/homekit/)\n\n"
    index_text += "## Coverage\n\n"
    index_text += "This documentation covers:\n"
    index_text += "- HomeKit framework API reference\n"
    index_text += "- Home, room, accessory, and service management\n"
    index_text += "- Characteristic manipulation and observation\n"
    index_text += "- Home automation triggers and actions\n"
    index_text += "- Camera and video doorbell video streaming\n"
    index_text += "- Matter accessory support\n"
    index_text += "- Secure remote access\n"
    index_text += "- Permission and access control\n\n"
    index_text += "## Table of Contents\n\n"

    for i, title in enumerate(documents.keys(), 1):
        safe = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:75]
        index_text += f"{i}. [{title}](/docs/web-scraped/apple-homekit/{i:03d}-{safe}.md)\n"

    index.write_text(index_text, encoding='utf-8')
    logger.info(f"Index saved")


def main():
    """Main entry point."""
    logger.info("Apple HomeKit Framework Documentation Scraper")
    logger.info("=============================================\n")

    collected = 0
    for url, title in HOMEKIT_PAGES:
        if scrape_page(url, title):
            collected += 1

    save_documents()

    logger.info(f"\n{'='*70}")
    logger.info(f"Done! Collected {collected} pages")
    logger.info(f"Output: {OUTPUT_DIR}")
    logger.info(f"{'='*70}")


if __name__ == "__main__":
    main()

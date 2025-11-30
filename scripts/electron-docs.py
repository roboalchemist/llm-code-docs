#!/usr/bin/env python3
"""
Electron Documentation Scraper
Downloads all Electron documentation pages and converts to markdown.
Electron is a framework for building desktop applications using JavaScript, HTML, and CSS.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# Electron documentation pages from sidebars.js
# Organized by category for clarity
ELECTRON_DOC_PAGES = [
    # Get Started
    "/docs/latest/",  # Introduction page
    "/docs/latest/why-electron",
    # Tutorial (correct URLs without numbers)
    "/docs/latest/tutorial/tutorial-prerequisites",
    "/docs/latest/tutorial/tutorial-first-app",
    "/docs/latest/tutorial/tutorial-preload",
    "/docs/latest/tutorial/tutorial-adding-features",
    "/docs/latest/tutorial/tutorial-packaging",
    "/docs/latest/tutorial/tutorial-publishing-updating",
    # Processes in Electron
    "/docs/latest/tutorial/process-model",
    "/docs/latest/tutorial/context-isolation",
    "/docs/latest/tutorial/ipc",
    "/docs/latest/tutorial/sandbox",
    "/docs/latest/tutorial/message-ports",
    # Best Practices
    "/docs/latest/tutorial/performance",
    "/docs/latest/tutorial/security",
    # Examples
    "/docs/latest/tutorial/examples",
    "/docs/latest/tutorial/dark-mode",
    "/docs/latest/tutorial/devices",
    "/docs/latest/tutorial/in-app-purchases",
    "/docs/latest/tutorial/keyboard-shortcuts",
    "/docs/latest/tutorial/launch-app-from-url-in-another-app",
    "/docs/latest/tutorial/linux-desktop-actions",
    "/docs/latest/tutorial/menus",
    "/docs/latest/tutorial/application-menu",
    "/docs/latest/tutorial/context-menu",
    "/docs/latest/tutorial/macos-dock",
    "/docs/latest/tutorial/tray",
    "/docs/latest/tutorial/multithreading",
    "/docs/latest/tutorial/native-file-drag-drop",
    "/docs/latest/tutorial/navigation-history",
    "/docs/latest/tutorial/notifications",
    "/docs/latest/tutorial/offscreen-rendering",
    "/docs/latest/tutorial/online-offline-events",
    "/docs/latest/tutorial/progress-bar",
    "/docs/latest/tutorial/recent-documents",
    "/docs/latest/tutorial/represented-file",
    "/docs/latest/tutorial/spellchecker",
    "/docs/latest/tutorial/web-embeds",
    "/docs/latest/tutorial/windows-taskbar",
    "/docs/latest/tutorial/window-customization",
    "/docs/latest/tutorial/custom-title-bar",
    "/docs/latest/tutorial/custom-window-interactions",
    "/docs/latest/tutorial/custom-window-styles",
    # Development
    "/docs/latest/tutorial/accessibility",
    "/docs/latest/tutorial/installation",
    "/docs/latest/tutorial/asar-archives",
    "/docs/latest/tutorial/asar-integrity",
    "/docs/latest/tutorial/boilerplates-and-clis",
    "/docs/latest/tutorial/esm",
    "/docs/latest/tutorial/fuses",
    "/docs/latest/tutorial/windows-arm",
    # Native Node Modules
    "/docs/latest/tutorial/using-native-node-modules",
    "/docs/latest/tutorial/native-code-and-electron",
    "/docs/latest/tutorial/native-code-and-electron-cpp-win32",
    "/docs/latest/tutorial/native-code-and-electron-swift-macos",
    "/docs/latest/tutorial/native-code-and-electron-cpp-linux",
    # Distribution
    "/docs/latest/tutorial/forge-overview",
    "/docs/latest/tutorial/distribution-overview",
    "/docs/latest/tutorial/application-distribution",
    "/docs/latest/tutorial/code-signing",
    "/docs/latest/tutorial/updates",
    "/docs/latest/tutorial/mac-app-store-submission-guide",
    "/docs/latest/tutorial/windows-store-guide",
    "/docs/latest/tutorial/snapcraft",
    # Testing And Debugging
    "/docs/latest/tutorial/automated-testing",
    "/docs/latest/tutorial/debugging-main-process",
    "/docs/latest/tutorial/debugging-vscode",
    "/docs/latest/tutorial/repl",
    "/docs/latest/tutorial/devtools-extension",
    "/docs/latest/tutorial/application-debugging",
    "/docs/latest/tutorial/testing-on-headless-ci",
    # References
    "/docs/latest/breaking-changes",
    "/docs/latest/tutorial/electron-timelines",
    "/docs/latest/tutorial/electron-versioning",
    "/docs/latest/faq",
    "/docs/latest/glossary",
    # Contributing - Build Instructions
    "/docs/latest/development/build-instructions-gn",
    "/docs/latest/development/build-instructions-linux",
    "/docs/latest/development/build-instructions-macos",
    "/docs/latest/development/build-instructions-windows",
    "/docs/latest/development/reclient",
    # Contributing - Debugging
    "/docs/latest/development/debugging",
    "/docs/latest/development/debugging-on-macos",
    "/docs/latest/development/debugging-on-windows",
    "/docs/latest/development/debugging-with-xcode",
    "/docs/latest/development/debugging-with-symbol-server",
    # Contributing - Development Guides
    "/docs/latest/development/api-history-migration-guide",
    "/docs/latest/development/clang-tidy",
    "/docs/latest/development/coding-style",
    "/docs/latest/development/creating-api",
    "/docs/latest/development/patches",
    "/docs/latest/development/source-code-directory-structure",
    "/docs/latest/development/style-guide",
    "/docs/latest/development/testing",
    # Contributing - GitHub
    "/docs/latest/development/issues",
    "/docs/latest/development/pull-requests",
    # Contributing - Upstream Development
    "/docs/latest/development/chromium-development",
    "/docs/latest/development/v8-development",
    # API - Main Process Modules
    "/docs/latest/api/app",
    "/docs/latest/api/auto-updater",
    "/docs/latest/api/base-window",
    "/docs/latest/api/browser-view",
    "/docs/latest/api/browser-window",
    "/docs/latest/api/clipboard",
    "/docs/latest/api/content-tracing",
    "/docs/latest/api/crash-reporter",
    "/docs/latest/api/desktop-capturer",
    "/docs/latest/api/dialog",
    "/docs/latest/api/global-shortcut",
    "/docs/latest/api/image-view",
    "/docs/latest/api/in-app-purchase",
    "/docs/latest/api/ipc-main",
    "/docs/latest/api/menu",
    "/docs/latest/api/menu-item",
    "/docs/latest/api/message-channel-main",
    "/docs/latest/api/message-port-main",
    "/docs/latest/api/native-image",
    "/docs/latest/api/native-theme",
    "/docs/latest/api/net",
    "/docs/latest/api/net-log",
    "/docs/latest/api/notification",
    "/docs/latest/api/power-monitor",
    "/docs/latest/api/power-save-blocker",
    "/docs/latest/api/process",
    "/docs/latest/api/protocol",
    "/docs/latest/api/push-notifications",
    "/docs/latest/api/safe-storage",
    "/docs/latest/api/screen",
    "/docs/latest/api/session",
    "/docs/latest/api/share-menu",
    "/docs/latest/api/shell",
    "/docs/latest/api/system-preferences",
    "/docs/latest/api/touch-bar",
    "/docs/latest/api/tray",
    "/docs/latest/api/utility-process",
    "/docs/latest/api/web-contents",
    "/docs/latest/api/web-contents-view",
    "/docs/latest/api/web-frame-main",
    "/docs/latest/api/view",
    # API - Renderer Process Modules
    "/docs/latest/api/context-bridge",
    "/docs/latest/api/ipc-renderer",
    "/docs/latest/api/web-frame",
    "/docs/latest/api/web-utils",
    # API - Utility Process Modules
    "/docs/latest/api/parent-port",
    # API - Custom DOM Elements
    "/docs/latest/api/webview-tag",
    "/docs/latest/api/window-open",
    # API - Chromium and Node.js
    "/docs/latest/api/command-line-switches",
    "/docs/latest/api/environment-variables",
    "/docs/latest/api/extensions",
    # API - Classes
    "/docs/latest/api/client-request",
    "/docs/latest/api/command-line",
    "/docs/latest/api/cookies",
    "/docs/latest/api/debugger",
    "/docs/latest/api/dock",
    "/docs/latest/api/download-item",
    "/docs/latest/api/incoming-message",
    "/docs/latest/api/navigation-history",
    "/docs/latest/api/service-worker-main",
    "/docs/latest/api/service-workers",
    "/docs/latest/api/touch-bar-button",
    "/docs/latest/api/touch-bar-color-picker",
    "/docs/latest/api/touch-bar-group",
    "/docs/latest/api/touch-bar-label",
    "/docs/latest/api/touch-bar-other-items-proxy",
    "/docs/latest/api/touch-bar-popover",
    "/docs/latest/api/touch-bar-scrubber",
    "/docs/latest/api/touch-bar-segmented-control",
    "/docs/latest/api/touch-bar-slider",
    "/docs/latest/api/touch-bar-spacer",
    "/docs/latest/api/web-request",
    # API Structures
    "/docs/latest/api/structures/base-window-options",
    "/docs/latest/api/structures/bluetooth-device",
    "/docs/latest/api/structures/browser-window-options",
    "/docs/latest/api/structures/certificate",
    "/docs/latest/api/structures/certificate-principal",
    "/docs/latest/api/structures/color-space",
    "/docs/latest/api/structures/cookie",
    "/docs/latest/api/structures/cpu-usage",
    "/docs/latest/api/structures/crash-report",
    "/docs/latest/api/structures/custom-scheme",
    "/docs/latest/api/structures/desktop-capturer-source",
    "/docs/latest/api/structures/display",
    "/docs/latest/api/structures/extension",
    "/docs/latest/api/structures/extension-info",
    "/docs/latest/api/structures/file-filter",
    "/docs/latest/api/structures/file-path-with-headers",
    "/docs/latest/api/structures/filesystem-permission-request",
    "/docs/latest/api/structures/gpu-feature-status",
    "/docs/latest/api/structures/hid-device",
    "/docs/latest/api/structures/input-event",
    "/docs/latest/api/structures/ipc-main-event",
    "/docs/latest/api/structures/ipc-main-invoke-event",
    "/docs/latest/api/structures/ipc-renderer-event",
    "/docs/latest/api/structures/jump-list-category",
    "/docs/latest/api/structures/jump-list-item",
    "/docs/latest/api/structures/keyboard-event",
    "/docs/latest/api/structures/keyboard-input-event",
    "/docs/latest/api/structures/media-access-permission-request",
    "/docs/latest/api/structures/memory-info",
    "/docs/latest/api/structures/memory-usage-details",
    "/docs/latest/api/structures/mime-typed-buffer",
    "/docs/latest/api/structures/mouse-input-event",
    "/docs/latest/api/structures/mouse-wheel-input-event",
    "/docs/latest/api/structures/navigation-entry",
    "/docs/latest/api/structures/notification-action",
    "/docs/latest/api/structures/notification-response",
    "/docs/latest/api/structures/offscreen-shared-texture",
    "/docs/latest/api/structures/open-external-permission-request",
    "/docs/latest/api/structures/payment-discount",
    "/docs/latest/api/structures/permission-request",
    "/docs/latest/api/structures/point",
    "/docs/latest/api/structures/post-body",
    "/docs/latest/api/structures/printer-info",
    "/docs/latest/api/structures/process-memory-info",
    "/docs/latest/api/structures/process-metric",
    "/docs/latest/api/structures/product",
    "/docs/latest/api/structures/product-discount",
    "/docs/latest/api/structures/product-subscription-period",
    "/docs/latest/api/structures/protocol-request",
    "/docs/latest/api/structures/protocol-response",
    "/docs/latest/api/structures/protocol-response-upload-data",
    "/docs/latest/api/structures/proxy-config",
    "/docs/latest/api/structures/rectangle",
    "/docs/latest/api/structures/referrer",
    "/docs/latest/api/structures/render-process-gone-details",
    "/docs/latest/api/structures/resolved-endpoint",
    "/docs/latest/api/structures/resolved-host",
    "/docs/latest/api/structures/scrubber-item",
    "/docs/latest/api/structures/segmented-control-segment",
    "/docs/latest/api/structures/serial-port",
    "/docs/latest/api/structures/service-worker-info",
    "/docs/latest/api/structures/shared-worker-info",
    "/docs/latest/api/structures/sharing-item",
    "/docs/latest/api/structures/shortcut-details",
    "/docs/latest/api/structures/size",
    "/docs/latest/api/structures/task",
    "/docs/latest/api/structures/thumbar-button",
    "/docs/latest/api/structures/trace-categories-and-options",
    "/docs/latest/api/structures/trace-config",
    "/docs/latest/api/structures/transaction",
    "/docs/latest/api/structures/upload-data",
    "/docs/latest/api/structures/upload-file",
    "/docs/latest/api/structures/upload-raw-data",
    "/docs/latest/api/structures/usb-device",
    "/docs/latest/api/structures/user-default-types",
    "/docs/latest/api/structures/web-preferences",
    "/docs/latest/api/structures/web-request-filter",
    "/docs/latest/api/structures/web-source",
    "/docs/latest/api/structures/window-open-handler-response",
    "/docs/latest/api/structures/shared-dictionary-info",
    "/docs/latest/api/structures/shared-dictionary-usage-info",
]

BASE_URL = "https://www.electronjs.org"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Electron uses Docusaurus, extract main article content
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try alternate selector for main content
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove navigation elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Remove "Edit this page" and pagination links
    html_content = re.sub(r'<a[^>]*>Edit this page</a>', '', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*pagination[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc for conversion
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    # Remove /docs/latest/ prefix
    clean_path = path.replace("/docs/latest/", "")

    if clean_path == "" or clean_path == "/":
        return "index.md"

    # Remove leading/trailing slashes
    clean_path = clean_path.strip("/")

    # Handle nested paths like api/structures/cookie
    if "/" in clean_path:
        # Convert to flat filename: api/structures/cookie -> api-structures-cookie.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all Electron documentation."""
    print("=" * 60)
    print("Electron Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(ELECTRON_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "electron"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(ELECTRON_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(ELECTRON_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.3)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()

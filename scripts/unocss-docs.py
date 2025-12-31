#!/usr/bin/env python3
"""
UnoCSS Documentation Scraper
Downloads UnoCSS documentation from GitHub repository and converts to markdown.
UnoCSS is an instant on-demand atomic CSS engine.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for UnoCSS GitHub repository
RAW_BASE_URL = "https://raw.githubusercontent.com/unocss/unocss/main"

# Complete list of documentation files (manually compiled from UnoCSS site structure)
DOC_FILES = [
    "README.md",
    "docs/index.md",
    # Guide
    "docs/guide/index.md",
    "docs/guide/why.md",
    "docs/guide/presets.md",
    "docs/guide/style-reset.md",
    "docs/guide/config-file.md",
    "docs/guide/extracting.md",
    "docs/guide/packages.md",
    # Config
    "docs/config/index.md",
    "docs/config/rules.md",
    "docs/config/variants.md",
    "docs/config/shortcuts.md",
    "docs/config/theme.md",
    "docs/config/extractors.md",
    "docs/config/preflights.md",
    "docs/config/safelist.md",
    "docs/config/layers.md",
    "docs/config/presets.md",
    "docs/config/transformers.md",
    "docs/config/autocomplete.md",
    # Integrations
    "docs/integrations/index.md",
    "docs/integrations/vite.md",
    "docs/integrations/nuxt.md",
    "docs/integrations/next.md",
    "docs/integrations/astro.md",
    "docs/integrations/svelte-scoped.md",
    "docs/integrations/webpack.md",
    "docs/integrations/runtime.md",
    "docs/integrations/cli.md",
    "docs/integrations/postcss.md",
    "docs/integrations/eslint.md",
    "docs/integrations/vscode.md",
    "docs/integrations/jetbrains.md",
    "docs/integrations/lsp.md",
    # Presets
    "docs/presets/index.md",
    "docs/presets/mini.md",
    "docs/presets/wind3.md",
    "docs/presets/wind4.md",
    "docs/presets/icons.md",
    "docs/presets/attributify.md",
    "docs/presets/typography.md",
    "docs/presets/web-fonts.md",
    "docs/presets/legacy-compat.md",
    "docs/presets/tagify.md",
    "docs/presets/rem-to-px.md",
    "docs/presets/community.md",
    # Transformers
    "docs/transformers/variant-group.md",
    "docs/transformers/directives.md",
    "docs/transformers/compile-class.md",
    "docs/transformers/attributify-jsx.md",
    # Extractors
    "docs/extractors/pug.md",
    "docs/extractors/mdc.md",
    "docs/extractors/svelte.md",
    "docs/extractors/arbitrary-variants.md",
    # Tools
    "docs/tools/inspector.md",
    "docs/tools/core.md",
    "docs/tools/autocomplete.md",
]


def download_file(repo_path, output_path):
    """Download a file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# UnoCSS Documentation
# Source: {raw_url}
# Path: {repo_path}

"""
        content = header + content

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def main():
    """Main function to download all UnoCSS documentation."""
    print("=" * 60)
    print("UnoCSS Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "unocss"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print(f"Found {len(DOC_FILES)} files to download")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(DOC_FILES, 1):
        print(f"[{idx:2d}/{len(DOC_FILES)}] ", end="")

        # Create output filename
        # Convert path like "docs/guide/index.md" to "guide-index.md"
        if repo_path == "README.md":
            output_filename = "main-README.md"
        elif repo_path == "docs/index.md":
            output_filename = "docs-index.md"
        elif repo_path.startswith("docs/"):
            # Remove "docs/" prefix
            relative_path = repo_path.replace("docs/", "")
            # Replace slashes with dashes
            output_filename = relative_path.replace("/", "-")
        else:
            output_filename = repo_path.replace("/", "-")

        output_path = output_dir / output_filename

        if download_file(repo_path, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()

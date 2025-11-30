#!/usr/bin/env python3
"""
DagsHub Documentation Scraper
Downloads all DagsHub documentation pages and converts to markdown.
DagsHub is a platform for managing multimodal AI data and models,
with features for dataset curation, experiment tracking, and model management.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# DagsHub documentation pages discovered from sitemap
DAGSHUB_DOC_PAGES = [
    # Main docs
    "/docs/",
    "/docs/quick_start/",
    "/docs/quick_start/upload_data/",
    "/docs/quick_start/version_data/",
    "/docs/quick_start/create_dataset/",
    "/docs/quick_start/query_data/",
    "/docs/quick_start/connect_existing_project/",
    # Feature Guide
    "/docs/feature_guide/",
    "/docs/feature_guide/experiment_tracking/",
    "/docs/feature_guide/data_engine/",
    "/docs/feature_guide/dagshub_storage/",
    "/docs/feature_guide/annotations/",
    "/docs/feature_guide/dagshub_diffing/",
    "/docs/feature_guide/dagshub_discussions/",
    "/docs/feature_guide/pipeline/",
    "/docs/feature_guide/data_science_pull_requests/",
    "/docs/feature_guide/topics/",
    "/docs/feature_guide/project_templates/",
    "/docs/feature_guide/automation/",
    # Use Cases
    "/docs/use_cases/",
    "/docs/use_cases/data_engine/",
    "/docs/use_cases/data_engine/connect_datasource/",
    "/docs/use_cases/data_engine/version_datasets/",
    "/docs/use_cases/data_engine/enrich_datasource/",
    "/docs/use_cases/data_engine/query_and_create_subsets/",
    "/docs/use_cases/data_engine/visualizing_datasets/",
    "/docs/use_cases/data_engine/train_model/",
    "/docs/use_cases/annotation/",
    "/docs/use_cases/data_versioning/",
    "/docs/use_cases/deploy_ml_model_to_cloud/",
    "/docs/use_cases/reproduce_experiment_results/",
    # Integration Guide
    "/docs/integration_guide/",
    "/docs/integration_guide/github/",
    "/docs/integration_guide/google_colab/",
    "/docs/integration_guide/dvc/",
    "/docs/integration_guide/mlflow_tracking/",
    "/docs/integration_guide/jenkins/",
    "/docs/integration_guide/label_studio/",
    "/docs/integration_guide/set_up_remote_storage_for_data_and_models/",
    "/docs/integration_guide/webhook/",
    "/docs/integration_guide/pycaret/",
    "/docs/integration_guide/giskard/",
    "/docs/integration_guide/hugging_face/",
    "/docs/integration_guide/weights_and_biases/",
    "/docs/integration_guide/connect_a_git_server_to_dagshub/",
    # Tutorials
    "/docs/tutorials/",
    "/docs/tutorials/pipeline_tutorial/setup/",
    "/docs/tutorials/experiment_tutorial/0_data/",
    "/docs/tutorials/experiment_tutorial/2_data_versioning/",
    # API and Client
    "/docs/api/",
    "/docs/client/",
    "/docs/client/index.html",
    # Reference
    "/docs/troubleshooting/",
    "/docs/faq/",
]

BASE_URL = "https://dagshub.com"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # DagsHub uses MkDocs Material - extract main article content
    article_match = re.search(
        r'<article[^>]*class="[^"]*md-content__inner[^"]*"[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try alternate selector for md-content
        main_match = re.search(
            r'<div[^>]*class="[^"]*md-content[^"]*"[^>]*>(.*?)</div>\s*(?:<script|<footer)',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove tabbed content duplicates (MkDocs shows same content in tabs)
    html_content = re.sub(r'<div[^>]*class="[^"]*tabbed-block[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)

    # Try pandoc on cleaned content
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
    if path == "/docs/" or path == "/docs":
        return "index.md"

    # Remove /docs/ prefix and trailing slashes
    clean_path = path.replace("/docs/", "").strip("/")

    # Handle .html files
    if clean_path.endswith(".html"):
        clean_path = clean_path.replace(".html", "")

    # Handle nested paths like quick_start/upload_data -> quick_start-upload_data.md
    if "/" in clean_path:
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all DagsHub documentation."""
    print("=" * 60)
    print("DagsHub Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(DAGSHUB_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "dagshub"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(DAGSHUB_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(DAGSHUB_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
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

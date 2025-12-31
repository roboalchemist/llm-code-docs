#!/usr/bin/env python3
"""
SendGrid Documentation Scraper
Downloads SendGrid documentation from official GitHub repositories.
SendGrid is an email delivery platform providing transactional and marketing email services.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for SendGrid GitHub repositories
RAW_BASE_URL = "https://raw.githubusercontent.com/sendgrid"

# Files to download from various SendGrid repositories
FILES_TO_DOWNLOAD = [
    # Main Node.js library
    ("sendgrid-nodejs/main/README.md", "sendgrid-nodejs-README.md"),
    ("sendgrid-nodejs/main/CONTRIBUTING.md", "sendgrid-nodejs-CONTRIBUTING.md"),
    ("sendgrid-nodejs/main/TROUBLESHOOTING.md", "sendgrid-nodejs-TROUBLESHOOTING.md"),

    # Main Python library
    ("sendgrid-python/main/README.md", "sendgrid-python-README.md"),
    ("sendgrid-python/main/CONTRIBUTING.md", "sendgrid-python-CONTRIBUTING.md"),
    ("sendgrid-python/main/TROUBLESHOOTING.md", "sendgrid-python-TROUBLESHOOTING.md"),

    # Go library
    ("sendgrid-go/main/README.md", "sendgrid-go-README.md"),
    ("sendgrid-go/main/TROUBLESHOOTING.md", "sendgrid-go-TROUBLESHOOTING.md"),

    # PHP library
    ("sendgrid-php/main/README.md", "sendgrid-php-README.md"),
    ("sendgrid-php/main/TROUBLESHOOTING.md", "sendgrid-php-TROUBLESHOOTING.md"),
    ("sendgrid-php/main/USE_CASES.md", "sendgrid-php-USE_CASES.md"),

    # Ruby library
    ("sendgrid-ruby/main/README.md", "sendgrid-ruby-README.md"),
    ("sendgrid-ruby/main/TROUBLESHOOTING.md", "sendgrid-ruby-TROUBLESHOOTING.md"),

    # C# library
    ("sendgrid-csharp/main/README.md", "sendgrid-csharp-README.md"),
    ("sendgrid-csharp/main/TROUBLESHOOTING.md", "sendgrid-csharp-TROUBLESHOOTING.md"),
    ("sendgrid-csharp/main/USE_CASES.md", "sendgrid-csharp-USE_CASES.md"),

    # Java library
    ("sendgrid-java/main/README.md", "sendgrid-java-README.md"),
    ("sendgrid-java/main/TROUBLESHOOTING.md", "sendgrid-java-TROUBLESHOOTING.md"),
]


def download_file(repo_path, output_filename, output_dir):
    """Download a file from SendGrid GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# SendGrid Documentation
# Source: {raw_url}
# Path: {repo_path}

"""
        content = header + content

        # Create output file
        output_path = output_dir / output_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def main():
    """Main function to download all SendGrid documentation."""
    print("=" * 60)
    print("SendGrid Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "sendgrid"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, (repo_path, output_filename) in enumerate(FILES_TO_DOWNLOAD, 1):
        print(f"[{idx:2d}/{len(FILES_TO_DOWNLOAD)}] ", end="")

        if download_file(repo_path, output_filename, output_dir):
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*") if f.is_file())
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

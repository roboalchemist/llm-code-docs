#!/usr/bin/env python3
"""
Ultralytics YOLOv8 Documentation Scraper
Downloads YOLOv8 documentation from GitHub repository and converts to markdown.
YOLOv8 is a state-of-the-art object detection, segmentation, and classification framework.
"""

import os
import sys
import requests
from pathlib import Path
import time
from urllib.parse import urljoin
import re

# GitHub raw content base URL for Ultralytics docs
BASE_URL = "https://raw.githubusercontent.com/ultralytics/ultralytics/main/docs/en/"

# Key documentation sections to scrape for YOLOv8
DOCS_SECTIONS = {
    # Core documentation
    "index.md": "Home",
    "quickstart.md": "Quickstart Guide",

    # Models
    "models/index.md": "Models Overview",
    "models/yolov8.md": "YOLOv8",
    "models/yolov9.md": "YOLOv9",
    "models/yolo11.md": "YOLO11",

    # Tasks
    "tasks/index.md": "Tasks Overview",
    "tasks/detect.md": "Object Detection",
    "tasks/segment.md": "Segmentation",
    "tasks/classify.md": "Classification",
    "tasks/pose.md": "Pose Estimation",
    "tasks/obb.md": "Oriented Bounding Boxes",

    # Modes
    "modes/index.md": "Modes Overview",
    "modes/predict.md": "Prediction",
    "modes/train.md": "Training",
    "modes/val.md": "Validation",
    "modes/export.md": "Export",
    "modes/track.md": "Tracking",
    "modes/benchmark.md": "Benchmark",

    # Usage
    "usage/index.md": "Usage Overview",
    "usage/cfg.md": "Configuration",
    "usage/callbacks.md": "Callbacks",
    "usage/data.md": "Data Handling",

    # Guides
    "guides/index.md": "Guides Overview",
    "guides/steps-of-a-cv-project.md": "CV Project Steps",
    "guides/security.md": "Security",
    "guides/region-plots.md": "Region Plots",
    "guides/heatmaps.md": "Heatmaps",
    "guides/object-counting.md": "Object Counting",
    "guides/speed-accuracy-tradeoff.md": "Speed vs Accuracy",
    "guides/deep-learning-interview-questions.md": "DL Interview Questions",

    # Integrations
    "integrations/index.md": "Integrations Overview",
    "integrations/amazon-sagemaker.md": "Amazon SageMaker",
    "integrations/clearml.md": "ClearML",
    "integrations/comet.md": "Comet ML",
    "integrations/dvc.md": "DVC",
    "integrations/mlflow.md": "MLFlow",
    "integrations/ray-tune.md": "Ray Tune",
    "integrations/tensorboard.md": "TensorBoard",
    "integrations/wandb.md": "Weights & Biases",

    # Help & Reference
    "help/index.md": "Help Overview",
    "reference/index.md": "API Reference",
}

REQUEST_DELAY = 0.3  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove .md extension, we'll add it back
    if path.endswith('.md'):
        path = path[:-3]

    # Replace slashes with dashes
    safe = path.replace("/", "-")

    # Ensure .md extension
    if not safe.endswith('.md'):
        safe = safe + '.md'

    return safe


def download_file(relative_path, output_dir):
    """Download a documentation file from GitHub."""
    try:
        url = BASE_URL + relative_path
        filename = sanitize_filename(relative_path)

        print(f"  Downloading: {relative_path}")

        response = requests.get(url, timeout=15)

        if response.status_code == 404:
            print(f"    -> Not found (404): {relative_path}")
            return False

        response.raise_for_status()

        content = response.text

        # Add metadata header if not already present
        if not content.startswith('# '):
            header = f"""# Source: {url}

"""
            content = header + content
        else:
            # Add source URL at the top
            lines = content.split('\n')
            insert_pos = 0
            # Find first non-heading line
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    insert_pos = i + 1
            lines.insert(insert_pos, f"Source: {url}\n")
            content = '\n'.join(lines)

        # Save to file
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {relative_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {relative_path}: {e}")
        return False


def main():
    """Main function to download Ultralytics YOLOv8 documentation."""
    print("=" * 70)
    print("Ultralytics YOLOv8 Documentation Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "ultralytics-yolov8"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all documentation files
    print("Downloading documentation files...")
    print()

    successful = 0
    failed = 0
    skipped = 0
    start_time = time.time()

    total_files = len(DOCS_SECTIONS)

    for idx, (file_path, description) in enumerate(DOCS_SECTIONS.items(), 1):
        print(f"[{idx:2d}/{total_files:2d}] {description:30s} ", end="")

        if download_file(file_path, output_dir):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    md_files = list(output_dir.glob("**/*.md"))
    total_size = sum(f.stat().st_size for f in md_files)
    print(f"Total files: {len(md_files)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        print("Note: Some documentation sections may not exist in the current version")
    else:
        print("All documentation downloaded successfully!")

    print()
    sys.exit(0 if failed <= len(DOCS_SECTIONS) // 2 else 1)


if __name__ == "__main__":
    main()

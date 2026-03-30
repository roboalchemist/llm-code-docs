#!/usr/bin/env python3
"""
Apache Airflow Documentation Extractor
Extracts documentation from apache/airflow GitHub repository.
Apache Airflow is an open-source workflow orchestration platform for authoring, scheduling, and monitoring data pipelines.
"""

import subprocess
import shutil
import tempfile
from pathlib import Path
import sys
import os

def extract_airflow_docs():
    """Extract Apache Airflow documentation from GitHub repository."""
    print("=" * 70)
    print("Apache Airflow Documentation Extractor")
    print("=" * 70)
    print()

    # Paths
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "apache-airflow"
    repo_url = "https://github.com/apache/airflow.git"
    docs_source = "airflow-core/docs"

    print(f"Repository: {repo_url}")
    print(f"Source folder: {docs_source}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        clone_path = temp_path / "airflow"

        print("Cloning repository (sparse checkout for docs only)...")
        try:
            # Clone with sparse checkout to speed up
            subprocess.run(
                ["git", "clone", "--depth=1", "--filter=blob:none", "--sparse", repo_url],
                cwd=temp_path,
                capture_output=True,
                text=True,
                timeout=300,
                check=True
            )

            # Configure sparse checkout for docs only
            subprocess.run(
                ["git", "sparse-checkout", "set", docs_source],
                cwd=clone_path,
                capture_output=True,
                text=True,
                timeout=60,
                check=True
            )

            print("✓ Repository cloned successfully")
            print()

            # Check if docs folder exists
            docs_path = clone_path / docs_source
            if not docs_path.exists():
                print(f"✗ Error: Documentation folder '{docs_source}' not found in repository")
                return False

            # Remove existing output directory
            if output_dir.exists():
                print(f"Removing existing documentation directory...")
                shutil.rmtree(output_dir)

            # Copy docs to output directory
            print(f"Copying documentation to {output_dir}...")
            shutil.copytree(docs_path, output_dir)

            print("✓ Documentation extracted successfully")
            print()

            # Print summary
            if output_dir.exists():
                file_count = sum(1 for _ in output_dir.rglob("*") if _.is_file())
                dir_count = sum(1 for _ in output_dir.rglob("*") if _.is_dir())
                print("=" * 70)
                print("Extraction Summary")
                print("=" * 70)
                print(f"Output directory: {output_dir}")
                print(f"Files extracted: {file_count}")
                print(f"Subdirectories: {dir_count}")
                print()
                return True
            else:
                print("✗ Error: Failed to extract documentation")
                return False

        except subprocess.CalledProcessError as e:
            print(f"✗ Error during git operation: {e.stderr}")
            return False
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

if __name__ == "__main__":
    success = extract_airflow_docs()
    sys.exit(0 if success else 1)

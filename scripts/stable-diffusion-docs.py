#!/usr/bin/env python3
"""
Stable Diffusion Documentation Extractor
Clones the CompVis/stable-diffusion repository and extracts README and configuration files.
Stable Diffusion is a latent text-to-image diffusion model for image synthesis from text prompts.
"""

import os
import sys
import subprocess
import shutil
import tempfile
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "stable-diffusion"


def run_command(cmd, cwd=None, timeout=300):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds: {cmd}")
        return 1, "", "Timeout"


def clone_stable_diffusion_repo():
    """Clone the Stable Diffusion repository and extract key files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "stable-diffusion"
        print(f"Cloning CompVis/stable-diffusion repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 --branch main https://github.com/CompVis/stable-diffusion.git {repo_path}",
            timeout=300
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        print(f"Cloned successfully. Extracting documentation files...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Extract key documentation files
        doc_files = [
            "README.md",
            "Stable_Diffusion_v1_Model_Card.md",
            "environment.yaml",
            "setup.py",
        ]

        # Copy root-level documentation files
        for doc_file in doc_files:
            src = repo_path / doc_file
            if src.exists():
                dst = OUTPUT_DIR / doc_file
                shutil.copy2(src, dst)
                print(f"  Extracted: {doc_file}")

        # Copy configs folder (contains model configurations)
        configs_src = repo_path / "configs"
        if configs_src.exists():
            configs_dst = OUTPUT_DIR / "configs"
            shutil.copytree(configs_src, configs_dst)
            print(f"  Extracted: configs/ (model configurations)")

        # Copy scripts folder (contains inference and training scripts)
        scripts_src = repo_path / "scripts"
        if scripts_src.exists():
            scripts_dst = OUTPUT_DIR / "scripts"
            shutil.copytree(scripts_src, scripts_dst)
            print(f"  Extracted: scripts/ (inference and training scripts)")

        # Copy ldm folder (contains the latent diffusion model implementation)
        ldm_src = repo_path / "ldm"
        if ldm_src.exists():
            ldm_dst = OUTPUT_DIR / "ldm"
            shutil.copytree(ldm_src, ldm_dst)
            print(f"  Extracted: ldm/ (model implementation)")

        print(f"Extracted to {OUTPUT_DIR}")

        # Count files
        all_files = list(OUTPUT_DIR.glob("**/*"))
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        py_files = list(OUTPUT_DIR.glob("**/*.py"))
        yaml_files = list(OUTPUT_DIR.glob("**/*.yaml"))

        print(f"Total files extracted: {len([f for f in all_files if f.is_file()])}")
        print(f"  - Markdown files: {len(md_files)}")
        print(f"  - Python files: {len(py_files)}")
        print(f"  - YAML files: {len(yaml_files)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Stable Diffusion Documentation Extractor")
    print("=" * 70)

    success = clone_stable_diffusion_repo()

    if success:
        print("\nStable Diffusion documentation extracted successfully!")
        return 0
    else:
        print("\nFailed to extract Stable Diffusion documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

"""Content hashing utilities for incremental updates."""

import hashlib
from pathlib import Path
from typing import Dict


def hash_file(file_path: Path) -> str:
    """
    Compute SHA256 hash of a file's contents.

    Args:
        file_path: Path to the file.

    Returns:
        Hexadecimal hash string.
    """
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as f:
        # Read in chunks to handle large files
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)

    return sha256.hexdigest()


def hash_string(content: str) -> str:
    """
    Compute SHA256 hash of a string.

    Args:
        content: String content to hash.

    Returns:
        Hexadecimal hash string.
    """
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def hash_files(file_paths: list[Path]) -> Dict[str, str]:
    """
    Compute hashes for multiple files.

    Args:
        file_paths: List of file paths to hash.

    Returns:
        Dictionary mapping file paths (as strings) to their hashes.
    """
    hashes = {}
    for path in file_paths:
        try:
            hashes[str(path)] = hash_file(path)
        except Exception as e:
            print(f"Warning: Could not hash {path}: {e}")
            continue
    return hashes

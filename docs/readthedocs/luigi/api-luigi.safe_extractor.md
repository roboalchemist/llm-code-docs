# luigi.safe_extractor

This module provides a class SafeExtractor that offers a secure way to extract tar files while
mitigating path traversal vulnerabilities, which can occur when files inside the archive are
crafted to escape the intended extraction directory.

The SafeExtractor ensures that the extracted file paths are validated before extraction to
prevent malicious archives from extracting files outside the intended directory.

Classes:

SafeExtractor: A class to securely extract tar files with protection against path traversal attacks.

Usage Example:

extractor = SafeExtractor(“/desired/directory”)
extractor.safe_extract(“archive.tar”)

Classes

`SafeExtractor`([path])

A class to safely extract tar files, ensuring that no path traversal vulnerabilities are exploited.

class luigi.safe_extractor.SafeExtractor(*path='.'*)

A class to safely extract tar files, ensuring that no path traversal
vulnerabilities are exploited.

Attributes:

path (str): The directory to extract files into.

Methods:
_is_within_directory(directory, target):

Checks if a target path is within a given directory.

safe_extract(tar_path, members=None, *, numeric_owner=False):

Safely extracts the contents of a tar file to the specified directory.

Initializes the SafeExtractor with the specified directory path.

Args:

path (str): The directory to extract files into. Defaults to the current directory.

safe_extract(*tar_path*, *members=None*, ***, *numeric_owner=False*)

Safely extracts the contents of a tar file to the specified directory.

Args:

tar_path (str): The path to the tar file to extract.
members (list, optional): A list of members to extract. Defaults to None.
numeric_owner (bool, optional): If True, only the numeric owner will be used. Defaults to False.

Raises:

RuntimeError: If a path traversal attempt is detected.
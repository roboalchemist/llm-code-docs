# Source: https://anyio.readthedocs.io/en/stable/tempfile.html

Title: Asynchronous Temporary File and Directory — AnyIO 0.0.post50 documentation

URL Source: https://anyio.readthedocs.io/en/stable/tempfile.html

Markdown Content:
This module provides asynchronous wrappers for handling temporary files and directories using the [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "(in Python v3.14)") module. The asynchronous methods execute blocking operations in worker threads.

Temporary File[](https://anyio.readthedocs.io/en/stable/tempfile.html#temporary-file "Link to this heading")
-------------------------------------------------------------------------------------------------------------

[`TemporaryFile`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TemporaryFile "anyio.TemporaryFile") creates a temporary file that is automatically deleted upon closure.

**Example:**

from anyio import TemporaryFile, run

async def main():
    async with TemporaryFile(mode="w+") as f:
        await f.write("Temporary file content")
        await f.seek(0)
        print(await f.read())  # Output: Temporary file content

run(main)

Named Temporary File[](https://anyio.readthedocs.io/en/stable/tempfile.html#named-temporary-file "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

[`NamedTemporaryFile`](https://anyio.readthedocs.io/en/stable/api.html#anyio.NamedTemporaryFile "anyio.NamedTemporaryFile") works similarly to [`TemporaryFile`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TemporaryFile "anyio.TemporaryFile"), but the file has a visible name in the filesystem.

**Example:**

from anyio import NamedTemporaryFile, run

async def main():
    async with NamedTemporaryFile(mode="w+", delete=True) as f:
        print(f"Temporary file name: {f.name}")
        await f.write("Named temp file content")
        await f.seek(0)
        print(await f.read())

run(main)

Spooled Temporary File[](https://anyio.readthedocs.io/en/stable/tempfile.html#spooled-temporary-file "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

[`SpooledTemporaryFile`](https://anyio.readthedocs.io/en/stable/api.html#anyio.SpooledTemporaryFile "anyio.SpooledTemporaryFile") is useful when temporary data is small and should be kept in memory rather than written to disk.

**Example:**

from anyio import SpooledTemporaryFile, run

async def main():
    async with SpooledTemporaryFile(max_size=1024, mode="w+") as f:
        await f.write("Spooled temp file content")
        await f.seek(0)
        print(await f.read())

run(main)

Temporary Directory[](https://anyio.readthedocs.io/en/stable/tempfile.html#temporary-directory "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

The [`TemporaryDirectory`](https://anyio.readthedocs.io/en/stable/api.html#anyio.TemporaryDirectory "anyio.TemporaryDirectory") provides an asynchronous way to create temporary directories.

**Example:**

from anyio import TemporaryDirectory, run

async def main():
    async with TemporaryDirectory() as temp_dir:
        print(f"Temporary directory path: {temp_dir}")

run(main)

Low-Level Temporary File and Directory Creation[](https://anyio.readthedocs.io/en/stable/tempfile.html#low-level-temporary-file-and-directory-creation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more control, the module provides lower-level functions:

*   [`mkstemp()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.mkstemp "anyio.mkstemp") - Creates a temporary file and returns a tuple of file descriptor and path.

*   [`mkdtemp()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.mkdtemp "anyio.mkdtemp") - Creates a temporary directory and returns the directory path.

*   [`gettempdir()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.gettempdir "anyio.gettempdir") - Returns the path of the default temporary directory.

*   [`gettempdirb()`](https://anyio.readthedocs.io/en/stable/api.html#anyio.gettempdirb "anyio.gettempdirb") - Returns the path of the default temporary directory in bytes.

**Example:**

from anyio import mkstemp, mkdtemp, gettempdir, run
import os

async def main():
    fd, path = await mkstemp(suffix=".txt", prefix="mkstemp_", text=True)
    print(f"Created temp file: {path}")

    temp_dir = await mkdtemp(prefix="mkdtemp_")
    print(f"Created temp dir: {temp_dir}")

    print(f"Default temp dir: {await gettempdir()}")

    os.remove(path)

run(main)

Note

Using these functions requires manual cleanup of the created files and directories.

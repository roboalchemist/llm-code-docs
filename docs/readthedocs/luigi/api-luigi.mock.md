# luigi.mock

This module provides a class `MockTarget`, an implementation of `Target`.
`MockTarget` contains all data in-memory.
The main purpose is unit testing workflows without writing to disk.

Classes

`MockFileSystem`()

MockFileSystem inspects/modifies _data to simulate file system operations.

`MockTarget`(fn[, is_tmp, mirror_on_stderr, ...])

Initializes a FileSystemTarget instance.

class luigi.mock.MockFileSystem

MockFileSystem inspects/modifies _data to simulate file system operations.

copy(*path*, *dest*, *raise_if_exists=False*)

Copies the contents of a single file path to dest

get_all_data()

get_data(*fn*)

exists(*path*)

Return `True` if file or directory at `path` exist, `False` otherwise

Parameters:

**path** (*str*) – a path within the FileSystem to check for existence.

remove(*path*, *recursive=True*, *skip_trash=True*)

Removes the given mockfile. skip_trash doesn’t have any meaning.

move(*path*, *dest*, *raise_if_exists=False*)

Moves a single file from path to dest

listdir(*path*)

listdir does a prefix match of self.get_all_data(), but doesn’t yet support globs.

isdir(*path*)

Return `True` if the location at `path` is a directory. If not, return `False`.

Parameters:

**path** (*str*) – a path within the FileSystem to check as a directory.

*Note*: This method is optional, not all FileSystem subclasses implements it.

mkdir(*path*, *parents=True*, *raise_if_exists=False*)

mkdir is a noop.

clear()

class luigi.mock.MockTarget(*fn*, *is_tmp=None*, *mirror_on_stderr=False*, *format=None*)

Initializes a FileSystemTarget instance.

Parameters:

**path** – the path associated with this FileSystemTarget.

fs = <luigi.mock.MockFileSystem object>

exists()

Returns `True` if the path for this FileSystemTarget exists; `False` otherwise.

This method is implemented by using `fs`.

move(*path*, *raise_if_exists=False*)

Call MockFileSystem’s move command

rename(**args*, ***kwargs*)

Call move to rename self

open(*mode='r'*)

Open the FileSystem target.

This method returns a file-like object which can either be read from or written to depending
on the specified mode.

Parameters:

**mode** (*str*) – the mode r opens the FileSystemTarget in read-only mode, whereas w will
open the FileSystemTarget in write mode. Subclasses can implement
additional options. Using b is not supported; initialize with
format=Nop instead.
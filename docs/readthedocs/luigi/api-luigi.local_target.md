# luigi.local_target

`LocalTarget` provides a concrete implementation of a `Target` class that uses files on the local file system

Classes

`LocalFileSystem`()

Wrapper for access to file system operations.

`LocalTarget`([path, format, is_tmp])

Initializes a FileSystemTarget instance.

`atomic_file`(path)

Simple class that writes to a temp file and moves it on close() Also cleans up the temp file if close is not invoked

class luigi.local_target.atomic_file(*path*)

Simple class that writes to a temp file and moves it on close()
Also cleans up the temp file if close is not invoked

move_to_final_destination()

generate_tmp_path(*path*)

class luigi.local_target.LocalFileSystem

Wrapper for access to file system operations.

Work in progress - add things as needed.

copy(*old_path*, *new_path*, *raise_if_exists=False*)

Copy a file or a directory with contents.
Currently, LocalFileSystem and MockFileSystem support only single file
copying but S3Client copies either a file or a directory as required.

exists(*path*)

Return `True` if file or directory at `path` exist, `False` otherwise

Parameters:

**path** (*str*) – a path within the FileSystem to check for existence.

mkdir(*path*, *parents=True*, *raise_if_exists=False*)

Create directory at location `path`

Creates the directory at `path` and implicitly create parent
directories if they do not already exist.

Parameters:

- 

**path** (*str*) – a path within the FileSystem to create as a directory.

- 

**parents** (*bool*) – Create parent directories when necessary. When
parents=False and the parent directory doesn’t
exist, raise luigi.target.MissingParentDirectory

- 

**raise_if_exists** (*bool*) – raise luigi.target.FileAlreadyExists if
the folder already exists.

isdir(*path*)

Return `True` if the location at `path` is a directory. If not, return `False`.

Parameters:

**path** (*str*) – a path within the FileSystem to check as a directory.

*Note*: This method is optional, not all FileSystem subclasses implements it.

listdir(*path*)

Return a list of files rooted in path.

This returns an iterable of the files rooted at `path`. This is intended to be a
recursive listing.

Parameters:

**path** (*str*) – a path within the FileSystem to list.

*Note*: This method is optional, not all FileSystem subclasses implements it.

remove(*path*, *recursive=True*)

Remove file or directory at location `path`

Parameters:

- 

**path** (*str*) – a path within the FileSystem to remove.

- 

**recursive** (*bool*) – if the path is a directory, recursively remove the directory and all
of its descendants. Defaults to `True`.

move(*old_path*, *new_path*, *raise_if_exists=False*)

Move file atomically. If source and destination are located
on different filesystems, atomicity is approximated
but cannot be guaranteed.

rename_dont_move(*path*, *dest*)

Rename `path` to `dest`, but don’t move it into the `dest`
folder (if it is a folder). This method is just a wrapper around the
`move` method of LocalTarget.

class luigi.local_target.LocalTarget(*path=None*, *format=None*, *is_tmp=False*)

Initializes a FileSystemTarget instance.

Parameters:

**path** – the path associated with this FileSystemTarget.

fs = <luigi.local_target.LocalFileSystem object>

makedirs()

Create all parent folders if they do not exist.

open(*mode='r'*)

Open the FileSystem target.

This method returns a file-like object which can either be read from or written to depending
on the specified mode.

Parameters:

**mode** (*str*) – the mode r opens the FileSystemTarget in read-only mode, whereas w will
open the FileSystemTarget in write mode. Subclasses can implement
additional options. Using b is not supported; initialize with
format=Nop instead.

move(*new_path*, *raise_if_exists=False*)

move_dir(*new_path*)

remove()

Remove the resource at the path specified by this FileSystemTarget.

This method is implemented by using `fs`.

copy(*new_path*, *raise_if_exists=False*)

property fn
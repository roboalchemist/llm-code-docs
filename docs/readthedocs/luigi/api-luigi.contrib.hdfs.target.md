# luigi.contrib.hdfs.target

Provides access to HDFS using the `HdfsTarget`, a subclass of `Target`.

Classes

`HdfsFlagTarget`(path[, format, client, flag])

Defines a target directory with a flag-file (defaults to _SUCCESS) used to signify job success.

`HdfsTarget`([path, format, is_tmp, fs])

Initializes a FileSystemTarget instance.

class luigi.contrib.hdfs.target.HdfsTarget(*path=None*, *format=None*, *is_tmp=False*, *fs=None*)

Initializes a FileSystemTarget instance.

Parameters:

**path** – the path associated with this FileSystemTarget.

property fs

The `FileSystem` associated with this FileSystemTarget.

glob_exists(*expected_files*)

open(*mode='r'*)

Open the FileSystem target.

This method returns a file-like object which can either be read from or written to depending
on the specified mode.

Parameters:

**mode** (*str*) – the mode r opens the FileSystemTarget in read-only mode, whereas w will
open the FileSystemTarget in write mode. Subclasses can implement
additional options. Using b is not supported; initialize with
format=Nop instead.

remove(*skip_trash=False*)

Remove the resource at the path specified by this FileSystemTarget.

This method is implemented by using `fs`.

rename(*path*, *raise_if_exists=False*)

Does not change self.path.

Unlike `move_dir()`, `rename()` might cause nested directories.
See spotify/luigi#522

move(*path*, *raise_if_exists=False*)

Alias for `rename()`

move_dir(*path*)

Move using `rename_dont_move`

New since after luigi v2.1: Does not change self.path

One could argue that the implementation should use the
mkdir+raise_if_exists approach, but we at Spotify have had more trouble
with that over just using plain mv.  See spotify/luigi#557

copy(*dst_dir*)

Copy to destination directory.

is_writable()

Currently only works with hadoopcli

class luigi.contrib.hdfs.target.HdfsFlagTarget(*path*, *format=None*, *client=None*, *flag='_SUCCESS'*)

Defines a target directory with a flag-file (defaults to _SUCCESS) used
to signify job success.

This checks for two things:

- 

the path exists (just like the HdfsTarget)

- 

the _SUCCESS file exists within the directory.

Because Hadoop outputs into a directory and not a single file,
the path is assumed to be a directory.

Initializes a HdfsFlagTarget.

Parameters:

- 

**path** (*str*) – the directory where the files are stored.

- 

**client**

- 

**flag** (*str*)

exists()

Returns `True` if the path for this FileSystemTarget exists; `False` otherwise.

This method is implemented by using `fs`.
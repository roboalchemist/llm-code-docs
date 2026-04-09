# luigi.contrib.hdfs.abstract_client

Module containing abstract class about hdfs clients.

Classes

`HdfsFileSystem`()

This client uses Apache 2.x syntax for file system commands, which also matched CDH4.

class luigi.contrib.hdfs.abstract_client.HdfsFileSystem

This client uses Apache 2.x syntax for file system commands, which also matched CDH4.

rename(*path*, *dest*)

Rename or move a file.

In hdfs land, “mv” is often called rename. So we add an alias for
`move()` called `rename()`. This is also to keep backward
compatibility since `move()` became standardized in luigi’s
filesystem interface.

rename_dont_move(*path*, *dest*)

Override this method with an implementation that uses rename2,
which is a rename operation that never moves.

rename2 -
https://github.com/apache/hadoop/blob/ae91b13/hadoop-hdfs-project/hadoop-hdfs/src/main/java/org/apache/hadoop/hdfs/protocol/ClientProtocol.java
(lines 483-523)

abstractmethod remove(*path*, *recursive=True*, *skip_trash=False*)

Remove file or directory at location `path`

Parameters:

- 

**path** (*str*) – a path within the FileSystem to remove.

- 

**recursive** (*bool*) – if the path is a directory, recursively remove the directory and all
of its descendants. Defaults to `True`.

abstractmethod chmod(*path*, *permissions*, *recursive=False*)

abstractmethod chown(*path*, *owner*, *group*, *recursive=False*)

abstractmethod count(*path*)

Count contents in a directory

abstractmethod copy(*path*, *destination*)

Copy a file or a directory with contents.
Currently, LocalFileSystem and MockFileSystem support only single file
copying but S3Client copies either a file or a directory as required.

abstractmethod put(*local_path*, *destination*)

abstractmethod get(*path*, *local_destination*)

abstractmethod mkdir(*path*, *parents=True*, *raise_if_exists=False*)

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

abstractmethod listdir(*path*, *ignore_directories=False*, *ignore_files=False*, *include_size=False*, *include_type=False*, *include_time=False*, *recursive=False*)

Return a list of files rooted in path.

This returns an iterable of the files rooted at `path`. This is intended to be a
recursive listing.

Parameters:

**path** (*str*) – a path within the FileSystem to list.

*Note*: This method is optional, not all FileSystem subclasses implements it.

abstractmethod touchz(*path*)
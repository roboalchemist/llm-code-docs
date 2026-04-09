# luigi.contrib.hdfs.hadoopcli_clients

The implementations of the hdfs clients.

Functions

`create_hadoopcli_client`()

Given that we want one of the hadoop cli clients, this one will return the right one.

Classes

`HdfsClient`()

This client uses Apache 2.x syntax for file system commands, which also matched CDH4.

`HdfsClientApache1`()

This client uses Apache 1.x syntax for file system commands, which are similar to CDH3 except for the file existence check.

`HdfsClientCdh3`()

This client uses CDH3 syntax for file system commands.

luigi.contrib.hdfs.hadoopcli_clients.create_hadoopcli_client()

Given that we want one of the hadoop cli clients,
this one will return the right one.

class luigi.contrib.hdfs.hadoopcli_clients.HdfsClient

This client uses Apache 2.x syntax for file system commands, which also matched CDH4.

recursive_listdir_cmd = ['-ls', '-R']

static call_check(*command*)

exists(*path*)

Use `hadoop fs -stat` to check file existence.

move(*path*, *dest*)

Move a file, as one would expect.

remove(*path*, *recursive=True*, *skip_trash=False*)

Remove file or directory at location `path`

Parameters:

- 

**path** (*str*) – a path within the FileSystem to remove.

- 

**recursive** (*bool*) – if the path is a directory, recursively remove the directory and all
of its descendants. Defaults to `True`.

chmod(*path*, *permissions*, *recursive=False*)

chown(*path*, *owner*, *group*, *recursive=False*)

count(*path*)

Count contents in a directory

copy(*path*, *destination*)

Copy a file or a directory with contents.
Currently, LocalFileSystem and MockFileSystem support only single file
copying but S3Client copies either a file or a directory as required.

put(*local_path*, *destination*)

get(*path*, *local_destination*)

getmerge(*path*, *local_destination*, *new_line=False*)

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

listdir(*path*, *ignore_directories=False*, *ignore_files=False*, *include_size=False*, *include_type=False*, *include_time=False*, *recursive=False*)

Return a list of files rooted in path.

This returns an iterable of the files rooted at `path`. This is intended to be a
recursive listing.

Parameters:

**path** (*str*) – a path within the FileSystem to list.

*Note*: This method is optional, not all FileSystem subclasses implements it.

touchz(*path*)

class luigi.contrib.hdfs.hadoopcli_clients.HdfsClientCdh3

This client uses CDH3 syntax for file system commands.

mkdir(*path*, *parents=True*, *raise_if_exists=False*)

No explicit -p switch, this version of Hadoop always creates parent directories.

remove(*path*, *recursive=True*, *skip_trash=False*)

Remove file or directory at location `path`

Parameters:

- 

**path** (*str*) – a path within the FileSystem to remove.

- 

**recursive** (*bool*) – if the path is a directory, recursively remove the directory and all
of its descendants. Defaults to `True`.

class luigi.contrib.hdfs.hadoopcli_clients.HdfsClientApache1

This client uses Apache 1.x syntax for file system commands,
which are similar to CDH3 except for the file existence check.

recursive_listdir_cmd = ['-lsr']

exists(*path*)

Use `hadoop fs -stat` to check file existence.
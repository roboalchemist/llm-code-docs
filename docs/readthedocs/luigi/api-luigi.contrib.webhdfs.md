# luigi.contrib.webhdfs

Provides a `WebHdfsTarget` using the Python hdfs [https://pypi.python.org/pypi/hdfs/]

This module is DEPRECATED and does not play well with rest of luigi’s hdfs
contrib module. You can consider migrating to
`luigi.contrib.hdfs.webhdfs_client.WebHdfsClient`

Classes

`AtomicWebHdfsFile`(path, client)

An Hdfs file that writes to a temp file and put to WebHdfs on close.

`ReadableWebHdfsFile`(path, client)

`WebHdfsTarget`(path[, client, format])

Initializes a FileSystemTarget instance.

class luigi.contrib.webhdfs.WebHdfsTarget(*path*, *client=None*, *format=None*)

Initializes a FileSystemTarget instance.

Parameters:

**path** – the path associated with this FileSystemTarget.

fs = None

open(*mode='r'*)

Open the FileSystem target.

This method returns a file-like object which can either be read from or written to depending
on the specified mode.

Parameters:

**mode** (*str*) – the mode r opens the FileSystemTarget in read-only mode, whereas w will
open the FileSystemTarget in write mode. Subclasses can implement
additional options. Using b is not supported; initialize with
format=Nop instead.

class luigi.contrib.webhdfs.ReadableWebHdfsFile(*path*, *client*)

read()

readlines(*char='\n'*)

close()

class luigi.contrib.webhdfs.AtomicWebHdfsFile(*path*, *client*)

An Hdfs file that writes to a temp file and put to WebHdfs on close.

move_to_final_destination()
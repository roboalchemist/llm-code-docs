# luigi.contrib.ftp

This library is a wrapper of ftplib or pysftp.
It is convenient to move data from/to (S)FTP servers.

There is an example on how to use it (example/ftp_experiment_outputs.py)

You can also find unittest for each class.

Be aware that normal ftp does not provide secure communication.

Classes

`AtomicFtpFile`(fs, path)

Simple class that writes to a temp file and upload to ftp on close().

`RemoteFileSystem`(host[, username, password, ...])

`RemoteTarget`(path, host[, format, username, ...])

Target used for reading from remote files.

class luigi.contrib.ftp.RemoteFileSystem(*host*, *username=None*, *password=None*, *port=None*, *tls=False*, *timeout=60*, *sftp=False*, *pysftp_conn_kwargs=None*)

exists(*path*, *mtime=None*)

Return True if file or directory at path exist, False otherwise.

Additional check on modified time when mtime is passed in.

Return False if the file’s modified time is older mtime.

remove(*path*, *recursive=True*)

Remove file or directory at location `path`.

Parameters:

- 

**path** (*str*) – a path within the FileSystem to remove.

- 

**recursive** (*bool*) – if the path is a directory, recursively remove the directory and
all of its descendants. Defaults to `True`.

put(*local_path*, *path*, *atomic=True*)

Put file from local filesystem to (s)FTP.

get(*path*, *local_path*)

Download file from (s)FTP to local filesystem.

listdir(*path='.'*)

Gets an list of the contents of path in (s)FTP

class luigi.contrib.ftp.AtomicFtpFile(*fs*, *path*)

Simple class that writes to a temp file and upload to ftp on close().

Also cleans up the temp file if close is not invoked.

Initializes an AtomicFtpfile instance.
:param fs:
:param path:
:type path: str

move_to_final_destination()

property fs

class luigi.contrib.ftp.RemoteTarget(*path*, *host*, *format=None*, *username=None*, *password=None*, *port=None*, *mtime=None*, *tls=False*, *timeout=60*, *sftp=False*, *pysftp_conn_kwargs=None*)

Target used for reading from remote files.

The target is implemented using intermediate files on the local system.
On Python2, these files may not be cleaned up.

Initializes a FileSystemTarget instance.

Parameters:

**path** – the path associated with this FileSystemTarget.

property fs

The `FileSystem` associated with this FileSystemTarget.

open(*mode*)

Open the FileSystem target.

This method returns a file-like object which can either be read from or written to depending
on the specified mode.

Parameters:

**mode** (*str*) – the mode r opens the FileSystemTarget in read-only mode, whereas w will
open the FileSystemTarget in write mode. Subclasses can implement
additional options.

exists()

Returns `True` if the path for this FileSystemTarget exists; `False` otherwise.

This method is implemented by using `fs`.

put(*local_path*, *atomic=True*)

get(*local_path*)
# luigi.contrib.ssh

Light-weight remote execution library and utilities.

There are some examples in the unittest but I added another that is more
luigi-specific in the examples directory (examples/ssh_remote_execution.py)

`RemoteContext` is meant to provide functionality similar to that of the
standard library subprocess module, but where the commands executed are run on
a remote machine instead, without the user having to think about prefixing
everything with “ssh” and credentials etc.

Using this mini library (which is just a convenience wrapper for subprocess),
`RemoteTarget` is created to let you stream data from a remotely stored file using
the luigi `FileSystemTarget` semantics.

As a bonus, `RemoteContext` also provides a really cool feature that let’s you
set up ssh tunnels super easily using a python context manager (there is an example
in the integration part of unittests).

This can be super convenient when you want secure communication using a non-secure
protocol or circumvent firewalls (as long as they are open for ssh traffic).

Classes

`AtomicRemoteFileWriter`(fs, path)

`RemoteContext`(host, **kwargs)

`RemoteFileSystem`(host, **kwargs)

`RemoteTarget`(path, host[, format])

Target used for reading from remote files.

Exceptions

`RemoteCalledProcessError`(returncode, ...[, ...])

exception luigi.contrib.ssh.RemoteCalledProcessError(*returncode*, *command*, *host*, *output=None*)

class luigi.contrib.ssh.RemoteContext(*host*, ***kwargs*)

Popen(*cmd*, ***kwargs*)

Remote Popen.

check_output(*cmd*)

Execute a shell command remotely and return the output.

Simplified version of Popen when you only want the output as a string and detect any errors.

tunnel(*local_port*, *remote_port=None*, *remote_host='localhost'*)

Open a tunnel between localhost:local_port and remote_host:remote_port via the host specified by this context.

Remember to close() the returned “tunnel” object in order to clean up
after yourself when you are done with the tunnel.

class luigi.contrib.ssh.RemoteFileSystem(*host*, ***kwargs*)

exists(*path*)

Return True if file or directory at path exist, False otherwise.

listdir(*path*)

Return a list of files rooted in path.

This returns an iterable of the files rooted at `path`. This is intended to be a
recursive listing.

Parameters:

**path** (*str*) – a path within the FileSystem to list.

*Note*: This method is optional, not all FileSystem subclasses implements it.

isdir(*path*)

Return True if directory at path exist, False otherwise.

remove(*path*, *recursive=True*)

Remove file or directory at location path.

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

put(*local_path*, *path*)

get(*path*, *local_path*)

class luigi.contrib.ssh.AtomicRemoteFileWriter(*fs*, *path*)

close()

property tmp_path

property fs

class luigi.contrib.ssh.RemoteTarget(*path*, *host*, *format=None*, ***kwargs*)

Target used for reading from remote files.

The target is implemented using ssh commands streaming data over the network.

Initializes a FileSystemTarget instance.

Parameters:

**path** – the path associated with this FileSystemTarget.

property fs

The `FileSystem` associated with this FileSystemTarget.

open(*mode='r'*)

Open the FileSystem target.

This method returns a file-like object which can either be read from or written to depending
on the specified mode.

Parameters:

**mode** (*str*) – the mode r opens the FileSystemTarget in read-only mode, whereas w will
open the FileSystemTarget in write mode. Subclasses can implement
additional options. Using b is not supported; initialize with
format=Nop instead.

put(*local_path*)

get(*local_path*)
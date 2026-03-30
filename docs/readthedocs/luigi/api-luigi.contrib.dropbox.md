# luigi.contrib.dropbox

Functions

`accept_trailing_slash`(func)

`accept_trailing_slash_in_existing_dirpaths`(func)

Classes

`AtomicWritableDropboxFile`(path, client)

Represents a file that will be created inside the Dropbox cloud

`DropboxClient`(token[, user_agent, ...])

Dropbox client for authentication, designed to be used by the `DropboxTarget` class.

`DropboxTarget`(path, token[, format, ...])

A Dropbox filesystem target.

`ReadableDropboxFile`(path, client)

Represents a file inside the Dropbox cloud which will be read

luigi.contrib.dropbox.accept_trailing_slash_in_existing_dirpaths(*func*)

luigi.contrib.dropbox.accept_trailing_slash(*func*)

class luigi.contrib.dropbox.DropboxClient(*token*, *user_agent='Luigi'*, *root_namespace_id=None*)

Dropbox client for authentication, designed to be used by the `DropboxTarget` class.

Parameters:

- 

**token** (*str*) – Dropbox Oauth2 Token. See `DropboxTarget` for more information about generating a token

- 

**root_namespace_id** (*str*) – Root namespace ID for interacting with Team Spaces

exists(*path*)

Return `True` if file or directory at `path` exist, `False` otherwise

Parameters:

**path** (*str*) – a path within the FileSystem to check for existence.

remove(*path*, *recursive=True*, *skip_trash=True*)

Remove file or directory at location `path`

Parameters:

- 

**path** (*str*) – a path within the FileSystem to remove.

- 

**recursive** (*bool*) – if the path is a directory, recursively remove the directory and all
of its descendants. Defaults to `True`.

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

listdir(*path*, ***kwargs*)

Return a list of files rooted in path.

This returns an iterable of the files rooted at `path`. This is intended to be a
recursive listing.

Parameters:

**path** (*str*) – a path within the FileSystem to list.

*Note*: This method is optional, not all FileSystem subclasses implements it.

move(*path*, *dest*)

Move a file, as one would expect.

copy(*path*, *dest*)

Copy a file or a directory with contents.
Currently, LocalFileSystem and MockFileSystem support only single file
copying but S3Client copies either a file or a directory as required.

download_as_bytes(*path*)

upload(*tmp_path*, *dest_path*)

class luigi.contrib.dropbox.ReadableDropboxFile(*path*, *client*)

Represents a file inside the Dropbox cloud which will be read

Parameters:

- 

**path** (*str*) – Dropbpx path of the file to be read (always starting with /)

- 

**client** (*DropboxClient*) – a DropboxClient object (initialized with a valid token)

read()

close()

readable()

writable()

seekable()

class luigi.contrib.dropbox.AtomicWritableDropboxFile(*path*, *client*)

Represents a file that will be created inside the Dropbox cloud

Parameters:

- 

**path** (*str*) – Destination path inside Dropbox

- 

**client** (*DropboxClient*) – a DropboxClient object (initialized with a valid token, for the desired account)

move_to_final_destination()

After editing the file locally, this function uploads it to the Dropbox cloud

class luigi.contrib.dropbox.DropboxTarget(*path*, *token*, *format=None*, *user_agent='Luigi'*, *root_namespace_id=None*)

A Dropbox filesystem target.

Create an Dropbox Target for storing data in a dropbox.com account

**About the path parameter**

The path must start with ‘/’ and should not end with ‘/’ (even if it is a directory).
The path must not contain adjacent slashes (‘/files//img.jpg’ is an invalid path)

If the app has ‘App folder’ access, then / will refer to this app folder (which
mean that there is no need to prepend the name of the app to the path)
Otherwise, if the app has ‘full access’, then / will refer to the root of the Dropbox folder

**About the token parameter:**

The Dropbox target requires a valid OAuth2 token as a parameter (which means that a Dropbox API app [https://www.dropbox.com/developers/apps] must be created. This app can have ‘App folder’ access
or ‘Full Dropbox’, as desired).

Information about generating the token can be read here:

- 

https://dropbox-sdk-python.readthedocs.io/en/latest/api/oauth.html#dropbox.oauth.DropboxOAuth2Flow

- 

https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/

Parameters:

- 

**path** (*str*) – Remote path in Dropbox (starting with ‘/’).

- 

**token** (*str*) – a valid OAuth2 Dropbox token.

- 

**format** (*luigi.Format*) – the luigi format to use (e.g. luigi.format.Nop)

- 

**root_namespace_id** (*str*) – Root namespace ID for interacting with Team Spaces

property fs

The `FileSystem` associated with this FileSystemTarget.

temporary_path()

A context manager that enables a reasonably short, general and
magic-less way to solve the Atomic Writes Problem.

- 

On *entering*, it will create the parent directories so the
temporary_path is writeable right away.
This step uses `FileSystem.mkdir()`.

- 

On *exiting*, it will move the temporary file if there was no exception thrown.
This step uses `FileSystem.rename_dont_move()`
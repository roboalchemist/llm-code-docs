# luigi.contrib.azureblob

Classes

`AtomicAzureBlobFile`(container, blob, client, ...)

`AzureBlobClient`([account_name, account_key, ...])

Create an Azure Blob Storage client for authentication.

`AzureBlobTarget`(container, blob[, client, ...])

Create an Azure Blob Target for storing data on Azure Blob Storage

`ReadableAzureBlobFile`(container, blob, ...)

class luigi.contrib.azureblob.AzureBlobClient(*account_name=None*, *account_key=None*, *sas_token=None*, ***kwargs*)

Create an Azure Blob Storage client for authentication.
Users can create multiple storage account, each of which acts like a silo. Under each storage account, we can
create a container. Inside each container, the user can create multiple blobs.

For each account, there should be an account key. This account key cannot be changed and one can access all the
containers and blobs under this account using the account key.

Usually using an account key might not always be the best idea as the key can be leaked and cannot be revoked. The
solution to this issue is to create Shared Access Signatures aka sas. A SAS can be created for an entire
container or just a single blob. SAS can be revoked.

Parameters:

- 

**account_name** (*str*) – The storage account name. This is used to authenticate requests signed with an account key            and to construct the storage endpoint. It is required unless a connection string is given,            or if a custom domain is used with anonymous authentication.

- 

**account_key** (*str*) – The storage account key. This is used for shared key authentication.

- 

**sas_token** (*str*) – A shared access signature token to use to authenticate requests instead of the account key.

- 

**kwargs** (*dict*) – 

A key-value pair to provide additional connection options.

  - 

protocol - The protocol to use for requests. Defaults to https.

  - 

connection_string - If specified, this will override all other parameters besides request session.                See http://azure.microsoft.com/en-us/documentation/articles/storage-configure-connection-string/ for the connection string format

  - 

endpoint_suffix - The host base component of the url, minus the account name. Defaults to Azure                (core.windows.net). Override this to use the China cloud (core.chinacloudapi.cn).

  - 

custom_domain - The custom domain to use. This can be set in the Azure Portal. For example, ‘www.mydomain.com’.

  - 

token_credential - A token credential used to authenticate HTTPS requests. The token value should be updated before its expiration.

property connection

container_client(*container_name*)

blob_client(*container_name*, *blob_name*)

upload(*tmp_path*, *container*, *blob*, ***kwargs*)

download_as_bytes(*container*, *blob*, *bytes_to_read=None*)

download_as_file(*container*, *blob*, *location*)

create_container(*container_name*)

delete_container(*container_name*)

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

Azure Blob Storage has no concept of directories. It always returns False
:param str path: Path of the Azure blob storage
:return: False

move(*path*, *dest*)

Move a file, as one would expect.

copy(*path*, *dest*)

Copy a file or a directory with contents.
Currently, LocalFileSystem and MockFileSystem support only single file
copying but S3Client copies either a file or a directory as required.

rename_dont_move(*path*, *dest*)

Potentially rename `path` to `dest`, but don’t move it into the
`dest` folder (if it is a folder).  This relates to Atomic Writes Problem.

This method has a reasonable but not bullet proof default
implementation.  It will just do `move()` if the file doesn’t
`exists()` already.

static splitfilepath(*filepath*)

class luigi.contrib.azureblob.ReadableAzureBlobFile(*container*, *blob*, *client*, *download_when_reading*, ***kwargs*)

read(*n=None*)

close()

readable()

writable()

seekable()

seek(*offset*, *whence=None*)

class luigi.contrib.azureblob.AtomicAzureBlobFile(*container*, *blob*, *client*, ***kwargs*)

move_to_final_destination()

class luigi.contrib.azureblob.AzureBlobTarget(*container*, *blob*, *client=None*, *format=None*, *download_when_reading=True*, ***kwargs*)

Create an Azure Blob Target for storing data on Azure Blob Storage

Parameters:

- 

**account_name** (*str*) – The storage account name. This is used to authenticate requests signed with an account key and to construct
the storage endpoint. It is required unless a connection string is given, or if a custom domain is
used with anonymous authentication.

- 

**container** (*str*) – The azure container in which the blob needs to be stored

- 

**blob** (*str*) – The name of the blob under container specified

- 

**client** (*str*) – An instance of `AzureBlobClient`. If none is specified, anonymous access would be used

- 

**format** (*str*) – An instance of `luigi.format`.

- 

**download_when_reading** (*bool*) – Determines whether the file has to be downloaded to temporary location on disk. Defaults to True.

Pass the argument **progress_callback** with signature *(func(current, total))* to get real time progress of upload

property fs

The `FileSystem` associated with `AzureBlobTarget`

open(*mode*)

Open the target for reading or writing

Parameters:

**mode** (*char*) – 

‘r’ for reading and ‘w’ for writing.

’b’ is not supported and will be stripped if used. For binary mode, use format

Returns:

- 

`ReadableAzureBlobFile` if ‘r’

- 

`AtomicAzureBlobFile` if ‘w’
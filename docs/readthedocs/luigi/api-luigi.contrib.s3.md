# luigi.contrib.s3

Implementation of Simple Storage Service support.
`S3Target` is a subclass of the Target class to support S3 file
system operations. The boto3 library is required to use S3 targets.

Classes

`AtomicS3File`(path, s3_client, **kwargs)

An S3 file that writes to a temp file and puts to S3 on close.

`ReadableS3File`(s3_key)

`S3Client`([aws_access_key_id, ...])

boto3-powered S3 client.

`S3EmrTarget`(*args, **kwargs)

Deprecated.

`S3EmrTask`(*args, **kwargs)

An external task that requires the existence of EMR output in S3.

`S3FlagTarget`(path[, format, client, flag])

Defines a target directory with a flag-file (defaults to _SUCCESS) used to signify job success.

`S3FlagTask`(*args, **kwargs)

An external task that requires the existence of EMR output in S3.

`S3PathTask`(*args, **kwargs)

A external task that to require existence of a path in S3.

`S3Target`(path[, format, client])

Target S3 file object

Exceptions

`DeprecatedBotoClientException`

`FileNotFoundException`

`InvalidDeleteException`

exception luigi.contrib.s3.InvalidDeleteException

exception luigi.contrib.s3.FileNotFoundException

exception luigi.contrib.s3.DeprecatedBotoClientException

class luigi.contrib.s3.S3Client(*aws_access_key_id=None*, *aws_secret_access_key=None*, *aws_session_token=None*, ***kwargs*)

boto3-powered S3 client.

DEFAULT_PART_SIZE = 8388608

DEFAULT_THREADS = 100

property s3

exists(*path*)

Does provided path exist on S3?

remove(*path*, *recursive=True*)

Remove a file or directory from S3.
:param path: File or directory to remove
:param recursive: Boolean indicator to remove object and children
:return: Boolean indicator denoting success of the removal of 1 or more files

move(*source_path*, *destination_path*, ***kwargs*)

Rename/move an object from one S3 location to another.
:param source_path: The s3:// path of the directory or key to copy from
:param destination_path: The s3:// path of the directory or key to copy to
:param kwargs: Keyword arguments are passed to the boto3 function copy

get_key(*path*)

Returns the object summary at the path

put(*local_path*, *destination_s3_path*, ***kwargs*)

Put an object stored locally to an S3 path.
:param local_path: Path to source local file
:param destination_s3_path: URL for target S3 location
:param kwargs: Keyword arguments are passed to the boto function put_object

put_string(*content*, *destination_s3_path*, ***kwargs*)

Put a string to an S3 path.
:param content: Data str
:param destination_s3_path: URL for target S3 location
:param kwargs: Keyword arguments are passed to the boto3 function put_object

put_multipart(*local_path*, *destination_s3_path*, *part_size=8388608*, ***kwargs*)

Put an object stored locally to an S3 path
using S3 multi-part upload (for files > 8Mb).
:param local_path: Path to source local file
:param destination_s3_path: URL for target S3 location
:param part_size: Part size in bytes. Default: 8388608 (8MB)
:param kwargs: Keyword arguments are passed to the boto function upload_fileobj as ExtraArgs

copy(*source_path*, *destination_path*, *threads=100*, *start_time=None*, *end_time=None*, *part_size=8388608*, ***kwargs*)

Copy object(s) from one S3 location to another. Works for individual keys or entire directories.
When files are larger than part_size, multipart uploading will be used.
:param source_path: The s3:// path of the directory or key to copy from
:param destination_path: The s3:// path of the directory or key to copy to
:param threads: Optional argument to define the number of threads to use when copying (min: 3 threads)
:param start_time: Optional argument to copy files with modified dates after start_time
:param end_time: Optional argument to copy files with modified dates before end_time
:param part_size: Part size in bytes
:param kwargs: Keyword arguments are passed to the boto function copy as ExtraArgs
:returns tuple (number_of_files_copied, total_size_copied_in_bytes)

get(*s3_path*, *destination_local_path*)

Get an object stored in S3 and write it to a local path.

get_as_bytes(*s3_path*)

Get the contents of an object stored in S3 as bytes

Parameters:

**s3_path** – URL for target S3 location

Returns:

File contents as pure bytes

get_as_string(*s3_path*, *encoding='utf-8'*)

Get the contents of an object stored in S3 as string.

Parameters:

- 

**s3_path** – URL for target S3 location

- 

**encoding** – Encoding to decode bytes to string

Returns:

File contents as a string

isdir(*path*)

Is the parameter S3 path a directory?

is_dir(*path*)

Is the parameter S3 path a directory?

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

listdir(*path*, *start_time=None*, *end_time=None*, *return_key=False*)

Get an iterable with S3 folder contents.
Iterable contains absolute paths for which queried path is a prefix.

Parameters:

- 

**path** – URL for target S3 location

- 

**start_time** – Optional argument to list files with modified (offset aware) datetime after start_time

- 

**end_time** – Optional argument to list files with modified (offset aware) datetime before end_time

- 

**return_key** – Optional argument, when set to True will return boto3’s ObjectSummary (instead of the filename)

list(*path*, *start_time=None*, *end_time=None*, *return_key=False*)

Get an iterable with S3 folder contents.
Iterable contains paths relative to queried path.

Parameters:

- 

**path** – URL for target S3 location

- 

**start_time** – Optional argument to list files with modified (offset aware) datetime after start_time

- 

**end_time** – Optional argument to list files with modified (offset aware) datetime before end_time

- 

**return_key** – Optional argument, when set to True will return boto3’s ObjectSummary (instead of the filename)

class luigi.contrib.s3.AtomicS3File(*path*, *s3_client*, ***kwargs*)

An S3 file that writes to a temp file and puts to S3 on close.

Parameters:

**kwargs** – Keyword arguments are passed to the boto function initiate_multipart_upload

move_to_final_destination()

class luigi.contrib.s3.ReadableS3File(*s3_key*)

read(*size=None*)

close()

readable()

writable()

seekable()

class luigi.contrib.s3.S3Target(*path*, *format=None*, *client=None*, ***kwargs*)

Target S3 file object

Parameters:

**kwargs** – Keyword arguments are passed to the boto function initiate_multipart_upload

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

class luigi.contrib.s3.S3FlagTarget(*path*, *format=None*, *client=None*, *flag='_SUCCESS'*)

Defines a target directory with a flag-file (defaults to _SUCCESS) used
to signify job success.

This checks for two things:

- 

the path exists (just like the S3Target)

- 

the _SUCCESS file exists within the directory.

Because Hadoop outputs into a directory and not a single file,
the path is assumed to be a directory.

This is meant to be a handy alternative to AtomicS3File.

The AtomicFile approach can be burdensome for S3 since there are no directories, per se.

If we have 1,000,000 output files, then we have to rename 1,000,000 objects.

Initializes a S3FlagTarget.

Parameters:

- 

**path** (*str*) – the directory where the files are stored.

- 

**client**

- 

**flag** (*str*)

fs = None

exists()

Returns `True` if the path for this FileSystemTarget exists; `False` otherwise.

This method is implemented by using `fs`.

class luigi.contrib.s3.S3EmrTarget(**args*, ***kwargs*)

Deprecated. Use `S3FlagTarget`

Initializes a S3FlagTarget.

Parameters:

- 

**path** (*str*) – the directory where the files are stored.

- 

**client**

- 

**flag** (*str*)

class luigi.contrib.s3.S3PathTask(**args*, ***kwargs*)

A external task that to require existence of a path in S3.

path

Parameter whose value is a `str`, and a base class for other parameter types.

Parameters are objects set on the Task class level to make it possible to parameterize tasks.
For instance:

```
class MyTask(luigi.Task):
    foo = luigi.Parameter()

class RequiringTask(luigi.Task):
    def requires(self):
        return MyTask(foo="hello")

    def run(self):
        print(self.requires().foo)  # prints "hello"

```
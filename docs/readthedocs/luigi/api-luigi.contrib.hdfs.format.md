# luigi.contrib.hdfs.format

Classes

`CompatibleHdfsFormat`(writer, reader[, input])

`HdfsAtomicWriteDirPipe`(path[, data_extension])

Writes a data<data_extension> file to a directory at <path>.

`HdfsAtomicWritePipe`(path)

File like object for writing to HDFS

`HdfsReadPipe`(path)

Initializes a InputPipeProcessWrapper instance.

`PlainDirFormat`()

`PlainFormat`()

Exceptions

`HdfsAtomicWriteError`

exception luigi.contrib.hdfs.format.HdfsAtomicWriteError

class luigi.contrib.hdfs.format.HdfsReadPipe(*path*)

Initializes a InputPipeProcessWrapper instance.

Parameters:

**command** – a subprocess.Popen instance with stdin=input_pipe and
stdout=subprocess.PIPE.
Alternatively, just its args argument as a convenience.

class luigi.contrib.hdfs.format.HdfsAtomicWritePipe(*path*)

File like object for writing to HDFS

The referenced file is first written to a temporary location and then
renamed to final location on close(). If close() isn’t called
the temporary file will be cleaned up when this object is
garbage collected

TODO: if this is buggy, change it so it first writes to a
local temporary file and then uploads it on completion

abort()

close()

class luigi.contrib.hdfs.format.HdfsAtomicWriteDirPipe(*path*, *data_extension=''*)

Writes a data<data_extension> file to a directory at <path>.

abort()

close()

class luigi.contrib.hdfs.format.PlainFormat

input = 'bytes'

output = 'hdfs'

hdfs_writer(*path*)

hdfs_reader(*path*)

pipe_reader(*path*)

pipe_writer(*output_pipe*)

class luigi.contrib.hdfs.format.PlainDirFormat

input = 'bytes'

output = 'hdfs'

hdfs_writer(*path*)

hdfs_reader(*path*)

pipe_reader(*path*)

pipe_writer(*path*)

class luigi.contrib.hdfs.format.CompatibleHdfsFormat(*writer*, *reader*, *input=None*)

output = 'hdfs'

pipe_writer(*output*)

pipe_reader(*input*)

hdfs_writer(*output*)

hdfs_reader(*input*)
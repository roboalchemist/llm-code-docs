# Building workflows

There are two fundamental building blocks of Luigi -
the `Task` class and the `Target` class.
Both are abstract classes and expect a few methods to be implemented.
In addition to those two concepts,
the `Parameter` class is an important concept that governs how a Task is run.

## Target

The `Target` class corresponds to a file on a disk,
a file on HDFS or some kind of a checkpoint, like an entry in a database.
Actually, the only method that Targets have to implement is the *exists*
method which returns True if and only if the Target exists.

In practice, implementing Target subclasses is rarely needed.
Luigi comes with a toolbox of several useful Targets.
In particular, `LocalTarget` and `HdfsTarget`,
but there is also support for other file systems:
`luigi.contrib.s3.S3Target`,
`luigi.contrib.ssh.RemoteTarget`,
`luigi.contrib.ftp.RemoteTarget`,
`luigi.contrib.mysqldb.MySqlTarget`,
`luigi.contrib.redshift.RedshiftTarget`, and several more.

Most of these targets, are file system-like.
For instance, `LocalTarget` and `HdfsTarget` map to a file on the local drive or a file in HDFS.
In addition these also wrap the underlying operations to make them atomic.
They both implement the `open()` method which returns a stream object that
could be read (`mode='r'`) from or written to (`mode='w'`).

Luigi comes with Gzip support by providing `format=format.Gzip`.
Adding support for other formats is pretty simple.

## Task

The `Task` class is a bit more conceptually interesting because this is
where computation is done.
There are a few methods that can be implemented to alter its behavior,
most notably `run()`, `output()` and `requires()`.

Tasks consume Targets that were created by some other task. They usually also output targets:
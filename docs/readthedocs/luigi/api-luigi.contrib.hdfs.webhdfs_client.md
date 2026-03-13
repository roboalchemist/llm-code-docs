# luigi.contrib.hdfs.webhdfs_client

A luigi file system client that wraps around the hdfs-library (a webhdfs
client)

Note. This wrapper client is not feature complete yet. As with most software
the authors only implement the features they need.  If you need to wrap more of
the file system operations, please do and contribute back.

Classes

`WebHdfsClient`([host, port, user, client_type])

A webhdfs that tries to confirm to luigis interface for file existence.

`webhdfs`(*args, **kwargs)

class luigi.contrib.hdfs.webhdfs_client.webhdfs(**args*, ***kwargs*)

port

Parameter whose value is an `int`.

user

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
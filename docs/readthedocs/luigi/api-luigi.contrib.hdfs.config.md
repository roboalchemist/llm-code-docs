# luigi.contrib.hdfs.config

You can configure what client by setting the “client” config under the “hdfs” section in the configuration, or using the `--hdfs-client` command line option.
“hadoopcli” is the slowest, but should work out of the box.

Functions

`get_configured_hadoop_version`()

CDH4 (hadoop 2+) has a slightly different syntax for interacting with hdfs via the command line.

`get_configured_hdfs_client`()

This is a helper that fetches the configuration value for 'client' in the [hdfs] section.

`load_hadoop_cmd`()

`tmppath`([path, include_unix_username])

@param path: target path for which it is needed to generate temporary location @type path: str @type include_unix_username: bool @rtype: str

Classes

`hadoopcli`(*args, **kwargs)

`hdfs`(*args, **kwargs)

class luigi.contrib.hdfs.config.hdfs(**args*, ***kwargs*)

client_version

Parameter whose value is an `int`.

namenode_host

Class to parse optional parameters.

namenode_port

Parameter whose value is an `int`.

client

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
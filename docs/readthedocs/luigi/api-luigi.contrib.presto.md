# luigi.contrib.presto

Classes

`PrestoClient`(connection[, sleep_time])

Helper class wrapping pyhive.presto.Connection for executing presto queries and tracking progress

`PrestoTarget`(client, catalog, database, table)

Target for presto-accessible tables

`PrestoTask`(*args, **kwargs)

Task for executing presto queries During its executions tracking url and percentage progress are set

`WithPrestoClient`(name, bases, attrs)

A metaclass for injecting PrestoClient as a _client field into a new instance of class T Presto connection options are taken from T-instance fields Fields should have the same names as in pyhive.presto.Cursor

`presto`(*args, **kwargs)

class luigi.contrib.presto.presto(**args*, ***kwargs*)

host

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
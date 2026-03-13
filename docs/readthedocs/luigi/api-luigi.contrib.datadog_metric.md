# luigi.contrib.datadog_metric

Classes

`DatadogMetricsCollector`(*args, **kwargs)

`datadog`(*args, **kwargs)

class luigi.contrib.datadog_metric.datadog(**args*, ***kwargs*)

api_key

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
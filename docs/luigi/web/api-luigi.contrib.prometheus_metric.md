# luigi.contrib.prometheus_metric

Classes

`PrometheusMetricsCollector`(*args, **kwargs)

`prometheus`(*args, **kwargs)

class luigi.contrib.prometheus_metric.prometheus(**args*, ***kwargs*)

use_task_family_in_labels

A Parameter whose value is a `bool`. This parameter has an implicit default value of
`False`. For the command line interface this means that the value is `False` unless you
add `"--the-bool-parameter"` to your command without giving a parameter value. This is
considered *implicit* parsing (the default). However, in some situations one might want to give
the explicit bool value (`"--the-bool-parameter true|false"`), e.g. when you configure the
default value to be `True`. This is called *explicit* parsing. When omitting the parameter
value, it is still considered `True` but to avoid ambiguities during argument parsing, make
sure to always place bool parameters behind the task family on the command line when using
explicit parsing.

You can toggle between the two parsing modes on a per-parameter base via

```
class MyTask(luigi.Task):
    implicit_bool = luigi.BoolParameter(parsing=luigi.BoolParameter.IMPLICIT_PARSING)
    explicit_bool = luigi.BoolParameter(parsing=luigi.BoolParameter.EXPLICIT_PARSING)

```
# luigi.server

Simple REST server that takes commands in a JSON payload
Interface to the `Scheduler` class.
See Using the Central Scheduler for more info.

Functions

`app`(scheduler)

`from_utc`(utcTime[, fmt])

convert UTC time string to time.struct_time: change datetime.datetime to time, return time.struct_time type

`run`([api_port, address, unix_socket, scheduler])

Runs one instance of the API server.

`stop`()

Classes

`AllRunHandler`(application, request, **kwargs)

`BaseTaskHistoryHandler`(application, request, ...)

`ByIdHandler`(application, request, **kwargs)

`ByNameHandler`(application, request, **kwargs)

`ByParamsHandler`(application, request, **kwargs)

`ByTaskIdHandler`(application, request, **kwargs)

`MetricsHandler`(application, request, **kwargs)

`RPCHandler`(*args, **kwargs)

Handle remote scheduling calls using rpc.RemoteSchedulerResponder.

`RecentRunHandler`(application, request, **kwargs)

`RootPathHandler`(application, request, **kwargs)

`SelectedRunHandler`(application, request, ...)

`cors`(*args, **kwargs)

class luigi.server.cors(**args*, ***kwargs*)

enabled

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
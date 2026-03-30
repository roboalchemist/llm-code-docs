# luigi.interface

This module contains the bindings for command line integration and dynamic loading of tasks

If you don’t want to run luigi from the command line. You may use the methods
defined in this module to programmatically run luigi.

Functions

`build`(tasks[, worker_scheduler_factory, ...])

Run internally, bypassing the cmdline parsing.

`run`(*args, **kwargs)

Please dont use.

Classes

`core`(*args, **kwargs)

Keeps track of a bunch of environment params.

Exceptions

`PidLockAlreadyTakenExit`

The exception thrown by `luigi.run()`, when the lock file is inaccessible

class luigi.interface.core(**args*, ***kwargs*)

Keeps track of a bunch of environment params.

Uses the internal luigi parameter mechanism.
The nice thing is that we can instantiate this class
and get an object with all the environment variables set.
This is arguably a bit of a hack.

use_cmdline_section = False

ignore_unconsumed = {'autoload_range', 'no_configure_logging'}

local_scheduler

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
# Source: https://python-logrus.readthedocs.io/en/latest/logrus.html

Title: logrus package — logrus documentation

URL Source: https://python-logrus.readthedocs.io/en/latest/logrus.html

Markdown Content:
logrus package

Better logging made easy with support for structlog and the standard logging module.

_class_ BetterBoundLogger(_logger_, _processors_, _context_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "Permalink to this definition")
Bases: `structlog.stdlib.BoundLogger`

A better version of structlog’s standard BoundLogger.

Used to add additonal methods to the default BoundLogger.

Parameters
*   **logger** (`Any`) –

*   **processors** (`Iterable`[`Callable`[[`Any`, `str`, `MutableMapping`[`str`, `Any`]], `Union`[`Mapping`[`str`, `Any`], `str`, `bytes`, `bytearray`, `Tuple`[`Any`, …]]]]) –

*   **context** (`Union`[`Dict`[`str`, `Any`], `Dict`[`Any`, `Any`]]) –

bind(_**new\_values_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger.bind)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger.bind "Permalink to this definition")
Return a new logger with _new\_values_ added to the existing ones.

Parameters
**new_values** (`Any`) –

Return type
[`BetterBoundLogger`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "logrus._core.BetterBoundLogger")

bind_fargs(_fargs\_map=None_, _**kwargs_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger.bind_fargs)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger.bind_fargs "Permalink to this definition")
Helper function for binding function arguments to logger.

These arguments are passed in as a mapping and then jsonified into a string.

Parameters
*   **fargs_map** (`Optional`[`Mapping`[`str`, `Any`]]) – A mapping of function arguments. We typically pass in locals() for this argument at the start of a function that contains log messages.

*   **kwargs** (`Any`) – Additional function arguments can be passed in as keyword arguments.

Return type
[`BetterBoundLogger`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "logrus._core.BetterBoundLogger")

new(_**new\_values_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger.new)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger.new "Permalink to this definition")
We override this function’s type signature _only_.

Parameters
**new_values** (`Any`) –

Return type
[`BetterBoundLogger`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "logrus._core.BetterBoundLogger")

trace(_event=None_, _*args_, _**kwargs_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger.trace)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger.trace "Permalink to this definition")
Log a new TRACE level message.

Parameters
*   **event** (`Union`[`str`, `Dict`[`str`, `Any`], `None`]) –

*   **args** (`Any`) –

*   **kwargs** (`Any`) –

Return type
`None`

try_unbind(_*keys_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger.try_unbind)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger.try_unbind "Permalink to this definition")
We override this function’s type signature _only_.

Parameters
**keys** (`str`) –

Return type
[`BetterBoundLogger`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "logrus._core.BetterBoundLogger")

unbind(_*keys_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#BetterBoundLogger.unbind)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger.unbind "Permalink to this definition")
We override this function’s type signature _only_.

Parameters
**keys** (`str`) –

Return type
[`BetterBoundLogger`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "logrus._core.BetterBoundLogger")

_class_ Log(_file_, _format='json'_, _level=None_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#Log)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.Log "Permalink to this definition")
Bases: `object`

Log specification for a file or stream.

Parameters
*   **file** (`str`) – The file to add log messages to (special values: stderr, stdout).

*   **format** (`Literal`[‘json’, ‘color’, ‘nocolor’]) – The logging format (e.g. color or json).

*   **level** (`Optional`[`Literal`[‘TRACE’, ‘DEBUG’, ‘INFO’, ‘WARNING’, ‘ERROR’, ‘CRITICAL’]]) – The logging level. If this is not set, a reasonable default level is used depending on whether we are logging to a file or the console (e.g. stderr).

file[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.Log.file "Permalink to this definition")format _='json'_[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.Log.format "Permalink to this definition")level _=None_[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.Log.level "Permalink to this definition")Logger(_name=None_, _**kwargs_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#Logger)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.Logger "Permalink to this definition")
Returns a structured logger.

This logger is capable of handling positional format arguments as well as keyword arguments and can be bound for context-specific logging.

Parameters
*   **name** (`Optional`[`str`]) – The name of the logger.

*   **kwargs** (`Any`) – These parameters will be bound to the returned logger.

Return type
[`BetterBoundLogger`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.BetterBoundLogger "logrus._core.BetterBoundLogger")

Returns
A structlog logger with a few extra custom methods (e.g. logger.trace() and logger.bind_fargs()). See structlog’s documentation for more information:

[https://www.structlog.org/en/stable/loggers.html](https://www.structlog.org/en/stable/loggers.html)

Warning

This logger should only be used for applications, NOT libraries.

get_default_logfile(_stem_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#get_default_logfile)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.get_default_logfile "Permalink to this definition")
Returns full path to logfile using default directory locations.

Parameters
**stem** (`str`) – The logfile’s final path component, without its suffix.

Return type
`Path`

init_logging(_*_, _logs=(Log(file='stderr',format='color',level=None),)_, _verbose=0_)[[source]](https://python-logrus.readthedocs.io/en/latest/_modules/logrus/_core.html#init_logging)[](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.init_logging "Permalink to this definition")
Configure standard logging (for libraries) and structlog (for apps).

This function can be called multiple times but will do nothing if called with the same arguments and structlog is still configured (this latter check is mostly just needed for testing).

Parameters
*   **logs** (`Iterable`[[`Log`](https://python-logrus.readthedocs.io/en/latest/logrus.html#logrus.Log "logrus._core.Log")]) – This list of Log objects determines which logging handlers we configure and enable, what logging level we use for each handler, and what log message format we use for each handler.

*   **verbose** (`int`) –

A non-negative integer. If greater than zero, this option affects the default logging level used when a Log object in `logs` does not have its level attribute set and causes additional values (e.g. PID, thread name) to be added to each log record. More precisely, the following rules apply to the `verbose` argument:

if verbose >= 1…
    *   The default log level is set to DEBUG instead of INFO.

    *   We show microseconds in each log record’s timestamp instead of milliseconds.

    *   The current PID and thread name are added to each log record.

if verbose >= 2…
    *   The line number, function name, module name, and function parameters [if the logger bound them by calling logger.bind_fargs()] are added to each log record.

if verbose >= 3…
    *   The default log level is set to TRACE instead of INFO.

Note

If no ‘stderr’ or ‘stdout’ Log is found in `logs`, we add a default ‘stderr’ Log object to the list.

Return type
`None`

Submodules[](https://python-logrus.readthedocs.io/en/latest/logrus.html#submodules "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

*   [logrus.pytest_plugin module](https://python-logrus.readthedocs.io/en/latest/logrus.pytest_plugin.html)

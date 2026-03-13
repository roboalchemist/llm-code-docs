# Switching from Standard Logging to Loguru

## Introduction to logging in Python

First and foremost, it is important to understand some basic concepts about logging in Python.

Logging is an essential part of any application, as it allows you to track the behavior of your code and diagnose issues. It associates messages with severity levels which are collected and dispatched to readable outputs called handlers.

For newcomers, take a look at the tutorial in the Python documentation: Logging HOWTO [https://docs.python.org/3/howto/logging.html].

## Fundamental differences between `logging` and `loguru`

Although `loguru` is written “from scratch” and does not rely on standard `logging` internally, both libraries serve the same purpose: provide functionalities to implement a flexible event logging system. The main difference is that standard `logging` requires the user to explicitly instantiate named `Logger` and configure them with `Handler`, `Formatter` and `Filter`, while `loguru` tries to narrow down the amount of configuration steps.

Apart from that, usage is globally the same, once the `logger` object is created or imported you can start using it to log messages with the appropriate severity (`logger.debug("Dev message")`, `logger.warning("Danger!")`, etc.), messages which are then sent to the configured handlers.

As for standard logging, default logs are sent to `sys.stderr` rather than `sys.stdout`. The POSIX standard specifies that  `stderr` is the correct stream for “diagnostic output”. The main compelling case in favor or logging to `stderr` is that it avoids mixing the actual output of the application with debug information. Consider for example pipe-redirection like `python my_app.py | other_app` which would not be possible if logs were emitted to `stdout`. Another major benefit is that Python resolves encoding issues on `sys.stderr` by escaping faulty characters (`"backslashreplace"` policy) while it raises an `UnicodeEncodeError` (`"strict"` policy) on `sys.stdout`.

## Replacing `getLogger()` function

It is usual to call `getLogger()` [https://docs.python.org/3/library/logging.html#logging.getLogger] at the beginning of each file to retrieve and use a logger across your module, like this: `logger = logging.getLogger(__name__)`.

Using Loguru, there is no need to explicitly get and name a logger, `from loguru import logger` suffices. Each time this imported logger is used, a record is created and will automatically contain the contextual `__name__` value.

As for standard logging, the `name` attribute can then be used to format and filter your logs.

## Replacing `Logger` objects

Loguru replaces the standard `Logger` [https://docs.python.org/3/library/logging.html#logging.Logger] configuration by a proper sink definition. Instead of configuring a logger, you should `add()` and parametrize your handlers. The `setLevel()` [https://docs.python.org/3/library/logging.html#logging.Logger.setLevel] and `addFilter()` [https://docs.python.org/3/library/logging.html#logging.Logger.addFilter] are suppressed by the configured sink `level` and `filter` parameters. The `propagate` [https://docs.python.org/3/library/logging.html#logging.Logger.propagate] attribute and `disable()` [https://docs.python.org/3/library/logging.html#logging.disable] function can be replaced by the `filter` option too. The `makeRecord()` [https://docs.python.org/3/library/logging.html#logging.Logger.makeRecord] method can be replaced using the `record["extra"]` dict.

Sometimes, more fine-grained control is required over a particular logger. In such case, Loguru provides the `bind()` method which can be in particular used to generate a specifically named logger.

For example, by calling `other_logger = logger.bind(name="other")`, each message logged using `other_logger` will populate the `record["extra"]` dict with the `name` value, while using `logger` won’t. This permits differentiating logs from `logger` or `other_logger` from within your sink or filter function.

Let suppose you want a sink to log only some very specific messages:

```
def specific_only(record):
    return "specific" in record["extra"]

logger.add("specific.log", filter=specific_only)

specific_logger = logger.bind(specific=True)

logger.info("General message")          # This is filtered-out by the specific sink
specific_logger.info("Module message")  # This is accepted by the specific sink (and others)

```
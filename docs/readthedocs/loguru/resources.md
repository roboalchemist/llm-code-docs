# Help & Guides

- Switching from Standard Logging to Loguru

  - Introduction to logging in Python

  - Fundamental differences between `logging` and `loguru`

  - Replacing `getLogger()` function

  - Replacing `Logger` objects

  - Replacing `Handler`, `Filter` and `Formatter` objects

  - Replacing `LogRecord` objects

  - Replacing `%` style formatting of messages

  - Replacing `exc_info` argument

  - Replacing `extra` argument and `LoggerAdapter` objects

  - Replacing `isEnabledFor()` method

  - Replacing `addLevelName()` and `getLevelName()` functions

  - Replacing `basicConfig()` and `dictConfig()` functions

  - Replacing `captureWarnings()` function

  - Replacing `assertLogs()` method from `unittest` library

  - Replacing `caplog` fixture from `pytest` library

- Frequently Asked Questions and Troubleshooting Tips for Loguru

  - How do I create and configure a logger?

  - Why are my logs duplicated in the output?

  - How do I set the logging level?

  - Why isn’t the level name shown when using an integer or a built-in level?

  - How do I customize the log format and re-use the default one?

  - Why are my logs not colored?

  - Why are my logs not showing up?

  - Why is the captured exception missing from the formatted message?

  - How can I use different loggers in different modules of my application?

  - Why are my log files sometimes duplicated or the content trimmed?

  - Why am I facing errors when I use a custom formatting function?

  - Why logging a message with f-string sometimes raises an exception?

  - How do I fix “ValueError: I/O operation error on closed file”?

  - How do I prevent “RuntimeError” due to “deadlock avoided”?

  - Why is the source (name, file, function, line) of the log message incorrect or missing?

  - Why can’t I access the `Logger` class and other types at runtime?

- Code Snippets and Recipes for Loguru

  - Security considerations when using Loguru

  - Avoiding logs to be printed twice on the terminal

  - Changing the level of an existing handler

  - Configuring Loguru to be used by a library or an application

  - Transmitting log messages across network, processes or Gunicorn workers

  - Using ZMQ to send and receive log messages

  - Resolving `UnicodeEncodeError` and other encoding issues

  - Logging entry and exit of functions with a decorator

  - Using logging function based on custom added levels

  - Setting permissions on created log files

  - Preserving an `opt()` parameter for the whole module

  - Serializing log messages using a custom function

  - Adapting colors and format of logged messages dynamically

  - Dynamically formatting messages to properly align values with padding

  - Customizing the formatting of exceptions

  - Displaying a stacktrace without using the error context

  - Manipulating newline terminator to write multiple logs on the same line

  - Capturing standard `stdout`, `stderr` and `warnings`

  - Circumventing modules whose `__name__` value is absent

  - Interoperability with `tqdm` iterations

  - Using Loguru’s `logger` within a Cython module

  - Creating independent loggers with separate set of handlers

  - Compatibility with `multiprocessing` using `enqueue` argument

  - Unit testing logs emitted by Loguru

  - Add OpenTelemetry `trace_id` and `span_id` to logs
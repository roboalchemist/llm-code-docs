# Source: https://loguru.readthedocs.io/en/stable/resources.html

Title: Help & Guides — loguru documentation

URL Source: https://loguru.readthedocs.io/en/stable/resources.html

Markdown Content:
Help & Guides — loguru documentation
===============

[loguru](https://loguru.readthedocs.io/en/stable/index.html)

*   [Overview](https://loguru.readthedocs.io/en/stable/overview.html)
*   [API Reference](https://loguru.readthedocs.io/en/stable/api.html)
*   [Help & Guides](https://loguru.readthedocs.io/en/stable/resources.html#)
    *   [Switching from Standard Logging to Loguru](https://loguru.readthedocs.io/en/stable/resources/migration.html)
    *   [Frequently Asked Questions and Troubleshooting Tips for Loguru](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html)
    *   [Code Snippets and Recipes for Loguru](https://loguru.readthedocs.io/en/stable/resources/recipes.html)

*   [Project Information](https://loguru.readthedocs.io/en/stable/project.html)

[![Image 1: Sponsored: Augment](https://media.ethicalads.io/media/images/2026/01/cropped_2Hd7jQi.png)](https://server.ethicalads.io/proxy/click/10072/019cdf48-2301-74e3-bdf1-604d435f00cc/)

[**Still Using Cursor?**Fix bugs faster with Augment's full-codebase context.**Install Now**](https://server.ethicalads.io/proxy/click/10072/019cdf48-2301-74e3-bdf1-604d435f00cc/)

_[Ad by EthicalAds](https://www.ethicalads.io/?ref=rtd-sidebar)_ · [ℹ️](https://www.ethicalads.io/advertisers/?ref=rtd-sidebar-buy-ads)

![Image 2](https://server.ethicalads.io/proxy/view/10072/019cdf48-2301-74e3-bdf1-604d435f00cc/)

[loguru](https://loguru.readthedocs.io/en/stable/index.html)

*   [](https://loguru.readthedocs.io/en/stable/index.html)
*   Help & Guides

* * *

Help & Guides[](https://loguru.readthedocs.io/en/stable/resources.html#help-guides "Link to this heading")
===========================================================================================================

*   [Switching from Standard Logging to Loguru](https://loguru.readthedocs.io/en/stable/resources/migration.html)
    *   [Introduction to logging in Python](https://loguru.readthedocs.io/en/stable/resources/migration.html#introduction-to-logging-in-python)
    *   [Fundamental differences between `logging` and `loguru`](https://loguru.readthedocs.io/en/stable/resources/migration.html#fundamental-differences-between-logging-and-loguru)
    *   [Replacing `getLogger()` function](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-getlogger-function)
    *   [Replacing `Logger` objects](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-logger-objects)
    *   [Replacing `Handler`, `Filter` and `Formatter` objects](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-handler-filter-and-formatter-objects)
    *   [Replacing `LogRecord` objects](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-logrecord-objects)
    *   [Replacing `%` style formatting of messages](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-style-formatting-of-messages)
    *   [Replacing `exc_info` argument](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-exc-info-argument)
    *   [Replacing `extra` argument and `LoggerAdapter` objects](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-extra-argument-and-loggeradapter-objects)
    *   [Replacing `isEnabledFor()` method](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-isenabledfor-method)
    *   [Replacing `addLevelName()` and `getLevelName()` functions](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-addlevelname-and-getlevelname-functions)
    *   [Replacing `basicConfig()` and `dictConfig()` functions](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-basicconfig-and-dictconfig-functions)
    *   [Replacing `captureWarnings()` function](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-capturewarnings-function)
    *   [Replacing `assertLogs()` method from `unittest` library](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-assertlogs-method-from-unittest-library)
    *   [Replacing `caplog` fixture from `pytest` library](https://loguru.readthedocs.io/en/stable/resources/migration.html#replacing-caplog-fixture-from-pytest-library)

*   [Frequently Asked Questions and Troubleshooting Tips for Loguru](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html)
    *   [How do I create and configure a logger?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#how-do-i-create-and-configure-a-logger)
    *   [Why are my logs duplicated in the output?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-are-my-logs-duplicated-in-the-output)
    *   [How do I set the logging level?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#how-do-i-set-the-logging-level)
    *   [How do I customize the log format and re-use the default one?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#how-do-i-customize-the-log-format-and-re-use-the-default-one)
    *   [Why are my logs not colored?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-are-my-logs-not-colored)
    *   [Why are my logs not appearing in the output?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-are-my-logs-not-appearing-in-the-output)
    *   [How can I use different loggers in different modules of my application?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#how-can-i-use-different-loggers-in-different-modules-of-my-application)
    *   [Why are my log files sometimes duplicated or the content trimmed?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-are-my-log-files-sometimes-duplicated-or-the-content-trimmed)
    *   [Why logging a message with f-string sometimes raises an exception?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-logging-a-message-with-f-string-sometimes-raises-an-exception)
    *   [How do I fix “ValueError: I/O operation error on closed file”?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#how-do-i-fix-valueerror-i-o-operation-error-on-closed-file)
    *   [How do I prevent “RuntimeError” due to “deadlock avoided”?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#how-do-i-prevent-runtimeerror-due-to-deadlock-avoided)
    *   [Why is the source (name, file, function, line) of the log message incorrect or missing?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-is-the-source-name-file-function-line-of-the-log-message-incorrect-or-missing)
    *   [Why can’t I access the `Logger` class and other types at runtime?](https://loguru.readthedocs.io/en/stable/resources/troubleshooting.html#why-can-t-i-access-the-logger-class-and-other-types-at-runtime)

*   [Code Snippets and Recipes for Loguru](https://loguru.readthedocs.io/en/stable/resources/recipes.html)
    *   [Security considerations when using Loguru](https://loguru.readthedocs.io/en/stable/resources/recipes.html#security-considerations-when-using-loguru)
    *   [Avoiding logs to be printed twice on the terminal](https://loguru.readthedocs.io/en/stable/resources/recipes.html#avoiding-logs-to-be-printed-twice-on-the-terminal)
    *   [Changing the level of an existing handler](https://loguru.readthedocs.io/en/stable/resources/recipes.html#changing-the-level-of-an-existing-handler)
    *   [Configuring Loguru to be used by a library or an application](https://loguru.readthedocs.io/en/stable/resources/recipes.html#configuring-loguru-to-be-used-by-a-library-or-an-application)
    *   [Sending and receiving log messages across network or processes](https://loguru.readthedocs.io/en/stable/resources/recipes.html#sending-and-receiving-log-messages-across-network-or-processes)
    *   [Resolving `UnicodeEncodeError` and other encoding issues](https://loguru.readthedocs.io/en/stable/resources/recipes.html#resolving-unicodeencodeerror-and-other-encoding-issues)
    *   [Logging entry and exit of functions with a decorator](https://loguru.readthedocs.io/en/stable/resources/recipes.html#logging-entry-and-exit-of-functions-with-a-decorator)
    *   [Using logging function based on custom added levels](https://loguru.readthedocs.io/en/stable/resources/recipes.html#using-logging-function-based-on-custom-added-levels)
    *   [Setting permissions on created log files](https://loguru.readthedocs.io/en/stable/resources/recipes.html#setting-permissions-on-created-log-files)
    *   [Preserving an `opt()` parameter for the whole module](https://loguru.readthedocs.io/en/stable/resources/recipes.html#preserving-an-opt-parameter-for-the-whole-module)
    *   [Serializing log messages using a custom function](https://loguru.readthedocs.io/en/stable/resources/recipes.html#serializing-log-messages-using-a-custom-function)
    *   [Rotating log file based on both size and time](https://loguru.readthedocs.io/en/stable/resources/recipes.html#rotating-log-file-based-on-both-size-and-time)
    *   [Adapting colors and format of logged messages dynamically](https://loguru.readthedocs.io/en/stable/resources/recipes.html#adapting-colors-and-format-of-logged-messages-dynamically)
    *   [Dynamically formatting messages to properly align values with padding](https://loguru.readthedocs.io/en/stable/resources/recipes.html#dynamically-formatting-messages-to-properly-align-values-with-padding)
    *   [Customizing the formatting of exceptions](https://loguru.readthedocs.io/en/stable/resources/recipes.html#customizing-the-formatting-of-exceptions)
    *   [Displaying a stacktrace without using the error context](https://loguru.readthedocs.io/en/stable/resources/recipes.html#displaying-a-stacktrace-without-using-the-error-context)
    *   [Manipulating newline terminator to write multiple logs on the same line](https://loguru.readthedocs.io/en/stable/resources/recipes.html#manipulating-newline-terminator-to-write-multiple-logs-on-the-same-line)
    *   [Capturing standard `stdout`, `stderr` and `warnings`](https://loguru.readthedocs.io/en/stable/resources/recipes.html#capturing-standard-stdout-stderr-and-warnings)
    *   [Circumventing modules whose `__name__` value is absent](https://loguru.readthedocs.io/en/stable/resources/recipes.html#circumventing-modules-whose-name-value-is-absent)
    *   [Interoperability with `tqdm` iterations](https://loguru.readthedocs.io/en/stable/resources/recipes.html#interoperability-with-tqdm-iterations)
    *   [Using Loguru’s `logger` within a Cython module](https://loguru.readthedocs.io/en/stable/resources/recipes.html#using-loguru-s-logger-within-a-cython-module)
    *   [Creating independent loggers with separate set of handlers](https://loguru.readthedocs.io/en/stable/resources/recipes.html#creating-independent-loggers-with-separate-set-of-handlers)
    *   [Compatibility with `multiprocessing` using `enqueue` argument](https://loguru.readthedocs.io/en/stable/resources/recipes.html#compatibility-with-multiprocessing-using-enqueue-argument)
    *   [Testing logging](https://loguru.readthedocs.io/en/stable/resources/recipes.html#testing-logging)

[Previous](https://loguru.readthedocs.io/en/stable/api/type_hints.html "Type Hints")[Next](https://loguru.readthedocs.io/en/stable/resources/migration.html "Switching from Standard Logging to Loguru")

* * *

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org/).

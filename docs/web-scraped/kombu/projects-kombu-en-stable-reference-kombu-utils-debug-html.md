# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.debug.html

Title: kombu.utils.debug — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.debug.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.debug.html).

Debugging Utilities - `kombu.utils.debug`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.debug.html#debugging-utilities-kombu-utils-debug "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Debugging support.

_class_ kombu.utils.debug.Logwrapped(_instance:[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport "kombu.transport.SLMQ.Transport")_, _logger:Logger|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _ident:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/debug.html#Logwrapped)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.debug.html#kombu.utils.debug.Logwrapped "Link to this definition")
Wrap all object methods, to log on call.

kombu.utils.debug.setup_logging(_loglevel:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=10_, _loggers:[list](https://docs.python.org/dev/library/stdtypes.html#list "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")]|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/debug.html#setup_logging)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.debug.html#kombu.utils.debug.setup_logging "Link to this definition")
Setup logging to stdout.

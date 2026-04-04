# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html

Title: kombu.utils.compat — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.compat.html).

Python Compatibility - `kombu.utils.compat`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#python-compatibility-kombu-utils-compat "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Python Compatibility Utilities.

kombu.utils.compat.coro(_gen_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/compat.html#coro)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#kombu.utils.compat.coro "Link to this definition")
Decorator to mark generator as co-routine.

kombu.utils.compat.detect_environment()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/compat.html#detect_environment)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#kombu.utils.compat.detect_environment "Link to this definition")
Detect the current environment: default, eventlet, or gevent.

kombu.utils.compat.entrypoints(_namespace_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/compat.html#entrypoints)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#kombu.utils.compat.entrypoints "Link to this definition")
Return setuptools entrypoints for namespace.

kombu.utils.compat.fileno(_f_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/compat.html#fileno)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#kombu.utils.compat.fileno "Link to this definition")
Get fileno from file-like object.

kombu.utils.compat.maybe_fileno(_f_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/compat.html#maybe_fileno)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#kombu.utils.compat.maybe_fileno "Link to this definition")
Get object fileno, or `None` if not defined.

kombu.utils.compat.nested(_*managers_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/compat.html#nested)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.compat.html#kombu.utils.compat.nested "Link to this definition")
Nest context managers.

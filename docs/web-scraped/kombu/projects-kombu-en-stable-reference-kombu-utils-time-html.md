# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.time.html

Title: kombu.utils.time — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.time.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.time.html).

Time Utilities - `kombu.utils.time`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.time.html#time-utilities-kombu-utils-time "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Time Utilities.

kombu.utils.time.maybe_s_to_ms(_v:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")|[float](https://docs.python.org/dev/library/functions.html#float "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")_)→[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/time.html#maybe_s_to_ms)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.time.html#kombu.utils.time.maybe_s_to_ms "Link to this definition")
Convert seconds to milliseconds, but return None for None.

# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html

Title: in Transports - kombu.transport — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.html).

Built-in transports.

*   [Data](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#data)

*   [Functions](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#functions)

[Data](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#data "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

kombu.transport.DEFAULT_TRANSPORT[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#kombu.transport.DEFAULT_TRANSPORT "Link to this definition")
Default transport used when no transport specified.

kombu.transport.TRANSPORT_ALIASES[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#kombu.transport.TRANSPORT_ALIASES "Link to this definition")
Mapping of transport aliases/class names.

[Functions](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#functions "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

kombu.transport.get_transport_cls(_transport:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport.html#get_transport_cls)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#kombu.transport.get_transport_cls "Link to this definition")
Get transport class by name.

The transport string is the full path to a transport class, e.g.:

"kombu.transport.pyamqp:Transport"

If the name does not include “.” (is not fully qualified), the alias table will be consulted.

kombu.transport.resolve_transport(_transport:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport.html#resolve_transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#kombu.transport.resolve_transport "Link to this definition")
Get transport by name.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.html#arguments "Link to this heading")

> transport (Union[str, type]): This can be either
> an actual transport class, or the fully qualified path to a transport class, or the alias of a transport.

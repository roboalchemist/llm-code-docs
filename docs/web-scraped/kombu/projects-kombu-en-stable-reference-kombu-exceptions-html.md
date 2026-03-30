# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html

Title: kombu.exceptions — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.exceptions.html).

Exceptions.

_exception_ kombu.exceptions.NotBoundError[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/exceptions.html#NotBoundError)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.NotBoundError "Link to this definition")
Trying to call channel dependent method on unbound entity.

_exception_ kombu.exceptions.MessageStateError[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/exceptions.html#MessageStateError)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.MessageStateError "Link to this definition")
The message has already been acknowledged.

kombu.exceptions.TimeoutError[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.TimeoutError "Link to this definition")
alias of [`timeout`](https://docs.python.org/dev/library/socket.html#socket.timeout "(in Python v3.15)")

_exception_ kombu.exceptions.LimitExceeded[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/exceptions.html#LimitExceeded)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.LimitExceeded "Link to this definition")
Limit exceeded.

_exception_ kombu.exceptions.ConnectionLimitExceeded[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/exceptions.html#ConnectionLimitExceeded)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.ConnectionLimitExceeded "Link to this definition")
Maximum number of simultaneous connections exceeded.

_exception_ kombu.exceptions.ChannelLimitExceeded[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/exceptions.html#ChannelLimitExceeded)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.ChannelLimitExceeded "Link to this definition")
Maximum number of simultaneous channels exceeded.

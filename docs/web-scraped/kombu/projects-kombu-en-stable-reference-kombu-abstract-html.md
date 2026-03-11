# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html

Title: kombu.abstract — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.abstract.html).

Object utilities.

_class_ kombu.abstract.MaybeChannelBound(_*args:[Any](https://docs.python.org/dev/library/typing.html#typing.Any "(in Python v3.15)")_, _**kwargs:[Any](https://docs.python.org/dev/library/typing.html#typing.Any "(in Python v3.15)")_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/abstract.html#MaybeChannelBound)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound "Link to this definition")
Mixin for classes that can be bound to an AMQP channel.

bind(_channel:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")|[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection")_)→_MaybeChannelBoundType[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/abstract.html#MaybeChannelBound.bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.bind "Link to this definition")
Create copy of the instance that is bound to a channel.

can_cache_declaration _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.can_cache_declaration "Link to this definition")
Defines whether maybe_declare can skip declaring this entity twice.

_property_ channel _:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.channel "Link to this definition")
Current channel if the object is bound.

_property_ is_bound _:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.is_bound "Link to this definition")
Flag set if the channel is bound.

maybe_bind(_channel:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")|[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection")_)→_MaybeChannelBoundType[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/abstract.html#MaybeChannelBound.maybe_bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.maybe_bind "Link to this definition")
Bind instance to channel if not already bound.

revive(_channel:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")_)→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/abstract.html#MaybeChannelBound.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.revive "Link to this definition")
Revive channel after the connection has been re-established.

Used by [`ensure()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.ensure "kombu.Connection.ensure").

when_bound()→[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/abstract.html#MaybeChannelBound.when_bound)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.abstract.html#kombu.abstract.MaybeChannelBound.when_bound "Link to this definition")
Callback called when the class is bound.

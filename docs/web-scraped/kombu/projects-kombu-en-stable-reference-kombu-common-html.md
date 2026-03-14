# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html

Title: kombu.common — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.common.html).

Common Utilities - `kombu.common`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#common-utilities-kombu-common "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Common Utilities.

_class_ kombu.common.Broadcast(_name=None_, _queue=None_, _unique=False_, _auto\_delete=True_, _exchange=None_, _alias=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#Broadcast)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.Broadcast "Link to this definition")
Broadcast queue.

Convenience class used to define broadcast queues.

Every queue instance will have a unique name, and both the queue and exchange is configured with auto deletion.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#arguments "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

> name (str): This is used as the name of the exchange. queue (str): By default a unique id is used for the queue
> 
> 
> > name for every consumer. You can specify a custom queue name here.
> 
> unique (bool): Always create a unique queue
> even if a queue name is supplied.
> 
> [**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#id1)kwargs (Any): See [`Queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "kombu.Queue") for a list
> of additional keyword arguments supported.

attrs _:[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),Any],...]_ _=(('name',None),('exchange',None),('routing\_key',None),('queue\_arguments',None),('binding\_arguments',None),('consumer\_arguments',None),('durable',<class'bool'>),('exclusive',<class'bool'>),('auto\_delete',<class'bool'>),('no\_ack',None),('alias',None),('bindings',<class'list'>),('no\_declare',<class'bool'>),('expires',<class'float'>),('message\_ttl',<class'float'>),('max\_length',<class'int'>),('max\_length\_bytes',<class'int'>),('max\_priority',<class'int'>),('queue',None))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.Broadcast.attrs "Link to this definition")
Generator collecting replies from `queue`.

kombu.common.drain_consumer(_consumer_, _limit=1_, _timeout=None_, _callbacks=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#drain_consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.drain_consumer "Link to this definition")
Drain messages from consumer instance.

kombu.common.eventloop(_conn_, _limit=None_, _timeout=None_, _ignore\_timeouts=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#eventloop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.eventloop "Link to this definition")
Best practice generator wrapper around `Connection.drain_events`.

Able to drain events forever, with a limit, and optionally ignoring timeout errors (a timeout of 1 is often used in environments where the socket can get “stuck”, and is a best practice for Kombu consumers).

`eventloop` is a generator.

Examples

>>> from kombu.common import eventloop

>>> def run(conn):
...     it = eventloop(conn, timeout=1, ignore_timeouts=True)
...     next(it)   # one event consumed, or timed out.
...
...     for _ in eventloop(conn, timeout=1, ignore_timeouts=True):
...         pass  # loop forever.

It also takes an optional limit parameter, and timeout errors are propagated by default:

for _ in eventloop(connection, limit=1, timeout=1):
    pass

kombu.common.insured(_pool_, _fun_, _args_, _kwargs_, _errback=None_, _on\_revive=None_, _**opts_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#insured)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.insured "Link to this definition")
Function wrapper to handle connection errors.

Ensures function performing broker commands completes despite intermittent connection failures.

kombu.common.itermessages(_conn_, _channel_, _queue_, _limit=1_, _timeout=None_, _callbacks=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#itermessages)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.itermessages "Link to this definition")
Iterator over messages.

kombu.common.maybe_declare(_entity_, _channel=None_, _retry=False_, _**retry\_policy_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#maybe_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.maybe_declare "Link to this definition")
Declare entity (cached).

kombu.common.send_reply(_exchange_, _req_, _msg_, _producer=None_, _retry=False_, _retry\_policy=None_, _**props_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/common.html#send_reply)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.send_reply "Link to this definition")
Send reply for request.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#id3 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

> exchange (kombu.Exchange, str): Reply exchange req (~kombu.Message): Original request, a message with
> 
> 
> > a `reply_to` property.
> 
> 
> producer (kombu.Producer): Producer instance retry (bool): If true must retry according to
> 
> 
> > the `reply_policy` argument.
> 
> 
> retry_policy (Dict): Retry settings. [**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#id4)props (Any): Extra properties.

kombu.common.uuid(_\_uuid:~typing.Callable[[]_, _~uuid.UUID]=<function uuid4>_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/uuid.html#uuid)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.uuid "Link to this definition")
Generate unique id in UUID4 format.

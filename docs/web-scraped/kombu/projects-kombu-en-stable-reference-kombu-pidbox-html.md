# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html

Title: kombu.pidbox — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.pidbox.html).

Generic process mailbox.

*   [Introduction](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#introduction)

    *   [Creating the applications Mailbox](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#creating-the-applications-mailbox)

    *   [Example Node](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#example-node)

    *   [Example Client](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#example-client)

*   [Mailbox](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#mailbox)

    *   [Mailbox Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#mailbox-options)

*   [Node](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#node)

[Introduction](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#introduction "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Creating the applications Mailbox](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#creating-the-applications-mailbox "Link to this heading")

>>> mailbox = pidbox.Mailbox('celerybeat', type='direct')

>>> @mailbox.handler
>>> def reload_schedule(state, **kwargs):
...     state['beat'].reload_schedule()

>>> @mailbox.handler
>>> def connection_info(state, **kwargs):
...     return {'connection': state['connection'].info()}

### [Example Node](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#example-node "Link to this heading")

>>> connection = kombu.Connection()
>>> state = {'beat': beat,
 'connection': connection}
>>> consumer = mailbox(connection).Node(hostname).listen()
>>> try:
...     while True:
...         connection.drain_events(timeout=1)
... finally:
...     consumer.cancel()

### [Example Client](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#example-client "Link to this heading")

>>> mailbox.cast('reload_schedule')   # cast is async.
>>> info = celerybeat.call('connection_info', timeout=1)

[Mailbox](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#mailbox "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.pidbox.Mailbox(_namespace_, _type='direct'_, _connection=None_, _clock=None_, _accept=None_, _serializer=None_, _producer\_pool=None_, _queue\_ttl=None_, _queue\_expires=None_, _queue\_durable=False_, _queue\_exclusive=False_, _reply\_queue\_ttl=None_, _reply\_queue\_expires=10.0_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox "Link to this definition")
Process Mailbox.

namespace _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.namespace "Link to this definition")
Name of application.

connection _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.connection "Link to this definition")
Connection (if bound).

type _='direct'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.type "Link to this definition")
Exchange type (usually direct, or fanout for broadcast).

exchange _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.exchange "Link to this definition")
mailbox exchange (init by constructor).

reply_exchange _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.reply_exchange "Link to this definition")
exchange to send replies to.

Node(_hostname=None_, _state=None_, _channel=None_, _handlers=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.Node)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.Node "Link to this definition")call(_destination_, _command_, _kwargs=None_, _timeout=None_, _callback=None_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.call)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.call "Link to this definition")cast(_destination_, _command_, _kwargs=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.cast)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.cast "Link to this definition")abcast(_command_, _kwargs=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.abcast)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.abcast "Link to this definition")multi_call(_command_, _kwargs=None_, _timeout=1_, _limit=None_, _callback=None_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.multi_call)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.multi_call "Link to this definition")get_reply_queue()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.get_reply_queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.get_reply_queue "Link to this definition")get_queue(_hostname_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Mailbox.get_queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox.get_queue "Link to this definition")
### [Mailbox Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#mailbox-options "Link to this heading")

Added in version 5.6.0.

The Mailbox supports several configuration options that affect the behavior of its exchanges and queues.

*   `durable`: If True, declares durable exchanges that survive broker restarts.

*   `exclusive`: If True, declares exclusive exchanges (usable by only one connection).

These provide finer control over broker-side behavior and are useful in production environments where queue durability matters.

[Node](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#node "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.pidbox.Node(_hostname_, _state=None_, _channel=None_, _handlers=None_, _mailbox=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node "Link to this definition")
Mailbox node.

hostname _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.hostname "Link to this definition")
hostname of the node.

mailbox _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.mailbox "Link to this definition")
the [`Mailbox`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Mailbox "kombu.pidbox.Mailbox") this is a node for.

handlers _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.handlers "Link to this definition")
map of method name/handlers.

state _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.state "Link to this definition")
current context (passed on to handlers)

channel _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.channel "Link to this definition")
current channel.

Consumer(_channel=None_, _no\_ack=True_, _accept=None_, _**options_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.Consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.Consumer "Link to this definition")handler(_fun_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.handler)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.handler "Link to this definition")listen(_channel=None_, _callback=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.listen)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.listen "Link to this definition")dispatch(_method_, _arguments=None_, _reply\_to=None_, _ticket=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.dispatch)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.dispatch "Link to this definition")dispatch_from_message(_body_, _message=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.dispatch_from_message "Link to this definition")handle_call(_method_, _arguments_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.handle_call)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.handle_call "Link to this definition")handle_cast(_method_, _arguments_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.handle_cast)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.handle_cast "Link to this definition")handle(_method_, _arguments=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.handle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.handle "Link to this definition")handle_message(_body_, _message=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.handle_message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.handle_message "Link to this definition")reply(_data_, _exchange_, _routing\_key_, _ticket_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pidbox.html#Node.reply)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pidbox.html#kombu.pidbox.Node.reply "Link to this definition")

# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html

Title: memory Transport - kombu.transport.memory — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.memory.html).

In-memory transport module for Kombu.

Simple transport using memory for storing messages. Messages can be passed only between threads.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: No

*   Supports Priority: No

*   Supports TTL: Yes

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#connection-string "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string is in the following format:

memory://

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#connection-string)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.memory.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/memory.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport "Link to this definition")
In-memory Transport.

_class_ Channel(_connection_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel "Link to this definition")
In-memory Channel.

after_reply_message_received(_queue_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel.after_reply_message_received "Link to this definition")
Callback called after RPC reply received.

Notes

Reply queue semantics: can be used to delete the queue after transient reply message received.

close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

do_restore _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel.do_restore "Link to this definition")
flag to restore unacked messages when channel goes out of scope.

events _={}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel.events "Link to this definition")queues _={}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel.queues "Link to this definition")supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

driver_name _='memory'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='memory'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/memory.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.driver_version "Link to this definition")global_state _=<kombu.transport.virtual.base.BrokerState object>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.global_state "Link to this definition")
memory backend state is global.

implements _={'asynchronous':False,'exchange\_type':frozenset({'direct','fanout','headers','topic'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Transport.implements "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#channel "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.memory.Channel(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/memory.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel "Link to this definition")
In-memory Channel.

after_reply_message_received(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/memory.html#Channel.after_reply_message_received)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel.after_reply_message_received "Link to this definition")
Callback called after RPC reply received.

Notes

Reply queue semantics: can be used to delete the queue after transient reply message received.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/memory.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

do_restore _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel.do_restore "Link to this definition")
flag to restore unacked messages when channel goes out of scope.

events _={}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel.events "Link to this definition")queues _={}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel.queues "Link to this definition")supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.memory.html#kombu.transport.memory.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html

Title: kombu.transport.pyro — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.pyro.html).

Pyro transport module for kombu.

Pyro transport, and Kombu Broker daemon.

Requires the `Pyro4` library to be installed.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: No

*   Supports Priority: No

*   Supports TTL: No

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#connection-string "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To use the Pyro transport with Kombu, use an url of the form:

pyro://localhost/kombu.broker

The hostname is where the transport will be looking for a Pyro name server, which is used in turn to locate the kombu.broker Pyro service. This broker can be launched by simply executing this transport module directly, with the command: `python -m kombu.transport.pyro`

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#transport-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#channel)

*   [KombuBroker](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombubroker)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.pyro.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyro.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport "Link to this definition")
Pyro Transport.

_class_ Channel(_connection_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.Channel "Link to this definition")
Pyro Channel.

after_reply_message_received(_queue_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.Channel.after_reply_message_received "Link to this definition")
Callback called after RPC reply received.

Notes

Reply queue semantics: can be used to delete the queue after transient reply message received.

close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

queues()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.Channel.queues "Link to this definition")_property_ shared_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.Channel.shared_queues "Link to this definition")default_port _=9090_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='pyro'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='pyro'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyro.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.driver_version "Link to this definition")global_state _=<kombu.transport.virtual.base.BrokerState object>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.global_state "Link to this definition")_property_ shared_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Transport.shared_queues "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.pyro.Channel(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyro.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Channel "Link to this definition")
Pyro Channel.

after_reply_message_received(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyro.html#Channel.after_reply_message_received)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Channel.after_reply_message_received "Link to this definition")
Callback called after RPC reply received.

Notes

Reply queue semantics: can be used to delete the queue after transient reply message received.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyro.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

queues()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyro.html#Channel.queues)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Channel.queues "Link to this definition")_property_ shared_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombu.transport.pyro.Channel.shared_queues "Link to this definition")
[KombuBroker](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyro.html#kombubroker "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

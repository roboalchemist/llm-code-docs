# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html

Title: kombu.transport.zookeeper — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.zookeeper.html).

Zookeeper transport module for kombu.

Zookeeper based transport. This transport uses the built-in kazoo Zookeeper based queue implementation.

**References**

*   [https://zookeeper.apache.org/doc/current/recipes.html#sc_recipes_Queues](https://zookeeper.apache.org/doc/current/recipes.html#sc_recipes_Queues)

*   [https://kazoo.readthedocs.io/en/latest/api/recipe/queue.html](https://kazoo.readthedocs.io/en/latest/api/recipe/queue.html)

**Limitations** This queue does not offer reliable consumption. An entry is removed from the queue prior to being processed. So if an error occurs, the consumer has to re-queue the item or it will be lost.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: No

*   Supports Priority: Yes

*   Supports TTL: No

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#connection-string "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connects to a zookeeper node as:

zookeeper://SERVER:PORT/VHOST

The <vhost> becomes the base for all the other znodes. So we can use it like a vhost.

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#transport-options "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.zookeeper.Transport(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/zookeeper.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport "Link to this definition")
Zookeeper Transport.

_class_ Channel(_connection_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.Channel "Link to this definition")
Zookeeper Channel.

_property_ client[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.Channel.client "Link to this definition")channel_errors _=(<class'amqp.exceptions.ChannelError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

connection_errors _=(<class'amqp.exceptions.ConnectionError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

default_port _=2181_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='kazoo'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='zookeeper'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/zookeeper.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.driver_version "Link to this definition")polling_interval _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#channel "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.zookeeper.Channel(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/zookeeper.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Channel "Link to this definition")
Zookeeper Channel.

_property_ client[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.zookeeper.html#kombu.transport.zookeeper.Channel.client "Link to this definition")

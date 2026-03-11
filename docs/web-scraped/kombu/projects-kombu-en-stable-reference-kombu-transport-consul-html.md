# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html

Title: kombu.transport.consul — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.consul.html).

Consul Transport module for Kombu.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It uses Consul.io’s Key/Value store to transport messages in Queues

It uses python-consul for talking to Consul’s HTTP API

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id1 "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Native

*   Supports Direct: Yes

*   Supports Topic: _Unreviewed_

*   Supports Fanout: _Unreviewed_

*   Supports Priority: _Unreviewed_

*   Supports TTL: _Unreviewed_

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#connection-string "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string has the following format:

consul://CONSUL_ADDRESS[:PORT]

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#features)

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id1)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#connection-string)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.consul.Transport(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/consul.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport "Link to this definition")
Consul K/V storage Transport for Kombu.

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.Channel "Link to this definition")
Consul Channel class which talks to the Consul Key/Value store.

index _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.Channel.index "Link to this definition")_property_ lock_name[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.Channel.lock_name "Link to this definition")prefix _='kombu'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.Channel.prefix "Link to this definition")session_ttl _=30_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.Channel.session_ttl "Link to this definition")timeout _='10s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.Channel.timeout "Link to this definition")default_port _=8500_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='consul'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='consul'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/consul.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.driver_version "Link to this definition")verify_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/consul.html#Transport.verify_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Transport.verify_connection "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#channel "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.consul.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/consul.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Channel "Link to this definition")
Consul Channel class which talks to the Consul Key/Value store.

index _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Channel.index "Link to this definition")_property_ lock_name[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Channel.lock_name "Link to this definition")prefix _='kombu'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Channel.prefix "Link to this definition")session_ttl _=30_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Channel.session_ttl "Link to this definition")timeout _='10s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.consul.html#kombu.transport.consul.Channel.timeout "Link to this definition")

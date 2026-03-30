# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html

Title: kombu.transport.etcd — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.etcd.html).

Etcd Transport module for Kombu.

It uses Etcd as a store to transport messages in Queues

It uses python-etcd for talking to Etcd’s HTTP API

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: _Unreviewed_

*   Supports Topic: _Unreviewed_

*   Supports Fanout: _Unreviewed_

*   Supports Priority: _Unreviewed_

*   Supports TTL: _Unreviewed_

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#connection-string "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string has the following format:

'etcd'://SERVER:PORT

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#connection-string)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.etcd.Transport(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/etcd.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport "Link to this definition")
Etcd storage Transport for Kombu.

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel "Link to this definition")
Etcd Channel class which talks to the Etcd.

index _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel.index "Link to this definition")lock_ttl _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel.lock_ttl "Link to this definition")_property_ lock_value[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel.lock_value "Link to this definition")prefix _='kombu'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel.prefix "Link to this definition")session_ttl _=30_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel.session_ttl "Link to this definition")timeout _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.Channel.timeout "Link to this definition")default_port _=2379_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='python-etcd'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='etcd'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/etcd.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.driver_version "Link to this definition")
Return the version of the etcd library.

Note

python-etcd has no __version__. This is a workaround.

implements _={'asynchronous':False,'exchange\_type':frozenset({'direct'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.implements "Link to this definition")polling_interval _=3_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

verify_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/etcd.html#Transport.verify_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Transport.verify_connection "Link to this definition")
Verify the connection works.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.etcd.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/etcd.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel "Link to this definition")
Etcd Channel class which talks to the Etcd.

index _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel.index "Link to this definition")lock_ttl _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel.lock_ttl "Link to this definition")_property_ lock_value[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel.lock_value "Link to this definition")prefix _='kombu'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel.prefix "Link to this definition")session_ttl _=30_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel.session_ttl "Link to this definition")timeout _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.etcd.html#kombu.transport.etcd.Channel.timeout "Link to this definition")

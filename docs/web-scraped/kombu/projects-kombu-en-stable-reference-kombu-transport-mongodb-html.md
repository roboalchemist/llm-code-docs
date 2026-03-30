# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html

Title: kombu.transport.mongodb — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.mongodb.html).

MongoDB transport module for kombu.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: Yes

*   Supports Priority: Yes

*   Supports TTL: Yes

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#connection-string "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> _Unreviewed_

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#transport-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   `connect_timeout`,

*   `ssl`,

*   `ttl`,

*   `capped_queue_size`,

*   `default_hostname`,

*   `default_port`,

*   `default_database`,

*   `messages_collection`,

*   `routing_collection`,

*   `broadcast_collection`,

*   `queues_collection`,

*   `calc_queue_size`,

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.mongodb.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport "Link to this definition")
MongoDB Transport.

_class_ Channel(_*vargs_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel "Link to this definition")
MongoDB Channel.

_property_ broadcast[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.broadcast "Link to this definition")broadcast_collection _='messages.broadcast'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.broadcast_collection "Link to this definition")calc_queue_size _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.calc_queue_size "Link to this definition")capped_queue_size _=100000_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.capped_queue_size "Link to this definition")_property_ client[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.client "Link to this definition")connect_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.connect_timeout "Link to this definition")default_database _='kombu\_default'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.default_database "Link to this definition")default_hostname _='127.0.0.1'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.default_hostname "Link to this definition")default_port _=27017_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.default_port "Link to this definition")from_transport_options _=('body\_encoding','deadletter\_queue','connect\_timeout','ssl','ttl','capped\_queue\_size','default\_hostname','default\_port','default\_database','messages\_collection','routing\_collection','broadcast\_collection','queues\_collection','calc\_queue\_size')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.from_transport_options "Link to this definition")get_now()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.get_now "Link to this definition")
Return current time in UTC.

get_table(_exchange_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

_property_ messages[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.messages "Link to this definition")messages_collection _='messages'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.messages_collection "Link to this definition")prepare_queue_arguments(_arguments_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.prepare_queue_arguments "Link to this definition")queue_delete(_queue_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.queue_delete "Link to this definition")
Delete queue.

_property_ queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.queues "Link to this definition")queues_collection _='messages.queues'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.queues_collection "Link to this definition")_property_ routing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.routing "Link to this definition")routing_collection _='messages.routing'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.routing_collection "Link to this definition")ssl _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.ssl "Link to this definition")supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

ttl _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.Channel.ttl "Link to this definition")as_uri(_uri:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _include\_password=False_, _mask='**'_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Transport.as_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.as_uri "Link to this definition")
Customise the display format of the URI.

can_parse_url _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.can_parse_url "Link to this definition")
Set to True if [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") should pass the URL unmodified.

channel_errors _=(<class'amqp.exceptions.ChannelError'>,<class'pymongo.errors.ConnectionFailure'>,<class'pymongo.errors.OperationFailure'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

connection_errors _=(<class'amqp.exceptions.ConnectionError'>,<class'pymongo.errors.ConnectionFailure'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

default_port _=27017_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='pymongo'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='mongodb'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.driver_version "Link to this definition")implements _={'asynchronous':False,'exchange\_type':frozenset({'direct','fanout','topic'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.implements "Link to this definition")polling_interval _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.mongodb.Channel(_*vargs_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel "Link to this definition")
MongoDB Channel.

_property_ broadcast[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.broadcast "Link to this definition")broadcast_collection _='messages.broadcast'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.broadcast_collection "Link to this definition")calc_queue_size _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.calc_queue_size "Link to this definition")capped_queue_size _=100000_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.capped_queue_size "Link to this definition")_property_ client[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.client "Link to this definition")connect_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.connect_timeout "Link to this definition")default_database _='kombu\_default'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.default_database "Link to this definition")default_hostname _='127.0.0.1'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.default_hostname "Link to this definition")default_port _=27017_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.default_port "Link to this definition")from_transport_options _=('body\_encoding','deadletter\_queue','connect\_timeout','ssl','ttl','capped\_queue\_size','default\_hostname','default\_port','default\_database','messages\_collection','routing\_collection','broadcast\_collection','queues\_collection','calc\_queue\_size')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.from_transport_options "Link to this definition")get_now()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Channel.get_now)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.get_now "Link to this definition")
Return current time in UTC.

get_table(_exchange_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Channel.get_table)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

_property_ messages[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.messages "Link to this definition")messages_collection _='messages'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.messages_collection "Link to this definition")prepare_queue_arguments(_arguments_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Channel.prepare_queue_arguments)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.prepare_queue_arguments "Link to this definition")queue_delete(_queue_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/mongodb.html#Channel.queue_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.queue_delete "Link to this definition")
Delete queue.

_property_ queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.queues "Link to this definition")queues_collection _='messages.queues'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.queues_collection "Link to this definition")_property_ routing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.routing "Link to this definition")routing_collection _='messages.routing'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.routing_collection "Link to this definition")ssl _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.ssl "Link to this definition")supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

ttl _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.mongodb.html#kombu.transport.mongodb.Channel.ttl "Link to this definition")

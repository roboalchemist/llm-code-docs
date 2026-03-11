# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html

Title: kombu.transport.redis — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.redis.html).

Redis transport module for Kombu.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#features "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: Yes

*   Supports Priority: Yes

*   Supports TTL: No

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#connection-string "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string has the following format:

redis://[USER:PASSWORD@]REDIS_ADDRESS[:PORT][/VIRTUALHOST]
rediss://[USER:PASSWORD@]REDIS_ADDRESS[:PORT][/VIRTUALHOST]

To use sentinel for dynamic Redis discovery, the connection string has following format:

sentinel://[USER:PASSWORD@]SENTINEL_ADDRESS[:PORT]

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#transport-options "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   `sep`

*   `ack_emulation`: (bool) If set to True transport will simulate Acknowledge of AMQP protocol.

*   `unacked_key`

*   `unacked_index_key`

*   `unacked_mutex_key`

*   `unacked_mutex_expire`

*   `visibility_timeout`

*   `unacked_restore_limit`

*   `fanout_prefix`

*   `fanout_patterns`

*   `global_keyprefix`: (str) The global key prefix to be prepended to all keys used by Kombu

*   `socket_timeout`

*   `socket_connect_timeout`

*   `socket_keepalive`

*   `socket_keepalive_options`

*   `queue_order_strategy`

*   `max_connections`

*   `health_check_interval`

*   `retry_on_timeout`

*   `priority_steps`

*   `client_name`: (str) The name to use when connecting to Redis server.

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#channel)

*   [SentinelChannel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#sentinelchannel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#transport "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.redis.Transport(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport "Link to this definition")
Redis Transport.

_class_ Channel(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel "Link to this definition")
Redis Channel.

_class_ QoS(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS "Link to this definition")
Redis Ack Emulation.

ack(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.ack "Link to this definition")
Acknowledge message and remove from transactional state.

append(_message_, _delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.append "Link to this definition")
Append message to transactional state.

pipe_or_acquire(_pipe=None_, _client=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.pipe_or_acquire "Link to this definition")reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.reject "Link to this definition")
Remove from transactional state and requeue message.

restore_at_shutdown _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.restore_at_shutdown "Link to this definition")
If disabled, unacked messages won’t be restored at shutdown.

restore_by_tag(_tag_, _client=None_, _leftmost=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.restore_by_tag "Link to this definition")restore_unacked(_client=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.restore_unacked "Link to this definition")
Restore all unacknowledged messages.

restore_visible(_start=0_, _num=10_, _interval=10_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.restore_visible "Link to this definition")
Restore any pending unacknowledged messages.

To be filled in for visibility_timeout style implementations.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#note "Link to this heading")

> This is implementation optional, and currently only used by the Redis transport.

_property_ unacked_index_key[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.unacked_index_key "Link to this definition")_property_ unacked_key[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.unacked_key "Link to this definition")_property_ unacked_mutex_expire[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.unacked_mutex_expire "Link to this definition")_property_ unacked_mutex_key[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.unacked_mutex_key "Link to this definition")_property_ visibility_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.QoS.visibility_timeout "Link to this definition")ack_emulation _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.ack_emulation "Link to this definition")_property_ active_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.active_queues "Link to this definition")
Set of queues being consumed from (excluding fanout queues).

_property_ async_pool[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.async_pool "Link to this definition")basic_cancel(_consumer\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.basic_consume "Link to this definition")
Consume from queue.

_property_ client[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.client "Link to this definition")
Client used to publish messages, BRPOP etc.

client_name _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.client_name "Link to this definition")close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

conn_or_acquire(_client=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.conn_or_acquire "Link to this definition")connection_class[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.connection_class "Link to this definition")
alias of `Connection`

connection_class_ssl[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.connection_class_ssl "Link to this definition")
alias of `SSLConnection`

fanout_patterns _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.fanout_patterns "Link to this definition")
If enabled the fanout exchange will support patterns in routing and binding keys (like a topic exchange but using PUB/SUB).

Enabled by default since Kombu 4.x. Disable for backwards compatibility with Kombu 3.x.

fanout_prefix _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.fanout_prefix "Link to this definition")
Transport option to disable fanout keyprefix. Can also be string, in which case it changes the default prefix (‘/{db}.’) into to something else. The prefix must include a leading slash and a trailing dot.

Enabled by default since Kombu 4.x. Disable for backwards compatibility with Kombu 3.x.

from_transport_options _=('body\_encoding','deadletter\_queue','sep','ack\_emulation','unacked\_key','unacked\_index\_key','unacked\_mutex\_key','unacked\_mutex\_expire','visibility\_timeout','unacked\_restore\_limit','fanout\_prefix','fanout\_patterns','global\_keyprefix','socket\_timeout','socket\_connect\_timeout','socket\_keepalive','socket\_keepalive\_options','queue\_order\_strategy','max\_connections','health\_check\_interval','retry\_on\_timeout','priority\_steps','client\_name')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.from_transport_options "Link to this definition")get_table(_exchange_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

global_keyprefix _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.global_keyprefix "Link to this definition")
The global key prefix will be prepended to all keys used by Kombu, which can be useful when a redis database is shared by different users. By default, no prefix is prepended.

health_check_interval _=25_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.health_check_interval "Link to this definition")keyprefix_fanout _='/{db}.'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.keyprefix_fanout "Link to this definition")keyprefix_queue _='\_kombu.binding.%s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.keyprefix_queue "Link to this definition")max_connections _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.max_connections "Link to this definition")_property_ pool[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.pool "Link to this definition")priority(_n_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.priority "Link to this definition")priority_steps _=[0,3,6,9]_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.priority_steps "Link to this definition")queue_order_strategy _='round\_robin'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.queue_order_strategy "Link to this definition")
Order in which we consume from queues.

Can be either string alias, or a cycle strategy class

*   `round_robin` ([`round_robin_cycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.round_robin_cycle "kombu.utils.scheduling.round_robin_cycle")).

> Make sure each queue has an equal opportunity to be consumed from.

*   `sorted` ([`sorted_cycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.sorted_cycle "kombu.utils.scheduling.sorted_cycle")).

> Consume from queues in alphabetical order. If the first queue in the sorted list always contains messages, then the rest of the queues will never be consumed from.

*   `priority` ([`priority_cycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.priority_cycle "kombu.utils.scheduling.priority_cycle")).

> Consume from queues in original order, so that if the first queue always contains messages, the rest of the queues in the list will never be consumed from.

The default is to consume from queues in round robin.

retry_on_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.retry_on_timeout "Link to this definition")sep _='\x06\x16'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.sep "Link to this definition")socket_connect_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.socket_connect_timeout "Link to this definition")socket_keepalive _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.socket_keepalive "Link to this definition")socket_keepalive_options _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.socket_keepalive_options "Link to this definition")socket_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.socket_timeout "Link to this definition")_property_ subclient[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.subclient "Link to this definition")
Pub/Sub connection used to consume fanout queues.

supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

unacked_index_key _='unacked\_index'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.unacked_index_key "Link to this definition")unacked_key _='unacked'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.unacked_key "Link to this definition")unacked_mutex_expire _=300_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.unacked_mutex_expire "Link to this definition")unacked_mutex_key _='unacked\_mutex'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.unacked_mutex_key "Link to this definition")unacked_restore_limit _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.unacked_restore_limit "Link to this definition")visibility_timeout _=3600_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.Channel.visibility_timeout "Link to this definition")brpop_timeout _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.brpop_timeout "Link to this definition")channel_errors _=(<class'amqp.exceptions.ChannelError'>,<class'redis.exceptions.DataError'>,<class'redis.exceptions.InvalidResponse'>,<class'redis.exceptions.ResponseError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

connection_errors _=(<class'amqp.exceptions.ConnectionError'>,<class'kombu.exceptions.InconsistencyError'>,<class'OSError'>,<class'OSError'>,<class'OSError'>,<class'redis.exceptions.ConnectionError'>,<class'redis.exceptions.BusyLoadingError'>,<class'redis.exceptions.AuthenticationError'>,<class'redis.exceptions.TimeoutError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

default_port _=6379_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='redis'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='redis'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.driver_version "Link to this definition")implements _={'asynchronous':True,'exchange\_type':frozenset({'direct','fanout','topic'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.implements "Link to this definition")on_readable(_fileno_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Transport.on_readable)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.on_readable "Link to this definition")
Handle AIO event for one of our file descriptors.

polling_interval _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

register_with_event_loop(_connection_, _loop_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Transport.register_with_event_loop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Transport.register_with_event_loop "Link to this definition")
Transport-specific notes

Added in version 5.6.0.

Redis now honours the generic [`polling_interval`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.polling_interval "kombu.transport.virtual.Transport.polling_interval") option (present in SQS, etcd, Zookeeper, …). When you pass

app.conf.broker_transport_options = {"polling_interval": 10}

the worker uses that value as the _timeout_ for the underlying `BRPOP` call, so it issues at most one poll every 10 seconds while the queue is empty. The default remains **1 second** to stay backward-compatible.

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#channel "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.redis.Channel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel "Link to this definition")
Redis Channel.

_class_ QoS(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS "Link to this definition")
Redis Ack Emulation.

ack(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.ack "Link to this definition")
Acknowledge message and remove from transactional state.

append(_message_, _delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.append "Link to this definition")
Append message to transactional state.

pipe_or_acquire(_pipe=None_, _client=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.pipe_or_acquire "Link to this definition")reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.reject "Link to this definition")
Remove from transactional state and requeue message.

restore_at_shutdown _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.restore_at_shutdown "Link to this definition")
If disabled, unacked messages won’t be restored at shutdown.

restore_by_tag(_tag_, _client=None_, _leftmost=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.restore_by_tag "Link to this definition")restore_unacked(_client=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.restore_unacked "Link to this definition")
Restore all unacknowledged messages.

restore_visible(_start=0_, _num=10_, _interval=10_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.restore_visible "Link to this definition")
Restore any pending unacknowledged messages.

To be filled in for visibility_timeout style implementations.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id1 "Link to this heading")

> This is implementation optional, and currently only used by the Redis transport.

_property_ unacked_index_key[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.unacked_index_key "Link to this definition")_property_ unacked_key[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.unacked_key "Link to this definition")_property_ unacked_mutex_expire[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.unacked_mutex_expire "Link to this definition")_property_ unacked_mutex_key[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.unacked_mutex_key "Link to this definition")_property_ visibility_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.QoS.visibility_timeout "Link to this definition")ack_emulation _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.ack_emulation "Link to this definition")_property_ active_queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.active_queues "Link to this definition")
Set of queues being consumed from (excluding fanout queues).

_property_ async_pool[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.async_pool "Link to this definition")basic_cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel.basic_cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_consume(_queue_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.basic_consume "Link to this definition")
Consume from queue.

_property_ client[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.client "Link to this definition")
Client used to publish messages, BRPOP etc.

client_name _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.client_name "Link to this definition")close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

conn_or_acquire(_client=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel.conn_or_acquire)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.conn_or_acquire "Link to this definition")connection_class[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.connection_class "Link to this definition")
alias of `Connection`

connection_class_ssl[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.connection_class_ssl "Link to this definition")
alias of `SSLConnection`

fanout_patterns _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.fanout_patterns "Link to this definition")
If enabled the fanout exchange will support patterns in routing and binding keys (like a topic exchange but using PUB/SUB).

Enabled by default since Kombu 4.x. Disable for backwards compatibility with Kombu 3.x.

fanout_prefix _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.fanout_prefix "Link to this definition")
Transport option to disable fanout keyprefix. Can also be string, in which case it changes the default prefix (‘/{db}.’) into to something else. The prefix must include a leading slash and a trailing dot.

Enabled by default since Kombu 4.x. Disable for backwards compatibility with Kombu 3.x.

from_transport_options _=('body\_encoding','deadletter\_queue','sep','ack\_emulation','unacked\_key','unacked\_index\_key','unacked\_mutex\_key','unacked\_mutex\_expire','visibility\_timeout','unacked\_restore\_limit','fanout\_prefix','fanout\_patterns','global\_keyprefix','socket\_timeout','socket\_connect\_timeout','socket\_keepalive','socket\_keepalive\_options','queue\_order\_strategy','max\_connections','health\_check\_interval','retry\_on\_timeout','priority\_steps','client\_name')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.from_transport_options "Link to this definition")get_table(_exchange_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel.get_table)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

global_keyprefix _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.global_keyprefix "Link to this definition")
The global key prefix will be prepended to all keys used by Kombu, which can be useful when a redis database is shared by different users. By default, no prefix is prepended.

health_check_interval _=25_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.health_check_interval "Link to this definition")keyprefix_fanout _='/{db}.'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.keyprefix_fanout "Link to this definition")keyprefix_queue _='\_kombu.binding.%s'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.keyprefix_queue "Link to this definition")max_connections _=10_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.max_connections "Link to this definition")_property_ pool[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.pool "Link to this definition")priority(_n_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#Channel.priority)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.priority "Link to this definition")priority_steps _=[0,3,6,9]_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.priority_steps "Link to this definition")queue_order_strategy _='round\_robin'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.queue_order_strategy "Link to this definition")
Order in which we consume from queues.

Can be either string alias, or a cycle strategy class

*   `round_robin` ([`round_robin_cycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.round_robin_cycle "kombu.utils.scheduling.round_robin_cycle")).

> Make sure each queue has an equal opportunity to be consumed from.

*   `sorted` ([`sorted_cycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.sorted_cycle "kombu.utils.scheduling.sorted_cycle")).

> Consume from queues in alphabetical order. If the first queue in the sorted list always contains messages, then the rest of the queues will never be consumed from.

*   `priority` ([`priority_cycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.priority_cycle "kombu.utils.scheduling.priority_cycle")).

> Consume from queues in original order, so that if the first queue always contains messages, the rest of the queues in the list will never be consumed from.

The default is to consume from queues in round robin.

retry_on_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.retry_on_timeout "Link to this definition")sep _='\x06\x16'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.sep "Link to this definition")socket_connect_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.socket_connect_timeout "Link to this definition")socket_keepalive _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.socket_keepalive "Link to this definition")socket_keepalive_options _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.socket_keepalive_options "Link to this definition")socket_timeout _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.socket_timeout "Link to this definition")_property_ subclient[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.subclient "Link to this definition")
Pub/Sub connection used to consume fanout queues.

supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

unacked_index_key _='unacked\_index'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.unacked_index_key "Link to this definition")unacked_key _='unacked'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.unacked_key "Link to this definition")unacked_mutex_expire _=300_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.unacked_mutex_expire "Link to this definition")unacked_mutex_key _='unacked\_mutex'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.unacked_mutex_key "Link to this definition")unacked_restore_limit _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.unacked_restore_limit "Link to this definition")visibility_timeout _=3600_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.Channel.visibility_timeout "Link to this definition")
[SentinelChannel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#sentinelchannel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.redis.SentinelChannel(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/redis.html#SentinelChannel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.SentinelChannel "Link to this definition")
Channel with explicit Redis Sentinel knowledge.

Broker url is supposed to look like:

sentinel://0.0.0.0:26379;sentinel://0.0.0.0:26380/...

where each sentinel is separated by a ;.

Other arguments for the sentinel should come from the transport options (see transport_options of [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection "kombu.connection.Connection")).

You must provide at least one option in Transport options:
*   master_name - name of the redis group to poll

### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#example "Link to this heading")

>>> import kombu
>>> c = kombu.Connection(
 'sentinel://sentinel1:26379;sentinel://sentinel2:26379',
 transport_options={'master_name': 'mymaster'}
)
>>> c.connect()

connection_class[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.SentinelChannel.connection_class "Link to this definition")
alias of `SentinelManagedConnection`

connection_class_ssl[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.SentinelChannel.connection_class_ssl "Link to this definition")
alias of `SentinelManagedSSLConnection`

from_transport_options _=('body\_encoding','deadletter\_queue','sep','ack\_emulation','unacked\_key','unacked\_index\_key','unacked\_mutex\_key','unacked\_mutex\_expire','visibility\_timeout','unacked\_restore\_limit','fanout\_prefix','fanout\_patterns','global\_keyprefix','socket\_timeout','socket\_connect\_timeout','socket\_keepalive','socket\_keepalive\_options','queue\_order\_strategy','max\_connections','health\_check\_interval','retry\_on\_timeout','priority\_steps','client\_name','master\_name','min\_other\_sentinels','sentinel\_kwargs')_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.redis.html#kombu.transport.redis.SentinelChannel.from_transport_options "Link to this definition")

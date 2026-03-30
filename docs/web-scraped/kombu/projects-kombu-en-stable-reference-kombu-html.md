# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html

Title: kombu — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.html).

*   [Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#connection)

*   [Exchange](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#exchange)

*   [Queue](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#queue)

*   [Message Producer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#message-producer)

*   [Message Consumer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#message-consumer)

Messaging library for Python.

kombu.enable_insecure_serializers(_choices=<object object>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/serialization.html#enable_insecure_serializers)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.enable_insecure_serializers "Link to this definition")
Enable serializers that are considered to be unsafe.

Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#note "Link to this heading")
------------------------------------------------------------------------------------------------------------

> Will enable `pickle`, `yaml` and `msgpack` by default, but you can also specify a list of serializers (by name or content type) to enable.

kombu.disable_insecure_serializers(_allowed=<object object>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/serialization.html#disable_insecure_serializers)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.disable_insecure_serializers "Link to this definition")
Disable untrusted serializers.

Will disable all serializers except `json` or you can specify a list of deserializers to allow.

Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id1 "Link to this heading")
-----------------------------------------------------------------------------------------------------------

> Producers will still be able to serialize data in these formats, but consumers will not accept incoming data using the untrusted content types.

[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id48)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#connection "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.Connection(_hostname='localhost'_, _userid=None_, _password=None_, _virtual\_host=None_, _port=None_, _insist=False_, _ssl=False_, _transport=None_, _connect\_timeout=5_, _transport\_options=None_, _login\_method=None_, _uri\_prefix=None_, _heartbeat=0_, _failover\_strategy='round-robin'_, _alternates=None_, _credential\_provider=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "Link to this definition")
A connection to the broker.

### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#example "Link to this heading")

>>> Connection('amqp://guest:guest@localhost:5672//')
>>> Connection('amqp://foo;amqp://bar',
...            failover_strategy='round-robin')
>>> Connection('redis://', transport_options={
...     'visibility_timeout': 3000,
... })

>>> import ssl
>>> Connection('amqp://', login_method='EXTERNAL', ssl={
...    'ca_certs': '/etc/pki/tls/certs/something.crt',
...    'keyfile': '/etc/something/system.key',
...    'certfile': '/etc/something/system.cert',
...    'cert_reqs': ssl.CERT_REQUIRED,
... })

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id2 "Link to this heading")

> SSL currently only works with the py-amqp, qpid and redis transports. For other transports you can use stunnel.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#arguments "Link to this heading")

> URL (str, Sequence): Broker URL, or a list of URLs.

### Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#keyword-arguments "Link to this heading")

> ssl (bool/dict): Use SSL to connect to the server.
> Default is `False`. May not be supported by the specified transport.
> 
> 
> transport (Transport): Default transport if not specified in the URL. connect_timeout (float): Timeout in seconds for connecting to the
> 
> 
> > server. May not be supported by the specified transport.
> 
> transport_options (Dict): A dict of additional connection arguments to
> pass to alternate kombu channel implementations. Consult the transport documentation for available options.
> 
> heartbeat (float): Heartbeat interval in int/float seconds.
> Note that if heartbeats are enabled then the [`heartbeat_check()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.heartbeat_check "kombu.Connection.heartbeat_check") method must be called regularly, around once per second.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id3 "Link to this heading")

> The connection is established lazily when needed. If you need the connection to be established, then force it by calling [`connect()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.connect "kombu.Connection.connect"):
> 
> 
> 
> >>> conn = Connection('amqp://')
> >>> conn.connect()
> 
> 
> and always remember to close the connection:
> 
> 
> 
> >>> conn.release()

These options have been replaced by the URL argument, but are still supported for backwards compatibility:

keyword hostname:
Host name/address. NOTE: You cannot specify both the URL argument and use the hostname keyword argument at the same time.

keyword userid:
Default user name if not provided in the URL.

keyword password:
Default password if not provided in the URL.

keyword virtual_host:
Default virtual host if not provided in the URL.

keyword port:
Default port if not provided in the URL.

Attributes

hostname _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.hostname "Link to this definition")port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.port "Link to this definition")userid _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.userid "Link to this definition")password _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.password "Link to this definition")virtual_host _='/'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.virtual_host "Link to this definition")ssl _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.ssl "Link to this definition")login_method _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.login_method "Link to this definition")failover_strategy _='round-robin'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.failover_strategy "Link to this definition")
Strategy used to select new hosts when reconnecting after connection failure. One of “round-robin”, “shuffle” or any custom iterator constantly yielding new URLs to try.

connect_timeout _=5_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.connect_timeout "Link to this definition")heartbeat _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.heartbeat "Link to this definition")
Heartbeat value, currently only supported by the py-amqp transport.

default_channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.default_channel "Link to this definition")
Default channel.

Created upon access and closed when the connection is closed.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id4 "Link to this heading")

> Can be used for automatic channel handling when you only need one channel, and also it is the channel implicitly used if a connection is passed instead of a channel, to functions that require a channel.

connected[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.connected "Link to this definition")
Return true if the connection has been established.

recoverable_connection_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.recoverable_connection_errors "Link to this definition")
Recoverable connection errors.

List of connection related exceptions that can be recovered from, but where the connection must be closed and re-established first.

recoverable_channel_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.recoverable_channel_errors "Link to this definition")
Recoverable channel errors.

List of channel related exceptions that can be automatically recovered from without re-establishing the connection.

connection_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.connection_errors "Link to this definition")
List of exceptions that may be raised by the connection.

channel_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.channel_errors "Link to this definition")
List of exceptions that may be raised by the channel.

transport[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.transport "Link to this definition")connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.connection "Link to this definition")
The underlying connection object.

#### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#warning "Link to this heading")

> This instance is transport specific, so do not depend on the interface of this object.

uri_prefix _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.uri_prefix "Link to this definition")declared_entities _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.declared_entities "Link to this definition")
The cache of declared entities is per connection, in case the server loses data.

cycle _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.cycle "Link to this definition")
Iterator returning the next broker URL to try in the event of connection failure (initialized by [`failover_strategy`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.failover_strategy "kombu.Connection.failover_strategy")).

host[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.host "Link to this definition")
The host as a host name/port pair separated by colon.

manager[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.manager "Link to this definition")
AMQP Management API.

Experimental manager that can be used to manage/monitor the broker instance.

Not available for all transports.

supports_heartbeats[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.supports_heartbeats "Link to this definition")is_evented[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.is_evented "Link to this definition")

Methods

as_uri(_include\_password=False_, _mask='**'_, _getfields=operator.itemgetter('port','userid','password','virtual\_host','transport')_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.as_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.as_uri "Link to this definition")
Convert connection parameters to URL form.

connect()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.connect)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.connect "Link to this definition")
Establish connection to server immediately.

channel()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.channel "Link to this definition")
Create and return a new channel.

drain_events(_**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.drain_events "Link to this definition")
Wait for a single event from the server.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id5 "Link to this heading")

> timeout (float): Timeout in seconds before we give up.

raises socket.timeout:
if the timeout is exceeded.:

release()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.release)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.release "Link to this definition")
Close the connection (if open).

autoretry(_fun_, _channel=None_, _**ensure\_options_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.autoretry)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.autoretry "Link to this definition")
Decorator for functions supporting a `channel` keyword argument.

The resulting callable will retry calling the function if it raises connection or channel related errors. The return value will be a tuple of `(retval, last_created_channel)`.

If a `channel` is not provided, then one will be automatically acquired (remember to close it afterwards).

#### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id6 "Link to this heading")

>>> channel = connection.channel()
>>> try:
...    ret, channel = connection.autoretry(
...         publish_messages, channel)
... finally:
...    channel.close()

ensure_connection(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.ensure_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.ensure_connection "Link to this definition")
Public interface of _ensure_connection for retro-compatibility.

Returns kombu.Connection instance.

ensure(_obj_, _fun_, _errback=None_, _max\_retries=None_, _interval\_start=1_, _interval\_step=1_, _interval\_max=1_, _on\_revive=None_, _retry\_errors=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.ensure)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.ensure "Link to this definition")
Ensure operation completes.

Regardless of any channel/connection errors occurring.

Retries by establishing the connection, and reapplying the function.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id7 "Link to this heading")

> obj: The object to ensure an action on. fun (Callable): Method to apply.
> 
> errback (Callable): Optional callback called each time the
> connection can’t be established. Arguments provided are the exception raised and the interval that will be slept `(exc, interval)`.
> 
> max_retries (int): Maximum number of times to retry.
> If this limit is exceeded the connection error will be re-raised.
> 
> interval_start (float): The number of seconds we start
> sleeping for.
> 
> interval_step (float): How many seconds added to the interval
> for each retry.
> 
> interval_max (float): Maximum number of seconds to sleep between
> each retry.
> 
> on_revive (Callable): Optional callback called whenever
> revival completes successfully
> 
> retry_errors (tuple): Optional list of errors to retry on
> regardless of the connection state.

Examples

>>> from kombu import Connection, Producer
>>> conn = Connection('amqp://')
>>> producer = Producer(conn)

>>> def errback(exc, interval):
...     logger.error('Error: %r', exc, exc_info=1)
...     logger.info('Retry in %s seconds.', interval)

>>> publish = conn.ensure(producer, producer.publish,
...                       errback=errback, max_retries=3)
>>> publish({'hello': 'world'}, routing_key='dest')

revive(_new\_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.revive "Link to this definition")
Revive connection after connection re-established.

create_transport()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.create_transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.create_transport "Link to this definition")get_transport_cls()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.get_transport_cls)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.get_transport_cls "Link to this definition")
Get the currently used transport class.

clone(_**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.clone)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.clone "Link to this definition")
Create a copy of the connection with same settings.

info()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.info)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.info "Link to this definition")
Get connection info.

switch(_conn\_str_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.switch)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.switch "Link to this definition")
Switch connection parameters to use a new URL or hostname.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id8 "Link to this heading")

> Does not reconnect!

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id9 "Link to this heading")

> conn_str (str): either a hostname or URL.

maybe_switch_next()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.maybe_switch_next)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.maybe_switch_next "Link to this definition")
Switch to next URL given by the current failover strategy.

heartbeat_check(_rate=2_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.heartbeat_check)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.heartbeat_check "Link to this definition")
Check heartbeats.

Allow the transport to perform any periodic tasks required to make heartbeats work. This should be called approximately every second.

If the current transport does not support heartbeats then this is a noop operation.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id10 "Link to this heading")

> rate (int): Rate is how often the tick is called
> compared to the actual heartbeat value. E.g. if the heartbeat is set to 3 seconds, and the tick is called every 3 / 2 seconds, then the rate is 2. This value is currently unused by any transports.

maybe_close_channel(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.maybe_close_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.maybe_close_channel "Link to this definition")
Close given channel, but ignore connection and channel errors.

register_with_event_loop(_loop_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.register_with_event_loop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.register_with_event_loop "Link to this definition")close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.close "Link to this definition")
Close the connection (if open).

_close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection._close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection._close "Link to this definition")
Really close connection, even if part of a connection pool.

completes_cycle(_retries_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.completes_cycle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.completes_cycle "Link to this definition")
Return true if the cycle is complete after number of retries.

get_manager(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.get_manager)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.get_manager "Link to this definition")Producer(_channel=None_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.Producer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.Producer "Link to this definition")
Create new [`kombu.Producer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "kombu.Producer") instance.

Consumer(_queues=None_, _channel=None_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.Consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.Consumer "Link to this definition")
Create new [`kombu.Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer") instance.

Pool(_limit=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.Pool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.Pool "Link to this definition")
Pool of connections.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id11 "Link to this heading")

> limit (int): Maximum number of active connections.
> Default is no limit.

#### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id12 "Link to this heading")

>>> connection = Connection('amqp://')
>>> pool = connection.Pool(2)
>>> c1 = pool.acquire()
>>> c2 = pool.acquire()
>>> c3 = pool.acquire()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "kombu/connection.py", line 354, in acquire
 raise ConnectionLimitExceeded(self.limit)
 kombu.exceptions.ConnectionLimitExceeded: 2
>>> c1.release()
>>> c3 = pool.acquire()

ChannelPool(_limit=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.ChannelPool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.ChannelPool "Link to this definition")
Pool of channels.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id13 "Link to this heading")

> limit (int): Maximum number of active channels.
> Default is no limit.

#### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id14 "Link to this heading")

>>> connection = Connection('amqp://')
>>> pool = connection.ChannelPool(2)
>>> c1 = pool.acquire()
>>> c2 = pool.acquire()
>>> c3 = pool.acquire()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "kombu/connection.py", line 354, in acquire
 raise ChannelLimitExceeded(self.limit)
 kombu.connection.ChannelLimitExceeded: 2
>>> c1.release()
>>> c3 = pool.acquire()

SimpleQueue(_name_, _no\_ack=None_, _queue\_opts=None_, _queue\_args=None_, _exchange\_opts=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.SimpleQueue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.SimpleQueue "Link to this definition")
Simple persistent queue API.

Create new [`SimpleQueue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue "kombu.simple.SimpleQueue"), using a channel from this connection.

If `name` is a string, a queue and exchange will be automatically created using that name as the name of the queue and exchange, also it will be used as the default routing key.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id15 "Link to this heading")

> name (str, kombu.Queue): Name of the queue/or a queue. no_ack (bool): Disable acknowledgments. Default is false. queue_opts (Dict): Additional keyword arguments passed to the
> 
> 
> > constructor of the automatically created [`Queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "kombu.Queue").
> 
> queue_args (Dict): Additional keyword arguments passed to the
> constructor of the automatically created [`Queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "kombu.Queue") for setting implementation extensions (e.g., in RabbitMQ).
> 
> exchange_opts (Dict): Additional keyword arguments passed to the
> constructor of the automatically created [`Exchange`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange "kombu.Exchange").
> 
> channel (ChannelT): Custom channel to use. If not specified the
> connection default channel is used.

SimpleBuffer(_name_, _no\_ack=None_, _queue\_opts=None_, _queue\_args=None_, _exchange\_opts=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.SimpleBuffer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.SimpleBuffer "Link to this definition")
Simple ephemeral queue API.

Create new [`SimpleQueue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue "kombu.simple.SimpleQueue") using a channel from this connection.

[Exchange](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id49)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#exchange "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Example creating an exchange declaration:

>>> news_exchange = Exchange('news', type='topic')

For now news_exchange is just a declaration, you can’t perform actions on it. It just describes the name and options for the exchange.

The exchange can be bound or unbound. Bound means the exchange is associated with a channel and operations can be performed on it. To bind the exchange you call the exchange with the channel as argument:

>>> bound_exchange = news_exchange(channel)

Now you can perform operations like `declare()` or `delete()`:

>>> # Declare exchange manually
>>> bound_exchange.declare()

>>> # Publish raw string message using low-level exchange API
>>> bound_exchange.publish(
...     'Cure for cancer found!',
...     routing_key='news.science',
... )

>>> # Delete exchange.
>>> bound_exchange.delete()

_class_ kombu.Exchange(_name=''_, _type=''_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange "Link to this definition")
An Exchange declaration.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id16 "Link to this heading")

> name (str): See [`name`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id0 "kombu.Exchange.name"). type (str): See [`type`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id21 "kombu.Exchange.type"). channel (kombu.Connection, ChannelT): See `channel`. durable (bool): See [`durable`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.durable "kombu.Exchange.durable"). auto_delete (bool): See [`auto_delete`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.auto_delete "kombu.Exchange.auto_delete"). delivery_mode (enum): See [`delivery_mode`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.delivery_mode "kombu.Exchange.delivery_mode"). arguments (Dict): See `arguments`. no_declare (bool): See [`no_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.no_declare "kombu.Exchange.no_declare")

name(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.name "Link to this definition")
Default is no name (the default exchange).

Type:
Name of the exchange.

type(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.type "Link to this definition")
_This description of AMQP exchange types was shamelessly stolen from the blog post `AMQP in 10 minutes: Part 4`\_ by Rajith Attapattu. Reading this article is recommended if you’re new to amqp._

“AMQP defines four default exchange types (routing algorithms) that covers most of the common messaging use cases. An AMQP broker can also define additional exchange types, so see your broker manual for more information about available exchange types.

> > *   direct (_default_)
> > 
> > 
> > > Direct match between the routing key in the message, and the routing criteria used when a queue is bound to this exchange.
> > 
> > *   topic
> > 
> > 
> > > Wildcard match between the routing key and the routing pattern specified in the exchange/queue binding. The routing key is treated as zero or more words delimited by “.” and supports special wildcard characters. “*” matches a single word and “#” matches zero or more words.
> > 
> > *   fanout
> > 
> > 
> > > Queues are bound to this exchange with no arguments. Hence any message sent to this exchange will be forwarded to all queues bound to this exchange.
> > 
> > *   headers
> > 
> > 
> > > Queues are bound to this exchange with a table of arguments containing headers and values (optional). A special argument named “x-match” determines the matching algorithm, where “all” implies an AND (all pairs must match) and “any” implies OR (at least one pair must match).
> > > 
> > > 
> > > `arguments` is used to specify the arguments.
> 
> 
> channel (ChannelT): The channel the exchange is bound to (if bound).
> 
> durable (bool): Durable exchanges remain active when a server restarts.
> Non-durable exchanges (transient exchanges) are purged when a server restarts. Default is `True`.
> 
> auto_delete (bool): If set, the exchange is deleted when all queues
> have finished using it. Default is `False`.
> 
> delivery_mode (enum): The default delivery mode used for messages.
> The value is an integer, or alias string.
> 
> 
> > *   1 or “transient”
> > 
> > 
> > > The message is transient. Which means it is stored in memory only, and is lost if the server dies or restarts.
> > 
> > *   2 or “persistent” (_default_)
> > The message is persistent. Which means the message is stored both in-memory, and on disk, and therefore preserved if the server dies or restarts.
> 
> 
> The default value is 2 (persistent).
> 
> arguments (Dict): Additional arguments to specify when the exchange
> is declared.
> 
> no_declare (bool): Never declare this exchange
> ([`declare()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.declare "kombu.Exchange.declare") does nothing).

maybe_bind(_channel:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")|[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection")_)→_MaybeChannelBoundType[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.maybe_bind "Link to this definition")
Bind instance to channel if not already bound.

Message(_body_, _delivery\_mode=None_, _properties=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.Message "Link to this definition")
Create message instance to be sent with [`publish()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.publish "kombu.Exchange.publish").

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id17 "Link to this heading")

> body (Any): Message body.
> 
> delivery_mode (bool): Set custom delivery mode.
> Defaults to [`delivery_mode`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.delivery_mode "kombu.Exchange.delivery_mode").
> 
> priority (int): Message priority, 0 to broker configured
> max priority, where higher is better.
> 
> content_type (str): The messages content_type. If content_type
> is set, no serialization occurs as it is assumed this is either a binary object, or you’ve done your own serialization. Leave blank if using built-in serialization as our library properly sets content_type.
> 
> content_encoding (str): The character set in which this object
> is encoded. Use “binary” if sending in raw binary objects. Leave blank if using built-in serialization as our library properly sets content_encoding.
> 
> 
> properties (Dict): Message properties.
> 
> 
> headers (Dict): Message headers.

PERSISTENT_DELIVERY_MODE _=2_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.PERSISTENT_DELIVERY_MODE "Link to this definition")TRANSIENT_DELIVERY_MODE _=1_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.TRANSIENT_DELIVERY_MODE "Link to this definition")attrs _:[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),Any],...]_ _=(('name',None),('type',None),('arguments',None),('durable',<class'bool'>),('passive',<class'bool'>),('auto\_delete',<class'bool'>),('delivery\_mode',<function Exchange.<lambda>>),('no\_declare',<class'bool'>))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.attrs "Link to this definition")auto_delete _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.auto_delete "Link to this definition")bind_to(_exchange=''_, _routing\_key=''_, _arguments=None_, _nowait=False_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.bind_to)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.bind_to "Link to this definition")
Bind the exchange to another exchange.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id18 "Link to this heading")

> nowait (bool): If set the server will not respond, and the call
> will not block waiting for a response. Default is `False`.

binding(_routing\_key=''_, _arguments=None_, _unbind\_arguments=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.binding)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.binding "Link to this definition")_property_ can_cache_declaration[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.can_cache_declaration "Link to this definition")
bool(x) -> bool

Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

declare(_nowait=False_, _passive=None_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.declare "Link to this definition")
Declare the exchange.

Creates the exchange on the broker, unless passive is set in which case it will only assert that the exchange exists.

Argument:nowait (bool): If set the server will not respond, and a
response will not be waited for. Default is `False`.

delete(_if\_unused=False_, _nowait=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.delete "Link to this definition")
Delete the exchange declaration on server.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id19 "Link to this heading")

> if_unused (bool): Delete only if the exchange has no bindings.
> Default is `False`.
> 
> nowait (bool): If set the server will not respond, and a
> response will not be waited for. Default is `False`.

delivery_mode _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.delivery_mode "Link to this definition")durable _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.durable "Link to this definition")name _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id0 "Link to this definition")no_declare _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.no_declare "Link to this definition")passive _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.passive "Link to this definition")publish(_message_, _routing\_key=None_, _mandatory=False_, _immediate=False_, _exchange=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.publish)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.publish "Link to this definition")
Publish message.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id20 "Link to this heading")

> message (Union[kombu.Message, str, bytes]):
> Message to publish.
> 
> 
> routing_key (str): Message routing key. mandatory (bool): Currently not supported. immediate (bool): Currently not supported.

type _='direct'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id21 "Link to this definition")unbind_from(_source=''_, _routing\_key=''_, _nowait=False_, _arguments=None_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Exchange.unbind_from)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange.unbind_from "Link to this definition")
Delete previously created exchange binding from the server.

[Queue](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id50)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#queue "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Example creating a queue using our exchange in the [`Exchange`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange "kombu.Exchange") example:

>>> science_news = Queue('science_news',
...                      exchange=news_exchange,
...                      routing_key='news.science')

For now science_news is just a declaration, you can’t perform actions on it. It just describes the name and options for the queue.

The queue can be bound or unbound. Bound means the queue is associated with a channel and operations can be performed on it. To bind the queue you call the queue instance with the channel as an argument:

>>> bound_science_news = science_news(channel)

Now you can perform operations like `declare()` or `purge()`:

>>> bound_science_news.declare()
>>> bound_science_news.purge()
>>> bound_science_news.delete()

_class_ kombu.Queue(_name=''_, _exchange=None_, _routing\_key=''_, _channel=None_, _bindings=None_, _on\_declared=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "Link to this definition")
A Queue declaration.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id22 "Link to this heading")

> name (str): See [`name`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id30 "kombu.Queue.name"). exchange (Exchange, str): See [`exchange`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id27 "kombu.Queue.exchange"). routing_key (str): See [`routing_key`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id32 "kombu.Queue.routing_key"). channel (kombu.Connection, ChannelT): See [`channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.channel "kombu.Queue.channel"). durable (bool): See [`durable`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id26 "kombu.Queue.durable"). exclusive (bool): See [`exclusive`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id28 "kombu.Queue.exclusive"). auto_delete (bool): See [`auto_delete`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id23 "kombu.Queue.auto_delete"). queue_arguments (Dict): See [`queue_arguments`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.queue_arguments "kombu.Queue.queue_arguments"). binding_arguments (Dict): See [`binding_arguments`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.binding_arguments "kombu.Queue.binding_arguments"). consumer_arguments (Dict): See [`consumer_arguments`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.consumer_arguments "kombu.Queue.consumer_arguments"). no_declare (bool): See [`no_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.no_declare "kombu.Queue.no_declare"). on_declared (Callable): See [`on_declared`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.on_declared "kombu.Queue.on_declared"). expires (float): See [`expires`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.expires "kombu.Queue.expires"). message_ttl (float): See [`message_ttl`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.message_ttl "kombu.Queue.message_ttl"). max_length (int): See [`max_length`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.max_length "kombu.Queue.max_length"). max_length_bytes (int): See [`max_length_bytes`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.max_length_bytes "kombu.Queue.max_length_bytes"). max_priority (int): See [`max_priority`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.max_priority "kombu.Queue.max_priority").

name(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.name "Link to this definition")
Default is no name (default queue destination).

Type:
Name of the queue.

exchange(_Exchange_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.exchange "Link to this definition")Type:
The [`Exchange`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Exchange "kombu.Exchange") the queue binds to.

routing_key(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.routing_key "Link to this definition")
The interpretation of the routing key depends on the [`Exchange.type`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id21 "kombu.Exchange.type").

*   direct exchange

> Matches if the routing key property of the message and the [`routing_key`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id32 "kombu.Queue.routing_key") attribute are identical.

*   fanout exchange

> Always matches, even if the binding does not have a key.

*   topic exchange

> Matches the routing key property of the message by a primitive pattern matching scheme. The message routing key then consists of words separated by dots (“.”, like domain names), and two special characters are available; star (“*”) and hash (“#”). The star matches any word, and the hash matches zero or more words. For example “*.stock.#” matches the routing keys “usd.stock” and “eur.stock.db” but not “stock.nasdaq”.

Type:
The routing key (if any), also called _binding key_.

channel(_ChannelT_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.channel "Link to this definition")Type:
The channel the Queue is bound to (if bound).

durable(_bool_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.durable "Link to this definition")
Non-durable queues (transient queues) are purged if/when a server restarts. Note that durable queues do not necessarily hold persistent messages, although it does not make sense to send persistent messages to a transient queue.

Default is `True`.

Type:
Durable queues remain active when a server restarts.

exclusive(_bool_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.exclusive "Link to this definition")
current connection. Setting the ‘exclusive’ flag always implies ‘auto-delete’.

Default is `False`.

Type:
Exclusive queues may only be consumed from by the

auto_delete(_bool_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.auto_delete "Link to this definition")
have finished using it. Last consumer can be canceled either explicitly or because its channel is closed. If there was no consumer ever on the queue, it won’t be deleted.

Type:
If set, the queue is deleted when all consumers

expires(_float_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.expires "Link to this definition")
queue should expire.

The expiry time decides how long the queue can stay unused before it’s automatically deleted. _Unused_ means the queue has no consumers, the queue has not been redeclared, and `Queue.get` has not been invoked for a duration of at least the expiration period.

See [https://www.rabbitmq.com/ttl.html#queue-ttl](https://www.rabbitmq.com/ttl.html#queue-ttl)

**RabbitMQ extension**: Only available when using RabbitMQ.

Type:
Set the expiry time (in seconds) for when this

message_ttl(_float_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.message_ttl "Link to this definition")
This setting controls how long messages can stay in the queue unconsumed. If the expiry time passes before a message consumer has received the message, the message is deleted and no consumer will see the message.

See [https://www.rabbitmq.com/ttl.html#per-queue-message-ttl](https://www.rabbitmq.com/ttl.html#per-queue-message-ttl)

**RabbitMQ extension**: Only available when using RabbitMQ.

Type:
Message time to live in seconds.

max_length(_int_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.max_length "Link to this definition")
queue can hold.

If the number of messages in the queue size exceeds this limit, new messages will be dropped (or dead-lettered if a dead letter exchange is active).

See [https://www.rabbitmq.com/maxlength.html](https://www.rabbitmq.com/maxlength.html)

**RabbitMQ extension**: Only available when using RabbitMQ.

Type:
Set the maximum number of messages that the

max_length_bytes(_int_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.max_length_bytes "Link to this definition")
of messages in the queue.

If the total size of all the messages in the queue exceeds this limit, new messages will be dropped (or dead-lettered if a dead letter exchange is active).

**RabbitMQ extension**: Only available when using RabbitMQ.

Type:
Set the max size (in bytes) for the total

max_priority(_int_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.max_priority "Link to this definition")
For example if the value is 10, then messages can delivered to this queue can have a `priority` value between 0 and 10, where 10 is the highest priority.

RabbitMQ queues without a max priority set will ignore the priority field in the message, so if you want priorities you need to set the max priority field to declare the queue as a priority queue.

**RabbitMQ extension**: Only available when using RabbitMQ.

Type:
Set the highest priority number for this queue.

queue_arguments(_Dict_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.queue_arguments "Link to this definition")
the queue. Can be used to to set the arguments value for RabbitMQ/AMQP’s `queue.declare`.

Type:
Additional arguments used when declaring

binding_arguments(_Dict_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.binding_arguments "Link to this definition")
the queue. Can be used to to set the arguments value for RabbitMQ/AMQP’s `queue.declare`.

Type:
Additional arguments used when binding

consumer_arguments(_Dict_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.consumer_arguments "Link to this definition")
from this queue. Can be used to to set the arguments value for RabbitMQ/AMQP’s `basic.consume`.

Type:
Additional arguments used when consuming

alias(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.alias "Link to this definition")
of this, for example to give alternate names to queues with automatically generated queue names.

Type:
Unused in Kombu, but applications can take advantage

on_declared(_Callable_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.on_declared "Link to this definition")
queue has been declared (the `queue_declare` operation is complete). This must be a function with a signature that accepts at least 3 positional arguments: `(name, messages, consumers)`.

Type:
Optional callback to be applied when the

no_declare(_bool_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.no_declare "Link to this definition")
entities ([`declare()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.declare "kombu.Queue.declare") does nothing).

Type:
Never declare this queue, nor related

maybe_bind(_channel:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")|[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection")_)→_MaybeChannelBoundType[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.maybe_bind "Link to this definition")
Bind instance to channel if not already bound.

_exception_ ContentDisallowed[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.ContentDisallowed "Link to this definition")
Consumer does not allow this content-type.

as_dict(_recurse=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.as_dict)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.as_dict "Link to this definition")attrs _:[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")[[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)"),Any],...]_ _=(('name',None),('exchange',None),('routing\_key',None),('queue\_arguments',None),('binding\_arguments',None),('consumer\_arguments',None),('durable',<class'bool'>),('exclusive',<class'bool'>),('auto\_delete',<class'bool'>),('no\_ack',None),('alias',None),('bindings',<class'list'>),('no\_declare',<class'bool'>),('expires',<class'float'>),('message\_ttl',<class'float'>),('max\_length',<class'int'>),('max\_length\_bytes',<class'int'>),('max\_priority',<class'int'>))_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.attrs "Link to this definition")auto_delete _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id23 "Link to this definition")bind(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.bind "Link to this definition")
Create copy of the instance that is bound to a channel.

bind_to(_exchange=''_, _routing\_key=''_, _arguments=None_, _nowait=False_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.bind_to)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.bind_to "Link to this definition")_property_ can_cache_declaration[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.can_cache_declaration "Link to this definition")
bool(x) -> bool

Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.cancel "Link to this definition")
Cancel a consumer by consumer tag.

consume(_consumer\_tag=''_, _callback=None_, _no\_ack=None_, _nowait=False_, _on\_cancel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.consume "Link to this definition")
Start a queue consumer.

Consumers last as long as the channel they were created on, or until the client cancels them.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id24 "Link to this heading")

> consumer_tag (str): Unique identifier for the consumer.
> The consumer tag is local to a connection, so two clients can use the same consumer tags. If this field is empty the server will generate a unique tag.
> 
> no_ack (bool): If enabled the broker will automatically
> ack messages.
> 
> 
> nowait (bool): Do not wait for a reply.
> 
> 
> callback (Callable): callback called for each delivered message.
> 
> on_cancel (Callable): callback called on cancel notify received
> from broker.

declare(_nowait=False_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.declare "Link to this definition")
Declare queue and exchange then binds queue to exchange.

delete(_if\_unused=False_, _if\_empty=False_, _nowait=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.delete "Link to this definition")
Delete the queue.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id25 "Link to this heading")

> if_unused (bool): If set, the server will only delete the queue
> if it has no consumers. A channel error will be raised if the queue has consumers.
> 
> if_empty (bool): If set, the server will only delete the queue if
> it is empty. If it is not empty a channel error will be raised.
> 
> 
> nowait (bool): Do not wait for a reply.

durable _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id26 "Link to this definition")exchange _=<unbound Exchange''(direct)>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id27 "Link to this definition")exclusive _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id28 "Link to this definition")_classmethod_ from_dict(_queue_, _**options_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.from_dict)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.from_dict "Link to this definition")get(_no\_ack=None_, _accept=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.get)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.get "Link to this definition")
Poll the server for a new message.

This method provides direct access to the messages in a queue using a synchronous dialogue, designed for specific types of applications where synchronous functionality is more important than performance.

Returns:
**~kombu.Message** – or `None` otherwise.

Return type:
if a message was available,

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id29 "Link to this heading")

> no_ack (bool): If enabled the broker will
> automatically ack messages.
> 
> 
> accept (Set[str]): Custom list of accepted content types.

name _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id30 "Link to this definition")no_ack _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.no_ack "Link to this definition")purge(_nowait=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.purge)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.purge "Link to this definition")
Remove all ready messages from the queue.

queue_bind(_nowait=False_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.queue_bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.queue_bind "Link to this definition")
Create the queue binding on the server.

queue_declare(_nowait=False_, _passive=False_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.queue_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.queue_declare "Link to this definition")
Declare queue on the server.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id31 "Link to this heading")

> nowait (bool): Do not wait for a reply. passive (bool): If set, the server will not create the queue.
> 
> 
> > The client can use this to check whether a queue exists without modifying the server state.

queue_unbind(_arguments=None_, _nowait=False_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.queue_unbind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.queue_unbind "Link to this definition")routing_key _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id32 "Link to this definition")unbind_from(_exchange=''_, _routing\_key=''_, _arguments=None_, _nowait=False_, _channel=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.unbind_from)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.unbind_from "Link to this definition")
Unbind queue by deleting the binding from the server.

when_bound()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/entity.html#Queue.when_bound)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue.when_bound "Link to this definition")
Callback called when the class is bound.

[Message Producer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id51)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#message-producer "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.Producer(_channel_, _exchange=None_, _routing\_key=None_, _serializer=None_, _auto\_declare=None_, _compression=None_, _on\_return=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Producer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "Link to this definition")
Message Producer.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id33 "Link to this heading")

> channel (kombu.Connection, ChannelT): Connection or channel. exchange (kombu.entity.Exchange, str): Optional default exchange. routing_key (str): Optional default routing key. serializer (str): Default serializer. Default is “json”. compression (str): Default compression method.
> 
> 
> > Default is no compression.
> 
> auto_declare (bool): Automatically declare the default exchange
> at instantiation. Default is `True`.
> 
> on_return (Callable): Callback to call for undeliverable messages,
> when the mandatory or immediate arguments to [`publish()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.publish "kombu.Producer.publish") is used. This callback needs the following signature: (exception, exchange, routing_key, message). Note that the producer needs to drain events to use this feature.

channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.channel "Link to this definition")exchange _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.exchange "Link to this definition")
Default exchange

routing_key _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.routing_key "Link to this definition")
Default routing key.

serializer _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.serializer "Link to this definition")
Default serializer to use. Default is JSON.

compression _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.compression "Link to this definition")
Default compression method. Disabled by default.

auto_declare _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.auto_declare "Link to this definition")
By default, if a default exchange is set, that exchange will be declare when publishing a message.

on_return _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.on_return "Link to this definition")
Basic return callback.

connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.connection "Link to this definition")declare()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Producer.declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.declare "Link to this definition")
Declare the exchange.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id34 "Link to this heading")

> This happens automatically at instantiation when the [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.auto_declare "kombu.Producer.auto_declare") flag is enabled.

maybe_declare(_entity_, _retry=False_, _**retry\_policy_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Producer.maybe_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.maybe_declare "Link to this definition")
Declare exchange if not already declared during this session.

publish(_body_, _routing\_key=None_, _delivery\_mode=None_, _mandatory=False_, _immediate=False_, _priority=0_, _content\_type=None_, _content\_encoding=None_, _serializer=None_, _headers=None_, _compression=None_, _exchange=None_, _retry=False_, _retry\_policy=None_, _declare=None_, _expiration=None_, _timeout=None_, _confirm\_timeout=None_, _**properties_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Producer.publish)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.publish "Link to this definition")
Publish message to the specified exchange.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id35 "Link to this heading")

> body (Any): Message body. routing_key (str): Message routing key. delivery_mode (enum): See `delivery_mode`. mandatory (bool): Currently not supported. immediate (bool): Currently not supported. priority (int): Message priority. A number between 0 and 9. content_type (str): Content type. Default is auto-detect. content_encoding (str): Content encoding. Default is auto-detect. serializer (str): Serializer to use. Default is auto-detect. compression (str): Compression method to use. Default is none. headers (Dict): Mapping of arbitrary headers to pass along
> 
> 
> > with the message body.
> 
> exchange (kombu.entity.Exchange, str): Override the exchange.
> Note that this exchange must have been declared.
> 
> declare (Sequence[EntityT]): Optional list of required entities
> that must have been declared before publishing the message. The entities will be declared using [`maybe_declare()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.common.html#kombu.common.maybe_declare "kombu.common.maybe_declare").
> 
> retry (bool): Retry publishing, or declaring entities if the
> connection is lost.
> 
> retry_policy (Dict): Retry configuration, this is the keywords
> supported by [`ensure()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.ensure "kombu.Connection.ensure").
> 
> expiration (float): A TTL in seconds can be specified per message.
> Default is no expiration.
> 
> timeout (float): Set timeout to wait maximum timeout second
> for message to publish.
> 
> confirm_timeout (float): Set confirm timeout to wait maximum timeout second
> for message to confirm publishing if the channel is set to confirm publish mode.
> 
> 
> [**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id36)properties (Any): Additional message properties, see AMQP spec.

revive(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Producer.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer.revive "Link to this definition")
Revive the producer after connection loss.

[Message Consumer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id52)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#message-consumer "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.Consumer(_channel_, _queues=None_, _no\_ack=None_, _auto\_declare=None_, _callbacks=None_, _on\_decode\_error=None_, _on\_message=None_, _accept=None_, _prefetch\_count=None_, _tag\_prefix=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "Link to this definition")
Message consumer.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id38 "Link to this heading")

> channel (kombu.Connection, ChannelT): see [`channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.channel "kombu.Consumer.channel"). queues (Sequence[kombu.Queue]): see [`queues`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.queues "kombu.Consumer.queues"). no_ack (bool): see [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.no_ack "kombu.Consumer.no_ack"). auto_declare (bool): see [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.auto_declare "kombu.Consumer.auto_declare") callbacks (Sequence[Callable]): see [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.callbacks "kombu.Consumer.callbacks"). on_message (Callable): See [`on_message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.on_message "kombu.Consumer.on_message") on_decode_error (Callable): see [`on_decode_error`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.on_decode_error "kombu.Consumer.on_decode_error"). prefetch_count (int): see `prefetch_count`.

channel _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.channel "Link to this definition")
The connection/channel to use for this consumer.

queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.queues "Link to this definition")
A single [`Queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "kombu.Queue"), or a list of queues to consume from.

no_ack _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.no_ack "Link to this definition")
Flag for automatic message acknowledgment. If enabled the messages are automatically acknowledged by the broker. This can increase performance but means that you have no control of when the message is removed.

Disabled by default.

auto_declare _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.auto_declare "Link to this definition")
By default all entities will be declared at instantiation, if you want to handle this manually you can set this to `False`.

callbacks _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.callbacks "Link to this definition")
List of callbacks called in order when a message is received.

The signature of the callbacks must take two arguments: (body, message), which is the decoded message body and the `Message` instance.

on_message _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.on_message "Link to this definition")
Optional function called whenever a message is received.

When defined this function will be called instead of the [`receive()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.receive "kombu.Consumer.receive") method, and [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.callbacks "kombu.Consumer.callbacks") will be disabled.

So this can be used as an alternative to [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.callbacks "kombu.Consumer.callbacks") when you don’t want the body to be automatically decoded. Note that the message will still be decompressed if the message has the `compression` header set.

The signature of the callback must take a single argument, which is the `Message` object.

Also note that the `message.body` attribute, which is the raw contents of the message body, may in some cases be a read-only `buffer` object.

on_decode_error _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.on_decode_error "Link to this definition")
Callback called when a message can’t be decoded.

The signature of the callback must take two arguments: (message, exc), which is the message that can’t be decoded and the exception that occurred while trying to decode it.

connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.connection "Link to this definition")declare()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.declare "Link to this definition")
Declare queues, exchanges and bindings.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id39 "Link to this heading")

> This is done automatically at instantiation when [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.auto_declare "kombu.Consumer.auto_declare") is set.

register_callback(_callback_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.register_callback)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.register_callback "Link to this definition")
Register a new callback to be called when a message is received.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id40 "Link to this heading")

> The signature of the callback needs to accept two arguments: (body, message), which is the decoded message body and the `Message` instance.

add_queue(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.add_queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.add_queue "Link to this definition")
Add a queue to the list of queues to consume from.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id41 "Link to this heading")

> This will not start consuming from the queue, for that you will have to call [`consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.consume "kombu.Consumer.consume") after.

consume(_no\_ack=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.consume "Link to this definition")
Start consuming messages.

Can be called multiple times, but note that while it will consume from new queues added since the last call, it will not cancel consuming from removed queues ( use [`cancel_by_queue()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.cancel_by_queue "kombu.Consumer.cancel_by_queue")).

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id42 "Link to this heading")

> no_ack (bool): See [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.no_ack "kombu.Consumer.no_ack").

cancel()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.cancel "Link to this definition")
End all active queue consumers.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id43 "Link to this heading")

> This does not affect already delivered messages, but it does mean the server will not send any more messages for this consumer.

cancel_by_queue(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.cancel_by_queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.cancel_by_queue "Link to this definition")
Cancel consumer by queue name.

consuming_from(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.consuming_from)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.consuming_from "Link to this definition")
Return `True` if currently consuming from queue’.

purge()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.purge)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.purge "Link to this definition")
Purge messages from all queues.

#### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id44 "Link to this heading")

> This will _delete all ready messages_, there is no undo operation.

flow(_active_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.flow)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.flow "Link to this definition")
Enable/disable flow from peer.

This is a simple flow-control mechanism that a peer can use to avoid overflowing its queues or otherwise finding itself receiving more messages than it can process.

The peer that receives a request to stop sending content will finish sending the current content (if any), and then wait until flow is reactivated.

qos(_prefetch\_size=0_, _prefetch\_count=0_, _apply\_global=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.qos)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.qos "Link to this definition")
Specify quality of service.

The client can request that messages should be sent in advance so that when the client finishes processing a message, the following message is already held locally, rather than needing to be sent down the channel. Prefetching gives a performance improvement.

The prefetch window is Ignored if the [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.no_ack "kombu.Consumer.no_ack") option is set.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id45 "Link to this heading")

> prefetch_size (int): Specify the prefetch window in octets.
> The server will send a message in advance if it is equal to or smaller in size than the available prefetch size (and also falls within other prefetch limits). May be set to zero, meaning “no specific limit”, although other prefetch limits may still apply.
> 
> prefetch_count (int): Specify the prefetch window in terms of
> whole messages.
> 
> 
> apply_global (bool): Apply new settings globally on all channels.

recover(_requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.recover)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.recover "Link to this definition")
Redeliver unacknowledged messages.

Asks the broker to redeliver all unacknowledged messages on the specified channel.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id46 "Link to this heading")

> requeue (bool): By default the messages will be redelivered
> to the original recipient. With requeue set to true, the server will attempt to requeue the message, potentially then delivering it to an alternative subscriber.

receive(_body_, _message_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.receive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.receive "Link to this definition")
Method called when a message is received.

This dispatches to the registered [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.callbacks "kombu.Consumer.callbacks").

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#id47 "Link to this heading")

> body (Any): The decoded message body. message (~kombu.Message): The message instance.

raises NotImplementedError:
If no consumer callbacks have been: registered.

revive(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer.revive "Link to this definition")
Revive consumer after connection loss.

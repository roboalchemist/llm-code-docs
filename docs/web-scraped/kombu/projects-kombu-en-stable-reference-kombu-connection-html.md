# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html

Title: kombu.connection — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.connection.html).

Client (Connection).

*   [Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#connection)

*   [Pools](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#pools)

[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id18)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#connection "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.connection.Connection(_hostname='localhost'_, _userid=None_, _password=None_, _virtual\_host=None_, _port=None_, _insist=False_, _ssl=False_, _transport=None_, _connect\_timeout=5_, _transport\_options=None_, _login\_method=None_, _uri\_prefix=None_, _heartbeat=0_, _failover\_strategy='round-robin'_, _alternates=None_, _credential\_provider=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection "Link to this definition")
A connection to the broker.

### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#example "Link to this heading")

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

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#note "Link to this heading")

> SSL currently only works with the py-amqp, qpid and redis transports. For other transports you can use stunnel.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#arguments "Link to this heading")

> URL (str, Sequence): Broker URL, or a list of URLs.

### Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#keyword-arguments "Link to this heading")

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
> Note that if heartbeats are enabled then the [`heartbeat_check()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.heartbeat_check "kombu.connection.Connection.heartbeat_check") method must be called regularly, around once per second.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id1 "Link to this heading")

> The connection is established lazily when needed. If you need the connection to be established, then force it by calling [`connect()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.connect "kombu.connection.Connection.connect"):
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

ChannelPool(_limit=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.ChannelPool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.ChannelPool "Link to this definition")
Pool of channels.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id2 "Link to this heading")

> limit (int): Maximum number of active channels.
> Default is no limit.

#### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id3 "Link to this heading")

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

Consumer(_queues=None_, _channel=None_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.Consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.Consumer "Link to this definition")
Create new [`kombu.Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer") instance.

Pool(_limit=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.Pool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.Pool "Link to this definition")
Pool of connections.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id4 "Link to this heading")

> limit (int): Maximum number of active connections.
> Default is no limit.

#### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id5 "Link to this heading")

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

Producer(_channel=None_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.Producer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.Producer "Link to this definition")
Create new [`kombu.Producer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "kombu.Producer") instance.

SimpleBuffer(_name_, _no\_ack=None_, _queue\_opts=None_, _queue\_args=None_, _exchange\_opts=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.SimpleBuffer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.SimpleBuffer "Link to this definition")
Simple ephemeral queue API.

Create new [`SimpleQueue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue "kombu.simple.SimpleQueue") using a channel from this connection.

SimpleQueue(_name_, _no\_ack=None_, _queue\_opts=None_, _queue\_args=None_, _exchange\_opts=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.SimpleQueue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.SimpleQueue "Link to this definition")
Simple persistent queue API.

Create new [`SimpleQueue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue "kombu.simple.SimpleQueue"), using a channel from this connection.

If `name` is a string, a queue and exchange will be automatically created using that name as the name of the queue and exchange, also it will be used as the default routing key.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id6 "Link to this heading")

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

as_uri(_include\_password=False_, _mask='**'_, _getfields=operator.itemgetter('port','userid','password','virtual\_host','transport')_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.as_uri)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.as_uri "Link to this definition")
Convert connection parameters to URL form.

autoretry(_fun_, _channel=None_, _**ensure\_options_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.autoretry)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.autoretry "Link to this definition")
Decorator for functions supporting a `channel` keyword argument.

The resulting callable will retry calling the function if it raises connection or channel related errors. The return value will be a tuple of `(retval, last_created_channel)`.

If a `channel` is not provided, then one will be automatically acquired (remember to close it afterwards).

#### Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id7 "Link to this heading")

>>> channel = connection.channel()
>>> try:
...    ret, channel = connection.autoretry(
...         publish_messages, channel)
... finally:
...    channel.close()

channel()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.channel "Link to this definition")
Create and return a new channel.

_property_ channel_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.channel_errors "Link to this definition")
List of exceptions that may be raised by the channel.

clone(_**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.clone)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.clone "Link to this definition")
Create a copy of the connection with same settings.

close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.close "Link to this definition")
Close the connection (if open).

collect(_socket\_timeout=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.collect)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.collect "Link to this definition")completes_cycle(_retries_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.completes_cycle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.completes_cycle "Link to this definition")
Return true if the cycle is complete after number of retries.

connect()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.connect)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.connect "Link to this definition")
Establish connection to server immediately.

connect_timeout _=5_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.connect_timeout "Link to this definition")_property_ connected[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.connected "Link to this definition")
Return true if the connection has been established.

_property_ connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.connection "Link to this definition")
The underlying connection object.

#### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#warning "Link to this heading")

> This instance is transport specific, so do not depend on the interface of this object.

_property_ connection_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.connection_errors "Link to this definition")
List of exceptions that may be raised by the connection.

create_transport()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.create_transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.create_transport "Link to this definition")cycle _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.cycle "Link to this definition")
Iterator returning the next broker URL to try in the event of connection failure (initialized by [`failover_strategy`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.failover_strategy "kombu.connection.Connection.failover_strategy")).

declared_entities _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.declared_entities "Link to this definition")
The cache of declared entities is per connection, in case the server loses data.

_property_ default_channel _:[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.SLMQ.html#kombu.transport.SLMQ.Transport.Channel "kombu.transport.SLMQ.Transport.Channel")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.default_channel "Link to this definition")
Default channel.

Created upon access and closed when the connection is closed.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id8 "Link to this heading")

> Can be used for automatic channel handling when you only need one channel, and also it is the channel implicitly used if a connection is passed instead of a channel, to functions that require a channel.

drain_events(_**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.drain_events "Link to this definition")
Wait for a single event from the server.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id9 "Link to this heading")

> timeout (float): Timeout in seconds before we give up.

raises socket.timeout:
if the timeout is exceeded.:

ensure(_obj_, _fun_, _errback=None_, _max\_retries=None_, _interval\_start=1_, _interval\_step=1_, _interval\_max=1_, _on\_revive=None_, _retry\_errors=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.ensure)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.ensure "Link to this definition")
Ensure operation completes.

Regardless of any channel/connection errors occurring.

Retries by establishing the connection, and reapplying the function.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id10 "Link to this heading")

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

ensure_connection(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.ensure_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.ensure_connection "Link to this definition")
Public interface of _ensure_connection for retro-compatibility.

Returns kombu.Connection instance.

failover_strategies _={'round-robin':<class'itertools.cycle'>,'shuffle':<function shufflecycle>}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.failover_strategies "Link to this definition")failover_strategy _='round-robin'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.failover_strategy "Link to this definition")
Strategy used to select new hosts when reconnecting after connection failure. One of “round-robin”, “shuffle” or any custom iterator constantly yielding new URLs to try.

get_heartbeat_interval()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.get_heartbeat_interval)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.get_heartbeat_interval "Link to this definition")get_manager(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.get_manager)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.get_manager "Link to this definition")get_transport_cls()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.get_transport_cls)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.get_transport_cls "Link to this definition")
Get the currently used transport class.

heartbeat _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.heartbeat "Link to this definition")
Heartbeat value, currently only supported by the py-amqp transport.

heartbeat_check(_rate=2_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.heartbeat_check)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.heartbeat_check "Link to this definition")
Check heartbeats.

Allow the transport to perform any periodic tasks required to make heartbeats work. This should be called approximately every second.

If the current transport does not support heartbeats then this is a noop operation.

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id11 "Link to this heading")

> rate (int): Rate is how often the tick is called
> compared to the actual heartbeat value. E.g. if the heartbeat is set to 3 seconds, and the tick is called every 3 / 2 seconds, then the rate is 2. This value is currently unused by any transports.

_property_ host[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.host "Link to this definition")
The host as a host name/port pair separated by colon.

hostname _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.hostname "Link to this definition")info()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.info)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.info "Link to this definition")
Get connection info.

_property_ is_evented[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.is_evented "Link to this definition")login_method _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.login_method "Link to this definition")_property_ manager[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.manager "Link to this definition")
AMQP Management API.

Experimental manager that can be used to manage/monitor the broker instance.

Not available for all transports.

maybe_close_channel(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.maybe_close_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.maybe_close_channel "Link to this definition")
Close given channel, but ignore connection and channel errors.

maybe_switch_next()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.maybe_switch_next)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.maybe_switch_next "Link to this definition")
Switch to next URL given by the current failover strategy.

password _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.password "Link to this definition")port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.port "Link to this definition")_property_ qos_semantics_matches_spec[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.qos_semantics_matches_spec "Link to this definition")_property_ recoverable_channel_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.recoverable_channel_errors "Link to this definition")
Recoverable channel errors.

List of channel related exceptions that can be automatically recovered from without re-establishing the connection.

_property_ recoverable_connection_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.recoverable_connection_errors "Link to this definition")
Recoverable connection errors.

List of connection related exceptions that can be recovered from, but where the connection must be closed and re-established first.

register_with_event_loop(_loop_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.register_with_event_loop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.register_with_event_loop "Link to this definition")release()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.release)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.release "Link to this definition")
Close the connection (if open).

resolve_aliases _={'librabbitmq':'amqp','pyamqp':'amqp'}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.resolve_aliases "Link to this definition")revive(_new\_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.revive "Link to this definition")
Revive connection after connection re-established.

ssl _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.ssl "Link to this definition")supports_exchange_type(_exchange\_type_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.supports_exchange_type)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.supports_exchange_type "Link to this definition")_property_ supports_heartbeats[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.supports_heartbeats "Link to this definition")switch(_conn\_str_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#Connection.switch)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.switch "Link to this definition")
Switch connection parameters to use a new URL or hostname.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id12 "Link to this heading")

> Does not reconnect!

#### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id13 "Link to this heading")

> conn_str (str): either a hostname or URL.

_property_ transport[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.transport "Link to this definition")transport_options _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.transport_options "Link to this definition")
Additional transport specific options, passed on to the transport instance.

uri_prefix _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.uri_prefix "Link to this definition")userid _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.userid "Link to this definition")virtual_host _='/'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.virtual_host "Link to this definition")
[Pools](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id19)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#pools "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See also

The shortcut methods [`Connection.Pool()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.Pool "kombu.connection.Connection.Pool") and [`Connection.ChannelPool()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection.ChannelPool "kombu.connection.Connection.ChannelPool") is the recommended way to instantiate these classes.

_class_ kombu.connection.ConnectionPool(_connection_, _limit=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#ConnectionPool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ConnectionPool "Link to this definition")
Pool of connections.

LimitExceeded _=<class'kombu.exceptions.ConnectionLimitExceeded'>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ConnectionPool.LimitExceeded "Link to this definition")acquire(_block=False_, _timeout=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ConnectionPool.acquire "Link to this definition")
Acquire resource.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id14 "Link to this heading")

> block (bool): If the limit is exceeded,
> then block until there is an available item.
> 
> timeout (float): Timeout to wait
> if `block` is true. Default is `None` (forever).

raises LimitExceeded:
if block is false and the limit has been exceeded.:

release(_resource_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ConnectionPool.release "Link to this definition")force_close_all(_close\_pool=True_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ConnectionPool.force_close_all "Link to this definition")
Close and remove all resources in the pool (also those in use).

Used to close resources from parent processes after fork (e.g. sockets/connections).

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id15 "Link to this heading")

> close_pool (bool): If True (default) then the pool is marked
> as closed. In case of False the pool can be reused.

_class_ kombu.connection.ChannelPool(_connection_, _limit=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/connection.html#ChannelPool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ChannelPool "Link to this definition")
Pool of channels.

LimitExceeded _=<class'kombu.exceptions.ChannelLimitExceeded'>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ChannelPool.LimitExceeded "Link to this definition")acquire(_block=False_, _timeout=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ChannelPool.acquire "Link to this definition")
Acquire resource.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id16 "Link to this heading")

> block (bool): If the limit is exceeded,
> then block until there is an available item.
> 
> timeout (float): Timeout to wait
> if `block` is true. Default is `None` (forever).

raises LimitExceeded:
if block is false and the limit has been exceeded.:

release(_resource_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ChannelPool.release "Link to this definition")force_close_all(_close\_pool=True_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.ChannelPool.force_close_all "Link to this definition")
Close and remove all resources in the pool (also those in use).

Used to close resources from parent processes after fork (e.g. sockets/connections).

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#id17 "Link to this heading")

> close_pool (bool): If True (default) then the pool is marked
> as closed. In case of False the pool can be reused.

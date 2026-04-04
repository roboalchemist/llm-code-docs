# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html

Title: Producer Pools - kombu.pools — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.pools.html).

Connection/Producer Pools - `kombu.pools`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#connection-producer-pools-kombu-pools "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Public resource pools.

_class_ kombu.pools.PoolGroup(_limit=None_, _close\_after\_fork=True_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#PoolGroup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.PoolGroup "Link to this definition")
Collection of resource pools.

create(_resource_, _limit_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#PoolGroup.create)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.PoolGroup.create "Link to this definition")_class_ kombu.pools.ProducerPool(_connections_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool "Link to this definition")
Pool of [`kombu.Producer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "kombu.Producer") instances.

_class_ Producer(_channel_, _exchange=None_, _routing\_key=None_, _serializer=None_, _auto\_declare=None_, _compression=None_, _on\_return=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer "Link to this definition")
Message Producer.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#arguments "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

> channel (kombu.Connection, ChannelT): Connection or channel. exchange (kombu.entity.Exchange, str): Optional default exchange. routing_key (str): Optional default routing key. serializer (str): Default serializer. Default is “json”. compression (str): Default compression method.
> 
> 
> > Default is no compression.
> 
> auto_declare (bool): Automatically declare the default exchange
> at instantiation. Default is `True`.
> 
> on_return (Callable): Callback to call for undeliverable messages,
> when the mandatory or immediate arguments to [`publish()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.publish "kombu.pools.ProducerPool.Producer.publish") is used. This callback needs the following signature: (exception, exchange, routing_key, message). Note that the producer needs to drain events to use this feature.

auto_declare _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.auto_declare "Link to this definition")
By default, if a default exchange is set, that exchange will be declare when publishing a message.

_property_ channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.channel "Link to this definition")close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.close "Link to this definition")compression _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.compression "Link to this definition")
Default compression method. Disabled by default.

_property_ connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.connection "Link to this definition")declare()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.declare "Link to this definition")
Declare the exchange.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#note "Link to this heading")

> This happens automatically at instantiation when the [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.auto_declare "kombu.pools.ProducerPool.Producer.auto_declare") flag is enabled.

exchange _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.exchange "Link to this definition")
Default exchange

maybe_declare(_entity_, _retry=False_, _**retry\_policy_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.maybe_declare "Link to this definition")
Declare exchange if not already declared during this session.

on_return _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.on_return "Link to this definition")
Basic return callback.

publish(_body_, _routing\_key=None_, _delivery\_mode=None_, _mandatory=False_, _immediate=False_, _priority=0_, _content\_type=None_, _content\_encoding=None_, _serializer=None_, _headers=None_, _compression=None_, _exchange=None_, _retry=False_, _retry\_policy=None_, _declare=None_, _expiration=None_, _timeout=None_, _confirm\_timeout=None_, _**properties_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.publish "Link to this definition")
Publish message to the specified exchange.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#id1 "Link to this heading")

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
> [**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#id2)properties (Any): Additional message properties, see AMQP spec.

release()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.release "Link to this definition")revive(_channel_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.revive "Link to this definition")
Revive the producer after connection loss.

routing_key _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.routing_key "Link to this definition")
Default routing key.

serializer _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.Producer.serializer "Link to this definition")
Default serializer to use. Default is JSON.

close_after_fork _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.close_after_fork "Link to this definition")close_resource(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool.close_resource)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.close_resource "Link to this definition")create_producer()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool.create_producer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.create_producer "Link to this definition")new()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool.new)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.new "Link to this definition")prepare(_p_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool.prepare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.prepare "Link to this definition")release(_resource_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool.release)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.release "Link to this definition")setup()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#ProducerPool.setup)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.ProducerPool.setup "Link to this definition")kombu.pools.get_limit()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#get_limit)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.get_limit "Link to this definition")
Get current connection pool limit.

kombu.pools.register_group(_group_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#register_group)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.register_group "Link to this definition")
Register group (can be used as decorator).

kombu.pools.reset(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#reset)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.reset "Link to this definition")
Reset all pools by closing open resources.

kombu.pools.set_limit(_limit_, _force=False_, _reset\_after=False_, _ignore\_errors=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/pools.html#set_limit)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.pools.html#kombu.pools.set_limit "Link to this definition")
Set new connection pool limit.

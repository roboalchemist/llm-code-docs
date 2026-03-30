# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html

Title: kombu.compat — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.compat.html).

Carrot Compatibility - `kombu.compat`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#module-kombu.compat "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Carrot compatibility interface.

See [https://pypi.org/project/carrot/](https://pypi.org/project/carrot/) for documentation.

*   [Publisher](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#publisher)

*   [Consumer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#consumer)

*   [ConsumerSet](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#consumerset)

[Publisher](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id22)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#publisher "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Replace with [`kombu.Producer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "kombu.Producer").

_class_ kombu.compat.Publisher(_connection_, _exchange=None_, _routing\_key=None_, _exchange\_type=None_, _durable=None_, _auto\_delete=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Publisher)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher "Link to this definition")
Carrot compatible producer.

auto_declare _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.auto_declare "Link to this definition")
By default, if a default exchange is set, that exchange will be declare when publishing a message.

auto_delete _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.auto_delete "Link to this definition")_property_ backend[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.backend "Link to this definition")_property_ channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.channel "Link to this definition")close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Publisher.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.close "Link to this definition")compression _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.compression "Link to this definition")
Default compression method. Disabled by default.

_property_ connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.connection "Link to this definition")declare()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.declare "Link to this definition")
Declare the exchange.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#note "Link to this heading")

> This happens automatically at instantiation when the [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.auto_declare "kombu.compat.Publisher.auto_declare") flag is enabled.

durable _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.durable "Link to this definition")exchange _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.exchange "Link to this definition")
Default exchange

exchange_type _='direct'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.exchange_type "Link to this definition")maybe_declare(_entity_, _retry=False_, _**retry\_policy_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.maybe_declare "Link to this definition")
Declare exchange if not already declared during this session.

on_return _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.on_return "Link to this definition")
Basic return callback.

publish(_body_, _routing\_key=None_, _delivery\_mode=None_, _mandatory=False_, _immediate=False_, _priority=0_, _content\_type=None_, _content\_encoding=None_, _serializer=None_, _headers=None_, _compression=None_, _exchange=None_, _retry=False_, _retry\_policy=None_, _declare=None_, _expiration=None_, _timeout=None_, _confirm\_timeout=None_, _**properties_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.publish "Link to this definition")
Publish message to the specified exchange.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#arguments "Link to this heading")

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
> [**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id1)properties (Any): Additional message properties, see AMQP spec.

release()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.release "Link to this definition")revive(_channel_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.revive "Link to this definition")
Revive the producer after connection loss.

routing_key _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.routing_key "Link to this definition")
Default routing key.

send(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Publisher.send)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.send "Link to this definition")serializer _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Publisher.serializer "Link to this definition")
Default serializer to use. Default is JSON.

[Consumer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id23)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#consumer "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Replace with [`kombu.Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer").

_class_ kombu.compat.Consumer(_connection_, _queue=None_, _exchange=None_, _routing\_key=None_, _exchange\_type=None_, _durable=None_, _exclusive=None_, _auto\_delete=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer "Link to this definition")
Carrot compatible consumer.

_exception_ ContentDisallowed[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.ContentDisallowed "Link to this definition")
Consumer does not allow this content-type.

args[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.ContentDisallowed.args "Link to this definition")with_traceback()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.ContentDisallowed.with_traceback "Link to this definition")
Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

accept _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.accept "Link to this definition")
List of accepted content-types.

An exception will be raised if the consumer receives a message with an untrusted content type. By default all content-types are accepted, but not if `kombu.disable_untrusted_serializers()` was called, in which case only json is allowed.

add_queue(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.add_queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.add_queue "Link to this definition")
Add a queue to the list of queues to consume from.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id3 "Link to this heading")

> This will not start consuming from the queue, for that you will have to call [`consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.consume "kombu.compat.Consumer.consume") after.

auto_declare _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.auto_declare "Link to this definition")
By default all entities will be declared at instantiation, if you want to handle this manually you can set this to `False`.

auto_delete _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.auto_delete "Link to this definition")callbacks _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.callbacks "Link to this definition")
List of callbacks called in order when a message is received.

The signature of the callbacks must take two arguments: (body, message), which is the decoded message body and the `Message` instance.

cancel()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.cancel "Link to this definition")
End all active queue consumers.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id4 "Link to this heading")

> This does not affect already delivered messages, but it does mean the server will not send any more messages for this consumer.

cancel_by_queue(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.cancel_by_queue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.cancel_by_queue "Link to this definition")
Cancel consumer by queue name.

channel _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.channel "Link to this definition")
The connection/channel to use for this consumer.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.close "Link to this definition")
End all active queue consumers.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id5 "Link to this heading")

> This does not affect already delivered messages, but it does mean the server will not send any more messages for this consumer.

_property_ connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.connection "Link to this definition")consume(_no\_ack=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.consume "Link to this definition")
Start consuming messages.

Can be called multiple times, but note that while it will consume from new queues added since the last call, it will not cancel consuming from removed queues ( use [`cancel_by_queue()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.cancel_by_queue "kombu.compat.Consumer.cancel_by_queue")).

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id6 "Link to this heading")

> no_ack (bool): See [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.no_ack "kombu.compat.Consumer.no_ack").

consuming_from(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.consuming_from)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.consuming_from "Link to this definition")
Return `True` if currently consuming from queue’.

declare()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.declare "Link to this definition")
Declare queues, exchanges and bindings.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id7 "Link to this heading")

> This is done automatically at instantiation when [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.auto_declare "kombu.compat.Consumer.auto_declare") is set.

discard_all(_filterfunc=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.discard_all)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.discard_all "Link to this definition")durable _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.durable "Link to this definition")exchange _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.exchange "Link to this definition")exchange_type _='direct'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.exchange_type "Link to this definition")exclusive _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.exclusive "Link to this definition")fetch(_no\_ack=None_, _enable\_callbacks=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.fetch)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.fetch "Link to this definition")flow(_active_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.flow)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.flow "Link to this definition")
Enable/disable flow from peer.

This is a simple flow-control mechanism that a peer can use to avoid overflowing its queues or otherwise finding itself receiving more messages than it can process.

The peer that receives a request to stop sending content will finish sending the current content (if any), and then wait until flow is reactivated.

iterconsume(_limit=None_, _no\_ack=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.iterconsume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.iterconsume "Link to this definition")iterqueue(_limit=None_, _infinite=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.iterqueue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.iterqueue "Link to this definition")no_ack _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.no_ack "Link to this definition")
Flag for automatic message acknowledgment. If enabled the messages are automatically acknowledged by the broker. This can increase performance but means that you have no control of when the message is removed.

Disabled by default.

on_decode_error _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.on_decode_error "Link to this definition")
Callback called when a message can’t be decoded.

The signature of the callback must take two arguments: (message, exc), which is the message that can’t be decoded and the exception that occurred while trying to decode it.

on_message _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.on_message "Link to this definition")
Optional function called whenever a message is received.

When defined this function will be called instead of the [`receive()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.receive "kombu.compat.Consumer.receive") method, and [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.callbacks "kombu.compat.Consumer.callbacks") will be disabled.

So this can be used as an alternative to [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.callbacks "kombu.compat.Consumer.callbacks") when you don’t want the body to be automatically decoded. Note that the message will still be decompressed if the message has the `compression` header set.

The signature of the callback must take a single argument, which is the `Message` object.

Also note that the `message.body` attribute, which is the raw contents of the message body, may in some cases be a read-only `buffer` object.

prefetch_count _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.prefetch_count "Link to this definition")
Initial prefetch count

If set, the consumer will set the prefetch_count QoS value at startup. Can also be changed using [`qos()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.qos "kombu.compat.Consumer.qos").

process_next()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.process_next)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.process_next "Link to this definition")purge()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.purge)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.purge "Link to this definition")
Purge messages from all queues.

### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#warning "Link to this heading")

> This will _delete all ready messages_, there is no undo operation.

qos(_prefetch\_size=0_, _prefetch\_count=0_, _apply\_global=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.qos)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.qos "Link to this definition")
Specify quality of service.

The client can request that messages should be sent in advance so that when the client finishes processing a message, the following message is already held locally, rather than needing to be sent down the channel. Prefetching gives a performance improvement.

The prefetch window is Ignored if the [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.no_ack "kombu.compat.Consumer.no_ack") option is set.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id8 "Link to this heading")

> prefetch_size (int): Specify the prefetch window in octets.
> The server will send a message in advance if it is equal to or smaller in size than the available prefetch size (and also falls within other prefetch limits). May be set to zero, meaning “no specific limit”, although other prefetch limits may still apply.
> 
> prefetch_count (int): Specify the prefetch window in terms of
> whole messages.
> 
> 
> apply_global (bool): Apply new settings globally on all channels.

queue _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.queue "Link to this definition")_property_ queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.queues "Link to this definition")receive(_body_, _message_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.receive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.receive "Link to this definition")
Method called when a message is received.

This dispatches to the registered [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.callbacks "kombu.compat.Consumer.callbacks").

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id9 "Link to this heading")

> body (Any): The decoded message body. message (~kombu.Message): The message instance.

raises NotImplementedError:
If no consumer callbacks have been: registered.

recover(_requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.recover)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.recover "Link to this definition")
Redeliver unacknowledged messages.

Asks the broker to redeliver all unacknowledged messages on the specified channel.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id10 "Link to this heading")

> requeue (bool): By default the messages will be redelivered
> to the original recipient. With requeue set to true, the server will attempt to requeue the message, potentially then delivering it to an alternative subscriber.

register_callback(_callback_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/messaging.html#Consumer.register_callback)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.register_callback "Link to this definition")
Register a new callback to be called when a message is received.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id11 "Link to this heading")

> The signature of the callback needs to accept two arguments: (body, message), which is the decoded message body and the `Message` instance.

revive(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.revive "Link to this definition")
Revive consumer after connection loss.

routing_key _=''_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.routing_key "Link to this definition")wait(_limit=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#Consumer.wait)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.Consumer.wait "Link to this definition")
[ConsumerSet](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id24)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#consumerset "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Replace with [`kombu.Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer").

_class_ kombu.compat.ConsumerSet(_connection_, _from\_dict=None_, _consumers=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet "Link to this definition")_exception_ ContentDisallowed[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.ContentDisallowed "Link to this definition")
Consumer does not allow this content-type.

args[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.ContentDisallowed.args "Link to this definition")with_traceback()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.ContentDisallowed.with_traceback "Link to this definition")
Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

accept _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.accept "Link to this definition")
List of accepted content-types.

An exception will be raised if the consumer receives a message with an untrusted content type. By default all content-types are accepted, but not if `kombu.disable_untrusted_serializers()` was called, in which case only json is allowed.

add_consumer(_consumer_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet.add_consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.add_consumer "Link to this definition")add_consumer_from_dict(_queue_, _**options_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet.add_consumer_from_dict)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.add_consumer_from_dict "Link to this definition")add_queue(_queue_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.add_queue "Link to this definition")
Add a queue to the list of queues to consume from.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id12 "Link to this heading")

> This will not start consuming from the queue, for that you will have to call [`consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.consume "kombu.compat.ConsumerSet.consume") after.

auto_declare _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.auto_declare "Link to this definition")
By default all entities will be declared at instantiation, if you want to handle this manually you can set this to `False`.

callbacks _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.callbacks "Link to this definition")
List of callbacks called in order when a message is received.

The signature of the callbacks must take two arguments: (body, message), which is the decoded message body and the `Message` instance.

cancel()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.cancel "Link to this definition")
End all active queue consumers.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id13 "Link to this heading")

> This does not affect already delivered messages, but it does mean the server will not send any more messages for this consumer.

cancel_by_queue(_queue_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.cancel_by_queue "Link to this definition")
Cancel consumer by queue name.

channel _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.channel "Link to this definition")
The connection/channel to use for this consumer.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.close "Link to this definition")
End all active queue consumers.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id14 "Link to this heading")

> This does not affect already delivered messages, but it does mean the server will not send any more messages for this consumer.

_property_ connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.connection "Link to this definition")consume(_no\_ack=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.consume "Link to this definition")
Start consuming messages.

Can be called multiple times, but note that while it will consume from new queues added since the last call, it will not cancel consuming from removed queues ( use [`cancel_by_queue()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.cancel_by_queue "kombu.compat.ConsumerSet.cancel_by_queue")).

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id15 "Link to this heading")

> no_ack (bool): See [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.no_ack "kombu.compat.ConsumerSet.no_ack").

consuming_from(_queue_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.consuming_from "Link to this definition")
Return `True` if currently consuming from queue’.

declare()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.declare "Link to this definition")
Declare queues, exchanges and bindings.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id16 "Link to this heading")

> This is done automatically at instantiation when [`auto_declare`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.auto_declare "kombu.compat.ConsumerSet.auto_declare") is set.

discard_all()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet.discard_all)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.discard_all "Link to this definition")flow(_active_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.flow "Link to this definition")
Enable/disable flow from peer.

This is a simple flow-control mechanism that a peer can use to avoid overflowing its queues or otherwise finding itself receiving more messages than it can process.

The peer that receives a request to stop sending content will finish sending the current content (if any), and then wait until flow is reactivated.

iterconsume(_limit=None_, _no\_ack=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet.iterconsume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.iterconsume "Link to this definition")no_ack _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.no_ack "Link to this definition")
Flag for automatic message acknowledgment. If enabled the messages are automatically acknowledged by the broker. This can increase performance but means that you have no control of when the message is removed.

Disabled by default.

on_decode_error _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.on_decode_error "Link to this definition")
Callback called when a message can’t be decoded.

The signature of the callback must take two arguments: (message, exc), which is the message that can’t be decoded and the exception that occurred while trying to decode it.

on_message _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.on_message "Link to this definition")
Optional function called whenever a message is received.

When defined this function will be called instead of the [`receive()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.receive "kombu.compat.ConsumerSet.receive") method, and [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.callbacks "kombu.compat.ConsumerSet.callbacks") will be disabled.

So this can be used as an alternative to [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.callbacks "kombu.compat.ConsumerSet.callbacks") when you don’t want the body to be automatically decoded. Note that the message will still be decompressed if the message has the `compression` header set.

The signature of the callback must take a single argument, which is the `Message` object.

Also note that the `message.body` attribute, which is the raw contents of the message body, may in some cases be a read-only `buffer` object.

prefetch_count _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.prefetch_count "Link to this definition")
Initial prefetch count

If set, the consumer will set the prefetch_count QoS value at startup. Can also be changed using [`qos()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.qos "kombu.compat.ConsumerSet.qos").

purge()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.purge "Link to this definition")
Purge messages from all queues.

### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id17 "Link to this heading")

> This will _delete all ready messages_, there is no undo operation.

qos(_prefetch\_size=0_, _prefetch\_count=0_, _apply\_global=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.qos "Link to this definition")
Specify quality of service.

The client can request that messages should be sent in advance so that when the client finishes processing a message, the following message is already held locally, rather than needing to be sent down the channel. Prefetching gives a performance improvement.

The prefetch window is Ignored if the [`no_ack`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.no_ack "kombu.compat.ConsumerSet.no_ack") option is set.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id18 "Link to this heading")

> prefetch_size (int): Specify the prefetch window in octets.
> The server will send a message in advance if it is equal to or smaller in size than the available prefetch size (and also falls within other prefetch limits). May be set to zero, meaning “no specific limit”, although other prefetch limits may still apply.
> 
> prefetch_count (int): Specify the prefetch window in terms of
> whole messages.
> 
> 
> apply_global (bool): Apply new settings globally on all channels.

_property_ queues[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.queues "Link to this definition")receive(_body_, _message_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.receive "Link to this definition")
Method called when a message is received.

This dispatches to the registered [`callbacks`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.callbacks "kombu.compat.ConsumerSet.callbacks").

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id19 "Link to this heading")

> body (Any): The decoded message body. message (~kombu.Message): The message instance.

raises NotImplementedError:
If no consumer callbacks have been: registered.

recover(_requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.recover "Link to this definition")
Redeliver unacknowledged messages.

Asks the broker to redeliver all unacknowledged messages on the specified channel.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id20 "Link to this heading")

> requeue (bool): By default the messages will be redelivered
> to the original recipient. With requeue set to true, the server will attempt to requeue the message, potentially then delivering it to an alternative subscriber.

register_callback(_callback_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.register_callback "Link to this definition")
Register a new callback to be called when a message is received.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#id21 "Link to this heading")

> The signature of the callback needs to accept two arguments: (body, message), which is the decoded message body and the `Message` instance.

revive(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compat.html#ConsumerSet.revive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compat.html#kombu.compat.ConsumerSet.revive "Link to this definition")
Revive consumer after connection loss.

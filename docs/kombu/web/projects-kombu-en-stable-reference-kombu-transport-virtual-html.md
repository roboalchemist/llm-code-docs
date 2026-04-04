# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html

Title: Virtual Transport Base Class - kombu.transport.virtual — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.virtual.html).

*   [Transports](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#transports)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#channel)

*   [Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#message)

*   [Quality Of Service](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#quality-of-service)

*   [In-memory State](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#in-memory-state)

[Transports](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#transports "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport "Link to this definition")
Virtual transport.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#arguments "Link to this heading")

> client (kombu.Connection): The client this is a transport for.

Channel _=<class'kombu.transport.virtual.base.Channel'>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.Channel "Link to this definition")Cycle _=<class'kombu.utils.scheduling.FairCycle'>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.Cycle "Link to this definition")polling_interval _=1.0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.polling_interval "Link to this definition")
Time to sleep between unsuccessful polls.

default_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.default_port "Link to this definition")
port number used when no port is specified.

state[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.state "Link to this definition")cycle _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.cycle "Link to this definition")
[`FairCycle`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.FairCycle "kombu.utils.scheduling.FairCycle") instance used to fairly drain events from channels (set by constructor).

establish_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Transport.establish_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.establish_connection "Link to this definition")close_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Transport.close_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.close_connection "Link to this definition")create_channel(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Transport.create_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.create_channel "Link to this definition")close_channel(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Transport.close_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.close_channel "Link to this definition")drain_events(_connection_, _timeout=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Transport.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Transport.drain_events "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id8)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.AbstractChannel[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#AbstractChannel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.AbstractChannel "Link to this definition")
Abstract channel interface.

This is an abstract class defining the channel methods you’d usually want to implement in a virtual channel.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#note "Link to this heading")

> Do not subclass directly, but rather inherit from [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel "kombu.transport.virtual.Channel").

_class_ kombu.transport.virtual.Channel(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel "Link to this definition")
Virtual channel.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id1 "Link to this heading")

> connection (ConnectionT): The transport instance this
> channel is part of.

Message _=<class'kombu.transport.virtual.base.Message'>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.Message "Link to this definition")
message class used.

state[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.state "Link to this definition")
Broker state containing exchanges and bindings.

qos[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.qos "Link to this definition")
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS "kombu.transport.virtual.QoS") manager for this channel.

do_restore _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.do_restore "Link to this definition")
flag to restore unacked messages when channel goes out of scope.

exchange_types _={'direct':<class'kombu.transport.virtual.exchange.DirectExchange'>,'fanout':<class'kombu.transport.virtual.exchange.FanoutExchange'>,'topic':<class'kombu.transport.virtual.exchange.TopicExchange'>}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.exchange_types "Link to this definition")
mapping of exchange types and corresponding classes.

exchange_declare(_exchange=None_, _type='direct'_, _durable=False_, _auto\_delete=False_, _arguments=None_, _nowait=False_, _passive=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.exchange_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.exchange_declare "Link to this definition")
Declare exchange.

exchange_delete(_exchange_, _if\_unused=False_, _nowait=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.exchange_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.exchange_delete "Link to this definition")
Delete exchange and all its bindings.

queue_declare(_queue=None_, _passive=False_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.queue_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.queue_declare "Link to this definition")
Declare queue.

queue_delete(_queue_, _if\_unused=False_, _if\_empty=False_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.queue_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.queue_delete "Link to this definition")
Delete queue.

queue_bind(_queue_, _exchange=None_, _routing\_key=''_, _arguments=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.queue_bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.queue_bind "Link to this definition")
Bind queue to exchange with routing key.

queue_purge(_queue_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.queue_purge)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.queue_purge "Link to this definition")
Remove all ready messages from queue.

basic_publish(_message_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_publish)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_publish "Link to this definition")
Publish message.

basic_consume(_queue_, _no\_ack_, _callback_, _consumer\_tag_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_consume "Link to this definition")
Consume from queue.

basic_cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

basic_get(_queue_, _no\_ack=False_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_get)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_get "Link to this definition")
Get message by direct access (synchronous).

basic_ack(_delivery\_tag_, _multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_ack "Link to this definition")
Acknowledge message.

basic_recover(_requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_recover)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_recover "Link to this definition")
Recover unacked messages.

basic_reject(_delivery\_tag_, _requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_reject)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_reject "Link to this definition")
Reject message.

basic_qos(_prefetch\_size=0_, _prefetch\_count=0_, _apply\_global=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.basic_qos)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.basic_qos "Link to this definition")
Change QoS settings for this channel.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id2 "Link to this heading")

> Only prefetch_count is supported.

get_table(_exchange_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.get_table)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

typeof(_exchange_, _default='direct'_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.typeof)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.typeof "Link to this definition")
Get the exchange type instance for exchange.

drain_events(_timeout=None_, _callback=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.drain_events "Link to this definition")prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.prepare_message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.prepare_message "Link to this definition")
Prepare message data.

message_to_python(_raw\_message_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.message_to_python)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.message_to_python "Link to this definition")
Convert raw message to [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message") instance.

flow(_active=True_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.flow)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.flow "Link to this definition")
Enable/disable message flow.

Raises:
[**NotImplementedError**](https://docs.python.org/dev/library/exceptions.html#NotImplementedError "(in Python v3.15)") – as flow: is not implemented by the base virtual implementation.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Channel.close "Link to this definition")
Close channel.

Cancel all consumers, and requeue unacked messages.

[Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id9)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#message "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.Message(_payload_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "Link to this definition")
Message object.

_exception_ MessageStateError[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.MessageStateError "Link to this definition")
The message has already been acknowledged.

args[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.MessageStateError.args "Link to this definition")with_traceback()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.MessageStateError.with_traceback "Link to this definition")
Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.accept "Link to this definition")ack(_multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.ack "Link to this definition")
Acknowledge this message as being processed.

This will remove the message from the queue.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.MessageStateError "kombu.transport.virtual.Message.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

ack_log_error(_logger_, _errors_, _multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.ack_log_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.ack_log_error "Link to this definition")_property_ acknowledged[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.acknowledged "Link to this definition")
Set to true if the message has been acknowledged.

body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.content_type "Link to this definition")decode()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.decode)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.decode "Link to this definition")
Deserialize the message body.

Returning the original python structure sent by the publisher.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id3 "Link to this heading")

> The return value is memoized, use _decode to force re-evaluation.

delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.delivery_tag "Link to this definition")errors _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.errors "Link to this definition")_property_ payload[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.payload "Link to this definition")
The decoded message body.

properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.properties "Link to this definition")reject(_requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.reject)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.reject "Link to this definition")
Reject this message.

The message will be discarded by the server.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.MessageStateError "kombu.transport.virtual.Message.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

reject_log_error(_logger_, _errors_, _requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.reject_log_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.reject_log_error "Link to this definition")requeue()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.requeue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.requeue "Link to this definition")
Reject this message and put it back on the queue.

### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#warning "Link to this heading")

> You must not use this method as a means of selecting messages to process.

raises MessageStateError:
If the message has already been: acknowledged/requeued/rejected.

serializable()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Message.serializable)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message.serializable "Link to this definition")
[Quality Of Service](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id10)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#quality-of-service "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.QoS(_channel_, _prefetch\_count=0_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS "Link to this definition")
Quality of Service guarantees.

Only supports prefetch_count at this point.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id4 "Link to this heading")

> channel (ChannelT): Connection channel. prefetch_count (int): Initial prefetch count (defaults to 0).

ack(_delivery\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.ack "Link to this definition")
Acknowledge message and remove from transactional state.

append(_message_, _delivery\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.append)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.append "Link to this definition")
Append message to transactional state.

can_consume()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.can_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.can_consume "Link to this definition")
Return true if the channel can be consumed from.

Used to ensure the client adhers to currently active prefetch limits.

can_consume_max_estimate()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.can_consume_max_estimate)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.can_consume_max_estimate "Link to this definition")
Return the maximum number of messages allowed to be returned.

Returns an estimated number of messages that a consumer may be allowed to consume at once from the broker. This is used for services where bulk ‘get message’ calls are preferred to many individual ‘get message’ calls - like SQS.

Returns:
**int**

Return type:
greater than zero.

get(_delivery\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.get)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.get "Link to this definition")prefetch_count _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.prefetch_count "Link to this definition")
current prefetch count value

reject(_delivery\_tag_, _requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.reject)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.reject "Link to this definition")
Remove from transactional state and requeue message.

restore_at_shutdown _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.restore_at_shutdown "Link to this definition")
If disabled, unacked messages won’t be restored at shutdown.

restore_unacked()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.restore_unacked)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.restore_unacked "Link to this definition")
Restore all unacknowledged messages.

restore_unacked_once(_stderr=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.restore_unacked_once)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.restore_unacked_once "Link to this definition")
Restore all unacknowledged messages at shutdown/gc collect.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id5 "Link to this heading")

> Can only be called once for each instance, subsequent calls will be ignored.

restore_visible(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#QoS.restore_visible)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.QoS.restore_visible "Link to this definition")
Restore any pending unacknowledged messages.

To be filled in for visibility_timeout style implementations.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id6 "Link to this heading")

> This is implementation optional, and currently only used by the Redis transport.

[In-memory State](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#id11)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#in-memory-state "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.virtual.BrokerState(_exchanges=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState "Link to this definition")
Broker state holds exchanges, queues and bindings.

binding_declare(_queue_, _exchange_, _routing\_key_, _arguments_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState.binding_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.binding_declare "Link to this definition")binding_delete(_queue_, _exchange_, _routing\_key_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState.binding_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.binding_delete "Link to this definition")bindings _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.bindings "Link to this definition")
This is the actual bindings registry, used to store bindings and to test ‘in’ relationships in constant time. It has the following structure:

{
    (queue, exchange, routing_key): arguments,
    # ...,
}

clear()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState.clear)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.clear "Link to this definition")exchanges _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.exchanges "Link to this definition")
Mapping of exchange name to [`kombu.transport.virtual.exchange.ExchangeType`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.exchange.html#kombu.transport.virtual.exchange.ExchangeType "kombu.transport.virtual.exchange.ExchangeType")

has_binding(_queue_, _exchange_, _routing\_key_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState.has_binding)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.has_binding "Link to this definition")queue_bindings(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState.queue_bindings)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.queue_bindings "Link to this definition")queue_bindings_delete(_queue_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#BrokerState.queue_bindings_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.queue_bindings_delete "Link to this definition")queue_index _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.BrokerState.queue_index "Link to this definition")
The queue index is used to access directly (constant time) all the bindings of a certain queue. It has the following structure:

{
    queue: {
        (queue, exchange, routing_key),
        # ...,
    },
    # ...,
}

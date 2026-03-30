# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html

Title: Transport Base Class - kombu.transport.base — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.base.html).

Base transport interface.

*   [Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#message)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#transport)

[Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#message "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.base.Message(_body=None_, _delivery\_tag=None_, _content\_type=None_, _content\_encoding=None_, _delivery\_info=None_, _properties=None_, _headers=None_, _postencode=None_, _accept=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message "Link to this definition")
Base class for received messages.

### Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#keyword-arguments "Link to this heading")

> channel (ChannelT): If message was received, this should be the
> channel that the message was received on.
> 
> 
> body (str): Message body.
> 
> delivery_mode (bool): Set custom delivery mode.
> Defaults to `delivery_mode`.
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

payload[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.payload "Link to this definition")
The decoded message body.

channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.channel "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.delivery_tag "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.content_type "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.content_encoding "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.delivery_info "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.properties "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.body "Link to this definition")acknowledged[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.acknowledged "Link to this definition")
Set to true if the message has been acknowledged.

ack(_multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.ack "Link to this definition")
Acknowledge this message as being processed.

This will remove the message from the queue.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.MessageStateError "kombu.exceptions.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

reject(_requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.reject)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.reject "Link to this definition")
Reject this message.

The message will be discarded by the server.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.exceptions.html#kombu.exceptions.MessageStateError "kombu.exceptions.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

requeue()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.requeue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.requeue "Link to this definition")
Reject this message and put it back on the queue.

#### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#warning "Link to this heading")

> You must not use this method as a means of selecting messages to process.

raises MessageStateError:
If the message has already been: acknowledged/requeued/rejected.

decode()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.decode)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Message.decode "Link to this definition")
Deserialize the message body.

Returning the original python structure sent by the publisher.

#### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#note "Link to this heading")

> The return value is memoized, use _decode to force re-evaluation.

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.base.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/base.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport "Link to this definition")
Base class for transports.

client _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.client "Link to this definition")
The [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") owning this instance.

default_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.default_port "Link to this definition")
Default port used when no port has been specified.

recoverable_connection_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.recoverable_connection_errors "Link to this definition")
Optional list of connection related exceptions that can be recovered from, but where the connection must be closed and re-established first.

If not defined then all [`connection_errors`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.connection_errors "kombu.transport.base.Transport.connection_errors") and [`channel_errors`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.channel_errors "kombu.transport.base.Transport.channel_errors") will be regarded as recoverable, but needing to close the connection first.

recoverable_channel_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.recoverable_channel_errors "Link to this definition")
Optional list of channel related exceptions that can be automatically recovered from without re-establishing the connection.

connection_errors _=(<class'amqp.exceptions.ConnectionError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

channel_errors _=(<class'amqp.exceptions.ChannelError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

establish_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/base.html#Transport.establish_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.establish_connection "Link to this definition")close_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/base.html#Transport.close_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.close_connection "Link to this definition")create_channel(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/base.html#Transport.create_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.create_channel "Link to this definition")close_channel(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/base.html#Transport.close_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.close_channel "Link to this definition")drain_events(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/base.html#Transport.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.base.html#kombu.transport.base.Transport.drain_events "Link to this definition")

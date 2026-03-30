# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html

Title: kombu.message — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.message.html).

Message class.

_class_ kombu.message.Message(_body=None_, _delivery\_tag=None_, _content\_type=None_, _content\_encoding=None_, _delivery\_info=None_, _properties=None_, _headers=None_, _postencode=None_, _accept=None_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message "Link to this definition")
Base class for received messages.

Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#keyword-arguments "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

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

_exception_ MessageStateError[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.MessageStateError "Link to this definition")
The message has already been acknowledged.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.accept "Link to this definition")ack(_multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.ack "Link to this definition")
Acknowledge this message as being processed.

This will remove the message from the queue.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.MessageStateError "kombu.message.Message.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

ack_log_error(_logger_, _errors_, _multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.ack_log_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.ack_log_error "Link to this definition")_property_ acknowledged[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.acknowledged "Link to this definition")
Set to true if the message has been acknowledged.

body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.content_type "Link to this definition")decode()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.decode)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.decode "Link to this definition")
Deserialize the message body.

Returning the original python structure sent by the publisher.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#note "Link to this heading")

> The return value is memoized, use _decode to force re-evaluation.

delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.delivery_tag "Link to this definition")errors _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.errors "Link to this definition")_property_ payload[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.payload "Link to this definition")
The decoded message body.

properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.properties "Link to this definition")reject(_requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.reject)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.reject "Link to this definition")
Reject this message.

The message will be discarded by the server.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.MessageStateError "kombu.message.Message.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

reject_log_error(_logger_, _errors_, _requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.reject_log_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.reject_log_error "Link to this definition")requeue()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/message.html#Message.requeue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#kombu.message.Message.requeue "Link to this definition")
Reject this message and put it back on the queue.

### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.message.html#warning "Link to this heading")

> You must not use this method as a means of selecting messages to process.

raises MessageStateError:
If the message has already been: acknowledged/requeued/rejected.

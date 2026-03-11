# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html

Title: Pure-python AMQP Transport - kombu.transport.pyamqp — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.pyamqp.html).

pyamqp transport module for Kombu.

Pure-Python amqp transport using py-amqp library.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#features "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Native

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: Yes

*   Supports Priority: Yes

*   Supports TTL: Yes

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#connection-string "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string can have the following formats:

amqp://[USER:PASSWORD@]BROKER_ADDRESS[:PORT][/VIRTUALHOST]
[USER:PASSWORD@]BROKER_ADDRESS[:PORT][/VIRTUALHOST]
amqp://

For TLS encryption use:

amqps://[USER:PASSWORD@]BROKER_ADDRESS[:PORT][/VIRTUALHOST]

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#transport-options "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Transport Options are passed to constructor of underlying py-amqp [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.connection.html#kombu.connection.Connection "kombu.connection.Connection") class.

[Using TLS](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#using-tls "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Transport over TLS can be enabled by `ssl` parameter of [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") class. By setting `ssl=True`, TLS transport is used:

conn = Connect('amqp://', ssl=True)

This is equivalent to `amqps://` transport URI:

conn = Connect('amqps://')

For adding additional parameters to underlying TLS, `ssl` parameter should be set with dict instead of True:

conn = Connect('amqp://broker.example.com', ssl={
        'keyfile': '/path/to/keyfile'
        'certfile': '/path/to/certfile',
        'ca_certs': '/path/to/ca_certfile'
    }
)

All parameters are passed to `ssl` parameter of [`amqp.connection.Connection`](https://docs.celeryq.dev/projects/amqp/en/latest/reference/amqp.connection.html#amqp.connection.Connection "(in py-amqp v5.3)") class.

SSL option `server_hostname` can be set to `None` which is causing using hostname from broker URL. This is useful when failover is used to fill `server_hostname` with currently used broker:

conn = Connect('amqp://broker1.example.com;broker2.example.com', ssl={
        'server_hostname': None
    }
)

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#transport-options)

*   [Using TLS](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#using-tls)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#transport)

*   [Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#connection)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#channel)

*   [Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#message)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#transport "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.pyamqp.Transport(_client_, _default\_port=None_, _default\_ssl\_port=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport "Link to this definition")
AMQP Transport.

_class_ Connection(_host='localhost:5672'_, _userid='guest'_, _password='guest'_, _login\_method=None_, _login\_response=None_, _authentication=()_, _virtual\_host='/'_, _locale='en\_US'_, _client\_properties=None_, _ssl=False_, _connect\_timeout=None_, _channel\_max=None_, _frame\_max=None_, _heartbeat=0_, _on\_open=None_, _on\_blocked=None_, _on\_unblocked=None_, _confirm\_publish=False_, _on\_tune\_ok=None_, _read\_timeout=None_, _write\_timeout=None_, _socket\_settings=None_, _frame\_handler=<function frame\_handler>_, _frame\_writer=<function frame\_writer>_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection "Link to this definition")
AMQP Connection.

_class_ Channel(_connection_, _channel\_id=None_, _auto\_decode=True_, _on\_open=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel "Link to this definition")
AMQP Channel.

_class_ Message(_msg_, _channel=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message "Link to this definition")
AMQP Message.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.Message.properties "Link to this definition")auto_decode[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.auto_decode "Link to this definition")channel_id[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.channel_id "Link to this definition")connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.connection "Link to this definition")is_closing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.is_closing "Link to this definition")message_to_python(_raw\_message_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.message_to_python "Link to this definition")
Convert encoded message body back to a Python value.

method_queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.method_queue "Link to this definition")prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_, _\_Message=<class'amqp.basic\_message.Message'>_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.prepare_message "Link to this definition")
Prepare message so that it can be sent using this transport.

prepare_queue_arguments(_arguments_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.Channel.prepare_queue_arguments "Link to this definition")auto_decode[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.auto_decode "Link to this definition")channel_id[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.channel_id "Link to this definition")connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.connection "Link to this definition")is_closing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.is_closing "Link to this definition")method_queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.Connection.method_queue "Link to this definition")channel_errors _=(<class'amqp.exceptions.ChannelError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

close_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.close_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.close_connection "Link to this definition")
Close the AMQP broker connection.

connection_errors _=(<class'amqp.exceptions.ConnectionError'>,<class'OSError'>,<class'OSError'>,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

create_channel(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.create_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.create_channel "Link to this definition")_property_ default_connection_params[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.default_connection_params "Link to this definition")default_port _=5672_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.default_port "Link to this definition")
Default port used when no port has been specified.

default_ssl_port _=5671_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.default_ssl_port "Link to this definition")drain_events(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.drain_events "Link to this definition")driver_name _='py-amqp'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='amqp'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.driver_version "Link to this definition")establish_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.establish_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.establish_connection "Link to this definition")
Establish connection to the AMQP broker.

get_heartbeat_interval(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.get_heartbeat_interval)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.get_heartbeat_interval "Link to this definition")get_manager(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.get_manager)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.get_manager "Link to this definition")heartbeat_check(_connection_, _rate=2_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.heartbeat_check)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.heartbeat_check "Link to this definition")implements _={'asynchronous':True,'exchange\_type':frozenset({'direct','fanout','headers','topic'}),'heartbeats':True}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.implements "Link to this definition")qos_semantics_matches_spec(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.qos_semantics_matches_spec)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.qos_semantics_matches_spec "Link to this definition")recoverable_channel_errors _=(<class'amqp.exceptions.RecoverableChannelError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.recoverable_channel_errors "Link to this definition")recoverable_connection_errors _=(<class'amqp.exceptions.RecoverableConnectionError'>,<class'amqp.exceptions.MessageNacked'>,<class'OSError'>,<class'OSError'>,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.recoverable_connection_errors "Link to this definition")register_with_event_loop(_connection_, _loop_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.register_with_event_loop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.register_with_event_loop "Link to this definition")verify_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Transport.verify_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Transport.verify_connection "Link to this definition")
[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#connection "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.pyamqp.Connection(_host='localhost:5672'_, _userid='guest'_, _password='guest'_, _login\_method=None_, _login\_response=None_, _authentication=()_, _virtual\_host='/'_, _locale='en\_US'_, _client\_properties=None_, _ssl=False_, _connect\_timeout=None_, _channel\_max=None_, _frame\_max=None_, _heartbeat=0_, _on\_open=None_, _on\_blocked=None_, _on\_unblocked=None_, _confirm\_publish=False_, _on\_tune\_ok=None_, _read\_timeout=None_, _write\_timeout=None_, _socket\_settings=None_, _frame\_handler=<function frame\_handler>_, _frame\_writer=<function frame\_writer>_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection "Link to this definition")
AMQP Connection.

_class_ Channel(_connection_, _channel\_id=None_, _auto\_decode=True_, _on\_open=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel "Link to this definition")
AMQP Channel.

Consumer(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Consumer "Link to this definition")_class_ Message(_msg_, _channel=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message "Link to this definition")
AMQP Message.

_exception_ MessageStateError[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError "Link to this definition")
The message has already been acknowledged.

args[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError.args "Link to this definition")with_traceback()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError.with_traceback "Link to this definition")
Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.accept "Link to this definition")ack(_multiple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.ack "Link to this definition")
Acknowledge this message as being processed.

This will remove the message from the queue.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError "kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

ack_log_error(_logger_, _errors_, _multiple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.ack_log_error "Link to this definition")_property_ acknowledged[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.acknowledged "Link to this definition")
Set to true if the message has been acknowledged.

body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.content_type "Link to this definition")decode()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.decode "Link to this definition")
Deserialize the message body.

Returning the original python structure sent by the publisher.

### Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#note "Link to this heading")

> The return value is memoized, use _decode to force re-evaluation.

delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.delivery_tag "Link to this definition")errors _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.errors "Link to this definition")_property_ payload[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.payload "Link to this definition")
The decoded message body.

properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.properties "Link to this definition")reject(_requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.reject "Link to this definition")
Reject this message.

The message will be discarded by the server.

Raises:
[**MessageStateError**](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError "kombu.transport.pyamqp.Connection.Channel.Message.MessageStateError") – If the message has already been: acknowledged/requeued/rejected.

reject_log_error(_logger_, _errors_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.reject_log_error "Link to this definition")requeue()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Message.requeue "Link to this definition")
Reject this message and put it back on the queue.

### Warning:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#warning "Link to this heading")

> You must not use this method as a means of selecting messages to process.

raises MessageStateError:
If the message has already been: acknowledged/requeued/rejected.

Producer(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.Producer "Link to this definition")after_reply_message_received(_queue_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.after_reply_message_received "Link to this definition")
Callback called after RPC reply received.

Notes

Reply queue semantics: can be used to delete the queue after transient reply message received.

auto_decode[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.auto_decode "Link to this definition")basic_ack(_delivery\_tag_, _multiple=False_, _argsig='Lb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_ack "Link to this definition")
Acknowledge one or more messages.

This method acknowledges one or more messages delivered via the Deliver or Get-Ok methods. The client can ask to confirm a single message or a set of messages up to and including a specific message.

Parameters:
*   **delivery_tag** –

longlong

server-assigned delivery tag

The server-assigned and channel-specific delivery tag

RULE:

> The delivery tag is valid only within the channel from which the message was received. I.e. a client MUST NOT receive a message on one channel and then acknowledge it on another.

RULE:

> The server MUST NOT use a zero value for delivery tags. Zero is reserved for client use, meaning “all messages so far received”.

*   **multiple** –

boolean

acknowledge multiple messages

If set to True, the delivery tag is treated as “up to and including”, so that the client can acknowledge multiple messages with a single method. If set to False, the delivery tag refers to a single message. If the multiple field is True, and the delivery tag is zero, tells the server to acknowledge all outstanding messages.

RULE:

> The server MUST validate that a non-zero delivery- tag refers to an delivered message, and raise a channel exception if this is not the case.

basic_cancel(_consumer\_tag_, _nowait=False_, _argsig='sb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_cancel "Link to this definition")
End a queue consumer.

This method cancels a consumer. This does not affect already delivered messages, but it does mean the server will not send any more messages for that consumer. The client may receive an arbitrary number of messages in between sending the cancel method and receiving the cancel-ok reply.

RULE:

> If the queue no longer exists when the client sends a cancel command, or the consumer has been cancelled for other reasons, this command has no effect.

Parameters:
*   **consumer_tag** –

shortstr

consumer tag

Identifier for the consumer, valid within the current connection.

RULE:

> The consumer tag is valid only within the channel from which the consumer was created. I.e. a client MUST NOT create a consumer in one channel and then use it in another.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

basic_consume(_queue=''_, _consumer\_tag=''_, _no\_local=False_, _no\_ack=False_, _exclusive=False_, _nowait=False_, _callback=None_, _arguments=None_, _on\_cancel=None_, _argsig='BssbbbbF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_consume "Link to this definition")
Start a queue consumer.

This method asks the server to start a “consumer”, which is a transient request for messages from a specific queue. Consumers last as long as the channel they were created on, or until the client cancels them.

RULE:

> The server SHOULD support at least 16 consumers per queue, unless the queue was declared as private, and ideally, impose no limit except as defined by available resources.

Parameters:
*   **queue** –

shortstr

Specifies the name of the queue to consume from. If the queue name is null, refers to the current queue for the channel, which is the last declared queue.

RULE:

> If the client did not previously declare a queue, and the queue name in this method is empty, the server MUST raise a connection exception with reply code 530 (not allowed).

*   **consumer_tag** –

shortstr

Specifies the identifier for the consumer. The consumer tag is local to a connection, so two clients can use the same consumer tags. If this field is empty the server will generate a unique tag.

RULE:

> The tag MUST NOT refer to an existing consumer. If the client attempts to create two consumers with the same non-empty tag the server MUST raise a connection exception with reply code 530 (not allowed).

*   **no_local** –

boolean

do not deliver own messages

If the no-local field is set the server will not send messages to the client that published them.

*   **no_ack** –

boolean

no acknowledgment needed

If this field is set the server does not expect acknowledgments for messages. That is, when a message is delivered to the client the server automatically and silently acknowledges it on behalf of the client. This functionality increases performance but at the cost of reliability. Messages can get lost if a client dies before it can deliver them to the application.

*   **exclusive** –

boolean

request exclusive access

Request exclusive consumer access, meaning only this consumer can access the queue.

RULE:

> If the server cannot grant exclusive access to the queue when asked, - because there are other consumers active - it MUST raise a channel exception with return code 403 (access refused).

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

*   **callback** –

Python callable

function/method called with each delivered message

For each message delivered by the broker, the callable will be called with a Message object as the single argument. If no callable is specified, messages are quietly discarded, no_ack should probably be set to True in that case.

basic_get(_queue=''_, _no\_ack=False_, _argsig='Bsb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_get "Link to this definition")
Direct access to a queue.

This method provides a direct access to the messages in a queue using a synchronous dialogue that is designed for specific types of application where synchronous functionality is more important than performance.

Parameters:
*   **queue** –

shortstr

Specifies the name of the queue to consume from. If the queue name is null, refers to the current queue for the channel, which is the last declared queue.

RULE:

> If the client did not previously declare a queue, and the queue name in this method is empty, the server MUST raise a connection exception with reply code 530 (not allowed).

*   **no_ack** –

boolean

no acknowledgment needed

If this field is set the server does not expect acknowledgments for messages. That is, when a message is delivered to the client the server automatically and silently acknowledges it on behalf of the client. This functionality increases performance but at the cost of reliability. Messages can get lost if a client dies before it can deliver them to the application.

Non-blocking, returns a amqp.basic_message.Message object, or None if queue is empty.

basic_publish(_msg_, _exchange=''_, _routing\_key=''_, _mandatory=False_, _immediate=False_, _timeout=None_, _confirm\_timeout=None_, _argsig='Bssbb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_publish "Link to this definition")
Publish a message.

This method publishes a message to a specific exchange. The message will be routed to queues as defined by the exchange configuration and distributed to any active consumers when the transaction, if any, is committed.

When channel is in confirm mode (when Connection parameter confirm_publish is set to True), each message is confirmed. When broker rejects published message (e.g. due internal broker constrains), MessageNacked exception is raised and set confirm_timeout to wait maximum confirm_timeout second for message to confirm.

Parameters:
*   **exchange** –

shortstr

Specifies the name of the exchange to publish to. The exchange name can be empty, meaning the default exchange. If the exchange name is specified, and that exchange does not exist, the server will raise a channel exception.

RULE:

> The server MUST accept a blank exchange name to mean the default exchange.

RULE:

> The exchange MAY refuse basic content in which case it MUST raise a channel exception with reply code 540 (not implemented).

*   **routing_key** –

shortstr

Message routing key

Specifies the routing key for the message. The routing key is used for routing messages depending on the exchange configuration.

*   **mandatory** –

boolean

indicate mandatory routing

This flag tells the server how to react if the message cannot be routed to a queue. If this flag is True, the server will return an unroutable message with a Return method. If this flag is False, the server silently drops the message.

RULE:

> The server SHOULD implement the mandatory flag.

*   **immediate** –

boolean

request immediate delivery

This flag tells the server how to react if the message cannot be routed to a queue consumer immediately. If this flag is set, the server will return an undeliverable message with a Return method. If this flag is zero, the server will queue the message, but with no guarantee that it will ever be consumed.

RULE:

> The server SHOULD implement the immediate flag.

*   **timeout** –

short

timeout for publish

Set timeout to wait maximum timeout second for message to publish.

*   **confirm_timeout** –

short

confirm_timeout for publish in confirm mode

When the channel is in confirm mode set confirm_timeout to wait maximum confirm_timeout second for message to confirm.

basic_publish_confirm(_*args_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_publish_confirm "Link to this definition")basic_qos(_prefetch\_size_, _prefetch\_count_, _a\_global_, _argsig='lBb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_qos "Link to this definition")
Specify quality of service.

This method requests a specific quality of service. The QoS can be specified for the current channel or for all channels on the connection. The particular properties and semantics of a qos method always depend on the content class semantics. Though the qos method could in principle apply to both peers, it is currently meaningful only for the server.

Parameters:
*   **prefetch_size** –

long

prefetch window in octets

The client can request that messages be sent in advance so that when the client finishes processing a message, the following message is already held locally, rather than needing to be sent down the channel. Prefetching gives a performance improvement. This field specifies the prefetch window size in octets. The server will send a message in advance if it is equal to or smaller in size than the available prefetch size (and also falls into other prefetch limits). May be set to zero, meaning “no specific limit”, although other prefetch limits may still apply. The prefetch-size is ignored if the no-ack option is set.

RULE:

> The server MUST ignore this setting when the client is not processing any messages - i.e. the prefetch size does not limit the transfer of single messages to a client, only the sending in advance of more messages while the client still has one or more unacknowledged messages.

*   **prefetch_count** –

short

prefetch window in messages

Specifies a prefetch window in terms of whole messages. This field may be used in combination with the prefetch-size field; a message will only be sent in advance if both prefetch windows (and those at the channel and connection level) allow it. The prefetch- count is ignored if the no-ack option is set.

RULE:

> The server MAY send less data in advance than allowed by the client’s specified prefetch windows but it MUST NOT send more.

*   **a_global** –

boolean

Defines a scope of QoS. Semantics of this parameter differs between AMQP 0-9-1 standard and RabbitMQ broker:

MEANING IN AMQP 0-9-1:
False: shared across all consumers on the channel True: shared across all consumers on the connection

MEANING IN RABBITMQ:False: applied separately to each new consumer
on the channel

True: shared across all consumers on the channel

basic_recover(_requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_recover "Link to this definition")
Redeliver unacknowledged messages.

This method asks the broker to redeliver all unacknowledged messages on a specified channel. Zero or more messages may be redelivered. This method is only allowed on non-transacted channels.

RULE:

> The server MUST set the redelivered flag on all messages that are resent.

RULE:

> The server MUST raise a channel exception if this is called on a transacted channel.

Parameters:
**requeue** –

boolean

requeue the message

If this field is False, the message will be redelivered to the original recipient. If this field is True, the server will attempt to requeue the message, potentially then delivering it to an alternative subscriber.

basic_recover_async(_requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_recover_async "Link to this definition")basic_reject(_delivery\_tag_, _requeue_, _argsig='Lb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.basic_reject "Link to this definition")
Reject an incoming message.

This method allows a client to reject a message. It can be used to interrupt and cancel large incoming messages, or return untreatable messages to their original queue.

RULE:

> The server SHOULD be capable of accepting and process the Reject method while sending message content with a Deliver or Get-Ok method. I.e. the server should read and process incoming methods while sending output frames. To cancel a partially-send content, the server sends a content body frame of size 1 (i.e. with no data except the frame-end octet).

RULE:

> The server SHOULD interpret this method as meaning that the client is unable to process the message at this time.

RULE:

> A client MUST NOT use this method as a means of selecting messages to process. A rejected message MAY be discarded or dead-lettered, not necessarily passed to another client.

Parameters:
*   **delivery_tag** –

longlong

server-assigned delivery tag

The server-assigned and channel-specific delivery tag

RULE:

> The delivery tag is valid only within the channel from which the message was received. I.e. a client MUST NOT receive a message on one channel and then acknowledge it on another.

RULE:

> The server MUST NOT use a zero value for delivery tags. Zero is reserved for client use, meaning “all messages so far received”.

*   **requeue** –

boolean

requeue the message

If this field is False, the message will be discarded. If this field is True, the server will attempt to requeue the message.

RULE:

> The server MUST NOT deliver the message to the same client within the context of the current channel. The recommended strategy is to attempt to deliver the message to an alternative consumer, and if that is not possible, to move the message to a dead-letter queue. The server MAY use more sophisticated tracking to hold the message on the queue and redeliver it to the same client at a later stage.

channel_id[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.channel_id "Link to this definition")close(_reply\_code=0_, _reply\_text=''_, _method\_sig=(0,0)_, _argsig='BsBB'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.close "Link to this definition")
Request a channel close.

This method indicates that the sender wants to close the channel. This may be due to internal conditions (e.g. a forced shut-down) or due to an error handling a specific method, i.e. an exception. When a close is due to an exception, the sender provides the class and method id of the method which caused the exception.

RULE:

> After sending this method any received method except Channel.Close-OK MUST be discarded.

RULE:

> The peer sending this method MAY use a counter or timeout to detect failure of the other peer to respond correctly with Channel.Close-OK..

Parameters:
*   **reply_code** –

short

The reply code. The AMQ reply codes are defined in AMQ RFC 011.

*   **reply_text** –

shortstr

The localised reply text. This text can be logged as an aid to resolving issues.

*   **class_id** –

short

failing method class

When the close is provoked by a method exception, this is the class of the method.

*   **method_id** –

short

failing method ID

When the close is provoked by a method exception, this is the ID of the method.

collect()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.collect "Link to this definition")
Tear down this object.

Best called after we’ve agreed to close with the server.

confirm_select(_nowait=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.confirm_select "Link to this definition")
Enable publisher confirms for this channel.

Note: This is an RabbitMQ extension.

Can now be used if the channel is in transactional mode.

Parameters:
**nowait** – If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.connection "Link to this definition")dispatch_method(_method\_sig_, _payload_, _content_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.dispatch_method "Link to this definition")exchange_bind(_destination_, _source=''_, _routing\_key=''_, _nowait=False_, _arguments=None_, _argsig='BsssbF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.exchange_bind "Link to this definition")
Bind an exchange to an exchange.

RULE:

> A server MUST allow and ignore duplicate bindings - that is, two or more bind methods for a specific exchanges, with identical arguments - without treating these as an error.

RULE:

> A server MUST allow cycles of exchange bindings to be created including allowing an exchange to be bound to itself.

RULE:

> A server MUST not deliver the same message more than once to a destination exchange, even if the topology of exchanges and bindings results in multiple (even infinite) routes to that exchange.

Parameters:
*   **reserved-1** – short

*   **destination** –

shortstr

Specifies the name of the destination exchange to bind.

RULE:

> A client MUST NOT be allowed to bind a non- existent destination exchange.

RULE:

> The server MUST accept a blank exchange name to mean the default exchange.

*   **source** –

shortstr

Specifies the name of the source exchange to bind.

RULE:

> A client MUST NOT be allowed to bind a non- existent source exchange.

RULE:

> The server MUST accept a blank exchange name to mean the default exchange.

*   **routing-key** –

shortstr

Specifies the routing key for the binding. The routing key is used for routing messages depending on the exchange configuration. Not all exchanges use a routing key - refer to the specific exchange documentation.

*   **no-wait** – bit

*   **arguments** –

table

A set of arguments for the binding. The syntax and semantics of these arguments depends on the exchange class.

exchange_declare(_exchange_, _type_, _passive=False_, _durable=False_, _auto\_delete=True_, _nowait=False_, _arguments=None_, _argsig='BssbbbbbF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.exchange_declare "Link to this definition")
Declare exchange, create if needed.

This method creates an exchange if it does not already exist, and if the exchange exists, verifies that it is of the correct and expected class.

RULE:

> The server SHOULD support a minimum of 16 exchanges per virtual host and ideally, impose no limit except as defined by available resources.

Parameters:
*   **exchange** –

shortstr

RULE:

> Exchange names starting with “amq.” are reserved for predeclared and standardised exchanges. If the client attempts to create an exchange starting with “amq.”, the server MUST raise a channel exception with reply code 403 (access refused).

*   **type** –

shortstr

exchange type

Each exchange belongs to one of a set of exchange types implemented by the server. The exchange types define the functionality of the exchange - i.e. how messages are routed through it. It is not valid or meaningful to attempt to change the type of an existing exchange.

RULE:

> If the exchange already exists with a different type, the server MUST raise a connection exception with a reply code 507 (not allowed).

RULE:

> If the server does not support the requested exchange type it MUST raise a connection exception with a reply code 503 (command invalid).

*   **passive** –

boolean

do not create exchange

If set, the server will not create the exchange. The client can use this to check whether an exchange exists without modifying the server state.

RULE:

> If set, and the exchange does not already exist, the server MUST raise a channel exception with reply code 404 (not found).

*   **durable** –

boolean

request a durable exchange

If set when creating a new exchange, the exchange will be marked as durable. Durable exchanges remain active when a server restarts. Non-durable exchanges (transient exchanges) are purged if/when a server restarts.

RULE:

> The server MUST support both durable and transient exchanges.

RULE:

> The server MUST ignore the durable field if the exchange already exists.

*   **auto_delete** –

boolean

auto-delete when unused

If set, the exchange is deleted when all queues have finished using it.

RULE:

> The server SHOULD allow for a reasonable delay between the point when it determines that an exchange is not being used (or no longer used), and the point when it deletes the exchange. At the least it must allow a client to create an exchange and then bind a queue to it, with a small but non-zero delay between these two actions.

RULE:

> The server MUST ignore the auto-delete field if the exchange already exists.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

*   **arguments** –

table

arguments for declaration

A set of arguments for the declaration. The syntax and semantics of these arguments depends on the server implementation. This field is ignored if passive is True.

exchange_delete(_exchange_, _if\_unused=False_, _nowait=False_, _argsig='Bsbb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.exchange_delete "Link to this definition")
Delete an exchange.

This method deletes an exchange. When an exchange is deleted all queue bindings on the exchange are cancelled.

Parameters:
*   **exchange** –

shortstr

RULE:

> The exchange MUST exist. Attempting to delete a non-existing exchange causes a channel exception.

*   **if_unused** –

boolean

delete only if unused

If set, the server will only delete the exchange if it has no queue bindings. If the exchange has queue bindings the server does not delete it but raises a channel exception instead.

RULE:

> If set, the server SHOULD delete the exchange but only if it has no queue bindings.

RULE:

> If set, the server SHOULD raise a channel exception if the exchange is in use.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

exchange_unbind(_destination_, _source=''_, _routing\_key=''_, _nowait=False_, _arguments=None_, _argsig='BsssbF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.exchange_unbind "Link to this definition")
Unbind an exchange from an exchange.

RULE:

> If a unbind fails, the server MUST raise a connection exception.

Parameters:
*   **reserved-1** – short

*   **destination** –

shortstr

Specifies the name of the destination exchange to unbind.

RULE:

> The client MUST NOT attempt to unbind an exchange that does not exist from an exchange.

RULE:

> The server MUST accept a blank exchange name to mean the default exchange.

*   **source** –

shortstr

Specifies the name of the source exchange to unbind.

RULE:

> The client MUST NOT attempt to unbind an exchange from an exchange that does not exist.

RULE:

> The server MUST accept a blank exchange name to mean the default exchange.

*   **routing-key** –

shortstr

Specifies the routing key of the binding to unbind.

*   **no-wait** – bit

*   **arguments** –

table

Specifies the arguments of the binding to unbind.

flow(_active_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.flow "Link to this definition")
Enable/disable flow from peer.

This method asks the peer to pause or restart the flow of content data. This is a simple flow-control mechanism that a peer can use to avoid overflowing its queues or otherwise finding itself receiving more messages than it can process. Note that this method is not intended for window control. The peer that receives a request to stop sending content should finish sending the current content, if any, and then wait until it receives a Flow restart method.

RULE:

> When a new channel is opened, it is active. Some applications assume that channels are inactive until started. To emulate this behaviour a client MAY open the channel, then pause it.

RULE:

> When sending content data in multiple frames, a peer SHOULD monitor the channel for incoming methods and respond to a Channel.Flow as rapidly as possible.

RULE:

> A peer MAY use the Channel.Flow method to throttle incoming content data for internal reasons, for example, when exchanging data over a slower connection.

RULE:

> The peer that requests a Channel.Flow method MAY disconnect and/or ban a peer that does not respect the request.

Parameters:
**active** –

boolean

start/stop content frames

If True, the peer starts sending content frames. If False, the peer stops sending content frames.

get_bindings()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.get_bindings "Link to this definition")is_closing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.is_closing "Link to this definition")message_to_python(_raw\_message_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.message_to_python "Link to this definition")
Convert encoded message body back to a Python value.

method_queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.method_queue "Link to this definition")no_ack_consumers _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.no_ack_consumers "Link to this definition")open()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.open "Link to this definition")
Open a channel for use.

This method opens a virtual connection (a channel).

RULE:

> This method MUST NOT be called when the channel is already open.

Parameters:
**out_of_band** –

shortstr (DEPRECATED)

out-of-band settings

Configures out-of-band transfers on this channel. The syntax and meaning of this field will be formally defined at a later date.

prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_, _\_Message=<class'amqp.basic\_message.Message'>_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.prepare_message "Link to this definition")
Prepare message so that it can be sent using this transport.

prepare_queue_arguments(_arguments_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.prepare_queue_arguments "Link to this definition")queue_bind(_queue_, _exchange=''_, _routing\_key=''_, _nowait=False_, _arguments=None_, _argsig='BsssbF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.queue_bind "Link to this definition")
Bind queue to an exchange.

This method binds a queue to an exchange. Until a queue is bound it will not receive any messages. In a classic messaging model, store-and-forward queues are bound to a dest exchange and subscription queues are bound to a dest_wild exchange.

RULE:

> A server MUST allow ignore duplicate bindings - that is, two or more bind methods for a specific queue, with identical arguments - without treating these as an error.

RULE:

> If a bind fails, the server MUST raise a connection exception.

RULE:

> The server MUST NOT allow a durable queue to bind to a transient exchange. If the client attempts this the server MUST raise a channel exception.

RULE:

> Bindings for durable queues are automatically durable and the server SHOULD restore such bindings after a server restart.

RULE:

> The server SHOULD support at least 4 bindings per queue, and ideally, impose no limit except as defined by available resources.

Parameters:
*   **queue** –

shortstr

Specifies the name of the queue to bind. If the queue name is empty, refers to the current queue for the channel, which is the last declared queue.

RULE:

> If the client did not previously declare a queue, and the queue name in this method is empty, the server MUST raise a connection exception with reply code 530 (not allowed).

RULE:

> If the queue does not exist the server MUST raise a channel exception with reply code 404 (not found).

*   **exchange** –

shortstr

The name of the exchange to bind to.

RULE:

> If the exchange does not exist the server MUST raise a channel exception with reply code 404 (not found).

*   **routing_key** –

shortstr

message routing key

Specifies the routing key for the binding. The routing key is used for routing messages depending on the exchange configuration. Not all exchanges use a routing key - refer to the specific exchange documentation. If the routing key is empty and the queue name is empty, the routing key will be the current queue for the channel, which is the last declared queue.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

*   **arguments** –

table

arguments for binding

A set of arguments for the binding. The syntax and semantics of these arguments depends on the exchange class.

queue_declare(_queue=''_, _passive=False_, _durable=False_, _exclusive=False_, _auto\_delete=True_, _nowait=False_, _arguments=None_, _argsig='BsbbbbbF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.queue_declare "Link to this definition")
Declare queue, create if needed.

This method creates or checks a queue. When creating a new queue the client can specify various properties that control the durability of the queue and its contents, and the level of sharing for the queue.

RULE:

> The server MUST create a default binding for a newly- created queue to the default exchange, which is an exchange of type ‘direct’.

RULE:

> The server SHOULD support a minimum of 256 queues per virtual host and ideally, impose no limit except as defined by available resources.

Parameters:
*   **queue** –

shortstr

RULE:

> The queue name MAY be empty, in which case the server MUST create a new queue with a unique generated name and return this to the client in the Declare-Ok method.

RULE:

> Queue names starting with “amq.” are reserved for predeclared and standardised server queues. If the queue name starts with “amq.” and the passive option is False, the server MUST raise a connection exception with reply code 403 (access refused).

*   **passive** –

boolean

do not create queue

If set, the server will not create the queue. The client can use this to check whether a queue exists without modifying the server state.

RULE:

> If set, and the queue does not already exist, the server MUST respond with a reply code 404 (not found) and raise a channel exception.

*   **durable** –

boolean

request a durable queue

If set when creating a new queue, the queue will be marked as durable. Durable queues remain active when a server restarts. Non-durable queues (transient queues) are purged if/when a server restarts. Note that durable queues do not necessarily hold persistent messages, although it does not make sense to send persistent messages to a transient queue.

RULE:

> The server MUST recreate the durable queue after a restart.

RULE:

> The server MUST support both durable and transient queues.

RULE:

> The server MUST ignore the durable field if the queue already exists.

*   **exclusive** –

boolean

request an exclusive queue

Exclusive queues may only be consumed from by the current connection. Setting the ‘exclusive’ flag always implies ‘auto-delete’.

RULE:

> The server MUST support both exclusive (private) and non-exclusive (shared) queues.

RULE:

> The server MUST raise a channel exception if ‘exclusive’ is specified and the queue already exists and is owned by a different connection.

*   **auto_delete** –

boolean

auto-delete queue when unused

If set, the queue is deleted when all consumers have finished using it. Last consumer can be cancelled either explicitly or because its channel is closed. If there was no consumer ever on the queue, it won’t be deleted.

RULE:

> The server SHOULD allow for a reasonable delay between the point when it determines that a queue is not being used (or no longer used), and the point when it deletes the queue. At the least it must allow a client to create a queue and then create a consumer to read from it, with a small but non-zero delay between these two actions. The server should equally allow for clients that may be disconnected prematurely, and wish to re- consume from the same queue without losing messages. We would recommend a configurable timeout, with a suitable default value being one minute.

RULE:

> The server MUST ignore the auto-delete field if the queue already exists.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

*   **arguments** –

table

arguments for declaration

A set of arguments for the declaration. The syntax and semantics of these arguments depends on the server implementation. This field is ignored if passive is True.

Returns a tuple containing 3 items:
the name of the queue (essential for automatically-named queues), message count and consumer count

queue_delete(_queue=''_, _if\_unused=False_, _if\_empty=False_, _nowait=False_, _argsig='Bsbbb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.queue_delete "Link to this definition")
Delete a queue.

This method deletes a queue. When a queue is deleted any pending messages are sent to a dead-letter queue if this is defined in the server configuration, and all consumers on the queue are cancelled.

RULE:

> The server SHOULD use a dead-letter queue to hold messages that were pending on a deleted queue, and MAY provide facilities for a system administrator to move these messages back to an active queue.

Parameters:
*   **queue** –

shortstr

Specifies the name of the queue to delete. If the queue name is empty, refers to the current queue for the channel, which is the last declared queue.

RULE:

> If the client did not previously declare a queue, and the queue name in this method is empty, the server MUST raise a connection exception with reply code 530 (not allowed).

RULE:

> The queue must exist. Attempting to delete a non- existing queue causes a channel exception.

*   **if_unused** –

boolean

delete only if unused

If set, the server will only delete the queue if it has no consumers. If the queue has consumers the server does does not delete it but raises a channel exception instead.

RULE:

> The server MUST respect the if-unused flag when deleting a queue.

*   **if_empty** –

boolean

delete only if empty

If set, the server will only delete the queue if it has no messages. If the queue is not empty the server raises a channel exception.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

If nowait is False, returns the number of deleted messages.

queue_purge(_queue=''_, _nowait=False_, _argsig='Bsb'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.queue_purge "Link to this definition")
Purge a queue.

This method removes all messages from a queue. It does not cancel consumers. Purged messages are deleted without any formal “undo” mechanism.

RULE:

> A call to purge MUST result in an empty queue.

RULE:

> On transacted channels the server MUST not purge messages that have already been sent to a client but not yet acknowledged.

RULE:

> The server MAY implement a purge queue or log that allows system administrators to recover accidentally-purged messages. The server SHOULD NOT keep purged messages in the same storage spaces as the live messages since the volumes of purged messages may get very large.

Parameters:
*   **queue** –

shortstr

Specifies the name of the queue to purge. If the queue name is empty, refers to the current queue for the channel, which is the last declared queue.

RULE:

> If the client did not previously declare a queue, and the queue name in this method is empty, the server MUST raise a connection exception with reply code 530 (not allowed).

RULE:

> The queue must exist. Attempting to purge a non- existing queue causes a channel exception.

*   **nowait** –

boolean

do not send a reply method

If set, the server will not respond to the method. The client should not wait for a reply method. If the server could not complete the method it will raise a channel or connection exception.

If nowait is False, returns a number of purged messages.

queue_unbind(_queue_, _exchange_, _routing\_key=''_, _nowait=False_, _arguments=None_, _argsig='BsssF'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.queue_unbind "Link to this definition")
Unbind a queue from an exchange.

This method unbinds a queue from an exchange.

RULE:

> If a unbind fails, the server MUST raise a connection exception.

Parameters:
*   **queue** –

shortstr

Specifies the name of the queue to unbind.

RULE:

> The client MUST either specify a queue name or have previously declared a queue on the same channel

RULE:

> The client MUST NOT attempt to unbind a queue that does not exist.

*   **exchange** –

shortstr

The name of the exchange to unbind from.

RULE:

> The client MUST NOT attempt to unbind a queue from an exchange that does not exist.

RULE:

> The server MUST accept a blank exchange name to mean the default exchange.

*   **routing_key** –

shortstr

routing key of binding

Specifies the routing key of the binding to unbind.

*   **arguments** –

table

arguments of binding

Specifies the arguments of the binding to unbind.

send_method(_sig_, _format=None_, _args=None_, _content=None_, _wait=None_, _callback=None_, _returns\_tuple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.send_method "Link to this definition")then(_on\_success_, _on\_error=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.then "Link to this definition")tx_commit()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.tx_commit "Link to this definition")
Commit the current transaction.

This method commits all messages published and acknowledged in the current transaction. A new transaction starts immediately after a commit.

tx_rollback()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.tx_rollback "Link to this definition")
Abandon the current transaction.

This method abandons all messages published and acknowledged in the current transaction. A new transaction starts immediately after a rollback.

tx_select()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.tx_select "Link to this definition")
Select standard transaction mode.

This method sets the channel to use standard transactions. The client must use this method at least once on a channel before using the Commit or Rollback methods.

wait(_method_, _callback=None_, _timeout=None_, _returns\_tuple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Channel.wait "Link to this definition")Transport(_host_, _connect\_timeout_, _ssl=False_, _read\_timeout=None_, _write\_timeout=None_, _socket\_settings=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.Transport "Link to this definition")auto_decode[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.auto_decode "Link to this definition")blocking_read(_timeout=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.blocking_read)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.blocking_read "Link to this definition")bytes_recv _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.bytes_recv "Link to this definition")
Number of successful reads from socket.

bytes_sent _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.bytes_sent "Link to this definition")
Number of successful writes to socket.

channel(_channel\_id=None_, _callback=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.channel "Link to this definition")
Create new channel.

Fetch a Channel object identified by the numeric channel_id, or create that object if it doesn’t already exist.

channel_errors _=(<class'amqp.exceptions.ChannelError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.channel_errors "Link to this definition")channel_id[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.channel_id "Link to this definition")client_heartbeat _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.client_heartbeat "Link to this definition")
Original heartbeat interval value proposed by client.

close(_reply\_code=0_, _reply\_text=''_, _method\_sig=(0,0)_, _argsig='BsBB'_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.close "Link to this definition")
Request a connection close.

This method indicates that the sender wants to close the connection. This may be due to internal conditions (e.g. a forced shut-down) or due to an error handling a specific method, i.e. an exception. When a close is due to an exception, the sender provides the class and method id of the method which caused the exception.

RULE:

> After sending this method any received method except the Close-OK method MUST be discarded.

RULE:

> The peer sending this method MAY use a counter or timeout to detect failure of the other peer to respond correctly with the Close-OK method.

RULE:

> When a server receives the Close method from a client it MUST delete all server-side resources associated with the client’s context. A client CANNOT reconnect to a context after sending or receiving a Close method.

Parameters:
*   **reply_code** –

short

The reply code. The AMQ reply codes are defined in AMQ RFC 011.

*   **reply_text** –

shortstr

The localised reply text. This text can be logged as an aid to resolving issues.

*   **class_id** –

short

failing method class

When the close is provoked by a method exception, this is the class of the method.

*   **method_id** –

short

failing method ID

When the close is provoked by a method exception, this is the ID of the method.

collect()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.collect)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.collect "Link to this definition")connect(_callback=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.connect)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.connect "Link to this definition")_property_ connected[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.connected "Link to this definition")connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.connection "Link to this definition")connection_errors _=(<class'amqp.exceptions.ConnectionError'>,<class'OSError'>,<class'OSError'>,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.connection_errors "Link to this definition")dispatch_method(_method\_sig_, _payload_, _content_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.dispatch_method "Link to this definition")drain_events(_timeout=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.drain_events "Link to this definition")_property_ frame_writer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.frame_writer "Link to this definition")heartbeat _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.heartbeat "Link to this definition")
Final heartbeat interval value (in float seconds) after negotiation

heartbeat_tick(_rate=2_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.heartbeat_tick)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.heartbeat_tick "Link to this definition")
Send heartbeat packets if necessary.

Raises:
**ConnectionForvced** – if none have been received recently.

Note

This should be called frequently, on the order of once per second.

Keyword Arguments:
**rate** ([_int_](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")) – Number of heartbeat frames to send during the heartbeat timeout

is_alive()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.is_alive)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.is_alive "Link to this definition")is_closing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.is_closing "Link to this definition")last_heartbeat_received _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.last_heartbeat_received "Link to this definition")
Time of last heartbeat received (in monotonic time, if available).

last_heartbeat_sent _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.last_heartbeat_sent "Link to this definition")
Time of last heartbeat sent (in monotonic time, if available).

library_properties _={'product':'py-amqp','product\_version':'5.3.1'}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.library_properties "Link to this definition")
These are sent to the server to announce what features we support, type of client etc.

method_queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.method_queue "Link to this definition")negotiate_capabilities _={'authentication\_failure\_close':True,'connection.blocked':True,'consumer\_cancel\_notify':True}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.negotiate_capabilities "Link to this definition")
Mapping of protocol extensions to enable. The server will report these in server_properties[capabilities], and if a key in this map is present the client will tell the server to either enable or disable the capability depending on the value set in this map. For example with:

> negotiate_capabilities = {
> ‘consumer_cancel_notify’: True,
> 
> 
> }

The client will enable this capability if the server reports support for it, but if the value is False the client will disable the capability.

_property_ on_inbound_frame[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.on_inbound_frame "Link to this definition")on_inbound_method(_channel\_id_, _method\_sig_, _payload_, _content_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.on_inbound_method)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.on_inbound_method "Link to this definition")prev_recv _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.prev_recv "Link to this definition")
Number of bytes received from socket at the last heartbeat check.

prev_sent _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.prev_sent "Link to this definition")
Number of bytes sent to socket at the last heartbeat check.

recoverable_channel_errors _=(<class'amqp.exceptions.RecoverableChannelError'>,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.recoverable_channel_errors "Link to this definition")recoverable_connection_errors _=(<class'amqp.exceptions.RecoverableConnectionError'>,<class'amqp.exceptions.MessageNacked'>,<class'OSError'>,<class'OSError'>,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.recoverable_connection_errors "Link to this definition")send_heartbeat()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.send_heartbeat)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.send_heartbeat "Link to this definition")send_method(_sig_, _format=None_, _args=None_, _content=None_, _wait=None_, _callback=None_, _returns\_tuple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.send_method "Link to this definition")_property_ server_capabilities[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.server_capabilities "Link to this definition")server_heartbeat _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.server_heartbeat "Link to this definition")
Original heartbeat interval proposed by server.

_property_ sock[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.sock "Link to this definition")then(_on\_success_, _on\_error=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/amqp/connection.html#Connection.then)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.then "Link to this definition")_property_ transport[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.transport "Link to this definition")wait(_method_, _callback=None_, _timeout=None_, _returns\_tuple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Connection.wait "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#channel "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.pyamqp.Channel(_connection_, _channel\_id=None_, _auto\_decode=True_, _on\_open=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel "Link to this definition")
AMQP Channel.

_class_ Message(_msg_, _channel=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message "Link to this definition")
AMQP Message.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.Message.properties "Link to this definition")auto_decode[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.auto_decode "Link to this definition")channel_id[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.channel_id "Link to this definition")connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.connection "Link to this definition")is_closing[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.is_closing "Link to this definition")message_to_python(_raw\_message_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Channel.message_to_python)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.message_to_python "Link to this definition")
Convert encoded message body back to a Python value.

method_queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.method_queue "Link to this definition")prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_, _\_Message=<class'amqp.basic\_message.Message'>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Channel.prepare_message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.prepare_message "Link to this definition")
Prepare message so that it can be sent using this transport.

prepare_queue_arguments(_arguments_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Channel.prepare_queue_arguments)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Channel.prepare_queue_arguments "Link to this definition")
[Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#id8)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#message "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.pyamqp.Message(_msg_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/pyamqp.html#Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message "Link to this definition")
AMQP Message.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.pyamqp.html#kombu.transport.pyamqp.Message.properties "Link to this definition")

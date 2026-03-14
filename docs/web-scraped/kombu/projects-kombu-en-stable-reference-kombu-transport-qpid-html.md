# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html

Title: Apache QPid Transport - kombu.transport.qpid — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.qpid.html).

Qpid Transport module for kombu.

[Qpid](https://qpid.apache.org/) transport using [qpid-python](https://pypi.org/project/qpid-python/) as the client and [qpid-tools](https://pypi.org/project/qpid-tools/) for broker management.

The use this transport you must install the necessary dependencies. These dependencies are available via PyPI and can be installed using the pip command:

$ pip install kombu[qpid]

or to install the requirements manually:

$ pip install qpid-tools qpid-python

Python 3 and PyPy Limitations

The Qpid transport does not support Python 3 or PyPy environments due to underlying dependencies not being compatible. This version is tested and works with with Python 2.7.

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Native

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: Yes

*   Supports Priority: Yes

*   Supports TTL: Yes

[Authentication](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#authentication "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This transport supports SASL authentication with the Qpid broker. Normally, SASL mechanisms are negotiated from a client list and a server list of possible mechanisms, but in practice, different SASL client libraries give different behaviors. These different behaviors cause the expected SASL mechanism to not be selected in many cases. As such, this transport restricts the mechanism types based on Kombu’s configuration according to the following table.

**Broker String****SASL Mechanism**
qpid://hostname/ANONYMOUS
qpid://username:password@hostname/PLAIN
see instructions below EXTERNAL

The user can override the above SASL selection behaviors and specify the SASL string using the [`login_method`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection.login_method "kombu.Connection.login_method") argument to the [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") object. The string can be a single SASL mechanism or a space separated list of SASL mechanisms. If you are using Celery with Kombu, this can be accomplished by setting the _BROKER\_LOGIN\_METHOD_ Celery option.

Note

While using SSL, Qpid users may want to override the SASL mechanism to use _EXTERNAL_. In that case, Qpid requires a username to be presented that matches the _CN_ of the SSL client certificate. Ensure that the broker string contains the corresponding username. For example, if the client certificate has _CN=asdf_ and the client connects to _example.com_ on port 5671, the broker string should be:

> **qpid://asdf@example.com:5671/**

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#transport-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `transport_options` argument to the [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") object are passed directly to the `qpid.messaging.endpoints.Connection` as keyword arguments. These options override and replace any other default or specified values. If using Celery, this can be accomplished by setting the _BROKER\_TRANSPORT\_OPTIONS_ Celery option.

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#features)

*   [Authentication](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#authentication)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#transport)

*   [Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#connection)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#channel)

*   [Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#message)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.qpid.Transport(_*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "Link to this definition")
Kombu native transport for a Qpid broker.

Provide a native transport for Kombu that allows consumers and producers to read and write messages to/from a broker. This Transport is capable of supporting both synchronous and asynchronous reading. All writes are synchronous through the [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") objects that support this Transport.

Asynchronous reads are done using a call to [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"), which synchronously reads messages that were fetched asynchronously, and then handles them through calls to the callback handlers maintained on the [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object.

The Transport also provides methods to establish and close a connection to the broker. This Transport establishes a factory-like pattern that allows for singleton pattern to consolidate all Connections into a single one.

The Transport can create [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") objects to communicate with the broker with using the [`create_channel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.create_channel "kombu.transport.qpid.Transport.create_channel") method.

The Transport identifies recoverable connection errors and recoverable channel errors according to the Kombu 3.0 interface. These exception are listed as tuples and store in the Transport class attribute recoverable_connection_errors and recoverable_channel_errors respectively. Any exception raised that is not a member of one of these tuples is considered non-recoverable. This allows Kombu support for automatic retry of certain operations to function correctly.

For backwards compatibility to the pre Kombu 3.0 exception interface, the recoverable errors are also listed as connection_errors and channel_errors.

_class_ Connection(_**connection\_options_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection "Link to this definition")
Qpid Connection.

Encapsulate a connection object for the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport").

Parameters:
*   **host** – The host that connections should connect to.

*   **port** – The port that connection should connect to.

*   **username** – The username that connections should connect with. Optional.

*   **password** – The password that connections should connect with. Optional but requires a username.

*   **transport** – The transport type that connections should use. Either ‘tcp’, or ‘ssl’ are expected as values.

*   **timeout** – the timeout used when a Connection connects to the broker.

*   **sasl_mechanisms** – The sasl authentication mechanism type to use. refer to SASL documentation for an explanation of valid values.

Note

qpid.messaging has an AuthenticationFailure exception type, but instead raises a ConnectionError with a message that indicates an authentication failure occurred in those situations. ConnectionError is listed as a recoverable error type, so kombu will attempt to retry if a ConnectionError is raised. Retrying the operation without adjusting the credentials is not correct, so this method specifically checks for a ConnectionError that indicates an Authentication Failure occurred. In those situations, the error type is mutated while preserving the original message and raised so kombu will allow the exception to not be considered recoverable.

A connection object is created by a [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") during a call to [`establish_connection()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.establish_connection "kombu.transport.qpid.Transport.establish_connection"). The [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") passes in connection options as keywords that should be used for any connections created. Each [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") creates exactly one Connection.

A Connection object maintains a reference to a `Connection` which can be accessed through a bound getter method named [`get_qpid_connection()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.get_qpid_connection "kombu.transport.qpid.Transport.Connection.get_qpid_connection") method. Each Channel uses a the Connection for each `BrokerAgent`, and the Transport maintains a session for all senders and receivers.

The Connection object is also responsible for maintaining the dictionary of references to callbacks that should be called when messages are received. These callbacks are saved in _callbacks, and keyed on the queue name associated with the received message. The _callbacks are setup in [`Channel.basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume"), removed in [`Channel.basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_cancel "kombu.transport.qpid.Channel.basic_cancel"), and called in [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events").

The following keys are expected to be passed in as keyword arguments at a minimum:

All keyword arguments are collected into the connection_options dict and passed directly through to `qpid.messaging.endpoints.Connection.establish()`.

_class_ Channel(_connection_, _transport_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel "Link to this definition")
Supports broker configuration and messaging send and receive.

Parameters:
*   **connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – A Connection object that this Channel can reference. Currently only used to access callbacks.

*   **transport** ([_kombu.transport.qpid.Transport_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport")) – The Transport this Channel is associated with.

A channel object is designed to have method-parity with a Channel as defined in AMQP 0-10 and earlier, which allows for the following broker actions:

> *   exchange declare and delete
> 
> *   queue declare and delete
> 
> *   queue bind and unbind operations
> 
> *   queue length and purge operations
> 
> *   sending/receiving/rejecting messages
> 
> *   structuring, encoding, and decoding messages
> 
> *   supports synchronous and asynchronous reads
> 
> *   reading state about the exchange, queues, and bindings

Channels are designed to all share a single TCP connection with a broker, but provide a level of isolated communication with the broker while benefiting from a shared TCP connection. The Channel is given its [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object by the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") that instantiates the channel.

This channel inherits from `StdChannel`, which makes this a ‘native’ channel versus a ‘virtual’ channel which would inherit from `kombu.transports.virtual`.

Messages sent using this channel are assigned a delivery_tag. The delivery_tag is generated for a message as they are prepared for sending by [`basic_publish()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_publish "kombu.transport.qpid.Transport.Connection.Channel.basic_publish"). The delivery_tag is unique per channel instance. The delivery_tag has no meaningful context in other objects, and is only maintained in the memory of this object, and the underlying [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object that provides support.

Each channel object instantiates exactly one [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object for prefetch limiting, and asynchronous ACKing. The [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is lazily instantiated through a property method [`qos()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.qos "kombu.transport.qpid.Transport.Connection.Channel.qos"). The [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is a supporting object that should not be accessed directly except by the channel itself.

Synchronous reads on a queue are done using a call to [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_get "kombu.transport.qpid.Transport.Connection.Channel.basic_get") which uses `_get()` to perform the reading. These methods read immediately and do not accept any form of timeout. [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_get "kombu.transport.qpid.Transport.Connection.Channel.basic_get") reads synchronously and ACKs messages before returning them. ACKing is done in all cases, because an application that reads messages using qpid.messaging, but does not ACK them will experience a memory leak. The no_ack argument to [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_get "kombu.transport.qpid.Transport.Connection.Channel.basic_get") does not affect ACKing functionality.

Asynchronous reads on a queue are done by starting a consumer using [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume"). Each call to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume") will cause a `Receiver` to be created on the `Session` started by the :class: Transport. The receiver will asynchronously read using qpid.messaging, and prefetch messages before the call to `Transport.basic_drain()` occurs. The prefetch_count value of the [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is the capacity value of the new receiver. The new receiver capacity must always be at least 1, otherwise none of the receivers will appear to be ready for reading, and will never be read from.

Each call to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume") creates a consumer, which is given a consumer tag that is identified by the caller of [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume"). Already started consumers can be cancelled using by their consumer_tag using [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_cancel "kombu.transport.qpid.Transport.Connection.Channel.basic_cancel"). Cancellation of a consumer causes the `Receiver` object to be closed.

Asynchronous message ACKing is supported through [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_ack "kombu.transport.qpid.Transport.Connection.Channel.basic_ack"), and is referenced by delivery_tag. The Channel object uses its [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object to perform the message ACKing.

_class_ Message(_payload_, _channel=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message "Link to this definition")
Message object.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.properties "Link to this definition")serializable()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.Message.serializable "Link to this definition")_class_ QoS(_session_, _prefetch\_count=1_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS "Link to this definition")
A helper object for message prefetch and ACKing purposes.

Keyword Arguments:
**prefetch_count** – Initial prefetch count, hard set to 1.

NOTE: prefetch_count is currently hard set to 1, and needs to be improved

This object is instantiated 1-for-1 with a [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") instance. QoS allows `prefetch_count` to be set to the number of outstanding messages the corresponding [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") should be allowed to prefetch. Setting `prefetch_count` to 0 disables prefetch limits, and the object can hold an arbitrary number of messages.

Messages are added using [`append()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.append "kombu.transport.qpid.Transport.Connection.Channel.QoS.append"), which are held until they are ACKed asynchronously through a call to [`ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.ack "kombu.transport.qpid.Transport.Connection.Channel.QoS.ack"). Messages that are received, but not ACKed will not be delivered by the broker to another consumer until an ACK is received, or the session is closed. Messages are referred to using delivery_tag, which are unique per [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel"). Delivery tags are managed outside of this object and are passed in with a message to [`append()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.append "kombu.transport.qpid.Transport.Connection.Channel.QoS.append"). Un-ACKed messages can be looked up from QoS using [`get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.get "kombu.transport.qpid.Transport.Connection.Channel.QoS.get") and can be rejected and forgotten using [`reject()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.reject "kombu.transport.qpid.Transport.Connection.Channel.QoS.reject").

ack(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.ack "Link to this definition")
Acknowledge a message by delivery_tag.

Called asynchronously once the message has been handled and can be forgotten by the broker.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – the delivery tag associated with the message to be acknowledged.

append(_message_, _delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.append "Link to this definition")
Append message to the list of un-ACKed messages.

Add a message, referenced by the delivery_tag, for ACKing, rejecting, or getting later. Messages are saved into a dict by delivery_tag.

Parameters:
*   **message** (_qpid.messaging.Message_) – A received message that has not yet been ACKed.

*   **delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – A UUID to refer to this message by upon receipt.

can_consume()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.can_consume "Link to this definition")
Return True if the [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") can consume more messages.

Used to ensure the client adheres to currently active prefetch limits.

Returns:
True, if this QoS object can accept more messages without violating the prefetch_count. If prefetch_count is 0, can_consume will always return True.

Return type:
[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")

can_consume_max_estimate()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.can_consume_max_estimate "Link to this definition")
Return the remaining message capacity.

Returns an estimated number of outstanding messages that a [`kombu.transport.qpid.Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") can accept without exceeding `prefetch_count`. If `prefetch_count` is 0, then this method returns 1.

Returns:
The number of estimated messages that can be fetched without violating the prefetch_count.

Return type:
[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")

get(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.get "Link to this definition")
Get an un-ACKed message by delivery_tag.

If called with an invalid delivery_tag a [`KeyError`](https://docs.python.org/dev/library/exceptions.html#KeyError "(in Python v3.15)") is raised.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be returned.

Returns:
An un-ACKed message that is looked up by delivery_tag.

Return type:
qpid.messaging.Message

reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.QoS.reject "Link to this definition")
Reject a message by delivery_tag.

Explicitly notify the broker that the channel associated with this QoS object is rejecting the message that was previously delivered.

If requeue is False, then the message is not requeued for delivery to another consumer. If requeue is True, then the message is requeued for delivery to another consumer.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be rejected.

Keyword Arguments:
**requeue** – If True, the broker will be notified to requeue the message. If False, the broker will be told to drop the message entirely. In both cases, the message will be removed from this object.

basic_ack(_delivery\_tag_, _multiple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_ack "Link to this definition")
Acknowledge a message by delivery_tag.

Acknowledges a message referenced by delivery_tag. Messages can only be ACKed using [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_ack "kombu.transport.qpid.Transport.Connection.Channel.basic_ack") if they were acquired using [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume"). This is the ACKing portion of the asynchronous read behavior.

Internally, this method uses the [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object, which stores messages and is responsible for the ACKing.

Parameters:
*   **delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be acknowledged.

*   **multiple** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – not implemented. If set to True an AssertionError is raised.

basic_cancel(_consumer\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

Request the consumer stops reading messages from its queue. The consumer is a `Receiver`, and it is closed using `close()`.

This method also cleans up all lingering references of the consumer.

Parameters:
**consumer_tag** (_an immutable object_) – The tag which refers to the consumer to be cancelled. Originally specified when the consumer was created as a parameter to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume").

basic_consume(_queue_, _no\_ack_, _callback_, _consumer\_tag_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "Link to this definition")
Start an asynchronous consumer that reads from a queue.

This method starts a consumer of type `Receiver` using the `Session` created and referenced by the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") that reads messages from a queue specified by name until stopped by a call to [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_cancel "kombu.transport.qpid.Transport.Connection.Channel.basic_cancel").

Messages are available later through a synchronous call to [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"), which will drain from the consumer started by this method. [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is synchronous, but the receiving of messages over the network occurs asynchronously, so it should still perform well. [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") calls the callback provided here with the Message of type self.Message.

Each consumer is referenced by a consumer_tag, which is provided by the caller of this method.

This method sets up the callback onto the self.connection object in a dict keyed by queue name. [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is responsible for calling that callback upon message receipt.

All messages that are received are added to the QoS object to be saved for asynchronous ACKing later after the message has been handled by the caller of [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"). Messages can be ACKed after being received through a call to [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_ack "kombu.transport.qpid.Transport.Connection.Channel.basic_ack").

If no_ack is True, The no_ack flag indicates that the receiver of the message will not call [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_ack "kombu.transport.qpid.Transport.Connection.Channel.basic_ack") later. Since the message will not be ACKed later, it is ACKed immediately.

[`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_consume "kombu.transport.qpid.Transport.Connection.Channel.basic_consume") transforms the message object type prior to calling the callback. Initially the message comes in as a `qpid.messaging.Message`. This method unpacks the payload of the `qpid.messaging.Message` and creates a new object of type self.Message.

This method wraps the user delivered callback in a runtime-built function which provides the type transformation from `qpid.messaging.Message` to [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message"), and adds the message to the associated [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object for asynchronous ACKing if necessary.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to consume messages from

*   **no_ack** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, then messages will not be saved for ACKing later, but will be ACKed immediately. If False, then messages will be saved for ACKing later with a call to [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_ack "kombu.transport.qpid.Transport.Connection.Channel.basic_ack").

*   **callback** (_a callable object_) – a callable that will be called when messages arrive on the queue.

*   **consumer_tag** (_an immutable object_) – a tag to reference the created consumer by. This consumer_tag is needed to cancel the consumer.

basic_get(_queue_, _no\_ack=False_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_get "Link to this definition")
Non-blocking single message get and ACK from a queue by name.

Internally this method uses `_get()` to fetch the message. If an `Empty` exception is raised by `_get()`, this method silences it and returns None. If `_get()` does return a message, that message is ACKed. The no_ack parameter has no effect on ACKing behavior, and all messages are ACKed in all cases. This method never adds fetched Messages to the internal QoS object for asynchronous ACKing.

This method converts the object type of the method as it passes through. Fetching from the broker, `_get()` returns a `qpid.messaging.Message`, but this method takes the payload of the `qpid.messaging.Message` and instantiates a [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message") object with the payload based on the class setting of self.Message.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The queue name to fetch a message from.

Keyword Arguments:
**no_ack** – The no_ack parameter has no effect on the ACK behavior of this method. Un-ACKed messages create a memory leak in qpid.messaging, and need to be ACKed in all cases.

Returns:
The received message.

Return type:
[`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message")

basic_publish(_message_, _exchange_, _routing\_key_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_publish "Link to this definition")
Publish message onto an exchange using a routing key.

Publish a message onto an exchange specified by name using a routing key specified by routing_key. Prepares the message in the following ways before sending:

*   encodes the body using [`encode_body()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.encode_body "kombu.transport.qpid.Transport.Connection.Channel.encode_body")

*   wraps the body as a buffer object, so that
`qpid.messaging.endpoints.Sender` uses a content type that can support arbitrarily large messages.

*   sets delivery_tag to a random uuid.UUID

*   sets the exchange and routing_key info as delivery_info

Internally uses `_put()` to send the message synchronously. This message is typically called by `kombu.messaging.Producer._publish` as the final step in message publication.

Parameters:
*   **message** ([_dict_](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")) – A dict containing key value pairs with the message data. A valid message dict can be generated using the [`prepare_message()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.prepare_message "kombu.transport.qpid.Transport.Connection.Channel.prepare_message") method.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange to submit this message onto.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The routing key to be used as the message is submitted onto the exchange.

basic_qos(_prefetch\_count_, _*args_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_qos "Link to this definition")
Change [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") settings for this Channel.

Set the number of un-acknowledged messages this Channel can fetch and hold. The prefetch_value is also used as the capacity for any new `Receiver` objects.

Currently, this value is hard coded to 1.

Parameters:
**prefetch_count** ([_int_](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")) – Not used. This method is hard-coded to 1.

basic_reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_reject "Link to this definition")
Reject a message by delivery_tag.

Rejects a message that has been received by the Channel, but not yet acknowledged. Messages are referenced by their delivery_tag.

If requeue is False, the rejected message will be dropped by the broker and not delivered to any other consumers. If requeue is True, then the rejected message will be requeued for delivery to another consumer, potentially to the same consumer who rejected the message previously.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be rejected.

Keyword Arguments:
**requeue** – If False, the rejected message will be dropped by the broker and not delivered to any other consumers. If True, then the rejected message will be requeued for delivery to another consumer, potentially to the same consumer who rejected the message previously.

body_encoding _='base64'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.body_encoding "Link to this definition")
Default body encoding. NOTE: `transport_options['body_encoding']` will override this value.

close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.close "Link to this definition")
Cancel all associated messages and close the Channel.

This cancels all consumers by calling [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.basic_cancel "kombu.transport.qpid.Transport.Connection.Channel.basic_cancel") for each known consumer_tag. It also closes the self._broker sessions. Closing the sessions implicitly causes all outstanding, un-ACKed messages to be considered undelivered by the broker.

codecs _={'base64':<kombu.transport.virtual.base.Base64 object>}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.codecs "Link to this definition")
Binary <-> ASCII codecs.

decode_body(_body_, _encoding=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.decode_body "Link to this definition")
Decode a body using an optionally specified encoding.

The encoding can be specified by name, and is looked up in self.codecs. self.codecs uses strings as its keys which specify the name of the encoding, and then the value is an instantiated object that can provide encoding/decoding of that type through encode and decode methods.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body to be encoded.

Keyword Arguments:
**encoding** – The encoding type to be used. Must be a supported codec listed in self.codecs.

Returns:
If encoding is specified, the decoded body is returned. If encoding is not specified, the body is returned unchanged.

Return type:
[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")

encode_body(_body_, _encoding=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.encode_body "Link to this definition")
Encode a body using an optionally specified encoding.

The encoding can be specified by name, and is looked up in self.codecs. self.codecs uses strings as its keys which specify the name of the encoding, and then the value is an instantiated object that can provide encoding/decoding of that type through encode and decode methods.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body to be encoded.

Keyword Arguments:
**encoding** – The encoding type to be used. Must be a supported codec listed in self.codecs.

Returns:
If encoding is specified, return a tuple with the first position being the encoded body, and the second position the encoding used. If encoding is not specified, the body is passed through unchanged.

Return type:
[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")

exchange_declare(_exchange=''_, _type='direct'_, _durable=False_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.exchange_declare "Link to this definition")
Create a new exchange.

Create an exchange of a specific type, and optionally have the exchange be durable. If an exchange of the requested name already exists, no action is taken and no exceptions are raised. Durable exchanges will survive a broker restart, non-durable exchanges will not.

Exchanges provide behaviors based on their type. The expected behaviors are those defined in the AMQP 0-10 and prior specifications including ‘direct’, ‘topic’, and ‘fanout’ functionality.

Keyword Arguments:
*   **type** – The exchange type. Valid values include ‘direct’, ‘topic’, and ‘fanout’.

*   **exchange** – The name of the exchange to be created. If no exchange is specified, then a blank string will be used as the name.

*   **durable** – True if the exchange should be durable, or False otherwise.

exchange_delete(_exchange\_name_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.exchange_delete "Link to this definition")
Delete an exchange specified by name.

Parameters:
**exchange_name** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange to be deleted.

prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.prepare_message "Link to this definition")
Prepare message data for sending.

This message is typically called by `kombu.messaging.Producer._publish()` as a preparation step in message publication.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body of the message

Keyword Arguments:
*   **priority** – A number between 0 and 9 that sets the priority of the message.

*   **content_type** – The content_type the message body should be treated as. If this is unset, the `qpid.messaging.endpoints.Sender` object tries to autodetect the content_type from the body.

*   **content_encoding** – The content_encoding the message body is encoded as.

*   **headers** – Additional Message headers that should be set. Passed in as a key-value pair.

*   **properties** – Message properties to be set on the message.

Returns:
Returns a dict object that encapsulates message attributes. See parameters for more details on attributes that can be set.

Return type:
[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")

_property_ qos[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.qos "Link to this definition")
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") manager for this channel.

Lazily instantiates an object of type [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") upon access to the self.qos attribute.

Returns:
An already existing, or newly created QoS object

Return type:
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS")

queue_bind(_queue_, _exchange_, _routing\_key_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.queue_bind "Link to this definition")
Bind a queue to an exchange with a bind key.

Bind a queue specified by name, to an exchange specified by name, with a specific bind key. The queue and exchange must already exist on the broker for the bind to complete successfully. Queues may be bound to exchanges multiple times with different keys.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be bound.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange that the queue should be bound to.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The bind key that the specified queue should bind to the specified exchange with.

queue_declare(_queue_, _passive=False_, _durable=False_, _exclusive=False_, _auto\_delete=True_, _nowait=False_, _arguments=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.queue_declare "Link to this definition")
Create a new queue specified by name.

If the queue already exists, no change is made to the queue, and the return value returns information about the existing queue.

The queue name is required and specified as the first argument.

If passive is True, the server will not create the queue. The client can use this to check whether a queue exists without modifying the server state. Default is False.

If durable is True, the queue will be durable. Durable queues remain active when a server restarts. Non-durable queues ( transient queues) are purged if/when a server restarts. Note that durable queues do not necessarily hold persistent messages, although it does not make sense to send persistent messages to a transient queue. Default is False.

If exclusive is True, the queue will be exclusive. Exclusive queues may only be consumed by the current connection. Setting the ‘exclusive’ flag always implies ‘auto-delete’. Default is False.

If auto_delete is True, the queue is deleted when all consumers have finished using it. The last consumer can be cancelled either explicitly or because its channel is closed. If there was no consumer ever on the queue, it won’t be deleted. Default is True.

The nowait parameter is unused. It was part of the 0-9-1 protocol, but this AMQP client implements 0-10 which removed the nowait option.

The arguments parameter is a set of arguments for the declaration of the queue. Arguments are passed as a dict or None. This field is ignored if passive is True. Default is None.

This method returns a `namedtuple` with the name ‘queue_declare_ok_t’ and the queue name as ‘queue’, message count on the queue as ‘message_count’, and the number of active consumers as ‘consumer_count’. The named tuple values are ordered as queue, message_count, and consumer_count respectively.

Due to Celery’s non-ACKing of events, a ring policy is set on any queue that starts with the string ‘celeryev’ or ends with the string ‘pidbox’. These are celery event queues, and Celery does not ack them, causing the messages to build-up. Eventually Qpid stops serving messages unless the ‘ring’ policy is set, at which point the buffer backing the queue becomes circular.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be created.

*   **passive** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the sever will not create the queue.

*   **durable** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue will be durable.

*   **exclusive** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue will be exclusive.

*   **auto_delete** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue is deleted when all consumers have finished using it.

*   **nowait** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – This parameter is unused since the 0-10 specification does not include it.

*   **arguments** ([_dict_](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")_or_ _None_) – A set of arguments for the declaration of the queue.

Returns:
A named tuple representing the declared queue as a named tuple. The tuple values are ordered as queue, message count, and the active consumer count.

Return type:
`namedtuple`

queue_delete(_queue_, _if\_unused=False_, _if\_empty=False_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.queue_delete "Link to this definition")
Delete a queue by name.

Delete a queue specified by name. Using the if_unused keyword argument, the delete can only occur if there are 0 consumers bound to it. Using the if_empty keyword argument, the delete can only occur if there are 0 messages in the queue.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be deleted.

Keyword Arguments:
*   **if_unused** – If True, delete only if the queue has 0 consumers. If False, delete a queue even with consumers bound to it.

*   **if_empty** – If True, only delete the queue if it is empty. If False, delete the queue if it is empty or not.

queue_purge(_queue_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.queue_purge "Link to this definition")
Remove all undelivered messages from queue.

Purge all undelivered messages from a queue specified by name. If the queue does not exist an exception is raised. The queue message depth is first checked, and then the broker is asked to purge that number of messages. The integer number of messages requested to be purged is returned. The actual number of messages purged may be different than the requested number of messages to purge.

Sometimes delivered messages are asked to be purged, but are not. This case fails silently, which is the correct behavior when a message that has been delivered to a different consumer, who has not ACKed the message, and still has an active session with the broker. Messages in that case are not safe for purging and will be retained by the broker. The client is unable to change this delivery behavior.

Internally, this method relies on `_purge()`.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue which should have all messages removed.

Returns:
The number of messages requested to be purged.

Return type:
[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")

Raises:
`qpid.messaging.exceptions.NotFound` if the queue being purged cannot be found.

queue_unbind(_queue_, _exchange_, _routing\_key_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.queue_unbind "Link to this definition")
Unbind a queue from an exchange with a given bind key.

Unbind a queue specified by name, from an exchange specified by name, that is already bound with a bind key. The queue and exchange must already exist on the broker, and bound with the bind key for the operation to complete successfully. Queues may be bound to exchanges multiple times with different keys, thus the bind key is a required field to unbind in an explicit way.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be unbound.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange that the queue should be unbound from.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The existing bind key between the specified queue and a specified exchange that should be unbound.

typeof(_exchange_, _default='direct'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.Channel.typeof "Link to this definition")
Get the exchange type.

Lookup and return the exchange type for an exchange specified by name. Exchange types are expected to be ‘direct’, ‘topic’, and ‘fanout’, which correspond with exchange functionality as specified in AMQP 0-10 and earlier. If the exchange cannot be found, the default exchange type is returned.

Parameters:
**exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The exchange to have its type lookup up.

Keyword Arguments:
**default** – The type of exchange to assume if the exchange does not exist.

Returns:
The exchange type either ‘direct’, ‘topic’, or ‘fanout’.

Return type:
[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")

close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.close "Link to this definition")
Close the connection.

Closing the connection will close all associated session, senders, or receivers used by the Connection.

close_channel(_channel_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.close_channel "Link to this definition")
Close a Channel.

Close a channel specified by a reference to the [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") object.

Parameters:
**channel** ([`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel").) – Channel that should be closed.

get_qpid_connection()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.Connection.get_qpid_connection "Link to this definition")
Return the existing connection (singleton).

Returns:
The existing qpid.messaging.Connection

Return type:
`qpid.messaging.endpoints.Connection`

channel_errors _=(None,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.channel_errors "Link to this definition")
Tuple of errors that can happen due to channel/method failure.

close_connection(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.close_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.close_connection "Link to this definition")
Close the [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object.

Parameters:
**connection** ([`kombu.transport.qpid.Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – The Connection that should be closed.

connection_errors _=(None,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.connection_errors "Link to this definition")
Tuple of errors that can happen due to connection failure.

create_channel(_connection_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.create_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.create_channel "Link to this definition")
Create and return a [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel").

Creates a new channel, and appends the channel to the list of channels known by the Connection. Once the new channel is created, it is returned.

Parameters:
**connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – The connection that should support the new [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel").

Returns:
The new Channel that is made.

Return type:
[`kombu.transport.qpid.Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel").

_property_ default_connection_params[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.default_connection_params "Link to this definition")
Return a dict with default connection parameters.

These connection parameters will be used whenever the creator of Transport does not specify a required parameter.

Returns:
A dict containing the default parameters.

Return type:
[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")

drain_events(_connection_, _timeout=0_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.drain_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "Link to this definition")
Handle and call callbacks for all ready Transport messages.

Drains all events that are ready from all `Receiver` that are asynchronously fetching messages.

For each drained message, the message is called to the appropriate callback. Callbacks are organized by queue name.

Parameters:
**connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – The [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") that contains the callbacks, indexed by queue name, which will be called by this method.

Keyword Arguments:
**timeout** – The timeout that limits how long this method will run for. The timeout could interrupt a blocking read that is waiting for a new message, or cause this method to return before all messages are drained. Defaults to 0.

driver_name _='qpid'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='qpid'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

establish_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.establish_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.establish_connection "Link to this definition")
Establish a Connection object.

Determines the correct options to use when creating any connections needed by this Transport, and create a [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object which saves those values for connections generated as they are needed. The options are a mixture of what is passed in through the creator of the Transport, and the defaults provided by [`default_connection_params()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.default_connection_params "kombu.transport.qpid.Transport.default_connection_params"). Options cover broker network settings, timeout behaviors, authentication, and identity verification settings.

This method also creates and stores a `Session` using the `Connection` created by this method. The Session is stored on self.

Returns:
The created [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object is returned.

Return type:
[`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")

implements _={'asynchronous':True,'exchange\_type':frozenset({'direct','fanout','topic'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.implements "Link to this definition")on_readable(_connection_, _loop_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.on_readable)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.on_readable "Link to this definition")
Handle any messages associated with this Transport.

This method clears a single message from the externally monitored file descriptor by issuing a read call to the self.r file descriptor which removes a single ‘0’ character that was placed into the pipe by the Qpid session message callback handler. Once a ‘0’ is read, all available events are drained through a call to [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events").

The file descriptor self.r is modified to be non-blocking, ensuring that an accidental call to this method when no more messages will not cause indefinite blocking.

Nothing is expected to be returned from [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") because [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") handles messages by calling callbacks that are maintained on the [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object. When [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") returns, all associated messages have been handled.

This method calls drain_events() which reads as many messages as are available for this Transport, and then returns. It blocks in the sense that reading and handling a large number of messages may take time, but it does not block waiting for a new message to arrive. When [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is called a timeout is not specified, which causes this behavior.

One interesting behavior of note is where multiple messages are ready, and this method removes a single ‘0’ character from self.r, but [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") may handle an arbitrary amount of messages. In that case, extra ‘0’ characters may be left on self.r to be read, where messages corresponding with those ‘0’ characters have already been handled. The external epoll loop will incorrectly think additional data is ready for reading, and will call on_readable unnecessarily, once for each ‘0’ to be read. Additional calls to [`on_readable()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.on_readable "kombu.transport.qpid.Transport.on_readable") produce no negative side effects, and will eventually clear out the symbols from the self.r file descriptor. If new messages show up during this draining period, they will also be properly handled.

Parameters:
*   **connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – The connection associated with the readable events, which contains the callbacks that need to be called for the readable objects.

*   **loop** ([_kombu.asynchronous.Hub_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.html#kombu.asynchronous.Hub "kombu.asynchronous.Hub")) – The asynchronous loop object that contains epoll like functionality.

polling_interval _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.polling_interval "Link to this definition")recoverable_channel_errors _=(None,)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.recoverable_channel_errors "Link to this definition")recoverable_connection_errors _=(None,<class'OSError'>)_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.recoverable_connection_errors "Link to this definition")register_with_event_loop(_connection_, _loop_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.register_with_event_loop)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.register_with_event_loop "Link to this definition")
Register a file descriptor and callback with the loop.

Register the callback self.on_readable to be called when an external epoll loop sees that the file descriptor registered is ready for reading. The file descriptor is created by this Transport, and is written to when a message is available.

Because supports_ev == True, Celery expects to call this method to give the Transport an opportunity to register a read file descriptor for external monitoring by celery using an Event I/O notification mechanism such as epoll. A callback is also registered that is to be called once the external epoll loop is ready to handle the epoll event associated with messages that are ready to be handled for this Transport.

The registration call is made exactly once per Transport after the Transport is instantiated.

Parameters:
*   **connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – A reference to the connection associated with this Transport.

*   **loop** ([_kombu.asynchronous.hub.Hub_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.hub.html#kombu.asynchronous.hub.Hub "kombu.asynchronous.hub.Hub")) – A reference to the external loop.

verify_runtime_environment()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Transport.verify_runtime_environment)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.verify_runtime_environment "Link to this definition")
Verify that the runtime environment is acceptable.

This method is called as part of __init__ and raises a RuntimeError in Python3 or PyPI environments. This module is not compatible with Python3 or PyPI. The RuntimeError identifies this to the user up front along with suggesting Python 2.6+ be used instead.

This method also checks that the dependencies qpidtoollibs and qpid.messaging are installed. If either one is not installed a RuntimeError is raised.

Raises:
RuntimeError if the runtime environment is not acceptable.

[Connection](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#connection "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.qpid.Connection(_**connection\_options_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "Link to this definition")
Qpid Connection.

Encapsulate a connection object for the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport").

Parameters:
*   **host** – The host that connections should connect to.

*   **port** – The port that connection should connect to.

*   **username** – The username that connections should connect with. Optional.

*   **password** – The password that connections should connect with. Optional but requires a username.

*   **transport** – The transport type that connections should use. Either ‘tcp’, or ‘ssl’ are expected as values.

*   **timeout** – the timeout used when a Connection connects to the broker.

*   **sasl_mechanisms** – The sasl authentication mechanism type to use. refer to SASL documentation for an explanation of valid values.

Note

qpid.messaging has an AuthenticationFailure exception type, but instead raises a ConnectionError with a message that indicates an authentication failure occurred in those situations. ConnectionError is listed as a recoverable error type, so kombu will attempt to retry if a ConnectionError is raised. Retrying the operation without adjusting the credentials is not correct, so this method specifically checks for a ConnectionError that indicates an Authentication Failure occurred. In those situations, the error type is mutated while preserving the original message and raised so kombu will allow the exception to not be considered recoverable.

A connection object is created by a [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") during a call to [`establish_connection()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.establish_connection "kombu.transport.qpid.Transport.establish_connection"). The [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") passes in connection options as keywords that should be used for any connections created. Each [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") creates exactly one Connection.

A Connection object maintains a reference to a `Connection` which can be accessed through a bound getter method named [`get_qpid_connection()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.get_qpid_connection "kombu.transport.qpid.Connection.get_qpid_connection") method. Each Channel uses a the Connection for each `BrokerAgent`, and the Transport maintains a session for all senders and receivers.

The Connection object is also responsible for maintaining the dictionary of references to callbacks that should be called when messages are received. These callbacks are saved in _callbacks, and keyed on the queue name associated with the received message. The _callbacks are setup in [`Channel.basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume"), removed in [`Channel.basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_cancel "kombu.transport.qpid.Channel.basic_cancel"), and called in [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events").

The following keys are expected to be passed in as keyword arguments at a minimum:

All keyword arguments are collected into the connection_options dict and passed directly through to `qpid.messaging.endpoints.Connection.establish()`.

_class_ Channel(_connection_, _transport_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel "Link to this definition")
Supports broker configuration and messaging send and receive.

Parameters:
*   **connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – A Connection object that this Channel can reference. Currently only used to access callbacks.

*   **transport** ([_kombu.transport.qpid.Transport_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport")) – The Transport this Channel is associated with.

A channel object is designed to have method-parity with a Channel as defined in AMQP 0-10 and earlier, which allows for the following broker actions:

> *   exchange declare and delete
> 
> *   queue declare and delete
> 
> *   queue bind and unbind operations
> 
> *   queue length and purge operations
> 
> *   sending/receiving/rejecting messages
> 
> *   structuring, encoding, and decoding messages
> 
> *   supports synchronous and asynchronous reads
> 
> *   reading state about the exchange, queues, and bindings

Channels are designed to all share a single TCP connection with a broker, but provide a level of isolated communication with the broker while benefiting from a shared TCP connection. The Channel is given its [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object by the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") that instantiates the channel.

This channel inherits from `StdChannel`, which makes this a ‘native’ channel versus a ‘virtual’ channel which would inherit from `kombu.transports.virtual`.

Messages sent using this channel are assigned a delivery_tag. The delivery_tag is generated for a message as they are prepared for sending by [`basic_publish()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_publish "kombu.transport.qpid.Connection.Channel.basic_publish"). The delivery_tag is unique per channel instance. The delivery_tag has no meaningful context in other objects, and is only maintained in the memory of this object, and the underlying [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object that provides support.

Each channel object instantiates exactly one [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object for prefetch limiting, and asynchronous ACKing. The [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is lazily instantiated through a property method [`qos()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.qos "kombu.transport.qpid.Connection.Channel.qos"). The [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is a supporting object that should not be accessed directly except by the channel itself.

Synchronous reads on a queue are done using a call to [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_get "kombu.transport.qpid.Connection.Channel.basic_get") which uses `_get()` to perform the reading. These methods read immediately and do not accept any form of timeout. [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_get "kombu.transport.qpid.Connection.Channel.basic_get") reads synchronously and ACKs messages before returning them. ACKing is done in all cases, because an application that reads messages using qpid.messaging, but does not ACK them will experience a memory leak. The no_ack argument to [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_get "kombu.transport.qpid.Connection.Channel.basic_get") does not affect ACKing functionality.

Asynchronous reads on a queue are done by starting a consumer using [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume"). Each call to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume") will cause a `Receiver` to be created on the `Session` started by the :class: Transport. The receiver will asynchronously read using qpid.messaging, and prefetch messages before the call to `Transport.basic_drain()` occurs. The prefetch_count value of the [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is the capacity value of the new receiver. The new receiver capacity must always be at least 1, otherwise none of the receivers will appear to be ready for reading, and will never be read from.

Each call to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume") creates a consumer, which is given a consumer tag that is identified by the caller of [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume"). Already started consumers can be cancelled using by their consumer_tag using [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_cancel "kombu.transport.qpid.Connection.Channel.basic_cancel"). Cancellation of a consumer causes the `Receiver` object to be closed.

Asynchronous message ACKing is supported through [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_ack "kombu.transport.qpid.Connection.Channel.basic_ack"), and is referenced by delivery_tag. The Channel object uses its [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object to perform the message ACKing.

_class_ Message(_payload_, _channel=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message "Link to this definition")
Message object.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.properties "Link to this definition")serializable()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.Message.serializable "Link to this definition")_class_ QoS(_session_, _prefetch\_count=1_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS "Link to this definition")
A helper object for message prefetch and ACKing purposes.

Keyword Arguments:
**prefetch_count** – Initial prefetch count, hard set to 1.

NOTE: prefetch_count is currently hard set to 1, and needs to be improved

This object is instantiated 1-for-1 with a [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") instance. QoS allows `prefetch_count` to be set to the number of outstanding messages the corresponding [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") should be allowed to prefetch. Setting `prefetch_count` to 0 disables prefetch limits, and the object can hold an arbitrary number of messages.

Messages are added using [`append()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.append "kombu.transport.qpid.Connection.Channel.QoS.append"), which are held until they are ACKed asynchronously through a call to [`ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.ack "kombu.transport.qpid.Connection.Channel.QoS.ack"). Messages that are received, but not ACKed will not be delivered by the broker to another consumer until an ACK is received, or the session is closed. Messages are referred to using delivery_tag, which are unique per [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel"). Delivery tags are managed outside of this object and are passed in with a message to [`append()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.append "kombu.transport.qpid.Connection.Channel.QoS.append"). Un-ACKed messages can be looked up from QoS using [`get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.get "kombu.transport.qpid.Connection.Channel.QoS.get") and can be rejected and forgotten using [`reject()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.reject "kombu.transport.qpid.Connection.Channel.QoS.reject").

ack(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.ack "Link to this definition")
Acknowledge a message by delivery_tag.

Called asynchronously once the message has been handled and can be forgotten by the broker.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – the delivery tag associated with the message to be acknowledged.

append(_message_, _delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.append "Link to this definition")
Append message to the list of un-ACKed messages.

Add a message, referenced by the delivery_tag, for ACKing, rejecting, or getting later. Messages are saved into a dict by delivery_tag.

Parameters:
*   **message** (_qpid.messaging.Message_) – A received message that has not yet been ACKed.

*   **delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – A UUID to refer to this message by upon receipt.

can_consume()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.can_consume "Link to this definition")
Return True if the [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") can consume more messages.

Used to ensure the client adheres to currently active prefetch limits.

Returns:
True, if this QoS object can accept more messages without violating the prefetch_count. If prefetch_count is 0, can_consume will always return True.

Return type:
[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")

can_consume_max_estimate()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.can_consume_max_estimate "Link to this definition")
Return the remaining message capacity.

Returns an estimated number of outstanding messages that a [`kombu.transport.qpid.Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") can accept without exceeding `prefetch_count`. If `prefetch_count` is 0, then this method returns 1.

Returns:
The number of estimated messages that can be fetched without violating the prefetch_count.

Return type:
[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")

get(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.get "Link to this definition")
Get an un-ACKed message by delivery_tag.

If called with an invalid delivery_tag a [`KeyError`](https://docs.python.org/dev/library/exceptions.html#KeyError "(in Python v3.15)") is raised.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be returned.

Returns:
An un-ACKed message that is looked up by delivery_tag.

Return type:
qpid.messaging.Message

reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.QoS.reject "Link to this definition")
Reject a message by delivery_tag.

Explicitly notify the broker that the channel associated with this QoS object is rejecting the message that was previously delivered.

If requeue is False, then the message is not requeued for delivery to another consumer. If requeue is True, then the message is requeued for delivery to another consumer.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be rejected.

Keyword Arguments:
**requeue** – If True, the broker will be notified to requeue the message. If False, the broker will be told to drop the message entirely. In both cases, the message will be removed from this object.

basic_ack(_delivery\_tag_, _multiple=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_ack "Link to this definition")
Acknowledge a message by delivery_tag.

Acknowledges a message referenced by delivery_tag. Messages can only be ACKed using [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_ack "kombu.transport.qpid.Connection.Channel.basic_ack") if they were acquired using [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume"). This is the ACKing portion of the asynchronous read behavior.

Internally, this method uses the [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object, which stores messages and is responsible for the ACKing.

Parameters:
*   **delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be acknowledged.

*   **multiple** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – not implemented. If set to True an AssertionError is raised.

basic_cancel(_consumer\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

Request the consumer stops reading messages from its queue. The consumer is a `Receiver`, and it is closed using `close()`.

This method also cleans up all lingering references of the consumer.

Parameters:
**consumer_tag** (_an immutable object_) – The tag which refers to the consumer to be cancelled. Originally specified when the consumer was created as a parameter to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume").

basic_consume(_queue_, _no\_ack_, _callback_, _consumer\_tag_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "Link to this definition")
Start an asynchronous consumer that reads from a queue.

This method starts a consumer of type `Receiver` using the `Session` created and referenced by the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") that reads messages from a queue specified by name until stopped by a call to [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_cancel "kombu.transport.qpid.Connection.Channel.basic_cancel").

Messages are available later through a synchronous call to [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"), which will drain from the consumer started by this method. [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is synchronous, but the receiving of messages over the network occurs asynchronously, so it should still perform well. [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") calls the callback provided here with the Message of type self.Message.

Each consumer is referenced by a consumer_tag, which is provided by the caller of this method.

This method sets up the callback onto the self.connection object in a dict keyed by queue name. [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is responsible for calling that callback upon message receipt.

All messages that are received are added to the QoS object to be saved for asynchronous ACKing later after the message has been handled by the caller of [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"). Messages can be ACKed after being received through a call to [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_ack "kombu.transport.qpid.Connection.Channel.basic_ack").

If no_ack is True, The no_ack flag indicates that the receiver of the message will not call [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_ack "kombu.transport.qpid.Connection.Channel.basic_ack") later. Since the message will not be ACKed later, it is ACKed immediately.

[`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_consume "kombu.transport.qpid.Connection.Channel.basic_consume") transforms the message object type prior to calling the callback. Initially the message comes in as a `qpid.messaging.Message`. This method unpacks the payload of the `qpid.messaging.Message` and creates a new object of type self.Message.

This method wraps the user delivered callback in a runtime-built function which provides the type transformation from `qpid.messaging.Message` to [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message"), and adds the message to the associated [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object for asynchronous ACKing if necessary.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to consume messages from

*   **no_ack** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, then messages will not be saved for ACKing later, but will be ACKed immediately. If False, then messages will be saved for ACKing later with a call to [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_ack "kombu.transport.qpid.Connection.Channel.basic_ack").

*   **callback** (_a callable object_) – a callable that will be called when messages arrive on the queue.

*   **consumer_tag** (_an immutable object_) – a tag to reference the created consumer by. This consumer_tag is needed to cancel the consumer.

basic_get(_queue_, _no\_ack=False_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_get "Link to this definition")
Non-blocking single message get and ACK from a queue by name.

Internally this method uses `_get()` to fetch the message. If an `Empty` exception is raised by `_get()`, this method silences it and returns None. If `_get()` does return a message, that message is ACKed. The no_ack parameter has no effect on ACKing behavior, and all messages are ACKed in all cases. This method never adds fetched Messages to the internal QoS object for asynchronous ACKing.

This method converts the object type of the method as it passes through. Fetching from the broker, `_get()` returns a `qpid.messaging.Message`, but this method takes the payload of the `qpid.messaging.Message` and instantiates a [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message") object with the payload based on the class setting of self.Message.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The queue name to fetch a message from.

Keyword Arguments:
**no_ack** – The no_ack parameter has no effect on the ACK behavior of this method. Un-ACKed messages create a memory leak in qpid.messaging, and need to be ACKed in all cases.

Returns:
The received message.

Return type:
[`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message")

basic_publish(_message_, _exchange_, _routing\_key_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_publish "Link to this definition")
Publish message onto an exchange using a routing key.

Publish a message onto an exchange specified by name using a routing key specified by routing_key. Prepares the message in the following ways before sending:

*   encodes the body using [`encode_body()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.encode_body "kombu.transport.qpid.Connection.Channel.encode_body")

*   wraps the body as a buffer object, so that
`qpid.messaging.endpoints.Sender` uses a content type that can support arbitrarily large messages.

*   sets delivery_tag to a random uuid.UUID

*   sets the exchange and routing_key info as delivery_info

Internally uses `_put()` to send the message synchronously. This message is typically called by `kombu.messaging.Producer._publish` as the final step in message publication.

Parameters:
*   **message** ([_dict_](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")) – A dict containing key value pairs with the message data. A valid message dict can be generated using the [`prepare_message()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.prepare_message "kombu.transport.qpid.Connection.Channel.prepare_message") method.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange to submit this message onto.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The routing key to be used as the message is submitted onto the exchange.

basic_qos(_prefetch\_count_, _*args_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_qos "Link to this definition")
Change [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") settings for this Channel.

Set the number of un-acknowledged messages this Channel can fetch and hold. The prefetch_value is also used as the capacity for any new `Receiver` objects.

Currently, this value is hard coded to 1.

Parameters:
**prefetch_count** ([_int_](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")) – Not used. This method is hard-coded to 1.

basic_reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_reject "Link to this definition")
Reject a message by delivery_tag.

Rejects a message that has been received by the Channel, but not yet acknowledged. Messages are referenced by their delivery_tag.

If requeue is False, the rejected message will be dropped by the broker and not delivered to any other consumers. If requeue is True, then the rejected message will be requeued for delivery to another consumer, potentially to the same consumer who rejected the message previously.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be rejected.

Keyword Arguments:
**requeue** – If False, the rejected message will be dropped by the broker and not delivered to any other consumers. If True, then the rejected message will be requeued for delivery to another consumer, potentially to the same consumer who rejected the message previously.

body_encoding _='base64'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.body_encoding "Link to this definition")
Default body encoding. NOTE: `transport_options['body_encoding']` will override this value.

close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.close "Link to this definition")
Cancel all associated messages and close the Channel.

This cancels all consumers by calling [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.basic_cancel "kombu.transport.qpid.Connection.Channel.basic_cancel") for each known consumer_tag. It also closes the self._broker sessions. Closing the sessions implicitly causes all outstanding, un-ACKed messages to be considered undelivered by the broker.

codecs _={'base64':<kombu.transport.virtual.base.Base64 object>}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.codecs "Link to this definition")
Binary <-> ASCII codecs.

decode_body(_body_, _encoding=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.decode_body "Link to this definition")
Decode a body using an optionally specified encoding.

The encoding can be specified by name, and is looked up in self.codecs. self.codecs uses strings as its keys which specify the name of the encoding, and then the value is an instantiated object that can provide encoding/decoding of that type through encode and decode methods.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body to be encoded.

Keyword Arguments:
**encoding** – The encoding type to be used. Must be a supported codec listed in self.codecs.

Returns:
If encoding is specified, the decoded body is returned. If encoding is not specified, the body is returned unchanged.

Return type:
[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")

encode_body(_body_, _encoding=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.encode_body "Link to this definition")
Encode a body using an optionally specified encoding.

The encoding can be specified by name, and is looked up in self.codecs. self.codecs uses strings as its keys which specify the name of the encoding, and then the value is an instantiated object that can provide encoding/decoding of that type through encode and decode methods.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body to be encoded.

Keyword Arguments:
**encoding** – The encoding type to be used. Must be a supported codec listed in self.codecs.

Returns:
If encoding is specified, return a tuple with the first position being the encoded body, and the second position the encoding used. If encoding is not specified, the body is passed through unchanged.

Return type:
[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")

exchange_declare(_exchange=''_, _type='direct'_, _durable=False_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.exchange_declare "Link to this definition")
Create a new exchange.

Create an exchange of a specific type, and optionally have the exchange be durable. If an exchange of the requested name already exists, no action is taken and no exceptions are raised. Durable exchanges will survive a broker restart, non-durable exchanges will not.

Exchanges provide behaviors based on their type. The expected behaviors are those defined in the AMQP 0-10 and prior specifications including ‘direct’, ‘topic’, and ‘fanout’ functionality.

Keyword Arguments:
*   **type** – The exchange type. Valid values include ‘direct’, ‘topic’, and ‘fanout’.

*   **exchange** – The name of the exchange to be created. If no exchange is specified, then a blank string will be used as the name.

*   **durable** – True if the exchange should be durable, or False otherwise.

exchange_delete(_exchange\_name_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.exchange_delete "Link to this definition")
Delete an exchange specified by name.

Parameters:
**exchange_name** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange to be deleted.

prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.prepare_message "Link to this definition")
Prepare message data for sending.

This message is typically called by `kombu.messaging.Producer._publish()` as a preparation step in message publication.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body of the message

Keyword Arguments:
*   **priority** – A number between 0 and 9 that sets the priority of the message.

*   **content_type** – The content_type the message body should be treated as. If this is unset, the `qpid.messaging.endpoints.Sender` object tries to autodetect the content_type from the body.

*   **content_encoding** – The content_encoding the message body is encoded as.

*   **headers** – Additional Message headers that should be set. Passed in as a key-value pair.

*   **properties** – Message properties to be set on the message.

Returns:
Returns a dict object that encapsulates message attributes. See parameters for more details on attributes that can be set.

Return type:
[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")

_property_ qos[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.qos "Link to this definition")
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") manager for this channel.

Lazily instantiates an object of type [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") upon access to the self.qos attribute.

Returns:
An already existing, or newly created QoS object

Return type:
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS")

queue_bind(_queue_, _exchange_, _routing\_key_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.queue_bind "Link to this definition")
Bind a queue to an exchange with a bind key.

Bind a queue specified by name, to an exchange specified by name, with a specific bind key. The queue and exchange must already exist on the broker for the bind to complete successfully. Queues may be bound to exchanges multiple times with different keys.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be bound.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange that the queue should be bound to.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The bind key that the specified queue should bind to the specified exchange with.

queue_declare(_queue_, _passive=False_, _durable=False_, _exclusive=False_, _auto\_delete=True_, _nowait=False_, _arguments=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.queue_declare "Link to this definition")
Create a new queue specified by name.

If the queue already exists, no change is made to the queue, and the return value returns information about the existing queue.

The queue name is required and specified as the first argument.

If passive is True, the server will not create the queue. The client can use this to check whether a queue exists without modifying the server state. Default is False.

If durable is True, the queue will be durable. Durable queues remain active when a server restarts. Non-durable queues ( transient queues) are purged if/when a server restarts. Note that durable queues do not necessarily hold persistent messages, although it does not make sense to send persistent messages to a transient queue. Default is False.

If exclusive is True, the queue will be exclusive. Exclusive queues may only be consumed by the current connection. Setting the ‘exclusive’ flag always implies ‘auto-delete’. Default is False.

If auto_delete is True, the queue is deleted when all consumers have finished using it. The last consumer can be cancelled either explicitly or because its channel is closed. If there was no consumer ever on the queue, it won’t be deleted. Default is True.

The nowait parameter is unused. It was part of the 0-9-1 protocol, but this AMQP client implements 0-10 which removed the nowait option.

The arguments parameter is a set of arguments for the declaration of the queue. Arguments are passed as a dict or None. This field is ignored if passive is True. Default is None.

This method returns a `namedtuple` with the name ‘queue_declare_ok_t’ and the queue name as ‘queue’, message count on the queue as ‘message_count’, and the number of active consumers as ‘consumer_count’. The named tuple values are ordered as queue, message_count, and consumer_count respectively.

Due to Celery’s non-ACKing of events, a ring policy is set on any queue that starts with the string ‘celeryev’ or ends with the string ‘pidbox’. These are celery event queues, and Celery does not ack them, causing the messages to build-up. Eventually Qpid stops serving messages unless the ‘ring’ policy is set, at which point the buffer backing the queue becomes circular.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be created.

*   **passive** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the sever will not create the queue.

*   **durable** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue will be durable.

*   **exclusive** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue will be exclusive.

*   **auto_delete** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue is deleted when all consumers have finished using it.

*   **nowait** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – This parameter is unused since the 0-10 specification does not include it.

*   **arguments** ([_dict_](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")_or_ _None_) – A set of arguments for the declaration of the queue.

Returns:
A named tuple representing the declared queue as a named tuple. The tuple values are ordered as queue, message count, and the active consumer count.

Return type:
`namedtuple`

queue_delete(_queue_, _if\_unused=False_, _if\_empty=False_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.queue_delete "Link to this definition")
Delete a queue by name.

Delete a queue specified by name. Using the if_unused keyword argument, the delete can only occur if there are 0 consumers bound to it. Using the if_empty keyword argument, the delete can only occur if there are 0 messages in the queue.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be deleted.

Keyword Arguments:
*   **if_unused** – If True, delete only if the queue has 0 consumers. If False, delete a queue even with consumers bound to it.

*   **if_empty** – If True, only delete the queue if it is empty. If False, delete the queue if it is empty or not.

queue_purge(_queue_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.queue_purge "Link to this definition")
Remove all undelivered messages from queue.

Purge all undelivered messages from a queue specified by name. If the queue does not exist an exception is raised. The queue message depth is first checked, and then the broker is asked to purge that number of messages. The integer number of messages requested to be purged is returned. The actual number of messages purged may be different than the requested number of messages to purge.

Sometimes delivered messages are asked to be purged, but are not. This case fails silently, which is the correct behavior when a message that has been delivered to a different consumer, who has not ACKed the message, and still has an active session with the broker. Messages in that case are not safe for purging and will be retained by the broker. The client is unable to change this delivery behavior.

Internally, this method relies on `_purge()`.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue which should have all messages removed.

Returns:
The number of messages requested to be purged.

Return type:
[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")

Raises:
`qpid.messaging.exceptions.NotFound` if the queue being purged cannot be found.

queue_unbind(_queue_, _exchange_, _routing\_key_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.queue_unbind "Link to this definition")
Unbind a queue from an exchange with a given bind key.

Unbind a queue specified by name, from an exchange specified by name, that is already bound with a bind key. The queue and exchange must already exist on the broker, and bound with the bind key for the operation to complete successfully. Queues may be bound to exchanges multiple times with different keys, thus the bind key is a required field to unbind in an explicit way.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be unbound.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange that the queue should be unbound from.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The existing bind key between the specified queue and a specified exchange that should be unbound.

typeof(_exchange_, _default='direct'_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.Channel.typeof "Link to this definition")
Get the exchange type.

Lookup and return the exchange type for an exchange specified by name. Exchange types are expected to be ‘direct’, ‘topic’, and ‘fanout’, which correspond with exchange functionality as specified in AMQP 0-10 and earlier. If the exchange cannot be found, the default exchange type is returned.

Parameters:
**exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The exchange to have its type lookup up.

Keyword Arguments:
**default** – The type of exchange to assume if the exchange does not exist.

Returns:
The exchange type either ‘direct’, ‘topic’, or ‘fanout’.

Return type:
[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Connection.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.close "Link to this definition")
Close the connection.

Closing the connection will close all associated session, senders, or receivers used by the Connection.

close_channel(_channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Connection.close_channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.close_channel "Link to this definition")
Close a Channel.

Close a channel specified by a reference to the [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") object.

Parameters:
**channel** ([`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel").) – Channel that should be closed.

get_qpid_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Connection.get_qpid_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection.get_qpid_connection "Link to this definition")
Return the existing connection (singleton).

Returns:
The existing qpid.messaging.Connection

Return type:
`qpid.messaging.endpoints.Connection`

[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id6)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.qpid.Channel(_connection_, _transport_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "Link to this definition")
Supports broker configuration and messaging send and receive.

Parameters:
*   **connection** ([_kombu.transport.qpid.Connection_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection")) – A Connection object that this Channel can reference. Currently only used to access callbacks.

*   **transport** ([_kombu.transport.qpid.Transport_](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport")) – The Transport this Channel is associated with.

A channel object is designed to have method-parity with a Channel as defined in AMQP 0-10 and earlier, which allows for the following broker actions:

> *   exchange declare and delete
> 
> *   queue declare and delete
> 
> *   queue bind and unbind operations
> 
> *   queue length and purge operations
> 
> *   sending/receiving/rejecting messages
> 
> *   structuring, encoding, and decoding messages
> 
> *   supports synchronous and asynchronous reads
> 
> *   reading state about the exchange, queues, and bindings

Channels are designed to all share a single TCP connection with a broker, but provide a level of isolated communication with the broker while benefiting from a shared TCP connection. The Channel is given its [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Connection "kombu.transport.qpid.Connection") object by the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") that instantiates the channel.

This channel inherits from `StdChannel`, which makes this a ‘native’ channel versus a ‘virtual’ channel which would inherit from `kombu.transports.virtual`.

Messages sent using this channel are assigned a delivery_tag. The delivery_tag is generated for a message as they are prepared for sending by [`basic_publish()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_publish "kombu.transport.qpid.Channel.basic_publish"). The delivery_tag is unique per channel instance. The delivery_tag has no meaningful context in other objects, and is only maintained in the memory of this object, and the underlying [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object that provides support.

Each channel object instantiates exactly one [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object for prefetch limiting, and asynchronous ACKing. The [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is lazily instantiated through a property method [`qos()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.qos "kombu.transport.qpid.Channel.qos"). The [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is a supporting object that should not be accessed directly except by the channel itself.

Synchronous reads on a queue are done using a call to [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_get "kombu.transport.qpid.Channel.basic_get") which uses `_get()` to perform the reading. These methods read immediately and do not accept any form of timeout. [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_get "kombu.transport.qpid.Channel.basic_get") reads synchronously and ACKs messages before returning them. ACKing is done in all cases, because an application that reads messages using qpid.messaging, but does not ACK them will experience a memory leak. The no_ack argument to [`basic_get()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_get "kombu.transport.qpid.Channel.basic_get") does not affect ACKing functionality.

Asynchronous reads on a queue are done by starting a consumer using [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume"). Each call to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume") will cause a `Receiver` to be created on the `Session` started by the :class: Transport. The receiver will asynchronously read using qpid.messaging, and prefetch messages before the call to `Transport.basic_drain()` occurs. The prefetch_count value of the [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object is the capacity value of the new receiver. The new receiver capacity must always be at least 1, otherwise none of the receivers will appear to be ready for reading, and will never be read from.

Each call to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume") creates a consumer, which is given a consumer tag that is identified by the caller of [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume"). Already started consumers can be cancelled using by their consumer_tag using [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_cancel "kombu.transport.qpid.Channel.basic_cancel"). Cancellation of a consumer causes the `Receiver` object to be closed.

Asynchronous message ACKing is supported through [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_ack "kombu.transport.qpid.Channel.basic_ack"), and is referenced by delivery_tag. The Channel object uses its [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object to perform the message ACKing.

_class_ Message(_payload_, _channel=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message "Link to this definition")
message class used.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.properties "Link to this definition")serializable()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.Message.serializable "Link to this definition")_class_ QoS(_session_, _prefetch\_count=1_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "Link to this definition")
A class reference that will be instantiated using the qos property.

ack(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS.ack "Link to this definition")
Acknowledge a message by delivery_tag.

Called asynchronously once the message has been handled and can be forgotten by the broker.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – the delivery tag associated with the message to be acknowledged.

append(_message_, _delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS.append "Link to this definition")
Append message to the list of un-ACKed messages.

Add a message, referenced by the delivery_tag, for ACKing, rejecting, or getting later. Messages are saved into a dict by delivery_tag.

Parameters:
*   **message** (_qpid.messaging.Message_) – A received message that has not yet been ACKed.

*   **delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – A UUID to refer to this message by upon receipt.

can_consume()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS.can_consume "Link to this definition")
Return True if the [`Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") can consume more messages.

Used to ensure the client adheres to currently active prefetch limits.

Returns:
True, if this QoS object can accept more messages without violating the prefetch_count. If prefetch_count is 0, can_consume will always return True.

Return type:
[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")

can_consume_max_estimate()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS.can_consume_max_estimate "Link to this definition")
Return the remaining message capacity.

Returns an estimated number of outstanding messages that a [`kombu.transport.qpid.Channel`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel "kombu.transport.qpid.Channel") can accept without exceeding `prefetch_count`. If `prefetch_count` is 0, then this method returns 1.

Returns:
The number of estimated messages that can be fetched without violating the prefetch_count.

Return type:
[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")

get(_delivery\_tag_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS.get "Link to this definition")
Get an un-ACKed message by delivery_tag.

If called with an invalid delivery_tag a [`KeyError`](https://docs.python.org/dev/library/exceptions.html#KeyError "(in Python v3.15)") is raised.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be returned.

Returns:
An un-ACKed message that is looked up by delivery_tag.

Return type:
qpid.messaging.Message

reject(_delivery\_tag_, _requeue=False_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS.reject "Link to this definition")
Reject a message by delivery_tag.

Explicitly notify the broker that the channel associated with this QoS object is rejecting the message that was previously delivered.

If requeue is False, then the message is not requeued for delivery to another consumer. If requeue is True, then the message is requeued for delivery to another consumer.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be rejected.

Keyword Arguments:
**requeue** – If True, the broker will be notified to requeue the message. If False, the broker will be told to drop the message entirely. In both cases, the message will be removed from this object.

basic_ack(_delivery\_tag_, _multiple=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_ack)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_ack "Link to this definition")
Acknowledge a message by delivery_tag.

Acknowledges a message referenced by delivery_tag. Messages can only be ACKed using [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_ack "kombu.transport.qpid.Channel.basic_ack") if they were acquired using [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume"). This is the ACKing portion of the asynchronous read behavior.

Internally, this method uses the [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object, which stores messages and is responsible for the ACKing.

Parameters:
*   **delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be acknowledged.

*   **multiple** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – not implemented. If set to True an AssertionError is raised.

basic_cancel(_consumer\_tag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_cancel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_cancel "Link to this definition")
Cancel consumer by consumer tag.

Request the consumer stops reading messages from its queue. The consumer is a `Receiver`, and it is closed using `close()`.

This method also cleans up all lingering references of the consumer.

Parameters:
**consumer_tag** (_an immutable object_) – The tag which refers to the consumer to be cancelled. Originally specified when the consumer was created as a parameter to [`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume").

basic_consume(_queue_, _no\_ack_, _callback_, _consumer\_tag_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "Link to this definition")
Start an asynchronous consumer that reads from a queue.

This method starts a consumer of type `Receiver` using the `Session` created and referenced by the [`Transport`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport "kombu.transport.qpid.Transport") that reads messages from a queue specified by name until stopped by a call to [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_cancel "kombu.transport.qpid.Channel.basic_cancel").

Messages are available later through a synchronous call to [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"), which will drain from the consumer started by this method. [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is synchronous, but the receiving of messages over the network occurs asynchronously, so it should still perform well. [`Transport.drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") calls the callback provided here with the Message of type self.Message.

Each consumer is referenced by a consumer_tag, which is provided by the caller of this method.

This method sets up the callback onto the self.connection object in a dict keyed by queue name. [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events") is responsible for calling that callback upon message receipt.

All messages that are received are added to the QoS object to be saved for asynchronous ACKing later after the message has been handled by the caller of [`drain_events()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Transport.drain_events "kombu.transport.qpid.Transport.drain_events"). Messages can be ACKed after being received through a call to [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_ack "kombu.transport.qpid.Channel.basic_ack").

If no_ack is True, The no_ack flag indicates that the receiver of the message will not call [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_ack "kombu.transport.qpid.Channel.basic_ack") later. Since the message will not be ACKed later, it is ACKed immediately.

[`basic_consume()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_consume "kombu.transport.qpid.Channel.basic_consume") transforms the message object type prior to calling the callback. Initially the message comes in as a `qpid.messaging.Message`. This method unpacks the payload of the `qpid.messaging.Message` and creates a new object of type self.Message.

This method wraps the user delivered callback in a runtime-built function which provides the type transformation from `qpid.messaging.Message` to [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message"), and adds the message to the associated [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") object for asynchronous ACKing if necessary.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to consume messages from

*   **no_ack** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, then messages will not be saved for ACKing later, but will be ACKed immediately. If False, then messages will be saved for ACKing later with a call to [`basic_ack()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_ack "kombu.transport.qpid.Channel.basic_ack").

*   **callback** (_a callable object_) – a callable that will be called when messages arrive on the queue.

*   **consumer_tag** (_an immutable object_) – a tag to reference the created consumer by. This consumer_tag is needed to cancel the consumer.

basic_get(_queue_, _no\_ack=False_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_get)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_get "Link to this definition")
Non-blocking single message get and ACK from a queue by name.

Internally this method uses `_get()` to fetch the message. If an `Empty` exception is raised by `_get()`, this method silences it and returns None. If `_get()` does return a message, that message is ACKed. The no_ack parameter has no effect on ACKing behavior, and all messages are ACKed in all cases. This method never adds fetched Messages to the internal QoS object for asynchronous ACKing.

This method converts the object type of the method as it passes through. Fetching from the broker, `_get()` returns a `qpid.messaging.Message`, but this method takes the payload of the `qpid.messaging.Message` and instantiates a [`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message") object with the payload based on the class setting of self.Message.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The queue name to fetch a message from.

Keyword Arguments:
**no_ack** – The no_ack parameter has no effect on the ACK behavior of this method. Un-ACKed messages create a memory leak in qpid.messaging, and need to be ACKed in all cases.

Returns:
The received message.

Return type:
[`Message`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.virtual.html#kombu.transport.virtual.Message "kombu.transport.virtual.Message")

basic_publish(_message_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_publish)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_publish "Link to this definition")
Publish message onto an exchange using a routing key.

Publish a message onto an exchange specified by name using a routing key specified by routing_key. Prepares the message in the following ways before sending:

*   encodes the body using [`encode_body()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.encode_body "kombu.transport.qpid.Channel.encode_body")

*   wraps the body as a buffer object, so that
`qpid.messaging.endpoints.Sender` uses a content type that can support arbitrarily large messages.

*   sets delivery_tag to a random uuid.UUID

*   sets the exchange and routing_key info as delivery_info

Internally uses `_put()` to send the message synchronously. This message is typically called by `kombu.messaging.Producer._publish` as the final step in message publication.

Parameters:
*   **message** ([_dict_](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")) – A dict containing key value pairs with the message data. A valid message dict can be generated using the [`prepare_message()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.prepare_message "kombu.transport.qpid.Channel.prepare_message") method.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange to submit this message onto.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The routing key to be used as the message is submitted onto the exchange.

basic_qos(_prefetch\_count_, _*args_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_qos)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_qos "Link to this definition")
Change [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") settings for this Channel.

Set the number of un-acknowledged messages this Channel can fetch and hold. The prefetch_value is also used as the capacity for any new `Receiver` objects.

Currently, this value is hard coded to 1.

Parameters:
**prefetch_count** ([_int_](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")) – Not used. This method is hard-coded to 1.

basic_reject(_delivery\_tag_, _requeue=False_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.basic_reject)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_reject "Link to this definition")
Reject a message by delivery_tag.

Rejects a message that has been received by the Channel, but not yet acknowledged. Messages are referenced by their delivery_tag.

If requeue is False, the rejected message will be dropped by the broker and not delivered to any other consumers. If requeue is True, then the rejected message will be requeued for delivery to another consumer, potentially to the same consumer who rejected the message previously.

Parameters:
**delivery_tag** ([_uuid.UUID_](https://docs.python.org/dev/library/uuid.html#uuid.UUID "(in Python v3.15)")) – The delivery tag associated with the message to be rejected.

Keyword Arguments:
**requeue** – If False, the rejected message will be dropped by the broker and not delivered to any other consumers. If True, then the rejected message will be requeued for delivery to another consumer, potentially to the same consumer who rejected the message previously.

body_encoding _='base64'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.body_encoding "Link to this definition")
Default body encoding. NOTE: `transport_options['body_encoding']` will override this value.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.close "Link to this definition")
Cancel all associated messages and close the Channel.

This cancels all consumers by calling [`basic_cancel()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.basic_cancel "kombu.transport.qpid.Channel.basic_cancel") for each known consumer_tag. It also closes the self._broker sessions. Closing the sessions implicitly causes all outstanding, un-ACKed messages to be considered undelivered by the broker.

codecs _={'base64':<kombu.transport.virtual.base.Base64 object>}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.codecs "Link to this definition")
Binary <-> ASCII codecs.

decode_body(_body_, _encoding=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.decode_body)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.decode_body "Link to this definition")
Decode a body using an optionally specified encoding.

The encoding can be specified by name, and is looked up in self.codecs. self.codecs uses strings as its keys which specify the name of the encoding, and then the value is an instantiated object that can provide encoding/decoding of that type through encode and decode methods.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body to be encoded.

Keyword Arguments:
**encoding** – The encoding type to be used. Must be a supported codec listed in self.codecs.

Returns:
If encoding is specified, the decoded body is returned. If encoding is not specified, the body is returned unchanged.

Return type:
[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")

encode_body(_body_, _encoding=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.encode_body)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.encode_body "Link to this definition")
Encode a body using an optionally specified encoding.

The encoding can be specified by name, and is looked up in self.codecs. self.codecs uses strings as its keys which specify the name of the encoding, and then the value is an instantiated object that can provide encoding/decoding of that type through encode and decode methods.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body to be encoded.

Keyword Arguments:
**encoding** – The encoding type to be used. Must be a supported codec listed in self.codecs.

Returns:
If encoding is specified, return a tuple with the first position being the encoded body, and the second position the encoding used. If encoding is not specified, the body is passed through unchanged.

Return type:
[tuple](https://docs.python.org/dev/library/stdtypes.html#tuple "(in Python v3.15)")

exchange_declare(_exchange=''_, _type='direct'_, _durable=False_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.exchange_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.exchange_declare "Link to this definition")
Create a new exchange.

Create an exchange of a specific type, and optionally have the exchange be durable. If an exchange of the requested name already exists, no action is taken and no exceptions are raised. Durable exchanges will survive a broker restart, non-durable exchanges will not.

Exchanges provide behaviors based on their type. The expected behaviors are those defined in the AMQP 0-10 and prior specifications including ‘direct’, ‘topic’, and ‘fanout’ functionality.

Keyword Arguments:
*   **type** – The exchange type. Valid values include ‘direct’, ‘topic’, and ‘fanout’.

*   **exchange** – The name of the exchange to be created. If no exchange is specified, then a blank string will be used as the name.

*   **durable** – True if the exchange should be durable, or False otherwise.

exchange_delete(_exchange\_name_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.exchange_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.exchange_delete "Link to this definition")
Delete an exchange specified by name.

Parameters:
**exchange_name** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange to be deleted.

prepare_message(_body_, _priority=None_, _content\_type=None_, _content\_encoding=None_, _headers=None_, _properties=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.prepare_message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.prepare_message "Link to this definition")
Prepare message data for sending.

This message is typically called by `kombu.messaging.Producer._publish()` as a preparation step in message publication.

Parameters:
**body** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The body of the message

Keyword Arguments:
*   **priority** – A number between 0 and 9 that sets the priority of the message.

*   **content_type** – The content_type the message body should be treated as. If this is unset, the `qpid.messaging.endpoints.Sender` object tries to autodetect the content_type from the body.

*   **content_encoding** – The content_encoding the message body is encoded as.

*   **headers** – Additional Message headers that should be set. Passed in as a key-value pair.

*   **properties** – Message properties to be set on the message.

Returns:
Returns a dict object that encapsulates message attributes. See parameters for more details on attributes that can be set.

Return type:
[dict](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")

_property_ qos[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.qos "Link to this definition")
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") manager for this channel.

Lazily instantiates an object of type [`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS") upon access to the self.qos attribute.

Returns:
An already existing, or newly created QoS object

Return type:
[`QoS`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.QoS "kombu.transport.qpid.QoS")

queue_bind(_queue_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.queue_bind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.queue_bind "Link to this definition")
Bind a queue to an exchange with a bind key.

Bind a queue specified by name, to an exchange specified by name, with a specific bind key. The queue and exchange must already exist on the broker for the bind to complete successfully. Queues may be bound to exchanges multiple times with different keys.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be bound.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange that the queue should be bound to.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The bind key that the specified queue should bind to the specified exchange with.

queue_declare(_queue_, _passive=False_, _durable=False_, _exclusive=False_, _auto\_delete=True_, _nowait=False_, _arguments=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.queue_declare)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.queue_declare "Link to this definition")
Create a new queue specified by name.

If the queue already exists, no change is made to the queue, and the return value returns information about the existing queue.

The queue name is required and specified as the first argument.

If passive is True, the server will not create the queue. The client can use this to check whether a queue exists without modifying the server state. Default is False.

If durable is True, the queue will be durable. Durable queues remain active when a server restarts. Non-durable queues ( transient queues) are purged if/when a server restarts. Note that durable queues do not necessarily hold persistent messages, although it does not make sense to send persistent messages to a transient queue. Default is False.

If exclusive is True, the queue will be exclusive. Exclusive queues may only be consumed by the current connection. Setting the ‘exclusive’ flag always implies ‘auto-delete’. Default is False.

If auto_delete is True, the queue is deleted when all consumers have finished using it. The last consumer can be cancelled either explicitly or because its channel is closed. If there was no consumer ever on the queue, it won’t be deleted. Default is True.

The nowait parameter is unused. It was part of the 0-9-1 protocol, but this AMQP client implements 0-10 which removed the nowait option.

The arguments parameter is a set of arguments for the declaration of the queue. Arguments are passed as a dict or None. This field is ignored if passive is True. Default is None.

This method returns a `namedtuple` with the name ‘queue_declare_ok_t’ and the queue name as ‘queue’, message count on the queue as ‘message_count’, and the number of active consumers as ‘consumer_count’. The named tuple values are ordered as queue, message_count, and consumer_count respectively.

Due to Celery’s non-ACKing of events, a ring policy is set on any queue that starts with the string ‘celeryev’ or ends with the string ‘pidbox’. These are celery event queues, and Celery does not ack them, causing the messages to build-up. Eventually Qpid stops serving messages unless the ‘ring’ policy is set, at which point the buffer backing the queue becomes circular.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be created.

*   **passive** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the sever will not create the queue.

*   **durable** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue will be durable.

*   **exclusive** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue will be exclusive.

*   **auto_delete** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – If True, the queue is deleted when all consumers have finished using it.

*   **nowait** ([_bool_](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")) – This parameter is unused since the 0-10 specification does not include it.

*   **arguments** ([_dict_](https://docs.python.org/dev/library/stdtypes.html#dict "(in Python v3.15)")_or_ _None_) – A set of arguments for the declaration of the queue.

Returns:
A named tuple representing the declared queue as a named tuple. The tuple values are ordered as queue, message count, and the active consumer count.

Return type:
`namedtuple`

queue_delete(_queue_, _if\_unused=False_, _if\_empty=False_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.queue_delete)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.queue_delete "Link to this definition")
Delete a queue by name.

Delete a queue specified by name. Using the if_unused keyword argument, the delete can only occur if there are 0 consumers bound to it. Using the if_empty keyword argument, the delete can only occur if there are 0 messages in the queue.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be deleted.

Keyword Arguments:
*   **if_unused** – If True, delete only if the queue has 0 consumers. If False, delete a queue even with consumers bound to it.

*   **if_empty** – If True, only delete the queue if it is empty. If False, delete the queue if it is empty or not.

queue_purge(_queue_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.queue_purge)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.queue_purge "Link to this definition")
Remove all undelivered messages from queue.

Purge all undelivered messages from a queue specified by name. If the queue does not exist an exception is raised. The queue message depth is first checked, and then the broker is asked to purge that number of messages. The integer number of messages requested to be purged is returned. The actual number of messages purged may be different than the requested number of messages to purge.

Sometimes delivered messages are asked to be purged, but are not. This case fails silently, which is the correct behavior when a message that has been delivered to a different consumer, who has not ACKed the message, and still has an active session with the broker. Messages in that case are not safe for purging and will be retained by the broker. The client is unable to change this delivery behavior.

Internally, this method relies on `_purge()`.

Parameters:
**queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue which should have all messages removed.

Returns:
The number of messages requested to be purged.

Return type:
[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")

Raises:
`qpid.messaging.exceptions.NotFound` if the queue being purged cannot be found.

queue_unbind(_queue_, _exchange_, _routing\_key_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.queue_unbind)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.queue_unbind "Link to this definition")
Unbind a queue from an exchange with a given bind key.

Unbind a queue specified by name, from an exchange specified by name, that is already bound with a bind key. The queue and exchange must already exist on the broker, and bound with the bind key for the operation to complete successfully. Queues may be bound to exchanges multiple times with different keys, thus the bind key is a required field to unbind in an explicit way.

Parameters:
*   **queue** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the queue to be unbound.

*   **exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The name of the exchange that the queue should be unbound from.

*   **routing_key** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The existing bind key between the specified queue and a specified exchange that should be unbound.

typeof(_exchange_, _default='direct'_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/qpid.html#Channel.typeof)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Channel.typeof "Link to this definition")
Get the exchange type.

Lookup and return the exchange type for an exchange specified by name. Exchange types are expected to be ‘direct’, ‘topic’, and ‘fanout’, which correspond with exchange functionality as specified in AMQP 0-10 and earlier. If the exchange cannot be found, the default exchange type is returned.

Parameters:
**exchange** ([_str_](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")) – The exchange to have its type lookup up.

Keyword Arguments:
**default** – The type of exchange to assume if the exchange does not exist.

Returns:
The exchange type either ‘direct’, ‘topic’, or ‘fanout’.

Return type:
[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")

[Message](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#id7)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#message "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.qpid.Message(_payload_, _channel=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Message)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message "Link to this definition")
Message object.

accept[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.accept "Link to this definition")body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.body "Link to this definition")channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.channel "Link to this definition")content_encoding[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.content_encoding "Link to this definition")content_type[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.content_type "Link to this definition")delivery_info[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.delivery_info "Link to this definition")delivery_tag[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.delivery_tag "Link to this definition")properties[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.properties "Link to this definition")serializable()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/virtual/base.html#Message.serializable)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.qpid.html#kombu.transport.qpid.Message.serializable "Link to this definition")

# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html

Title: system Transport - kombu.transport.filesystem — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.transport.filesystem.html).

File-system Transport module for kombu.

Transport using the file-system as the message store. Messages written to the queue are stored in data_folder_in directory and messages read from the queue are read from data_folder_out directory. Both directories must be created manually. Simple example:

*   Producer:

import kombu

conn = kombu.Connection(
    'filesystem://', transport_options={
        'data_folder_in': 'data_in', 'data_folder_out': 'data_out'
    }
)
conn.connect()

test_queue = kombu.Queue('test', routing_key='test')

with conn as conn:
    with conn.default_channel as channel:
        producer = kombu.Producer(channel)
        producer.publish(
                    {'hello': 'world'},
                    retry=True,
                    exchange=test_queue.exchange,
                    routing_key=test_queue.routing_key,
                    declare=[test_queue],
                    serializer='pickle'
        )

*   Consumer:

import kombu

conn = kombu.Connection(
    'filesystem://', transport_options={
        'data_folder_in': 'data_out', 'data_folder_out': 'data_in'
    }
)
conn.connect()

def callback(body, message):
    print(body, message)
    message.ack()

test_queue = kombu.Queue('test', routing_key='test')

with conn as conn:
    with conn.default_channel as channel:
        consumer = kombu.Consumer(
            conn, [test_queue], accept=['pickle']
        )
        consumer.register_callback(callback)
        with consumer:
            conn.drain_events(timeout=1)

[Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#features "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Type: Virtual

*   Supports Direct: Yes

*   Supports Topic: Yes

*   Supports Fanout: Yes

*   Supports Priority: No

*   Supports TTL: No

[Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#connection-string "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Connection string is in the following format:

filesystem://

[Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#transport-options "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   `data_folder_in` - directory where are messages stored when written to queue.

*   `data_folder_out` - directory from which are messages read when read from queue.

*   `store_processed` - if set to True, all processed messages are backed up to `processed_folder`.

*   `processed_folder` - directory where are backed up processed files.

*   `control_folder` - directory where are exchange-queue table stored.

*   [Features](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#features)

*   [Connection String](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#connection-string)

*   [Transport Options](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#transport-options)

*   [Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#transport)

*   [Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#channel)

[Transport](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#transport "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.filesystem.Transport(_client_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/filesystem.html#Transport)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport "Link to this definition")
Filesystem Transport.

_class_ Channel(_connection_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel "Link to this definition")
Filesystem Channel.

_property_ control_folder[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.control_folder "Link to this definition")_property_ data_folder_in[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.data_folder_in "Link to this definition")_property_ data_folder_out[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.data_folder_out "Link to this definition")get_table(_exchange_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

_property_ processed_folder[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.processed_folder "Link to this definition")_property_ store_processed[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.store_processed "Link to this definition")supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.Channel.transport_options "Link to this definition")default_port _=0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.default_port "Link to this definition")
port number used when no port is specified.

driver_name _='filesystem'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.driver_name "Link to this definition")
Name of driver library (e.g. ‘py-amqp’, ‘redis’).

driver_type _='filesystem'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.driver_type "Link to this definition")
Type of driver, can be used to separate transports using the AMQP protocol (driver_type: ‘amqp’), Redis (driver_type: ‘redis’), etc…

driver_version()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/filesystem.html#Transport.driver_version)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.driver_version "Link to this definition")global_state _=<kombu.transport.virtual.base.BrokerState object>_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.global_state "Link to this definition")implements _={'asynchronous':False,'exchange\_type':frozenset({'direct','fanout','topic'}),'heartbeats':False}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Transport.implements "Link to this definition")
[Channel](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#id5)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#channel "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.transport.filesystem.Channel(_connection_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/filesystem.html#Channel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel "Link to this definition")
Filesystem Channel.

_property_ control_folder[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.control_folder "Link to this definition")_property_ data_folder_in[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.data_folder_in "Link to this definition")_property_ data_folder_out[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.data_folder_out "Link to this definition")get_table(_exchange_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/transport/filesystem.html#Channel.get_table)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.get_table "Link to this definition")
Get table of bindings for exchange.

_property_ processed_folder[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.processed_folder "Link to this definition")_property_ store_processed[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.store_processed "Link to this definition")supports_fanout _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.supports_fanout "Link to this definition")
flag set if the channel supports fanout exchanges.

_property_ transport_options[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.transport.filesystem.html#kombu.transport.filesystem.Channel.transport_options "Link to this definition")

# Source: https://kafka-python.readthedocs.io/

Title: kafka-python — kafka-python 2.3.0 documentation

URL Source: https://kafka-python.readthedocs.io/

Markdown Content:
[![Image 1: https://img.shields.io/badge/kafka-4.0--0.8-brightgreen.svg](https://img.shields.io/badge/kafka-4.0--0.8-brightgreen.svg)](https://kafka-python.readthedocs.io/en/master/compatibility.html)[![Image 2: https://img.shields.io/pypi/pyversions/kafka-python.svg](https://img.shields.io/pypi/pyversions/kafka-python.svg)](https://pypi.python.org/pypi/kafka-python)[![Image 3: https://coveralls.io/repos/dpkp/kafka-python/badge.svg?branch=master&service=github](https://coveralls.io/repos/dpkp/kafka-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/dpkp/kafka-python?branch=master)[![Image 4: https://img.shields.io/github/actions/workflow/status/dpkp/kafka-python/python-package.yml](https://img.shields.io/github/actions/workflow/status/dpkp/kafka-python/python-package.yml)](https://github.com/dpkp/kafka-python/actions/workflows/python-package.yml)[![Image 5: https://img.shields.io/badge/license-Apache%202-blue.svg](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://github.com/dpkp/kafka-python/blob/master/LICENSE)
Python client for the Apache Kafka distributed stream processing system. kafka-python is designed to function much like the official java client, with a sprinkling of pythonic interfaces (e.g., consumer iterators).

Please note that the master branch may contain unreleased features. For release documentation, please see readthedocs and/or python’s inline help.

New in 2.3 release: python -m kafka.* interfaces for quick scripts and testing.

pip install kafka-python

KafkaConsumer[](https://kafka-python.readthedocs.io/#kafkaconsumer "Link to this heading")
-------------------------------------------------------------------------------------------

[`KafkaConsumer`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer "kafka.KafkaConsumer") is a high-level message consumer, intended to operate as similarly as possible to the official java client. Full support for coordinated consumer groups requires use of kafka brokers that support the Group APIs: kafka v0.9+.

See [KafkaConsumer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html) for API and configuration details.

The consumer iterator returns ConsumerRecords, which are simple namedtuples that expose basic message attributes: topic, partition, offset, key, and value:

from kafka import KafkaConsumer
consumer = KafkaConsumer('my_favorite_topic')
for msg in consumer:
    print (msg)

# join a consumer group for dynamic partition assignment and offset commits

from kafka import KafkaConsumer
consumer = KafkaConsumer('my_favorite_topic', group_id='my_favorite_group')
for msg in consumer:
    print (msg)

# manually assign the partition list for the consumer

from kafka import TopicPartition
consumer = KafkaConsumer(bootstrap_servers='localhost:1234')
consumer.assign([TopicPartition('foobar', 2)])
msg = next(consumer)

# Deserialize msgpack-encoded values

consumer = KafkaConsumer(value_deserializer=msgpack.loads)
consumer.subscribe(['msgpackfoo'])
for msg in consumer:
    assert isinstance(msg.value, dict)

# Access record headers. The returned value is a list of tuples

# with str, bytes for key and value

for msg in consumer:
    print (msg.headers)

# Read only committed messages from transactional topic

consumer = KafkaConsumer(isolation_level='read_committed')
consumer.subscribe(['txn_topic'])
for msg in consumer:
    print(msg)

# Get consumer metrics

metrics = consumer.metrics()

KafkaProducer[](https://kafka-python.readthedocs.io/#kafkaproducer "Link to this heading")
-------------------------------------------------------------------------------------------

[`KafkaProducer`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html#kafka.KafkaProducer "kafka.KafkaProducer") is a high-level, asynchronous message producer. The class is intended to operate as similarly as possible to the official java client. See [KafkaProducer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html) for more details.

from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:1234')
for_ in range(100):
    producer.send('foobar', b'some_message_bytes')

# Block until a single message is sent (or timeout)

future = producer.send('foobar', b'another_message')
result = future.get(timeout=60)

# Block until all pending messages are at least put on the network

# NOTE: This does not guarantee delivery or success! It is really

# only useful if you configure internal batching using linger_ms

producer.flush()

# Use a key for hashed-partitioning

producer.send('foobar', key=b'foo', value=b'bar')

# Serialize json messages

import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('fizzbuzz', {'foo': 'bar'})

# Serialize string keys

producer = KafkaProducer(key_serializer=str.encode)
producer.send('flipflap', key='ping', value=b'1234')

# Compress messages

producer = KafkaProducer(compression_type='gzip')
for i in range(1000):
    producer.send('foobar', b'msg %d' % i)

# Use transactions

producer = KafkaProducer(transactional_id='fizzbuzz')
producer.init_transactions()
producer.begin_transaction()
future = producer.send('txn_topic', value=b'yes')
future.get() # wait for successful produce
producer.commit_transaction() # commit the transaction

producer.begin_transaction()
future = producer.send('txn_topic', value=b'no')
future.get() # wait for successful produce
producer.abort_transaction() # abort the transaction

# Include record headers. The format is list of tuples with string key

# and bytes value

producer.send('foobar', value=b'c29tZSB2YWx1ZQ==', headers=[('content-encoding', b'base64')])

# Get producer performance metrics

metrics = producer.metrics()

Module CLI Interface[](https://kafka-python.readthedocs.io/#module-cli-interface "Link to this heading")
---------------------------------------------------------------------------------------------------------

kafka-python also provides simple command-line interfaces for consumer, producer, and admin clients. Access via `python -m kafka.consumer`, `python -m kafka.producer`, and `python -m kafka.admin`. See [Usage](https://kafka-python.readthedocs.io/en/master/usage.html) for more details.

Thread safety[](https://kafka-python.readthedocs.io/#thread-safety "Link to this heading")
-------------------------------------------------------------------------------------------

The KafkaProducer can be used across threads without issue, unlike the KafkaConsumer which cannot.

While it is possible to use the KafkaConsumer in a thread-local manner, multiprocessing is recommended.

Compression[](https://kafka-python.readthedocs.io/#compression "Link to this heading")
---------------------------------------------------------------------------------------

kafka-python supports the following compression formats:

> * gzip
>
> * LZ4
>
> * Snappy
>
> * Zstandard (zstd)

gzip is supported natively, the others require installing additional libraries. See [Install](https://kafka-python.readthedocs.io/en/master/install.html) for more information.

Optimized CRC32 Validation[](https://kafka-python.readthedocs.io/#optimized-crc32-validation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Kafka uses CRC32 checksums to validate messages. kafka-python includes a pure python implementation for compatibility. To improve performance for high-throughput applications, kafka-python will use crc32c for optimized native code if installed. See [Install](https://kafka-python.readthedocs.io/en/master/install.html) for installation instructions and [https://pypi.org/project/crc32c/](https://pypi.org/project/crc32c/) for details on the underlying crc32c lib.

Protocol[](https://kafka-python.readthedocs.io/#protocol "Link to this heading")
---------------------------------------------------------------------------------

A secondary goal of kafka-python is to provide an easy-to-use protocol layer for interacting with kafka brokers via the python repl. This is useful for testing, probing, and general experimentation. The protocol support is leveraged to enable a [`check_version()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.check_version "kafka.KafkaClient.check_version") method that probes a kafka broker and attempts to identify which version it is running (0.8.0 to 2.6+).

Debugging[](https://kafka-python.readthedocs.io/#debugging "Link to this heading")
-----------------------------------------------------------------------------------

Use python’s logging module to view internal operational events. See [https://docs.python.org/3/howto/logging.html](https://docs.python.org/3/howto/logging.html) for overview / howto.

import logging
logging.basicConfig(level=logging.DEBUG)

# Source: https://docs.confluent.io/cloud/current/client-apps/producer.md

# Source: https://docs.confluent.io/platform/current/clients/producer.md

<a id="kafka-producer-cc"></a>

<a id="kafka-producer"></a>

# Kafka Producer for Confluent Platform

An Apache KafkaÂ® Producer is a client application that publishes (writes) events to a
Kafka cluster. This section gives an overview of the Kafka producer and an
introduction to the configuration settings for tuning.

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

The Kafka producer is conceptually much simpler than the consumer
since it does not need group coordination. A producer **partitioner**
maps each message to a topic partition, and the producer sends a produce request to
the leader of that partition. The partitioners shipped with Kafka guarantee that all
messages with the same non-empty key will be sent to the same
partition.

#### IMPORTANT
If you explicitly set the partition field when creating a ProducerRecord, the default
behavior described in this section will be overridden.

If the key is provided, the partitioner will hash the key with murmur2 algorithm
and divide it by the number of partitions. The result is that the same key is
always assigned to the same partition. If a key is not provided, the partition
is assigned with awareness to batching. If a batch of records is not full and
has not yet been sent to the broker, it will select the same partition as a
prior record Partitions for newly created batches are assigned randomly. For
more information, see [KIP-480: Sticky Partitioner](https://cwiki.apache.org/confluence/display/KAFKA/KIP-480%3A+Sticky+Partitioner)
and the related [Confluent blog post](https://www.confluent.io/blog/apache-kafka-producer-improvements-sticky-partitioner/).

Each partition in the Kafka cluster has a leader and a set of replicas
among the brokers. All writes to the partition must go through the
partition leader. The replicas are kept in sync by fetching from the
leader. When the leader shuts down or fails, the next leader is
chosen from among the in-sync replicas. Depending on how the producer
is configured, each produce request to the partition leader can be
held until the replicas have successfully acknowledged the write.
This gives the producer some control over message durability at some
cost to overall throughput.

Messages written to the partition leader are not immediately readable
by consumers regardless of the producerâs acknowledgement settings.
When all in-sync replicas have acknowledged the write, then the
message is considered **committed**, which makes it available for
reading. This ensures that messages cannot be lost by a broker failure
*after* they have already been read. Note that this implies that
messages which were acknowledged by the leader only (that is, `acks=1`)
can be lost if the partition leader fails before the replicas have
copied the message. Nevertheless, this is often a reasonable
compromise in practice to ensure durability in most cases while not
impacting throughput too significantly.

Most of the subtlety around producers is tied to achieving high
throughput with batching/compression and ensuring message delivery
guarantees as mentioned above. In the next section, the
most common settings to tune producer behavior are discussed.

## Kafka Producer Configuration

The full list of configuration settings are available in [Kafka Producer Configurations](/platform/current/installation/configuration/producer-configs.html). The
key configuration settings and how they affect the producerâs behavior are
highlighted below.

### Core Configuration

These settings are the same for Java, C/C++, Python, Go and .NET clients.

- `bootstrap.servers`: You are required to set this property so that the producer can find the Kafka
  cluster.
- `client.id`: Optional, but you should set this property on each instance because it enables you to more easily correlate requests on
  the broker with the client instance which made it, which can be helpful in debugging and troubleshooting scenarios.
  You can also use client IDs to enforce client quotas. For more information, see [client quotas](/platform/current/kafka/post-deployment.html#quotas).

### Message Durability

- `acks`: You can control the durability of messages written to
  Kafka through this setting. The default value of `all` guarantees that
  not only will the partition leader accept the write, but it will be successfully
  replicated to all of the in-sync replicas. A value of `1` requires an explicit
  acknowledgement from the partition leader that the write succeeded. A value of
  `0` maximizes throughput, but you will have no guarantee that the message was
  successfully written to the brokerâs log since the broker does not send a
  response. This also means that you will not be able to determine the offset of
  the message. Note that for the C/C++, Python, Go and .NET clients, this is a
  per-topic configuration. This setting can be applied globally using the
  `default_topic_conf` sub-configuration in C/C++ and `default.topic.config`
  sub-configuration in Python, Go and .NET.

### Message Ordering

In general, messages are written to the broker
in the same order that they are received by the producer client. However,
this can change depending on some settings.

- `retries`: This setting enables message retries when set to a value larger than `0` (which is the default).
  If retries are enabled, message reordering can occur since the retry might occur after a following write
  succeeded.
- `max.in.flight.requests.per.connection`: To enable retries without reordering, set this property to `1`.
  This helps ensure that only one request can be sent to the broker at a time. Without retries enabled,
  the broker will preserve the order of writes it receives, but there
  could be gaps due to individual send failures.

### Batching and Compression

Kafka producers attempt to collect sent
messages into batches to improve throughput.

- `batch.size`: Use with the Java client to control the maximum size in bytes of each
  message batch.
- `linger.ms`: Use this setting to give more time for batches to fill by delaying the producer sending.
- `compression.type`: Enable compression with this setting. Compression covers full
  message batches, so larger batches will typically mean a higher compression ratio.
  When using snappy compression, you need write access to the `/tmp` directory. If you donât have write access to the `/tmp` directory because itâs set to `noexec`, pass in a directory path for snappy that you have write access to:
  ```none
  -Dorg.xerial.snappy.tempdir=/path/to/newtmp
  ```
- `batch.num.messages` - Use with the C/C++, Python, Go and .NET clients to set a limit on the number of messages contained
  in each batch.

### Queuing Limit

- `buffer.memory`: Use to limit the total memory
  that is available to the Java client for collecting unsent
  messages. When this limit is hit, the producer will block on
  additional sends for as long as `max.block.ms` before raising an
  exception.
- `request.timeout.ms`: Set a timeout to avoid keeping records queued indefinitely.
  If this timeout expires before a message can be successfully sent, then it will be removed
  from the queue and an exception will be thrown. The C/C++, Python, Go
  and .NET clients have similar settings.

## Producer examples

Confluent provides a number of resources to help you get started with Kafka producers.

- For a tutorial on how to build a Kafka producer that can write records to Confluent Cloud or Confluent Platform,
  see [How to build your first Apache KafkaProducer application](https://developer.confluent.io/tutorials/creating-first-apache-kafka-producer-application/confluent.html)
- For producer examples in several different languages, see
  [Build Consumer](https://developer.confluent.io/get-started/java/), and use the language selector to choose Java,
  Python, Go, .NET, JavaScript Client, C/C++, REST, Spring Boot, and more. Click **Build Producer** to see example producer code for the language you chose.

## Learn More

- For a step-by-step tutorial with thorough explanations that break down a sample Kafka Producer application, check out [How to build your first Apache KafkaProducer application](https://developer.confluent.io/tutorials/creating-first-apache-kafka-producer-application/confluent.html).
- For Hello World examples of Kafka clients in various programming languages including Java, see [Kafka Client Examples for Confluent Platform](examples-index.md#client-examples).
- To learn about the [producer API](https://developer.confluent.io/learn-kafka/apache-kafka/producers/) see the free
  [Apache Kafka 101](https://developer.confluent.io/learn-kafka/apache-kafka/) course on Confluent Developer.

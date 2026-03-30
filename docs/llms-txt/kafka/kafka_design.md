# Source: https://docs.confluent.io/kafka/design/index.md

<a id="design-overview"></a>

# Kafka Design Overview

Apache KafkaÂ® is an open-source distributed streaming system used for stream processing,
real-time data pipelines, and data integration at scale.

Kafka is designed to be able to act as a unified platform for handling
all the real-time data feeds [a large company might have](https://developer.confluent.io/what-is-apache-kafka/).
To accomplish this goal, a broad set of use cases was considered and the following requirements decided. Kafka:

- Must have high-throughput to support high volume event streams such as real-time log aggregation.
- Requires the ability to gracefully deal with large data backlogs in order to support periodic data loads from offline systems.
- Must handle low-latency delivery for more traditional messaging use-cases.

The goal for Kafka is to support partitioned, distributed, real-time
processing feeds to create new, derived feeds. This motivated Kafkaâs partitioning and consumer model.

Finally, in cases where the stream is fed into other data systems for
serving, it was important that the system would guarantee fault-tolerance in case of machine failures.

Supporting these uses led to a design with a number of unique
elements, making Kafka more like a database log than a traditional messaging system.
These elements are outlined in this section.

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

## Topics in this section

The topics in this section are an edited version of the [design documentation](https://kafka.apache.org/documentation/) on the Kafka site, and
outline some elements of Kafka design.

- [Kafka and the File System](file-system-constant-time.md#file-system) - Describes how Kafka uses the file system to maintain performance at scale.
- [Designed for Efficiency](efficient-design.md#efficient-design) - Describes how Kafka avoids byte-copying and uses batching and compression to optimize efficiency.
- [Producer Design](producer-design.md#producer-design) - Provides an in-depth view on how Producers provide load balancing and batch messages sent to brokers.
- [Consumer Design](consumer-design.md#consumer-design) - Details on why Consumers pull from the broker, and how consumer position is tracked with offsets.
- [Kafka Message Delivery Guarantees](delivery-semantics.md#delivery-semantics) - Describes how Kafka provides semantic guarantees between the broker and producers and consumers, and how
  Kafka supports exactly once delivery semantics.
- [Kafka Replication and Committed Messages](replication.md#replication) - Describes replication and new leader election enables the message guarantees provided by Kafka.
- [Kafka Log Compaction](log_compaction.md#log-compaction) - Describes how compaction enables Kafka to maintain state, and how compaction is configured.
- [Kafka Quotas](quotas.md#quotas) - Describes how and why to use client quotas in Kafka.

## Learn more

- [Building Systems Using Transactions in Apache Kafka](https://developer.confluent.io/learn/kafka-transactions-and-guarantees/)
- To learn how Kafka transactions provide you with accurate, repeatable results from chains of
  many stream processors or microservices, connected via event streams, see
  [Building Systems Using Transactions in Apache Kafka](https://developer.confluent.io/learn/kafka-transactions-and-guarantees/).
- To learn how Kafka architecture has been simplified by the introduction of Apache
  Kafka Raft Metadata mode (KRaft), see [KRaft: Apache Kafka without ZooKeeper](https://developer.confluent.io/learn/kraft/).
- To learn how serverless infrastructure is built and apply these learnings to your own projects,
  see [Cloud-Native Apache Kafka: Designing Cloud Systems for Speed and Scale](https://developer.confluent.io/learn/cloud-native-kafka/)

#### NOTE
This website includes content developed at the [Apache Software Foundation](https://www.apache.org/)
under the terms of the [Apache License v2](https://www.apache.org/licenses/LICENSE-2.0.html).

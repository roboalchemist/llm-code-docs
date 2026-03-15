# Source: https://docs.confluent.io/cloud/current/client-apps/consumer.md

# Source: https://docs.confluent.io/platform/current/clients/consumer.md

<a id="kafka-consumer"></a>

# Kafka Consumer for Confluent Platform

An Apache KafkaÂ® Consumer is a client application that subscribes to (reads and
processes) events. This section provides an overview of the Kafka consumer and an
introduction to the configuration settings for tuning.

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

The Kafka consumer works by issuing âfetchâ requests to the brokers leading
the partitions it wants to consume. The consumer offset is specified in
the log with each request. The consumer receives back a chunk of log that contains
all of the messages in that topic beginning from
the offset position. The consumer has significant control over this position and
can rewind it to re-consume data if desired.

## Consumer groups

A [consumer group](../_glossary.md#term-consumer-group) is a set of consumers that cooperate to consume
data from some topics. You set the group for a consumer by setting
its `group.id` in the properties file for the consumer.
To use the `subscribe` or  `commit` methods provided by
the [KafkaConsumer API](https://docs.confluent.io/platform/current/clients/javadocs/javadoc/index.html?org/apache/kafka/clients/consumer/package-summary.html),
you must assign the consumer to a consumer group by setting the `group.id` property.
If you donât, an exception occurs when these methods are called.

When assigned to a group, the partitions of all the topics are divided
among the consumers in the group. As new group members arrive and old
members leave, the partitions are re-assigned so that each member
receives a proportional share of the partitions. This is known as
rebalancing the group.

One of the brokers is designated as the groupâs **coordinator** and is
responsible for managing the members of the group as well as their partition
assignments. The coordinator of each group is chosen from the leaders of the
internal offsets topic, `__consumer_offsets`, which is used to store committed
offsets. Basically, the groupâs ID is hashed to one of the partitions for this
topic, and the leader of that partition is selected as the coordinator. In this
way, management of consumer groups is divided roughly equally across all the
brokers in the cluster, which allows the number of groups to scale by increasing
the number of brokers.

When the consumer starts up, it finds the coordinator for its group
and sends a request to join the group. The coordinator then begins a
group rebalance so that the new member is assigned its fair share of
the groupâs partitions. Every rebalance results in a new
**generation** of the group.

Each member in the group must send heartbeats to the coordinator in
order to remain a member of the group. If no heartbeat is received
before expiration of the configured **session timeout**, then the
coordinator will kick the member out of the group and reassign its
partitions to another member.

For a short video that describes consumer groups, group leaders, and group coordinators, watch:

<iframe width="600" height="400" src="https://www.youtube.com/embed/xbJRNwfnQb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Offset management

After the consumer receives its assignment from
the coordinator, it must determine the initial position for each
assigned partition. When the group is first created, before any
messages have been consumed, the position is set according to a
configurable offset reset policy (`auto.offset.reset`). Typically,
consumption starts either at the earliest offset or the latest offset.

As a consumer in the group reads messages from the partitions assigned
by the coordinator, it must commit the offsets corresponding to the
messages it has read. If the consumer crashes or is shut down, its
partitions will be re-assigned to another member, which will begin
consumption from the last committed offset of each partition. If the
consumer crashes before any offset has been committed, then the
consumer which takes over its partitions will use the reset policy.

The offset commit policy is crucial to providing the message delivery
guarantees needed by your application. By default, the consumer is
configured to use an automatic commit policy, which triggers a commit
on a periodic interval. The consumer also supports a commit API which
can be used for manual offset management. Correct offset management
is crucial because it affects [delivery semantics](/platform/current/streams/concepts.html#streams-concepts-processing-guarantees).

By default, the consumer is configured
to auto-commit offsets. The `auto.commit.offset.interval`  property sets the upper time bound of the
commit interval.
Using auto-commit offsets can give you âat-least-onceâ delivery, but you must consume all data
returned from a `ConsumerRecords<K, V> poll(Duration timeout)` call before any subsequent `poll` calls, or before closing the consumer.

To explain further; when auto-commit is enabled, every time the `poll` method is called and data is fetched,
the consumer is ready to automatically commit the offsets of messages that have been returned by the poll.
If the processing of these messages is not completed before the next auto-commit interval,
thereâs a risk of losing the messageâs progress if the consumer crashes or is otherwise restarted.
In this case, when the consumer restarts, it will begin consuming from the last committed offset.
When this happens, the last committed position can be as old as the auto-commit interval.
Any messages that have arrived since the last commit are read again.

If you want to reduce the window for duplicates, you can
reduce the auto-commit interval, but some users may want even finer
control over offsets. The consumer therefore supports a commit API
which gives you full control over offsets. Note that when you use the commit API directly, you should first
disable auto-commit in the configuration by setting the
`enable.auto.commit` property to `false`.

Each call to the commit API results in an offset commit request being
sent to the broker. Using the synchronous API, the consumer is blocked
until that request returns successfully. This may reduce overall
throughput since the consumer might otherwise be able to process
records while that commit is pending.

One way to deal with this is to increase the amount of data that is returned
when polling. The consumer has a configuration setting `fetch.min.bytes` which
controls how much data is returned in each fetch. The broker will hold on to
the fetch until enough data is available (or `fetch.max.wait.ms` expires).
The tradeoff, however, is that this also increases the amount of duplicates
that have to be dealt with in a worst-case failure.

A second option is to use asynchronous commits. Instead of waiting for
the request to complete, the consumer can send the request and return
immediately by using asynchronous commits.

So if it helps performance, why not always use asynchronous commits? The main
reason is that the consumer does not retry the request if the commit fails.
This is something that committing synchronously gives you for free; it will
will retry indefinitely until the commit succeeds or an unrecoverable
error is encountered. The problem with asynchronous commits is dealing
with commit ordering. By the time the consumer finds out that a commit
has failed, you may already have processed the next batch of messages
and even sent the next commit. In this case, a retry of the old commit
could cause duplicate consumption.

Instead of complicating the consumer internals to try and handle this
problem in a sane way, the API gives you a callback which is invoked
when the commit either succeeds or fails. If you like, you can use
this callback to retry the commit, but you will have to deal with the
same reordering problem.

Offset commit failures are merely annoying if the following commits
succeed since they wonât actually result in duplicate reads. However,
if the last commit fails before a rebalance occurs or before the
consumer is shut down, then offsets will be reset to the last commit
and you will likely see duplicates. A common pattern is therefore to
combine async commits in the poll loop with sync commits on rebalances
or shut down. Committing on close is straightforward, but you need a way
to hook into rebalances.

Each rebalance has two phases: partition revocation and partition
assignment. The revocation method is always called before a rebalance
and is the last chance to commit offsets before the partitions are
re-assigned. The assignment method is always called after the
rebalance and can be used to set the initial position of the assigned
partitions. In this case, the revocation hook is used to commit the
current offsets synchronously.

In general, asynchronous commits should be considered less safe than
synchronous commits. Consecutive commit failures before a crash will
result in increased duplicate processing. You can mitigate this danger
by adding logic to handle commit failures in the callback or by mixing
occasional synchronous commits, but you shouldnât add too
much complexity unless testing shows it is necessary. If you need more
reliability, synchronous commits are there for you, and you can still
scale up by increasing the number of topic partitions and the number
of consumers in the group. But if you just want to maximize throughput
and youâre willing to accept some increase in the number of
duplicates, then asynchronous commits may be a good option.

A somewhat obvious point, but one thatâs worth making is that
asynchronous commits only make sense for âat least onceâ message
delivery. To get âat most once,â you need to know if the commit
succeeded before consuming the message. This implies a synchronous
commit unless you have the ability to âunreadâ a message after you
find that the commit failed.

In the examples, we
show several detailed examples of the commit API and discuss the
tradeoffs in terms of performance and reliability.

When writing to an external system, the consumerâs position must be coordinated
with what is stored as output. That is why the consumer stores its offset in the
same place as its output. For example, a connector populates data in HDFS along
with the offsets of the data it reads so that it is guaranteed that either data
and offsets are both updated, or neither is. A similar pattern is followed for
many other data systems that require these stronger semantics, and for which the
messages do not have a primary key to allow for deduplication.

This is how Kafka supports [exactly-once processing](/platform/current/streams/concepts.html#streams-concepts-processing-guarantees) in
Kafka Streams, and the transactional producer or consumer can be used generally to
provide exactly-once delivery when transferring and processing data between Kafka
topics. Otherwise, Kafka guarantees at-least-once delivery by default, and you
can implement at-most-once delivery by disabling retries on the producer and
committing offsets in the consumer prior to processing a batch of messages.

## Kafka consumer configuration

The full list of configuration settings are available in
[Kafka Consumer Configurations](/platform/current/installation/configuration/consumer-configs.html).
Several of the key configuration settings and how they affect the consumerâs
behavior are highlighted below.

### Core configuration

Following are some important consumer properties:

- `bootstrap.servers`: You are required to set this property so that the consumer can find the Kafka
  cluster.
- `client.id`: Optional, but you should set this property to easily correlate requests on the broker with
  the client instance which made it. Typically, all consumers within the
  same group will share the same client ID in order to enforce [client quotas](/platform/current/kafka/post-deployment.html#quotas).

<a id="consumer-group-config"></a>

### Group configuration

The following properties apply to consumer groups.

- `group.id`: Optional but you should always configure a group ID unless
  you are using the simple assignment API and you donât need to store
  offsets in Kafka.
- `session.timeout.ms`:  Control the session timeout by overriding this value. The default is 10 seconds in the C/C++ and Java
  clients, but you can increase the time to avoid excessive rebalancing, for example
  due to poor network connectivity or long GC pauses. The main drawback to using a larger session timeout is that it will
  take longer for the coordinator to detect when a consumer instance has
  crashed, which means it will also take longer for another consumer in
  the group to take over its partitions. For normal shutdowns, however,
  the consumer sends an explicit request to the coordinator to leave the
  group which triggers an immediate rebalance.
- `heartbeat.interval.ms`: This controls how often the consumer will
  send heartbeats to the coordinator. It is also the way that the
  consumer detects when a rebalance is needed, so a lower heartbeat
  interval will generally mean faster rebalancing. The default setting is
  three seconds. For larger groups, it may be wise to increase this
  setting.
- `max.poll.interval.ms`: This property specifies the maximum time allowed time between
  calls to the consumers poll method (`Consume` method in .NET) before the consumer
  process is assumed to have failed.
  The default is 300 seconds and can be safely increased if your application
  requires more time to process messages. If you are using the Java consumer, you can also
  adjust `max.poll.records` to tune the number of records that are handled on every
  loop iteration.

### Offset management configuration

There are two main settings for offset management; whether auto-commit is enabled and the
offset reset policy.

- `enable.auto.commit`: This setting enables auto-commit (the default), which means the consumer
  automatically commit offsets periodically at the interval set by `auto.commit.interval.ms`. The
  default interval is 5 seconds.
- `auto.offset.reset`: Defines the behavior of the consumer when there is no
  committed position (which occurs when the group is first initialized) or when
  an offset is out of range. There are several ways to set the offset. You can
  choose either to reset the position to the `earliest` offset or the
  `latest` offset (the default). You can also reset to a configured
  `duration` from the current timestamp.

### Partition assignment configuration

`partition.assignment.strategy` sets the partition assignment strategy for a consumer, meaning how partition ownership
is distributed between consumer instances when group management is used. All consumers in the same consumer
group must have the same partition strategy.

The `partition.assignment.strategy` parameter is not supported when the
consumer group protocol, `group.protocol=consumer`, is enabled. This
configuration applies only when using the classic consumer group protocol,
`group.protocol=classic`, which is the default.

[partition.assignment.strategy](/platform/current/installation/configuration/consumer-configs.html#partition-assignment-strategy) accepts a comma-separated list of fully qualified class names that implement the
[PartitionAssignor](/platform/current/clients/javadocs/javadoc/org/apache/kafka/clients/consumer/ConsumerPartitionAssignor.html) interface.
The list enables you to update the strategy for a group, while temporarily
keeping the old one for consumers that have not transitioned to the new strategy yet.

When you configure Kafka consumers, the choice of assignment strategy is important and depends on the specific requirements
for partition balancing, consumer group stability, and rebalance behavior.
In most cases, the default (range assignment) works well, but for specific use cases, changing the assignment strategy can significantly
impact performance and reliability.

Available options are:

* Range Assignment (Default)
  - How it Works: The `org.apache.kafka.clients.consumer.RangeAssignor` works by evenly distributing partitions of each topic across the consumers in a consumer group. It sorts both the partitions and consumers. Partitions are assigned to consumers in chunks (ranges), aiming for an even distribution.
  - Advantages: It works well when partition count is higher than consumer count, providing a simple and efficient means of partition distribution.
  - Disadvantages: Can result in uneven load distribution if the number of partitions is not a multiple of the number of consumers.
* Round Robin Assignment
  - How it Works: The `org.apache.kafka.clients.consumer.RoundRobinAssignor` distributes partitions across all consumers one by one in a round-robin fashion.
    It ensures a more even distribution of partitions across consumers, regardless of the number of partitions.
  - Advantages: Leads to a more balanced partition allocation across consumers,
    useful when handling a varying number of partitions or when partitions have significantly different sizes.
  - Disadvantages: May lead to more rebalances compared to Range Assignment in some scenarios.
* Sticky Assignor
  - How it Works: The `org.apache.kafka.clients.consumer.StickyAssignor` aims to maintain a stable partition assignment
    while still balancing the partitions across consumers. It tries to keep the previously assigned partitions to a consumer as unchanged as possible if a rebalance occurs.
  - Advantages: It minimizes the number of partition reassignments across rebalances,
    reducing the potential for missed messages or duplicated processing.
  - Disadvantages: While it offers stability, it might not always result in the
    most balanced partition distribution if the cluster or consumer group changes frequently.
* Cooperative Sticky Assignor
  - How it Works: An evolution of the StickyAssignor, the `org.apache.kafka.clients.consumer.CooperativeStickyAssignor` enables
    more incremental rebalancing, which can reduce the latency and resources required during the rebalance process.
  - Advantages: It supports more granular changes to the consumer group memberships
    or to the partitions themselves, making rebalances less impactful. Note that this assignor reduces
    rebalance *impact*, not the frequency of rebalances. For consumer groups where all members subscribe to the same set of topics, the `org.apache.kafka.clients.consumer.ConstrainedCooperativeStickyAssignor` provides the same benefits and is optimized for this common scenario.
  - Disadvantages: Not all consumers or versions of Kafka support this assignor; requires careful
    management to ensure compatibility across the consumer group.

### Upgrade to CooperativeStickyAssignor

To migrate an existing consumer group from an eager rebalance assignor (for
example, `RangeAssignor` or `StickyAssignor`) to the cooperative protocol
introduced by [KIP-429: Kafka Consumer Incremental Rebalance Protocol](https://cwiki.apache.org/confluence/display/KAFKA/KIP-429%3A+Kafka+Consumer+Incremental+Rebalance+Protocol),
use a two-step rolling bounce to minimize disruption during the transition.
After completing step 1 (configuring dual assignors), the consumer group operates
in a mixed-mode period where members that still use an eager assignor continue
to perform full-stop rebalances. After completing step 2 (switching to the cooperative
assignor), rebalances become incremental and avoid full-stop rebalances.

#### NOTE
`CooperativeStickyAssignor` requires Kafka client version 2.4.0 or later.
Ensure all consumers in your group meet this version requirement before
beginning the upgrade.

1. Prepare (dual list, keep current first).

   Set [partition.assignment.strategy](/platform/current/installation/configuration/consumer-configs.html#partition-assignment-strategy)
   to include both your current assignor and `CooperativeStickyAssignor`, with
   the current assignor listed first. Perform a rolling restart so all members
   pick up the new list. The coordinator will continue to select the first commonly
   supported assignor (the existing one), so there is no behavior change yet.

   Example properties:
   ```properties
   partition.assignment.strategy=org.apache.kafka.clients.consumer.StickyAssignor,org.apache.kafka.clients.consumer.CooperativeStickyAssignor
   ```

   Fully qualified class names shown here refer to the Java consumer. For other
   client libraries, configure the equivalent assignor using the clientâs
   configuration API.

   Example Java configuration:
   ```java
   props.put(ConsumerConfig.PARTITION_ASSIGNMENT_STRATEGY_CONFIG,
             Arrays.asList(StickyAssignor.class.getName(),
                           CooperativeStickyAssignor.class.getName()));
   ```
2. Switch (make cooperative first or only).

   After all members have been upgraded to client versions that support cooperative
   rebalancing, update the configuration to make `CooperativeStickyAssignor`
   the first (or only) value and roll the group again. The coordinator then
   selects cooperative rebalancing and the group transitions incrementally
   with minimal disruption.

   Example properties:
   ```properties
   partition.assignment.strategy=org.apache.kafka.clients.consumer.CooperativeStickyAssignor
   ```

   Fully qualified class names shown here refer to the Java consumer. For other
   client libraries, configure the equivalent assignor using the clientâs
   configuration API.

   Example Java configuration:
   ```java
   props.put(ConsumerConfig.PARTITION_ASSIGNMENT_STRATEGY_CONFIG,
             Collections.singletonList(CooperativeStickyAssignor.class.getName()));
   ```

   Verify the switch: after the rollout, check consumer application logs for messages indicating the selected partition assignor (for example, âUsing partition assignor class â¦CooperativeStickyAssignorâ).

#### Notes

- All members in the group must advertise a compatible, ordered list of assignors.
  The coordinator selects the first assignor that is present in every memberâs list.
- Do not switch to listing only `CooperativeStickyAssignor` until all members run
  client versions that support it (2.4.0 or later); otherwise the group fails to
  find a common assignor.
- Static membership (`group.instance.id`) further reduces movement during
  restarts and pairs well with cooperative rebalancing. In Kubernetes environments,
  use StatefulSets to provide stable pod identities that can serve as static member IDs.
- If using manual offset commits (`enable.auto.commit=false`), handle
  `RebalanceInProgressException` by calling `poll()` in the next loop iteration
  to complete the rebalancing process.
- For background and the detailed upgrade rationale, see
  [KIP-429: Kafka Consumer Incremental Rebalance Protocol](https://cwiki.apache.org/confluence/display/KAFKA/KIP-429%3A+Kafka+Consumer+Incremental+Rebalance+Protocol)
  (see the âCompatibility and Upgrade Pathâ section).

## Message handling

While the Java consumer does all IO and processing in the foreground
thread, librdkafka-based clients (C/C++, Python, Go and C#) use a background
thread. The main consequence of this is that polling is totally safe when used from multiple
threads. You can use this to parallelize message handling in multiple threads.
From a high level, poll is taking messages off of a queue which is filled in the background.

Another consequence of using a background thread is that all heartbeats and rebalancing
are executed in the background. The benefit of this is that you donât need to worry
about message handling causing the consumer to âmissâ a rebalance. The drawback,
however, is that the background thread will continue heart beating even if your message
processor dies. If this happens, then the consumer will continue to hold on to its
partitions and the read lag will continue to build until the process is shut down.

Although the clients have taken different approaches internally, they are not as far
apart as they seem. To provide the same abstraction in the Java client, you could
place a queue in between the poll loop and the message processors. The poll loop would fill the
queue and the processors would pull messages off of it.

<a id="kafka-consumer-describe-group"></a>

## Kafka consumer group tool

Kafka includes the `kafka-consumer-groups` command-line utility to view and manage consumer groups, which is also provided
with Confluent Platform. Find the tool in the `bin` folder under your installation directory.

You can also use the Confluent CLI to complete some of these tasks.
For more information, see the [Confluent CLI reference](https://docs.confluent.io/confluent-cli/current/command-reference/kafka/consumer/group/index.html).

### List consumer groups

You can get a list of the active groups in the cluster using the `kafka-consumer-groups`  tool. On
a large cluster, this may take a while since it collects
the list by inspecting each broker in the cluster.

```bash
bin/kafka-consumer-groups --bootstrap-server host:9092 --list
```

Your output will be a list of list of all consumer groups for the cluster, including consumers for
internal use.
The output might resemble:

```bash
_confluent-controlcenter-7-6-0-1
ConfluentTelemetryReporterSampler--4418883999569981189
test-1234
_confluent-controlcenter-7-6-0-lastProduceTimeConsumer
_confluent-controlcenter-7-6-0-1-command
```

To use the Confluent CLI for this task, see
[confluent kafka consumer group list](https://docs.confluent.io/confluent-cli/current/command-reference/kafka/consumer/group/confluent_kafka_consumer_group_list.html).

### Describe groups

The `kafka-consumer-groups` tool can also be used to collect
information on a current group. For example, to see the current
assignments for the `test-1234` group, you could use the following command:

```bash
bin/kafka-consumer-groups --bootstrap-server host:9092 --describe --group test-1234
```

The output from this command will list the clients, topics, partitions and more for that group.
The output might resemble:

```bash
GROUP      TOPIC        PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID        HOST            CLIENT-ID
test-1234  test-metrics 5          258420          258519          -               test-client-1234    /127.0.0.1     test-client
test-1234  test-metrics 10         257002          257097          -               test-client-1234    /127.0.0.1     test-client
test-1234  test-metrics 4          259580          259660          -               test-client-1234    /127.0.0.1     test-client
test-1234  test-metrics 7          254004          254131          -               test-client-1234    /127.0.0.1     test-client
```

If you happen to invoke this while a rebalance is in progress, the
command will report an error. Retry again and you should see the
assignments for all the members in the current generation.

To use the Confluent CLI for this task, see
[confluent kafka consumer group describe](https://docs.confluent.io/confluent-cli/current/command-reference/kafka/consumer/group/confluent_kafka_consumer_group_describe.html).

### Reset offsets

You can also use this tool to reset the [consumer offset](../_glossary.md#term-consumer-offset) in scenarios where a consumer is stalled or significantly lagging.
Make sure you deactivate the consumer before you reset its offset.
You have many options for changing the offset.
For example, you can reset offsets by shifting forward or backward with `shift-by` or reset them to the beginning with `--to-earliest`.
For all the options, see the [kafka-consumer-group tool usage details](/kafka/operations-tools/kafka-tools.html#kafka-consumer-groups-sh).

To reset the offsets back by 20 positions, use the following command:

```bash
bin/kafka-consumer-groups.sh --bootstrap-server host:9092 --group test-1234 --reset-offsets --shift-by -20 --topic test-metrics -execute --group test-1234
```

The output will contain the group, topic and partitions, and the new offset for each:

```bash
GROUP             TOPIC                          PARTITION  NEW-OFFSET
test-1234         test-metrics                   5          258400
test-1234         test-metrics                   10         256082
test-1234         test-metrics                   4          259560
test-1234         test-metrics                   7          254984
```

## Consumer examples

Confluent provides a number of resources to help you get started with Kafka consumers.

- For a tutorial on how to build a Kafka consumer that can read records from Confluent Cloud or Confluent Platform,
  see [How to build your first Apache KafkaConsumer application](https://developer.confluent.io/tutorials/creating-first-apache-kafka-consumer-application/confluent.html)
- For consumer examples in several different languages, see
  [Get Started](https://developer.confluent.io/get-started/java/), and use the language selector to choose Java,
  Python, Go, .NET, JavaScript Client, C/C++, REST, Spring Boot, and more.
  Click **Build Consumer** in the navigation menu to see example consumer code for the language you chose.
- Use **Confluent for VS Code** to generate a consumer project for you. You can
  choose from these languages:
  - Java
  - Go
  - Python

  For more information, see [Confluent for VS Code with Confluent Cloud](/cloud/current/client-apps/vs-code-extension.html)
  and [Confluent for VS Code with Confluent Platform](/platform/current/clients/vs-code-extension.html).

## Related content

- [Consumer Design](/kafka/design/consumer-design.html)
- For a step-by-step tutorial with thorough explanations that break down a sample Kafka Consumer application, check out
  [How to build your first Apache KafkaConsumer application](https://developer.confluent.io/tutorials/creating-first-apache-kafka-consumer-application/confluent.html).
- For Hello World examples of Kafka clients in various programming languages including Java, see
  [Code Examples for Apache Kafka](https://developer.confluent.io/get-started/).
- To see examples of consumers written in various languages, see [Kafka Client Examples for Confluent Platform](examples-index.md#client-examples).
- Blog post: [Apache Kafka Data Access Semantics: Consumers and Membership](https://www.confluent.io/blog/apache-kafka-data-access-semantics-consumers-and-membership/)
- Free course: [Apache Kafka 101](https://developer.confluent.io/learn-kafka/apache-kafka/consumers)
- Interactive diagram: [Kafka Internals](https://developer.confluent.io/#kafka-internals)
- Confluent Support: [How to reset an offset for a specific consumer group](https://support.confluent.io/hc/en-us/articles/360040784511)

# Source: https://docs.datadoghq.com/tracing/guide/monitor-kafka-queues.md

---
title: Monitoring Kafka Queues
description: >-
  Learn how to monitor Kafka queues with APM tracing to track message
  processing, performance, and data flow through your messaging systems.
breadcrumbs: Docs > APM > Tracing Guides > Monitoring Kafka Queues
---

# Monitoring Kafka Queues

## Overview{% #overview %}

In event-driven pipelines, queuing and streaming technologies such as Kafka are essential to the successful operation of your systems. Ensuring that messages are being reliably and quickly conveyed between services can be difficult due to the many technologies and teams involved in such an environment. The Datadog Kafka integration and APM enable your team to monitor the health and efficiency of your infrastructure and pipelines.

### The Kafka integration{% #the-kafka-integration %}

Visualize the performance of your cluster in real time and correlate the performance of Kafka with the rest of your applications by using [the Datadog Kafka integration](https://docs.datadoghq.com/integrations/kafka). Datadog also provides a [MSK integration](https://docs.datadoghq.com/integrations/amazon_msk/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/monitor_kafka_queues/kafka_dashboard.2f4e352fc1cf2586d33477b08788bdbb.png?auto=format"
   alt="Kafka Dashboard" /%}

### Data Stream Monitoring{% #data-stream-monitoring %}

[Datadog Data Streams Monitoring](https://app.datadoghq.com/data-streams/onboarding) provides a standardized method for your teams to measure pipeline health and end-to-end latencies for events traversing your system. The deep visibility offered by Data Streams Monitoring enables you to pinpoint faulty producers, consumers, or queues driving delays and lag in the pipeline. You can discover hard-to-debug pipeline issues such as blocked messages, hot partitions, or offline consumers. And you can collaborate seamlessly across relevant infrastructure or app teams.

{% video
   url="https://datadog-docs.imgix.net/images/tracing/guide/monitor_kafka_queues/dash-2022-data-streams-compressed-blurb2.mp4" /%}

### Distributed traces{% #distributed-traces %}

APM's distributed tracing gives you expanded visibility into the performance of your services by measuring request volume and latency. Create graphs and alerts to monitor your APM data, and visualize the activity of a single request in a flame graph, like the one shown below, to better understand the sources of latency and errors.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/monitor_kafka_queues/kafka_trace.bfaa97abce5946a568f6b65daecd9e0d.png?auto=format"
   alt="A Kafka consumer span" /%}

APM can automatically trace requests to and from Kafka clients. This means you can collect traces without modifying your source code. Datadog injects headers in the Kafka messages so as to propagate the context of the trace from the producer to the consumer.

Check which Kafka libraries are supported in our [compatibility pages](https://docs.datadoghq.com/tracing/trace_collection/compatibility/).

#### Setup{% #setup %}

To trace Kafka applications, Datadog traces the producing and consuming calls within the Kafka SDK. So to monitor Kafka, you just have to setup APM on your services. See [the APM trace collection documentation](https://docs.datadoghq.com/tracing/trace_collection/) for guidance on getting started with APM and distributed tracing.

## Monitor your application in APM{% #monitor-your-application-in-apm %}

A classic Kafka setup shows a trace with a producer span, and as a child, a consumer span. Any work that generates a trace in the consumption side is represented by child spans of the consumer span. Each span has a set of tags with the `messaging` prefix. The following table describes the tags you can find on Kafka spans.

{% alert level="info" %}
To get a more global understanding of spans metadata in Datadog, read [Span Tags Semantics](https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention).
{% /alert %}

| **Name**                         | **Type** | **Description**                                                                                                                                                                                                                 |
| -------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `messaging.system`               | `string` | `Kafka`                                                                                                                                                                                                                         |
| `messaging.destination`          | `string` | The topic the message is sent to.                                                                                                                                                                                               |
| `messaging.destination_kind`     | `string` | `Queue`                                                                                                                                                                                                                         |
| `messaging.protocol`             | `string` | The name of the transport protocol.                                                                                                                                                                                             |
| `messaging.protocol_version`     | `string` | The version of the transport protocol.                                                                                                                                                                                          |
| `messaging.url`                  | `string` | The connection string to the messaging system.                                                                                                                                                                                  |
| `messaging.message_id`           | `string` | A value used by the messaging system as an identifier for the message, represented as a string.                                                                                                                                 |
| `messaging.conversation_id`      | `string` | The conversation ID for the conversation that the message belongs to, represented as a string.                                                                                                                                  |
| `messaging.message_payload_size` | `number` | The size of the uncompressed message payload in bytes.                                                                                                                                                                          |
| `messaging.operation`            | `string` | A string identifying the kind of message consumption.Examples: `send` (a message sent to a producer), `receive` (a message is received by a consumer), or `process` (a message previously received is processed by a consumer). |
| `messaging.consumer_id`          | `string` | `{messaging.kafka.consumer_group} - {messaging.kafka.client_id}` if both are present.`messaging.kafka.consumer_group` if not.                                                                                                   |
| `messaging.kafka.message_key`    | `string` | Message keys in Kafka are used for grouping alike messages to ensure they're processed on the same partition.They differ from `messaging.message_id` in that they're not unique.                                                |
| `messaging.kafka.consumer_group` | `string` | Name of the Kafka Consumer Group that is handling the message. Only applies to consumers, not producers.                                                                                                                        |
| `messaging.kafka.client_id`      | `string` | Client ID for the Consumer or Producer that is handling the message.                                                                                                                                                            |
| `messaging.kafka.partition`      | `string` | Partition the message is sent to.                                                                                                                                                                                               |
| `messaging.kafka.tombstone`      | `string` | A Boolean that is true if the message is a tombstone.                                                                                                                                                                           |
| `messaging.kafka.client_id`      | `string` | Client ID for the Consumer or Producer that is handling the message.                                                                                                                                                            |

## Special use cases{% #special-use-cases %}

{% tab title="Java" %}
See [Java's tracer documentation](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/#networking-framework-compatibility) for configuration of Kafka.
{% /tab %}

{% tab title=".NET" %}
The [Kafka .NET Client documentation](https://docs.confluent.io/kafka-clients/dotnet/current/overview.html#the-consume-loop) states that a typical Kafka consumer application is centered around a consume loop, which repeatedly calls the Consume method to retrieve records one-by-one. The `Consume` method polls the system for messages. Thus, by default, the consumer span is created when a message is returned and closed before consuming the next message. The span duration is then representative of the computation between one message consumption and the next.

When a message is not processed completely before consuming the next one, or when multiple messages are consumed at once, you can set `DD_TRACE_KAFKA_CREATE_CONSUMER_SCOPE_ENABLED` to `false` in your consuming application. When this setting is `false`, the consumer span is created and immediately closed. If you have child spans to trace, follow [the headers extraction and injection documentation for .NET custom instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/dotnet/#headers-extraction-and-injection) to extract the trace context.

The .NET tracer allows tracing Confluent.Kafka since [v1.27.0](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v1.27.0). The trace context propagation API is available since [v2.7.0](https://github.com/DataDog/dd-trace-dotnet/releases/tag/v2.7.0).
{% /tab %}

{% tab title="Ruby" %}
The Kafka integration provides tracing of the `ruby-kafka` gem. Follow [Ruby's tracer documentation](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby/#kafka) to enable it.
{% /tab %}

### Disable tracing for Kafka{% #disable-tracing-for-kafka %}

If you want to disable Kafka tracing on an application, set the appropriate [language-specific configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/).

## Further reading{% #further-reading %}

- [Set up trace collection](https://docs.datadoghq.com/tracing/trace_collection)
- [Kafka integration](https://docs.datadoghq.com/integrations/kafka)
- [Data Streams Monitoring](https://docs.datadoghq.com/data_streams/)

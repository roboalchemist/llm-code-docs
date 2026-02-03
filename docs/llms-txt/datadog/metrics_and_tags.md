# Source: https://docs.datadoghq.com/data_streams/metrics_and_tags.md

---
title: Metrics and Tags
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Data Streams Monitoring > Metrics and Tags
---

# Metrics and Tags

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Data Streams Monitoring is not available for the  site.
{% /alert %}


{% /callout %}

This document discusses the following Data Streams Monitoring metrics and their tags:

- `data_streams.latency`
- `data_streams.kafka.lag_seconds`
- `data_streams.kafka.lag_messages`
- `data_streams.sqs.dead_letter_queue.messages`
- `data_streams.payload_size`

### data_streams.latency{% #data_streamslatency %}

This metric measures latency between two points in the pipeline. The value can represent different types of latency, depending on its tags.

{% dl %}

{% dt %}
`pathway_type`
{% /dt %}

{% dd %}
What information the metric value represents. Possible pathway types:
- `full`: end-to-end latency between data origin (`start`) and another point (`end`) in the pipeline
  - `start` tag: data origin
  - `end` tag: arbitrary point where data is last tracked
- `edge`: latency between two services, connected through a queue or directly over HTTP/gRPC. Measures duration between time of produce in the producer (`start`) and time of consume in the consumer (`end`)
  - `start` tag: the upstream producer service
  - `end` tag: the downstream consumer service
- `partial_edge`: latency between a service and a queue, if the producer or consumer is not known (that is, not instrumented with Data Streams Monitoring)
  - `start` tag: the upstream producer service/queue
  - `end` tag: the downstream consumer service/queue
- `internal`: latency within the service. Measures time between *consume* and the folllowing *produce* operation.

{% /dd %}

{% dt %}
`start`
{% /dt %}

{% dd %}
The name of the node where Data Streams Monitoring first detects the payload. This node can be a service (the original producer) or a queue (the original producer is not known to Data Streams Monitoring).When the `pathway_type` tag is set to `full` (end-to-end latency), `start` always refers to the start of the pipeline.For example:
{% image
   source="https://datadog-docs.imgix.net/images/data_streams/dsm_pipeline.c7ea229b48395e2cec391e1c5bb56377.png?auto=format"
   alt="Diagram of a pipeline that flows from 'Service A' to 'Queue A' to 'Service B' to 'Queue B' to 'Service C'." /%}
The query `start:serviceA and end:serviceC and pathway_type:full` measures end-to-end latency for this pipeline.The query `start:serviceB and end:serviceC and pathway_type:full` **does not** measure latency for this pipeline, as there is no data originating at Service B.
{% /dd %}

{% dt %}
`end`
{% /dt %}

{% dd %}
The name of a node where the pipeline ends. You can use `end` to get data for partial pipelines.For example:
{% image
   source="https://datadog-docs.imgix.net/images/data_streams/dsm_pipeline.c7ea229b48395e2cec391e1c5bb56377.png?auto=format"
   alt="Diagram of a pipeline that flows from 'Service A' to 'Queue A' to 'Service B' to 'Queue B' to 'Service C'." /%}
You can use `start:serviceA and end:serviceB and pathway_type:full` to measure the first part of this pipeline.
{% /dd %}

{% dt %}
`service`
{% /dt %}

{% dd %}
The name of the service where data is collected.
{% /dd %}

{% dt %}
`type`
{% /dt %}

{% dd %}
The name of the queueing technology for which the data is generated, for example: Kafka, RabbitMQ, SQS. For HTTP and gRPC, `type` is set to `http` or `grpc`.
{% /dd %}

{% dt %}
`topic`
{% /dt %}

{% dd %}
The name of the topic the data is produced to or consumed from, if any.
{% /dd %}

{% dt %}
`direction`
{% /dt %}

{% dd %}
The direction of data flow for a particular `service`. Possible values:
- `in`: the consume operation or serving data over HTTP/gRPC
- `out`: the produce operation or sending data over HTTP/gRPC

{% /dd %}

{% dt %}
`env`
{% /dt %}

{% dd %}
Environment in which the service is running
{% /dd %}

{% dt %}
`pathway`
{% /dt %}

{% dd %}
An ordered list of services, separated by `/`, that the data travels through. If the data goes through the same service multiple times consecutively, the service name is added only once.
{% /dd %}

{% dt %}
`detailed_pathway`
{% /dt %}

{% dd %}
An ordered list of services and queues, separated by `/`, that the data travels through. The same as `pathway` but with queues in addition to services.
{% /dd %}

{% dt %}
`visited_queues`
{% /dt %}

{% dd %}
Represents all queues the data goes through. (Queues directly at the start or end of the pipeline are excluded.) You can use this tag to make your query more specific if your data is flowing through multiple queues.Consider the following pipeline:
{% image
   source="https://datadog-docs.imgix.net/images/data_streams/visited-queues-disambiguation.70eaab887ca783de30b6d5ba57e33b7a.png?auto=format"
   alt="Diagram of a pipeline that flows from 'Service A', splits into two ('Queue A' and 'Queue B'), and merges at 'Service B'." /%}
To measure data flow from Service A to Queue A to Service B, you can query `start:serviceA and end:serviceB and visited_queues:queueA`.To measure data flow from Service A to Queue B to Service B, you can query `start:serviceA and end:serviceB and visited_queues:queueB`.
{% /dd %}

{% dt %}
`visited_services`
{% /dt %}

{% dd %}
Represents all services the data goes through. (Services directly at the start or end of the pipeline are excluded.)
{% /dd %}

{% dt %}
`upstream_service`
{% /dt %}

{% dd %}
The name of the service upstream from a particular `service`.
{% /dd %}

{% dt %}
`exchange`
{% /dt %}

{% dd %}
For RabbitMQ, the name of the exchange the data went to.
{% /dd %}

{% dt %}
`hash`
{% /dt %}

{% dd %}
A unique identifier, computed using various tag values (`type`, `service`, `direction`, `parent_hash`, and others).
{% /dd %}

{% dt %}
`parent_hash`
{% /dt %}

{% dd %}
The `hash` of the node upstream from the node on the pathway.
{% /dd %}

{% /dl %}

### data_streams.kafka.lag_seconds{% #data_streamskafkalag_seconds %}

This metric represents the lag (in seconds) between the last produce and consume operations.

{% dl %}

{% dt %}
`partition`
{% /dt %}

{% dd %}
The Kafka partition.
{% /dd %}

{% dt %}
`env`
{% /dt %}

{% dd %}
The environment in which the consumer service is running.
{% /dd %}

{% dt %}
`topic`
{% /dt %}

{% dd %}
The Kafka topic.
{% /dd %}

{% dt %}
`consumer_group`
{% /dt %}

{% dd %}
The Kafka consumer group.
{% /dd %}

{% /dl %}

### data_streams.kafka.lag_messages{% #data_streamskafkalag_messages %}

This metric represents the lag (in offsets) between the last produce and consume operations.

{% dl %}

{% dt %}
`partition`
{% /dt %}

{% dd %}
The Kafka partition.
{% /dd %}

{% dt %}
`env`
{% /dt %}

{% dd %}
The environment in which the consumer service is running.
{% /dd %}

{% dt %}
`topic`
{% /dt %}

{% dd %}
The Kafka topic.
{% /dd %}

{% dt %}
`consumer_group`
{% /dt %}

{% dd %}
The Kafka consumer group.
{% /dd %}

{% /dl %}

### data_streams.payload_size{% #data_streamspayload_size %}

This metric is a distribution metric representing the message size distribution in bytes of messages going through the Data Streams. The tags are the same as for the `data_streams.latency` metric.

### data_streams.sqs.dead_letter_queue.messages{% #data_streamssqsdead_letter_queuemessages %}

This metric represents the number of a messages in an SQS dead-letter queue. It is used to to measure the number of dead-lettered messages for a given queue.

{% dl %}

{% dt %}
`arn`
{% /dt %}

{% dd %}
The ARN (Amazon Resource Name) of the queue.
{% /dd %}

{% dt %}
`aws_account`
{% /dt %}

{% dd %}
The AWS Account number of the queue (and dead-letter queue).
{% /dd %}

{% dt %}
`dlq`
{% /dt %}

{% dd %}
The ARN of the dead letter queue that messages are being sent to.
{% /dd %}

{% dt %}
`queue`
{% /dt %}

{% dd %}
The name of the queue.
{% /dd %}

{% dt %}
`region`
{% /dt %}

{% dd %}
The AWS region of the queue (and dead-letter queue).
{% /dd %}

{% /dl %}

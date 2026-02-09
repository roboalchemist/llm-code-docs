# Source: https://docs.datadoghq.com/data_streams.md

---
title: Data Streams Monitoring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Data Streams Monitoring
---

# Data Streams Monitoring

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Data Streams Monitoring is not available for the  site.
{% /alert %}


{% /callout %}

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/map_view2.8517b245178bd2008452cb0b274e3f35.png?auto=format"
   alt="Data Streams Monitoring page in Datadog, showing the Map view. Highlights a service called 'authenticator'. A topology map visualization of left-to-right data flow, where the authenticator service is displayed in the center with its upstream and downstream services and queues." /%}

Data Streams Monitoring provides a standardized method for teams to understand and manage pipelines at scale by making it easy to:

- Measure pipeline health with end-to-end latencies for events traversing across your system.
- Pinpoint faulty producers, consumers or queues, then pivot to related logs or clusters to troubleshoot faster.
- Prevent cascading delays by equipping service owners to stop backed up events from overwhelming downstream services.

### Supported languages and technologies{% #supported-languages-and-technologies %}

Data Streams Monitoring instruments Kafka *clients* (consumers/producers). If you can instrument your client infrastructure, you can use Data Streams Monitoring.

| Java                                                                                  | Python | .NET | Node.js | Go  | Ruby |
| ------------------------------------------------------------------------------------- | ------ | ---- | ------- | --- | ---- |
| Apache Kafka(self-hosted, Amazon MSK, Confluent Cloud, or any other hosting platform) | yes    | yes  | yes     | yes | yes  | yes |
| Amazon Kinesis                                                                        | yes    | yes  | yes     | yes |
| Amazon SNS                                                                            | yes    | yes  | yes     | yes |
| Amazon SQS                                                                            | yes    | yes  | yes     | yes |
| Azure Service Bus                                                                     | yes    |
| Google Pub/Sub                                                                        | yes    | yes  |
| IBM MQ                                                                                | yes    | yes  |
| RabbitMQ                                                                              | yes    | yes  | yes     | yes |

Data Streams Monitoring requires minimum Datadog tracer versions. See each setup page for details.

#### Support for OpenTelemetry{% #support-for-opentelemetry %}

Data Streams Monitoring supports OpenTelemetry. If you have set up Datadog APM to work with OpenTelemetry, no additional setup is required to use Data Streams Monitoring. See [OpenTelemetry Compatibility](https://docs.datadoghq.com/opentelemetry/compatibility).

## Setup{% #setup %}

### By language{% #by-language %}

- [java](https://docs.datadoghq.com/data_streams/java/)
- [Python](https://docs.datadoghq.com/data_streams/python)
- [.NET](https://docs.datadoghq.com/data_streams/dotnet/)
- [Node](https://docs.datadoghq.com/data_streams/nodejs/)
- [Go](https://docs.datadoghq.com/data_streams/go)
- [Ruby](https://docs.datadoghq.com/data_streams/ruby)

### By technology{% #by-technology %}

- [Kafka](https://docs.datadoghq.com/data_streams/setup/technologies/kafka/)
- [Amazon SQS](https://docs.datadoghq.com/data_streams/setup/technologies/sqs/)
- [RabbitMQ](https://docs.datadoghq.com/data_streams/setup/technologies/rabbitmq/)
- [Amazon SNS](https://docs.datadoghq.com/data_streams/setup/technologies/sns/)
- [Kinesis](https://docs.datadoghq.com/data_streams/setup/technologies/kinesis/)
- [Google Cloud Pub/Sub](https://docs.datadoghq.com/data_streams/setup/technologies/google_pubsub/)
- [IBM MQ](https://docs.datadoghq.com/data_streams/setup/technologies/ibm_mq/)
- [Azure Service Bus](https://docs.datadoghq.com/data_streams/setup/technologies/azure_service_bus/)

## Explore Data Streams Monitoring{% #explore-data-streams-monitoring %}

### Visualize the architecture of your streaming data pipelines{% #visualize-the-architecture-of-your-streaming-data-pipelines %}

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/topology_map.9c1cece2c272d1de3502da82177f3401.png?auto=format"
   alt="A DSM topology map visualization. " /%}

Data Streams Monitoring provides an out-of-the-box [topology map](https://app.datadoghq.com/data-streams/map), so that you can visualize data flow across your pipelines and identify producer/consumer services, queue dependencies, service ownership, and key health metrics.

### Measure end-to-end pipeline health with new metrics{% #measure-end-to-end-pipeline-health-with-new-metrics %}

With Data Streams Monitoring, you can measure the time it usually takes for events to traverse between any two points in your asynchronous system:

| Metric Name                    | Notable Tags                                  | Description                                                                        |
| ------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| data_streams.latency           | `start`, `end`, `env`                         | End to end latency of a pathway from a specified source to destination service.    |
| data_streams.kafka.lag_seconds | `consumer_group`, `partition`, `topic`, `env` | Lag in seconds between producer and consumer. Requires Java Agent v1.9.0 or later. |
| data_streams.payload_size      | `consumer_group`, `topic`, `env`              | Incoming and outgoing throughput in bytes.                                         |

You can also graph and visualize these metrics on any dashboard or notebook:

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/data_streams_metric_monitor.6b6b920f302993a17b8fad0588fb6c84.png?auto=format"
   alt="Datadog Data Streams Monitoring monitor" /%}

### Monitor end-to-end latency of any pathway{% #monitor-end-to-end-latency-of-any-pathway %}

Depending on how events traverse through your system, different paths can lead to increased latency. With the [**Measure** tab](https://app.datadoghq.com/data-streams/measure), you can select a start service and end service for end-to-end latency information to identify bottlenecks and optimize performance. Easily create a monitor for that pathway, or export to a dashboard.

Alternatively, click a service to open a detailed side panel and view the **Pathways** tab for latency between the service and upstream services.

### Alert on slowdowns in event-driven applications{% #alert-on-slowdowns-in-event-driven-applications %}

Slowdowns caused by high consumer lag or stale messages can lead to cascading failures and increase downtime. With out-of-the-box alerts, you can pinpoint where bottlenecks occur in your pipelines and respond to them right away. For supplementary metrics, Datadog provides additional integrations for message queue technologies like [Kafka](https://docs.datadoghq.com/integrations/kafka/) and [SQS](https://docs.datadoghq.com/integrations/amazon_sqs/).

Through Data Stream Monitoring's out-of-the-box monitor templates, you can setup monitors on metrics like consumer lag, throughput, and latency in one click.

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/add_monitors_and_synthetic_tests.4ecf0aa715cc25a8bc84e7074ffd9f83.png?auto=format"
   alt="Datadog Data Streams Monitoring Monitor Templates" /%}
Click 'Add Monitors and Synthetic Tests' to view monitor templates
### Attribute incoming messages to any queue, service, or cluster{% #attribute-incoming-messages-to-any-queue-service-or-cluster %}

High lag on a consuming service, increased resource use on a Kafka broker, and increased RabbitMQ or Amazon SQS queue size are frequently explained by changes in the way adjacent services are producing to or consuming from these entities.

Click on the **Throughput** tab on any service or queue in Data Streams Monitoring to quickly detect changes in throughput, and which upstream or downstream service these changes originate from. Once the [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/) is configured, you can immediately pivot to the corresponding team's Slack channel or on-call engineer.

By filtering to a single Kafka, RabbitMQ, or Amazon SQS cluster, you can detect changes in incoming or outgoing traffic for all detected topics or queues running on that cluster:

### Quickly pivot to identify root causes in infrastructure, logs, or traces{% #quickly-pivot-to-identify-root-causes-in-infrastructure-logs-or-traces %}

Datadog automatically links the infrastructure powering your services and related logs through [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging), so you can easily localize bottlenecks. Click the **Infra**, **Logs** or **Traces** tabs to further troubleshoot why pathway latency or consumer lag has increased.

### Monitor connector throughput and status{% #monitor-connector-throughput-and-status %}

{% image
   source="https://datadog-docs.imgix.net/images/data_streams/connectors_topology.40c327f51bbee4074763cfc9cef7f65f.png?auto=format"
   alt="A DSM topology map, showing a connector called 'analytics-sink'. The visualization indicates that the connector has a status of FAILED." /%}

Datadog can automatically detect your managed [Confluent Cloud](https://www.confluent.io/confluent-cloud/) connectors and visualize them in the Data Streams Monitoring topology map. Install and configure the [Confluent Cloud integration](https://docs.datadoghq.com/integrations/confluent_cloud/) to collect information from your Confluent Cloud connectorsâincluding throughput, status, and topic dependencies.

## Further Reading{% #further-reading %}

- [Kafka Integration](https://docs.datadoghq.com/integrations/kafka/)
- [Amazon SQS Integration](https://docs.datadoghq.com/integrations/amazon_sqs/)
- [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/)
- [Track and improve the performance of streaming data pipelines with Datadog Data Streams Monitoring](https://www.datadoghq.com/blog/data-streams-monitoring/)
- [Troubleshoot streaming data pipelines directly from APM with Datadog Data Streams Monitoring](https://www.datadoghq.com/blog/data-streams-monitoring-apm-integration/)
- [Monitor SQS with Data Streams Monitoring](https://www.datadoghq.com/blog/data-streams-monitoring-sqs/)
- [Autodiscover Confluent Cloud connectors and easily monitor performance in Data Streams Monitoring](https://www.datadoghq.com/blog/confluent-connector-dsm-autodiscovery/)
- [Ensure trust across the entire data life cycle with Datadog Data Observability](https://www.datadoghq.com/blog/data-observability/)

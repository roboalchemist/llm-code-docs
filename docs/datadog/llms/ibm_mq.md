# Source: https://docs.datadoghq.com/data_streams/setup/technologies/ibm_mq.md

---
title: Data Streams Monitoring for IBM MQ
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Data Streams Monitoring > Setup Data Streams Monitoring > Data Streams
  Monitoring for IBM MQ
---

# Data Streams Monitoring for IBM MQ

### Prerequisites{% #prerequisites %}

- [Datadog Agent v7.34.0 or later](https://docs.datadoghq.com/agent)

| Language                                                              | Library                                                                                                    | Minimal tracer version | Recommended tracer version |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------------- |
| [.NET](https://docs.datadoghq.com/data_streams/setup/language/dotnet) | [IBMMQDotnetClient](https://www.nuget.org/packages/IBMMQDotnetClient)                                      | 2.49.0                 | 2.49.0 or later            |
| [Java](https://docs.datadoghq.com/data_streams/setup/language/java)   | [IBM MQ classes for Java and JMS](https://mvnrepository.com/artifact/com.ibm.mq/com.ibm.mq.jakarta.client) | 1.55.0                 | 1.55.0 or later            |

### Limitations{% #limitations %}

For other queue technologies, Datadog's tracers modify messages to add Data Streams Monitoring context information. However, context propagation for IBM MQ is error-prone, as unexpected additional fields can appear in messages. To avoid risk to customer services, Datadog does not propagate context for IBM MQ traces.

Because of this limitation, the Data Streams Monitoring pathways view cannot filter IBM MQ messages based on upstream pathway.

Latency metrics for pathways that entirely flow through IBM MQ are available, though they are approximated. Message throughput and full presence on the Data Streams Topology map are fully supported.

### Setting up Data Streams Monitoring{% #setting-up-data-streams-monitoring %}

See setup instructions for [.NET](https://docs.datadoghq.com/data_streams/setup/language/dotnet) or [Java](https://docs.datadoghq.com/data_streams/setup/language/java).

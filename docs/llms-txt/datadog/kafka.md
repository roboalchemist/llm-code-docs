# Source: https://docs.datadoghq.com/data_streams/setup/technologies/kafka.md

---
title: Data Streams Monitoring for Kafka
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Data Streams Monitoring > Setup Data Streams Monitoring > Data Streams
  Monitoring for Kafka
---

# Data Streams Monitoring for Kafka

### Prerequisites{% #prerequisites %}

- [Datadog Agent v7.34.0 or later](https://docs.datadoghq.com/agent)

| Language                                                                                 | Library                                                                                                                       | Minimal tracer version    | Recommended tracer version |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------- |
| [Java](https://docs.datadoghq.com/data_streams/java)                                     | [kafka-clients](https://mvnrepository.com/artifact/org.apache.kafka/kafka-clients) (Lag generation is not supported for v3.7) | 1.9.0                     | 1.43.0 or later            |
| [Go](https://docs.datadoghq.com/data_streams/go)                                         | [confluent-kafka-go](https://github.com/confluentinc/confluent-kafka-go)                                                      | 1.56.1                    | 1.66.0 or later            |
| [Sarama](https://github.com/IBM/sarama)                                                  | 1.56.1                                                                                                                        | 1.66.0 or later           |
| [kafka-go](https://github.com/segmentio/kafka-go)                                        | 1.63.0                                                                                                                        | 1.63.0 or later           |
| [Node.js](https://docs.datadoghq.com/data_streams/nodejs)                                | [kafkajs](https://www.npmjs.com/package/kafkajs)                                                                              | 2.39.0 or 3.26.0 or 4.5.0 | 5.25.0 or later            |
| [confluent-kafka-javascript](https://github.com/confluentinc/confluent-kafka-javascript) | 5.52.0                                                                                                                        | 5.52.0 or later           |
| [Python](https://docs.datadoghq.com/python)                                              | [confluent-kafka](https://pypi.org/project/confluent-kafka/)                                                                  | 1.16.0                    | 2.11.0 or later            |
| [aiokafka](https://pypi.org/project/aiokafka/)                                           | 4.1.0                                                                                                                         | 4.1.0 or later            |
| [.NET](https://docs.datadoghq.com/data_streams/dotnet)                                   | [Confluent.Kafka](https://www.nuget.org/packages/Confluent.Kafka)                                                             | 2.28.0                    | 2.41.0 or later            |
| [Ruby](https://docs.datadoghq.com/data_streams/Ruby)                                     | [Ruby Kafka](https://github.com/zendesk/ruby-kafka)                                                                           | 2.23.0                    | 2.23.0 or later            |
| [Karafka](https://karafka.io/docs/)                                                      | 2.23.0                                                                                                                        | 2.23.0 or later           |

{% alert level="info" %}
[Kafka Streams](https://kafka.apache.org/documentation/streams/) is partially supported for Java, and can lead to latency measurements being missed.
{% /alert %}

### Supported Kafka deployments{% #supported-kafka-deployments %}

Instrumenting your consumers and producers with Data Streams Monitoring allows you to view your topology and track your pipelines with [ready-to-go metrics](https://docs.datadoghq.com/data_streams/#measure-end-to-end-pipeline-health-with-new-metrics) independently of how Kafka is deployed. Additionally, the following Kafka deployments have further integration support, providing more insights into the health of your Kafka cluster:

| Model              | Integration                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Self Hosted        | [Kafka Broker](https://docs.datadoghq.com/integrations/kafka/?tab=host) & [Kafka Consumer](https://docs.datadoghq.com/integrations/kafka/?tab=host#kafka-consumer-integration) |
| Confluent Platform | [Confluent Platform](https://docs.datadoghq.com/integrations/confluent_platform/)                                                                                              |
| Confluent Cloud    | [Confluent Cloud](https://docs.datadoghq.com/integrations/confluent_cloud/)                                                                                                    |
| Amazon MSK         | [Amazon MSK](https://docs.datadoghq.com/integrations/amazon_msk_cloud/) or [Amazon MSK (Agent)](https://docs.datadoghq.com/integrations/amazon_msk/)                           |
| Red Panda          | Not yet integrated                                                                                                                                                             |

### Setting up Data Streams Monitoring{% #setting-up-data-streams-monitoring %}

See setup instructions for [Java](https://docs.datadoghq.com/data_streams/setup/language/java), [Go](https://docs.datadoghq.com/data_streams/setup/language/go), [Node.js](https://docs.datadoghq.com/data_streams/setup/language/nodejs), [Python](https://docs.datadoghq.com/data_streams/setup/language/python), [.NET](https://docs.datadoghq.com/data_streams/setup/language/dotnet) or [Ruby](https://docs.datadoghq.com/data_streams/setup/language/ruby).

### Monitoring Kafka Pipelines{% #monitoring-kafka-pipelines %}

Data Streams Monitoring uses message headers to propagate context through Kafka streams. If `log.message.format.version` is set in the Kafka broker configuration, it must be set to `0.11.0.0` or higher. Data Streams Monitoring is not supported for versions lower than this.

# Source: https://docs.datadoghq.com/data_streams/setup/technologies/rabbitmq.md

---
title: Data Streams Monitoring for RabbitMQ
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Data Streams Monitoring > Setup Data Streams Monitoring > Data Streams
  Monitoring for RabbitMQ
---

# Data Streams Monitoring for RabbitMQ

### Prerequisites{% #prerequisites %}

- [Datadog Agent v7.34.0 or later](https://docs.datadoghq.com/agent)

| Language                                                  | Library                                                                    | Minimal tracer version    | Recommended tracer version |
| --------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------- | -------------------------- |
| [Java](https://docs.datadoghq.com/data_streams/java)      | [amqp-client](https://mvnrepository.com/artifact/com.rabbitmq/amqp-client) | 1.9.0                     | 1.42.2 or later            |
| [Node.js](https://docs.datadoghq.com/data_streams/nodejs) | [amqplib](https://www.npmjs.com/package/amqplib)                           | 3.48.0 or 4.27.0 or 5.3.0 | 5.3.0 or later             |
| [Node.js](https://docs.datadoghq.com/data_streams/nodejs) | [rhea](https://www.npmjs.com/package/rhea)                                 | 5.3.0 or 4.27.0 or 3.48.0 | 5.3.0 or later             |
| [Python](https://docs.datadoghq.com/data_streams/python)  | [Kombu](https://pypi.org/project/kombu/)                                   | 2.6.0                     | 2.6.0 or later             |
| [.NET](https://docs.datadoghq.com/data_streams/dotnet)    | [RabbitMQ.Client](https://www.nuget.org/packages/RabbitMQ.Client)          | 2.28.0                    | 2.37.0 or later            |

### Setting up Data Streams Monitoring{% #setting-up-data-streams-monitoring %}

See setup instructions for [Java](https://docs.datadoghq.com/data_streams/setup/language/java), [Node.js](https://docs.datadoghq.com/data_streams/setup/language/nodejs), [Python](https://docs.datadoghq.com/data_streams/setup/language/python), or [.NET](https://docs.datadoghq.com/data_streams/setup/language/dotnet).

### Monitoring RabbitMQ pipelines{% #monitoring-rabbitmq-pipelines %}

The [RabbitMQ integration](https://docs.datadoghq.com/integrations/rabbitmq/?tab=host) can provide detailed monitoring and metrics of your RabbitMQ deployments. For full compatibility with Data Streams Monitoring, Datadog recommends configuring the integration as follows:

```yaml
instances:
  - prometheus_plugin:
      url: http://<HOST>:15692
      unaggregated_endpoint: detailed?family=queue_coarse_metrics&family=queue_consumer_count&family=channel_exchange_metrics&family=channel_queue_exchange_metrics&family=node_coarse_metrics
```

This ensures that all RabbitMQ graphs populate, and that you see detailed metrics for individual exchanges as well as queues.

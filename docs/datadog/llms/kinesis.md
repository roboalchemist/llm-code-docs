# Source: https://docs.datadoghq.com/data_streams/setup/technologies/kinesis.md

---
title: Data Streams Monitoring for Amazon Kinesis
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Data Streams Monitoring > Setup Data Streams Monitoring > Data Streams
  Monitoring for Amazon Kinesis
---

# Data Streams Monitoring for Amazon Kinesis

### Prerequisites{% #prerequisites %}

- [Datadog Agent v7.34.0 or later](https://docs.datadoghq.com/agent)

| Language                                                                          | Library                                                                               | Minimal tracer version    | Recommended tracer version | Minimal Lambda Library version                                                |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------- | -------------------------- | ----------------------------------------------------------------------------- |
| [Java](https://docs.datadoghq.com/data_streams/java)                              | [Kinesis (v1)](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-kinesis) | 1.22.0                    | 1.42.2 or later            | Not supported                                                                 |
| [Kinesis (v2)](https://mvnrepository.com/artifact/software.amazon.awssdk/kinesis) | 1.22.0                                                                                | 1.42.2 or later           | Not supported              |
| [Node.js](https://docs.datadoghq.com/data_streams/nodejs)                         | [client-kinesis](https://www.npmjs.com/package/@aws-sdk/client-kinesis)               | 3.47.0 or 4.26.0 or 5.2.0 | 5.18.0 or later            | Not supported                                                                 |
| [Python](https://docs.datadoghq.com/data_streams/python)                          | [Botocore](https://pypi.org/project/botocore/)                                        | 1.20.0                    | 2.8.0 or later             | [112](https://github.com/DataDog/datadog-lambda-python/releases/tag/v7.112.0) |
| [.NET](https://docs.datadoghq.com/data_streams/dotnet)                            | [Amazon Kinesis SDK](https://www.nuget.org/packages/AWSSDK.Kinesis)                   | 3.7.0                     | 3.7.0 or later             | Not supported                                                                 |

### Setting up Data Streams Monitoring{% #setting-up-data-streams-monitoring %}

See setup instructions for [Java](https://docs.datadoghq.com/data_streams/setup/language/java), [Node.js](https://docs.datadoghq.com/data_streams/setup/language/nodejs), [Python](https://docs.datadoghq.com/data_streams/setup/language/python), or [.NET](https://docs.datadoghq.com/data_streams/setup/language/dotnet).

### Monitoring Kinesis pipelines{% #monitoring-kinesis-pipelines %}

There are no message attributes in Kinesis to propagate context and track a message's full path through a Kinesis stream. As a result, Data Streams Monitoring's end-to-end latency metrics are approximated based on summing latency on segments of a message's path, from the producing service through a Kinesis Stream, to a consumer service. Throughput metrics are based on segments from the producing service through a Kinesis Stream, to the consumer service. The full topology of data streams can still be visualized through instrumenting services.

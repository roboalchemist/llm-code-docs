# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kafka_node.dataset.md

---
title: MSK Broker Node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > MSK Broker Node
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.kafka_node.dataset/index.html
---

# MSK Broker Node

An MSK Broker Node in Amazon Managed Streaming for Apache Kafka (MSK) represents an individual Kafka broker within a cluster. Each broker node handles read and write requests, stores message data, and participates in replication for fault tolerance. The node's configuration, such as instance type and storage, determines performance and capacity.

```
aws.kafka_node
```

## Fields

| Title                 | ID   | Type   | Data Type                                   | Description |
| --------------------- | ---- | ------ | ------------------------------------------- | ----------- |
| _key                  | core | string |
| account_id            | core | string |
| added_to_cluster_time | core | string | The start time.                             |
| broker_node_info      | core | json   | The broker node info.                       |
| controller_node_info  | core | json   | The ControllerNodeInfo.                     |
| instance_type         | core | string | The instance type.                          |
| node_arn              | core | string | The Amazon Resource Name (ARN) of the node. |
| node_type             | core | string | The node type.                              |
| tags                  | core | hstore |
| zookeeper_node_info   | core | json   | The ZookeeperNodeInfo.                      |

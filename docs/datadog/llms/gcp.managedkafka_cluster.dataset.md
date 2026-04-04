# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.managedkafka_cluster.dataset.md

---
title: Managed Kafka Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Kafka Cluster
---

# Managed Kafka Cluster

A Managed Kafka Cluster on Google Cloud is a fully managed service for running Apache Kafka without handling infrastructure or operations. It automates provisioning, scaling, patching, and monitoring of Kafka brokers, ensuring high availability and security. This service allows developers to focus on building real-time data streaming and event-driven applications while Google Cloud manages the underlying cluster performance and reliability.

```
gcp.managedkafka_cluster
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                  | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| capacity_config      | core | json          | Required. Capacity configuration for the Kafka cluster.                                                                    |
| create_time          | core | timestamp     | Output only. The time when the cluster was created.                                                                        |
| datadog_display_name | core | string        |
| gcp_config           | core | json          | Required. Configuration properties for a Kafka cluster deployed to Google Cloud Platform.                                  |
| labels               | core | array<string> | Optional. Labels as key value pairs.                                                                                       |
| name                 | core | string        | Identifier. The name of the cluster. Structured like: projects/{project_number}/locations/{location}/clusters/{cluster_id} |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| rebalance_config     | core | json          | Optional. Rebalance configuration for the Kafka cluster.                                                                   |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                      |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                      |
| state                | core | string        | Output only. The current state of the cluster.                                                                             |
| tags                 | core | hstore_csv    |
| tls_config           | core | json          | Optional. TLS configuration for the Kafka cluster.                                                                         |
| update_options       | core | json          | Optional. UpdateOptions represents options that control how updates to the cluster are applied.                            |
| update_time          | core | timestamp     | Output only. The time when the cluster was last updated.                                                                   |
| zone_id              | core | string        |

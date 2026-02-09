# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dax_cluster.dataset.md

---
title: DAX Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DAX Cluster
---

# DAX Cluster

An AWS DAX Cluster is a managed in-memory cache for DynamoDB that delivers fast read performance by reducing response times from milliseconds to microseconds. It is fully compatible with DynamoDB APIs, allowing applications to use it without code changes. The cluster consists of multiple nodes for high availability and can scale to meet workload demands.

```
aws.dax_cluster
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                            | Description |
| -------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| active_nodes                     | core | int64         | The number of nodes in the cluster that are active (i.e., capable of serving requests).                                                                                                                                              |
| cluster_arn                      | core | string        | The Amazon Resource Name (ARN) that uniquely identifies the cluster.                                                                                                                                                                 |
| cluster_discovery_endpoint       | core | json          | The endpoint for this DAX cluster, consisting of a DNS name, a port number, and a URL. Applications should use the URL to configure the DAX client to find their cluster.                                                            |
| cluster_endpoint_encryption_type | core | string        | The type of encryption supported by the cluster's endpoint. Values are: NONE for no encryption TLS for Transport Layer Security                                                                                                      |
| cluster_name                     | core | string        | The name of the DAX cluster.                                                                                                                                                                                                         |
| description                      | core | string        | The description of the cluster.                                                                                                                                                                                                      |
| iam_role_arn                     | core | string        | A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.                                                              |
| node_ids_to_remove               | core | array<string> | A list of nodes to be removed from the cluster.                                                                                                                                                                                      |
| node_type                        | core | string        | The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)                                                                                                                                       |
| nodes                            | core | json          | A list of nodes that are currently in the cluster.                                                                                                                                                                                   |
| notification_configuration       | core | json          | Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).                                                                 |
| parameter_group                  | core | json          | The parameter group being used by nodes in the cluster.                                                                                                                                                                              |
| preferred_maintenance_window     | core | string        | A range of time when maintenance of DAX cluster software will be performed. For example: sun:01:00-sun:09:00. Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window. |
| security_groups                  | core | json          | A list of security groups, and the status of each, for the nodes in the cluster.                                                                                                                                                     |
| sse_description                  | core | json          | The description of the server-side encryption status on the specified DAX cluster.                                                                                                                                                   |
| status                           | core | string        | The current status of the cluster.                                                                                                                                                                                                   |
| subnet_group                     | core | string        | The subnet group where the DAX cluster is running.                                                                                                                                                                                   |
| tags                             | core | hstore_csv    |
| total_nodes                      | core | int64         | The total number of nodes in the cluster.                                                                                                                                                                                            |

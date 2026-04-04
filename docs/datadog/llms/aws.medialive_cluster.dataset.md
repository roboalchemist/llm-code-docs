# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_cluster.dataset.md

---
title: Elemental MediaLive Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Cluster
---

# Elemental MediaLive Cluster

Elemental MediaLive Cluster in AWS is a managed resource that enables high-availability live video encoding by grouping multiple MediaLive resources together. It ensures redundancy and fault tolerance for live video workflows, allowing broadcasters to deliver reliable, scalable, and resilient live streaming experiences.

```
aws.medialive_cluster
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                                                                                                                   | Description |
| ----------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| arn               | core | string        | The ARN of this Cluster. It is automatically assigned when the Cluster is created.                                                                                                                                                                          |
| channel_ids       | core | array<string> | An array of the IDs of the Channels that are associated with this Cluster. One Channel is associated with the Cluster as follows: A Channel belongs to a ChannelPlacementGroup. A ChannelPlacementGroup is attached to a Node. A Node belongs to a Cluster. |
| cluster_type      | core | string        | The hardware type for the Cluster.                                                                                                                                                                                                                          |
| id                | core | string        | The ID of the Cluster. Unique in the AWS account. The ID is the resource-id portion of the ARN.                                                                                                                                                             |
| instance_role_arn | core | string        | The ARN of the IAM role for the Node in this Cluster. Any Nodes that are associated with this Cluster assume this role. The role gives permissions to the operations that you expect these Node to perform.                                                 |
| name              | core | string        | The name that you specified for the Cluster.                                                                                                                                                                                                                |
| network_settings  | core | json          | Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with.                                                                                                                                  |
| state             | core | string        | The current state of the Cluster.                                                                                                                                                                                                                           |
| tags              | core | hstore_csv    |

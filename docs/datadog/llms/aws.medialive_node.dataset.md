# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_node.dataset.md

---
title: Elemental MediaLive Node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Node
---

# Elemental MediaLive Node

Elemental MediaLive Node is a managed resource in AWS Elemental MediaLive that represents a compute node used to process live video channels. Nodes provide the underlying infrastructure for encoding and delivering live video streams with high availability and scalability. They are part of the MediaLive Multiplex and Channel workflows, ensuring reliable video processing and distribution.

```
aws.medialive_node
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                        | Description |
| ------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string        |
| account_id               | core | string        |
| arn                      | core | string        | The ARN of the Node. It is automatically assigned when the Node is created.                                                                                                                      |
| channel_placement_groups | core | array<string> | An array of IDs. Each ID is one ChannelPlacementGroup that is associated with this Node. Empty if the Node is not yet associated with any groups.                                                |
| cluster_id               | core | string        | The ID of the Cluster that the Node belongs to.                                                                                                                                                  |
| connection_state         | core | string        | The current connection state of the Node.                                                                                                                                                        |
| id                       | core | string        | The unique ID of the Node. Unique in the Cluster. The ID is the resource-id portion of the ARN.                                                                                                  |
| instance_arn             | core | string        | The EC2 ARN of the Instance associated with the Node.                                                                                                                                            |
| managed_instance_id      | core | string        | At the routing layer will get it from the callerId/context for use with bring your own device.                                                                                                   |
| name                     | core | string        | The name that you specified for the Node.                                                                                                                                                        |
| node_interface_mappings  | core | json          | Documentation update needed                                                                                                                                                                      |
| role                     | core | string        | The initial role current role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails. |
| sdi_source_mappings      | core | json          | An array of SDI source mappings. Each mapping connects one logical SdiSource to the physical SDI card and port that the physical SDI source uses.                                                |
| state                    | core | string        | The current state of the Node.                                                                                                                                                                   |
| tags                     | core | hstore_csv    |

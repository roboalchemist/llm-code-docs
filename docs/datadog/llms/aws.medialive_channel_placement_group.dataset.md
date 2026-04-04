# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_channel_placement_group.dataset.md

---
title: Elemental MediaLive Channel Placement Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elemental MediaLive Channel
  Placement Group
---

# Elemental MediaLive Channel Placement Group

An Elemental MediaLive Channel Placement Group in AWS is a configuration that defines how MediaLive channels are distributed across infrastructure to improve reliability and performance. It helps ensure that channels are placed on separate hardware or availability zones to reduce the risk of simultaneous failures and maintain consistent broadcast quality.

```
aws.medialive_channel_placement_group
```

## Fields

| Title      | ID   | Type          | Data Type                                                                                                      | Description |
| ---------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string        |
| account_id | core | string        |
| arn        | core | string        | The ARN of this ChannelPlacementGroup. It is automatically assigned when the ChannelPlacementGroup is created. |
| channels   | core | array<string> | Used in ListChannelPlacementGroupsResult                                                                       |
| cluster_id | core | string        | The ID of the Cluster that the Node belongs to.                                                                |
| id         | core | string        | The ID of the ChannelPlacementGroup. Unique in the AWS account. The ID is the resource-id portion of the ARN.  |
| name       | core | string        | The name that you specified for the ChannelPlacementGroup.                                                     |
| nodes      | core | array<string> | An array with one item, which is the single Node that is associated with the ChannelPlacementGroup.            |
| state      | core | string        | The current state of the ChannelPlacementGroup.                                                                |
| tags       | core | hstore_csv    |

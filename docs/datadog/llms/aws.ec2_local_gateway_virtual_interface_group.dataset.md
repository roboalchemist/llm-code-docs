# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_local_gateway_virtual_interface_group.dataset.md

---
title: EC2 Local Gateway Virtual Interface Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > EC2 Local Gateway Virtual Interface
  Group
---

# EC2 Local Gateway Virtual Interface Group

An EC2 Local Gateway Virtual Interface Group is an AWS resource that groups together one or more local gateway virtual interfaces. It enables communication between on-premises networks and Amazon VPCs through a local gateway, typically used in Outposts environments. This grouping helps manage connectivity and routing for hybrid workloads.

```
aws.ec2_local_gateway_virtual_interface_group
```

## Fields

| Title                                    | ID   | Type          | Data Type                                                                                      | Description |
| ---------------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string        |
| account_id                               | core | string        |
| local_gateway_id                         | core | string        | The ID of the local gateway.                                                                   |
| local_gateway_virtual_interface_group_id | core | string        | The ID of the virtual interface group.                                                         |
| local_gateway_virtual_interface_ids      | core | array<string> | The IDs of the virtual interfaces.                                                             |
| owner_id                                 | core | string        | The ID of the Amazon Web Services account that owns the local gateway virtual interface group. |
| tags                                     | core | hstore_csv    |

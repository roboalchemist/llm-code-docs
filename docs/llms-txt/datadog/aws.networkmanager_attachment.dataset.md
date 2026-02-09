# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_attachment.dataset.md

---
title: Network Manager Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Attachment
---

# Network Manager Attachment

An AWS Network Manager Attachment represents a connection between a core network and an external resource, such as a VPC, VPN, or transit gateway. It defines how different network components are linked within the AWS Global Network, enabling centralized management of connectivity, routing, and policies across multiple regions and accounts.

```
aws.networkmanager_attachment
```

## Fields

| Title                                  | ID   | Type          | Data Type                                                                                                                                                                            | Description |
| -------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                   | core | string        |
| account_id                             | core | string        |
| attachment_id                          | core | string        | The ID of the attachment.                                                                                                                                                            |
| attachment_policy_rule_number          | core | int64         | The policy rule number associated with the attachment.                                                                                                                               |
| attachment_type                        | core | string        | The type of attachment.                                                                                                                                                              |
| core_network_arn                       | core | string        | The ARN of a core network.                                                                                                                                                           |
| core_network_id                        | core | string        | The ID of a core network.                                                                                                                                                            |
| created_at                             | core | timestamp     | The timestamp when the attachment was created.                                                                                                                                       |
| edge_location                          | core | string        | The Region where the edge is located. This is returned for all attachment types except a Direct Connect gateway attachment, which instead returns EdgeLocations.                     |
| edge_locations                         | core | array<string> | The edge locations that the Direct Connect gateway is associated with. This is returned only for Direct Connect gateway attachments. All other attachment types retrun EdgeLocation. |
| last_modification_errors               | core | json          | Describes the error associated with the attachment request.                                                                                                                          |
| network_function_group_name            | core | string        | The name of the network function group.                                                                                                                                              |
| owner_account_id                       | core | string        | The ID of the attachment account owner.                                                                                                                                              |
| proposed_network_function_group_change | core | json          | Describes a proposed change to a network function group associated with the attachment.                                                                                              |
| proposed_segment_change                | core | json          | The attachment to move from one segment to another.                                                                                                                                  |
| resource_arn                           | core | string        | The attachment resource ARN.                                                                                                                                                         |
| segment_name                           | core | string        | The name of the segment attachment.                                                                                                                                                  |
| state                                  | core | string        | The state of the attachment.                                                                                                                                                         |
| tags                                   | core | hstore_csv    |
| updated_at                             | core | timestamp     | The timestamp when the attachment was last updated.                                                                                                                                  |

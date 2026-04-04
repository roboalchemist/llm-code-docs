# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_peering.dataset.md

---
title: Network Manager Peering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Peering
---

# Network Manager Peering

Network Manager Peering in AWS enables the creation and management of peering connections between global networks managed by AWS Network Manager. It allows organizations to connect their transit gateways across different AWS Regions or accounts, providing secure and scalable interconnectivity for distributed workloads. This helps simplify global network operations and ensures consistent connectivity across multiple environments.

```
aws.networkmanager_peering
```

## Fields

| Title                    | ID   | Type       | Data Type                                                     | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| core_network_arn         | core | string     | The ARN of a core network.                                    |
| core_network_id          | core | string     | The ID of the core network for the peering request.           |
| created_at               | core | timestamp  | The timestamp when the attachment peer was created.           |
| edge_location            | core | string     | The edge location for the peer.                               |
| last_modification_errors | core | json       | Describes the error associated with the Connect peer request. |
| owner_account_id         | core | string     | The ID of the account owner.                                  |
| peering_id               | core | string     | The ID of the peering attachment.                             |
| peering_type             | core | string     | The type of peering. This will be TRANSIT_GATEWAY.            |
| resource_arn             | core | string     | The resource ARN of the peer.                                 |
| state                    | core | string     | The current state of the peering connection.                  |
| tags                     | core | hstore_csv |

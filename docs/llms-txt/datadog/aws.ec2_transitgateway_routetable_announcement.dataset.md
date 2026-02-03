# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_transitgateway_routetable_announcement.dataset.md

---
title: Ec2 Transitgateway Routetable Announcement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Ec2 Transitgateway Routetable
  Announcement
---

# Ec2 Transitgateway Routetable Announcement

This table represents the ec2_transitgateway_routetable_announcement resource from Amazon Web Services.

```
aws.ec2_transitgateway_routetable_announcement
```

## Fields

| Title                                       | ID   | Type       | Data Type                                                                    | Description |
| ------------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------- | ----------- |
| _key                                        | core | string     |
| account_id                                  | core | string     |
| announcement_direction                      | core | string     | The direction for the route table announcement.                              |
| core_network_id                             | core | string     | The ID of the core network for the transit gateway route table announcement. |
| creation_time                               | core | timestamp  | The timestamp when the transit gateway route table announcement was created. |
| peer_core_network_id                        | core | string     | The ID of the core network ID for the peer.                                  |
| peer_transit_gateway_id                     | core | string     | The ID of the peer transit gateway.                                          |
| peering_attachment_id                       | core | string     | The ID of the peering attachment.                                            |
| state                                       | core | string     | The state of the transit gateway announcement.                               |
| tags                                        | core | hstore_csv |
| transit_gateway_id                          | core | string     | The ID of the transit gateway.                                               |
| transit_gateway_route_table_announcement_id | core | string     | The ID of the transit gateway route table announcement.                      |
| transit_gateway_route_table_id              | core | string     | The ID of the transit gateway route table.                                   |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datafusion_dns_peering.dataset.md

---
title: DNS Peering Zone
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DNS Peering Zone
---

# DNS Peering Zone

A DNS Peering Zone in Google Cloud allows private DNS resolution across different Virtual Private Cloud (VPC) networks that are connected through VPC peering. It enables one VPC to use DNS records from another VPC without exposing them publicly. This helps maintain secure and efficient name resolution between peered networks while keeping DNS management centralized.

```
gcp.datafusion_dns_peering
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Optional description of the dns zone.                                                                                                       |
| domain               | core | string        | Required. The dns name suffix of the zone.                                                                                                            |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. The resource name of the dns peering zone. Format: projects/{project}/locations/{location}/instances/{instance}/dnsPeerings/{dns_peering} |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| target_network       | core | string        | Optional. Optional target network to which dns peering should happen.                                                                                 |
| target_project       | core | string        | Optional. Optional target project to which dns peering should happen.                                                                                 |
| zone_id              | core | string        |

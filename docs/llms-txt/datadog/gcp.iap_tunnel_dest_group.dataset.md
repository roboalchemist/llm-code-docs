# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.iap_tunnel_dest_group.dataset.md

---
title: IAP Tunnel Destination Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAP Tunnel Destination Group
---

# IAP Tunnel Destination Group

An IAP Tunnel Destination Group in Google Cloud is a configuration resource used with Identity-Aware Proxy (IAP) to define a set of destination instances or endpoints accessible through IAP TCP forwarding. It allows secure, identity-based access to internal resources without exposing them to the public internet, simplifying access control and auditing for administrative or development connections.

```
gcp.iap_tunnel_dest_group
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                   | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| cidrs                | core | array<string> | Optional. Unordered list. List of CIDRs that this group applies to.                                                                         |
| datadog_display_name | core | string        |
| fqdns                | core | array<string> | Optional. Unordered list. List of FQDNs that this group applies to.                                                                         |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. Identifier for the TunnelDestGroup. Must be unique within the project and contain only lower case letters (a-z) and dashes (-). |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |

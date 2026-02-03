# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.certificatemanager_certificate_map.dataset.md

---
title: Certificate Map
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Certificate Map
---

# Certificate Map

Certificate Map in Google Cloud is a resource used to organize and manage SSL/TLS certificates for load balancers. It allows you to define rules that map incoming requests to the appropriate certificate based on hostnames or other criteria. This helps simplify certificate management at scale, especially when serving multiple domains or subdomains through the same load balancer.

```
gcp.certificatemanager_certificate_map
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of a Certificate Map.                                                                                                           |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. One or more paragraphs of text description of a certificate map.                                                                                          |
| gclb_targets         | core | json          | Output only. A list of GCLB targets that use this Certificate Map. A Target Proxy is only present on this list if it's attached to a Forwarding Rule.               |
| labels               | core | array<string> | Optional. Set of labels associated with a Certificate Map.                                                                                                          |
| name                 | core | string        | Identifier. A user-defined name of the Certificate Map. Certificate Map names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*`. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The update timestamp of a Certificate Map.                                                                                                             |
| zone_id              | core | string        |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dns_resource_record_set.dataset.md

---
title: Cloud DNS Resource Record Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud DNS Resource Record Set
---

# Cloud DNS Resource Record Set

Cloud DNS Resource Record Set in Google Cloud represents a collection of DNS records that share the same name, type, and routing policy within a managed zone. It defines how domain names are resolved to IP addresses or other resources. Each record set can include multiple records for redundancy or load balancing, supporting record types like A, AAAA, CNAME, MX, TXT, and more.

```
gcp.dns_resource_record_set
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| kind                 | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | For example, www.example.com.                                                                                                                                                                                                                                       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| routing_policy       | core | json          | Configures dynamic query responses based on either the geo location of the querying user or a weighted round robin based routing policy. A valid `ResourceRecordSet` contains only `rrdata` (for static resolution) or a `routing_policy` (for dynamic resolution). |
| rrdatas              | core | array<string> | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples.                                                                                                                                                                                    |
| signature_rrdatas    | core | array<string> | As defined in RFC 4034 (section 3.2).                                                                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| ttl                  | core | int64         | Number of seconds that this `ResourceRecordSet` can be cached by resolvers.                                                                                                                                                                                         |
| type                 | core | string        | The identifier of a supported record type. See the list of Supported DNS record types.                                                                                                                                                                              |
| zone_id              | core | string        |

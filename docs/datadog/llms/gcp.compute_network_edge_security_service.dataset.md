# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_network_edge_security_service.dataset.md

---
title: Network Edge Security Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Edge Security Service
---

# Network Edge Security Service

Network Edge Security Service in Google Cloud provides centralized security controls for traffic entering or leaving a Virtual Private Cloud (VPC). It enables policy enforcement at the network edge, offering protection against threats, managing access, and ensuring compliance. This service integrates with Google's global network to deliver low-latency, scalable, and consistent security across distributed environments.

```
gcp.compute_network_edge_security_service
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| id                   | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                        |
| kind                 | core | string        | Output only. [Output only] Type of the resource. Alwayscompute#networkEdgeSecurityService for NetworkEdgeSecurityServices                                                                                                                                                                                                                                                                                                                           |
| labels               | core | array<string> |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region               | core | string        | Output only. [Output Only] URL of the region where the resource resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.                                                                                                                                                                                                                                                            |
| region_id            | core | string        |
| resource_name        | core | string        |
| security_policy      | core | string        | The resource URL for the network edge security service associated with this network edge security service.                                                                                                                                                                                                                                                                                                                                          |
| self_link            | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                     |
| self_link_with_id    | core | string        | Output only. [Output Only] Server-defined URL for this resource with the resource id.                                                                                                                                                                                                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |

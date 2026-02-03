# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_external_vpn_gateway.dataset.md

---
title: External VPN Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > External VPN Gateway
---

# External VPN Gateway

External VPN Gateway in Google Cloud represents a physical or virtual VPN device located outside of Google Cloud that connects to Cloud VPN. It allows you to establish secure, encrypted tunnels between your on-premises network or another cloud provider and your Google Cloud Virtual Private Cloud (VPC). This resource is used when configuring Classic VPN or HA VPN to define the external gateway's IP addresses and redundancy settings, enabling reliable hybrid or multi-cloud connectivity.

```
gcp.compute_external_vpn_gateway
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
| interfaces           | core | json          | A list of interfaces for this external VPN gateway. If your peer-side gateway is an on-premises gateway and non-AWS cloud providers' gateway, at most two interfaces can be provided for an external VPN gateway. If your peer side is an AWS virtual private gateway, four interfaces should be provided for an external VPN gateway.                                                                                                              |
| kind                 | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#externalVpnGateway for externalVpnGateways.                                                                                                                                                                                                                                                                                                                                          |
| labels               | core | array<string> | Labels for this resource. These can only be added or modified by thesetLabels method. Each label key/value pair must comply withRFC1035. Label values may be empty.                                                                                                                                                                                                                                                                                 |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| redundancy_type      | core | string        | Indicates the user-supplied redundancy type of this external VPN gateway.                                                                                                                                                                                                                                                                                                                                                                           |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                     |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |

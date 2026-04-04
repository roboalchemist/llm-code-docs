# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_firewall_endpoint_association.dataset.md

---
title: Firewall Endpoint Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firewall Endpoint Association
---

# Firewall Endpoint Association

Firewall Endpoint Association in Google Cloud links a network endpoint group or interface with a specific firewall policy endpoint. It enables traffic inspection and enforcement by directing network traffic through the associated firewall endpoint. This association ensures that security rules and threat protection are consistently applied to the connected resources within a Virtual Private Cloud (VPC).

```
gcp.networksecurity_firewall_endpoint_association
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                       | Description |
| --------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| create_time           | core | timestamp     | Output only. Create time stamp                                                                  |
| datadog_display_name  | core | string        |
| disabled              | core | bool          | Optional. Whether the association is disabled. True indicates that traffic won't be intercepted |
| firewall_endpoint     | core | string        | Required. The URL of the FirewallEndpoint that is being associated.                             |
| labels                | core | array<string> | Optional. Labels as key value pairs                                                             |
| name                  | core | string        | Immutable. Identifier. name of resource                                                         |
| network               | core | string        | Required. The URL of the network that is being associated.                                      |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| reconciling           | core | bool          | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128.    |
| region_id             | core | string        |
| resource_name         | core | string        |
| state                 | core | string        | Output only. Current state of the association.                                                  |
| tags                  | core | hstore_csv    |
| tls_inspection_policy | core | string        | Optional. The URL of the TlsInspectionPolicy that is being associated.                          |
| update_time           | core | timestamp     | Output only. Update time stamp                                                                  |
| zone_id               | core | string        |

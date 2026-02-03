# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networksecurity_firewall_endpoint.dataset.md

---
title: Firewall Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Firewall Endpoint
---

# Firewall Endpoint

Firewall Endpoint in Google Cloud is a managed network security service that provides a dedicated point for enforcing firewall policies. It allows you to control and inspect traffic between virtual networks, workloads, and the internet. By using firewall endpoints, you can centralize security rules, improve visibility, and ensure consistent protection across your environment.

```
gcp.networksecurity_firewall_endpoint
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| associated_networks  | core | array<string> | Output only. List of networks that are associated with this endpoint in the local zone. This is a projection of the FirewallEndpointAssociations pointing at this endpoint. A network will only appear in this list after traffic routing is fully configured. Format: projects/{project}/global/networks/{name}. |
| associations         | core | json          | Output only. List of FirewallEndpointAssociations that are associated to this endpoint. An association will only appear in this list after traffic routing is fully configured.                                                                                                                                   |
| billing_project_id   | core | string        | Required. Project to bill on endpoint uptime usage.                                                                                                                                                                                                                                                               |
| create_time          | core | timestamp     | Output only. Create time stamp.                                                                                                                                                                                                                                                                                   |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the firewall endpoint. Max length 2048 characters.                                                                                                                                                                                                                                       |
| labels               | core | array<string> | Optional. Labels as key value pairs                                                                                                                                                                                                                                                                               |
| name                 | core | string        | Immutable. Identifier. Name of resource.                                                                                                                                                                                                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128.                                                                                                                                                                                                                      |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. [Output Only] Reserved for future use.                                                                                                                                                                                                                                                               |
| satisfies_pzs        | core | bool          | Output only. [Output Only] Reserved for future use.                                                                                                                                                                                                                                                               |
| state                | core | string        | Output only. Current state of the endpoint.                                                                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Update time stamp                                                                                                                                                                                                                                                                                    |
| zone_id              | core | string        |

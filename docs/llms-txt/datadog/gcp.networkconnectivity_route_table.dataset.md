# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkconnectivity_route_table.dataset.md

---
title: Route Table
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Route Table
---

# Route Table

A Route Table in Google Cloud defines how network traffic is directed within a Virtual Private Cloud (VPC). It contains a set of routes that determine the path packets take based on destination IP addresses. Each VPC network has its own system-generated route table, and custom routes can be added to control traffic flow between subnets, to the internet, or to on-premises networks.

```
gcp.networkconnectivity_route_table
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time the route table was created.                                                                                                                                                                                           |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of the route table.                                                                                                                                                                                                  |
| labels               | core | array<string> | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).                                            |
| name                 | core | string        | Immutable. The name of the route table. Route table names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}`                                                  |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current lifecycle state of this route table.                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. The Google-generated UUID for the route table. This value is unique across all route table resources. If a route table is deleted and another with the same name is created, the new route table is assigned a different `uid`. |
| update_time          | core | timestamp     | Output only. The time the route table was last updated.                                                                                                                                                                                      |
| zone_id              | core | string        |

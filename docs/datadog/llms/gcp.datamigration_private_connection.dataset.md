# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datamigration_private_connection.dataset.md

---
title: PrivateConnection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > PrivateConnection
---

# PrivateConnection

PrivateConnection in Google Cloud is a resource that enables private network connectivity between a customer's Virtual Private Cloud (VPC) and Google services or partner services. It allows data to travel over Google's internal network instead of the public internet, improving security, performance, and reliability. This resource is commonly used for establishing private service access or connecting to managed services privately.

```
gcp.datamigration_private_connection
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The create time of the resource.                                                                                                                                                                                                    |
| datadog_display_name | core | string        |
| error                | core | json          | Output only. The error details in case of state FAILED.                                                                                                                                                                                          |
| gcp_display_name     | core | string        | The private connection display name.                                                                                                                                                                                                             |
| labels               | core | array<string> | The resource labels for private connections to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| name                 | core | string        | The name of the resource.                                                                                                                                                                                                                        |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                            |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                            |
| state                | core | string        | Output only. The state of the private connection.                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update time of the resource.                                                                                                                                                                                               |
| vpc_peering_config   | core | json          | VPC peering configuration.                                                                                                                                                                                                                       |
| zone_id              | core | string        |

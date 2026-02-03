# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datastream_private_connection.dataset.md

---
title: Datastream Private Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Datastream Private Connection
---

# Datastream Private Connection

Datastream Private Connection in Google Cloud is a network configuration that enables secure, private connectivity between Datastream and data sources or destinations without using the public internet. It leverages Private Service Connect to establish a private link, ensuring data replication and streaming occur within the Google Cloud network for improved security, performance, and compliance.

```
gcp.datastream_private_connection
```

## Fields

| Title                | ID   | Type          | Data Type                                                                          | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The create time of the resource.                                      |
| datadog_display_name | core | string        |
| error                | core | json          | Output only. In case of error, the details of the error in a user-friendly format. |
| gcp_display_name     | core | string        | Required. Display name.                                                            |
| labels               | core | array<string> | Labels.                                                                            |
| name                 | core | string        | Output only. Identifier. The resource's name.                                      |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| psc_interface_config | core | json          | PSC Interface Config.                                                              |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                              |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                              |
| state                | core | string        | Output only. The state of the Private Connection.                                  |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The update time of the resource.                                      |
| vpc_peering_config   | core | json          | VPC Peering Config.                                                                |
| zone_id              | core | string        |

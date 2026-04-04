# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datamigration_connection_profile.dataset.md

---
title: Connection Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connection Profile
---

# Connection Profile

A Connection Profile in Google Cloud is a configuration resource that stores connection details for data sources or destinations used in Database Migration Service. It defines parameters such as host, port, username, and authentication method, allowing secure and reusable connections between databases or services without embedding credentials directly in migration jobs.

```
gcp.datamigration_connection_profile
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| alloydb              | core | json          | An AlloyDB cluster connection profile.                                                                                                                                                                                                          |
| ancestors            | core | array<string> |
| cloudsql             | core | json          | A CloudSQL database connection profile.                                                                                                                                                                                                         |
| create_time          | core | timestamp     | Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".                                                                         |
| datadog_display_name | core | string        |
| error                | core | json          | Output only. The error details in case of state FAILED.                                                                                                                                                                                         |
| gcp_display_name     | core | string        | The connection profile display name.                                                                                                                                                                                                            |
| labels               | core | array<string> | The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| mysql                | core | json          | A MySQL database connection profile.                                                                                                                                                                                                            |
| name                 | core | string        | The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}.                                                                                                     |
| oracle               | core | json          | An Oracle database connection profile.                                                                                                                                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| postgresql           | core | json          | A PostgreSQL database connection profile.                                                                                                                                                                                                       |
| project_id           | core | string        |
| project_number       | core | string        |
| provider             | core | string        | The database provider.                                                                                                                                                                                                                          |
| region_id            | core | string        |
| resource_name        | core | string        |
| role                 | core | string        | Optional. The connection profile role.                                                                                                                                                                                                          |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                           |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                           |
| sqlserver            | core | json          | Connection profile for a SQL Server data source.                                                                                                                                                                                                |
| state                | core | string        | The current connection profile state (e.g. DRAFT, READY, or FAILED).                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".                                                                    |
| zone_id              | core | string        |

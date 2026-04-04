# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datastream_connection_profile.dataset.md

---
title: Datastream Connection Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Datastream Connection Profile
---

# Datastream Connection Profile

A Datastream Connection Profile in Google Cloud defines the connection details for a data source or destination used in Datastream. It stores configuration information such as connection type, network settings, authentication credentials, and endpoint details. This profile allows Datastream to securely connect to databases or storage systems for continuous data replication and streaming.

```
gcp.datastream_connection_profile
```

## Fields

| Title                          | ID   | Type          | Data Type                                      | Description |
| ------------------------------ | ---- | ------------- | ---------------------------------------------- | ----------- |
| _key                           | core | string        |
| ancestors                      | core | array<string> |
| bigquery_profile               | core | json          | BigQuery Connection Profile configuration.     |
| create_time                    | core | timestamp     | Output only. The create time of the resource.  |
| datadog_display_name           | core | string        |
| forward_ssh_connectivity       | core | json          | Forward SSH tunnel connectivity.               |
| gcp_display_name               | core | string        | Required. Display name.                        |
| gcs_profile                    | core | json          | Cloud Storage ConnectionProfile configuration. |
| labels                         | core | array<string> | Labels.                                        |
| mongodb_profile                | core | json          | MongoDB Connection Profile configuration.      |
| mysql_profile                  | core | json          | MySQL ConnectionProfile configuration.         |
| name                           | core | string        | Output only. Identifier. The resource's name.  |
| oracle_profile                 | core | json          | Oracle ConnectionProfile configuration.        |
| organization_id                | core | string        |
| parent                         | core | string        |
| postgresql_profile             | core | json          | PostgreSQL Connection Profile configuration.   |
| private_connectivity           | core | json          | Private connectivity.                          |
| project_id                     | core | string        |
| project_number                 | core | string        |
| region_id                      | core | string        |
| resource_name                  | core | string        |
| salesforce_profile             | core | json          | Salesforce Connection Profile configuration.   |
| satisfies_pzi                  | core | bool          | Output only. Reserved for future use.          |
| satisfies_pzs                  | core | bool          | Output only. Reserved for future use.          |
| sql_server_profile             | core | json          | SQLServer Connection Profile configuration.    |
| static_service_ip_connectivity | core | json          | Static Service IP connectivity.                |
| tags                           | core | hstore_csv    |
| update_time                    | core | timestamp     | Output only. The update time of the resource.  |
| zone_id                        | core | string        |

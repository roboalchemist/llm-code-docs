# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.oracledatabase_autonomous_database.dataset.md

---
title: Oracle Database Autonomous Database
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Oracle Database Autonomous Database
---

# Oracle Database Autonomous Database

This table represents the Oracle Database Autonomous Database resource from Google Cloud Platform.

```
gcp.oracledatabase_autonomous_database
```

## Fields

| Title                                 | ID   | Type          | Data Type                                                                                                                                                                                                                                          | Description |
| ------------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string        |
| admin_password                        | core | string        | Optional. The password for the default ADMIN user.                                                                                                                                                                                                 |
| ancestors                             | core | array<string> |
| cidr                                  | core | string        | Optional. The subnet CIDR range for the Autonomous Database.                                                                                                                                                                                       |
| create_time                           | core | timestamp     | Output only. The date and time that the Autonomous Database was created.                                                                                                                                                                           |
| database                              | core | string        | Optional. The name of the Autonomous Database. The database name must be unique in the project. The name must begin with a letter and can contain a maximum of 30 alphanumeric characters.                                                         |
| datadog_display_name                  | core | string        |
| disaster_recovery_supported_locations | core | array<string> | Output only. List of supported GCP region to clone the Autonomous Database for disaster recovery. Format: `project/{project}/locations/{location}`.                                                                                                |
| entitlement_id                        | core | string        | Output only. The ID of the subscription entitlement associated with the Autonomous Database.                                                                                                                                                       |
| gcp_display_name                      | core | string        | Optional. The display name for the Autonomous Database. The name does not have to be unique within your project.                                                                                                                                   |
| labels                                | core | array<string> | Optional. The labels or tags associated with the Autonomous Database.                                                                                                                                                                              |
| name                                  | core | string        | Identifier. The name of the Autonomous Database resource in the following format: projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database}                                                                                  |
| network                               | core | string        | Optional. The name of the VPC network used by the Autonomous Database in the following format: projects/{project}/global/networks/{network}                                                                                                        |
| odb_network                           | core | string        | Optional. The name of the OdbNetwork associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet. |
| odb_subnet                            | core | string        | Optional. The name of the OdbSubnet associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}                                                                     |
| organization_id                       | core | string        |
| parent                                | core | string        |
| peer_autonomous_databases             | core | array<string> | Output only. The peer Autonomous Database names of the given Autonomous Database.                                                                                                                                                                  |
| project_id                            | core | string        |
| project_number                        | core | string        |
| properties                            | core | json          | Optional. The properties of the Autonomous Database.                                                                                                                                                                                               |
| region_id                             | core | string        |
| resource_name                         | core | string        |
| source_config                         | core | json          | Optional. The source Autonomous Database configuration for the standby Autonomous Database. The source Autonomous Database is configured while creating the Peer Autonomous Database and can't be updated after creation.                          |
| tags                                  | core | hstore_csv    |
| zone_id                               | core | string        |

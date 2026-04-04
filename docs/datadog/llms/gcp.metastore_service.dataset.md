# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.metastore_service.dataset.md

---
title: Dataproc Metastore Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Metastore Service
---

# Dataproc Metastore Service

Dataproc Metastore Service is a fully managed, centralized metadata repository for Apache Hive metastore on Google Cloud. It simplifies the management of metadata for big data ecosystems by providing a scalable, reliable, and secure service that integrates with Dataproc, BigQuery, and other analytics tools. This service helps ensure consistent metadata access across workloads, reduces operational overhead, and supports interoperability between different data processing frameworks.

```
gcp.metastore_service
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                                                                | Description |
| ---------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| artifact_gcs_uri             | core | string        | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored.                                                                                                       |
| create_time                  | core | timestamp     | Output only. The time when the metastore service was created.                                                                                                                                                                            |
| database_type                | core | string        | Immutable. The database type that the Metastore service stores its data.                                                                                                                                                                 |
| datadog_display_name         | core | string        |
| deletion_protection          | core | bool          | Optional. Indicates if the dataproc metastore should be protected against accidental deletions.                                                                                                                                          |
| encryption_config            | core | json          | Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.                                                                                                             |
| endpoint_uri                 | core | string        | Output only. The URI of the endpoint used to access the metastore service.                                                                                                                                                               |
| hive_metastore_config        | core | json          | Configuration information specific to running Hive metastore software as the metastore service.                                                                                                                                          |
| labels                       | core | array<string> | User-defined labels for the metastore service.                                                                                                                                                                                           |
| maintenance_window           | core | json          | Optional. The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type. |
| metadata_integration         | core | json          | Optional. The setting that defines how metastore metadata should be integrated with external services and systems.                                                                                                                       |
| metadata_management_activity | core | json          | Output only. The metadata management activities of the metastore service.                                                                                                                                                                |
| name                         | core | string        | Immutable. Identifier. The relative resource name of the metastore service, in the following format:projects/{project_number}/locations/{location_id}/services/{service_id}.                                                             |
| network                      | core | string        | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}.                                            |
| network_config               | core | json          | Optional. The configuration specifying the network settings for the Dataproc Metastore service.                                                                                                                                          |
| organization_id              | core | string        |
| parent                       | core | string        |
| port                         | core | int64         | Optional. The TCP port at which the metastore service is reached. Default: 9083.                                                                                                                                                         |
| project_id                   | core | string        |
| project_number               | core | string        |
| region_id                    | core | string        |
| release_channel              | core | string        | Immutable. The release channel of the service. If unspecified, defaults to STABLE.                                                                                                                                                       |
| resource_name                | core | string        |
| scaling_config               | core | json          | Optional. Scaling configuration of the metastore service.                                                                                                                                                                                |
| scheduled_backup             | core | json          | Optional. The configuration of scheduled backup for the metastore service.                                                                                                                                                               |
| state                        | core | string        | Output only. The current state of the metastore service.                                                                                                                                                                                 |
| state_message                | core | string        | Output only. Additional information about the current state of the metastore service, if available.                                                                                                                                      |
| tags                         | core | hstore_csv    |
| telemetry_config             | core | json          | Optional. The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to JSON.                                                                                                           |
| tier                         | core | string        | Optional. The tier of the service.                                                                                                                                                                                                       |
| uid                          | core | string        | Output only. The globally unique resource identifier of the metastore service.                                                                                                                                                           |
| update_time                  | core | timestamp     | Output only. The time when the metastore service was last updated.                                                                                                                                                                       |
| zone_id                      | core | string        |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.datafusion_instance.dataset.md

---
title: Cloud Data Fusion Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Data Fusion Instance
---

# Cloud Data Fusion Instance

Cloud Data Fusion Instance is a fully managed, cloud-native data integration service that allows users to build and manage ETL and ELT data pipelines visually. It provides a graphical interface for designing data flows, connecting to various data sources, transforming data, and loading it into target systems. The service supports both batch and streaming data processing and integrates with other Google Cloud services such as BigQuery, Cloud Storage, and Dataproc. It helps simplify data integration, reduce development time, and improve data reliability across hybrid and multi-cloud environments.

```
gcp.datafusion_instance
```

## Fields

| Title                                     | ID   | Type          | Data Type                                                                                                                                                                                                                            | Description |
| ----------------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                      | core | string        |
| accelerators                              | core | json          | Output only. List of accelerators enabled for this CDF instance.                                                                                                                                                                     |
| ancestors                                 | core | array<string> |
| api_endpoint                              | core | string        | Output only. Endpoint on which the REST APIs is accessible.                                                                                                                                                                          |
| available_version                         | core | json          | Output only. Available versions that the instance can be upgraded to using UpdateInstanceRequest.                                                                                                                                    |
| create_time                               | core | timestamp     | Output only. The time the instance was created.                                                                                                                                                                                      |
| crypto_key_config                         | core | json          | Optional. The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.                                                                                                                   |
| datadog_display_name                      | core | string        |
| dataplex_data_lineage_integration_enabled | core | bool          | Optional. Option to enable the Dataplex Lineage Integration feature.                                                                                                                                                                 |
| dataproc_service_account                  | core | string        | Optional. User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines. This allows users to have fine-grained access control on Dataproc's accesses to cloud resources. |
| description                               | core | string        | Optional. A description of this instance.                                                                                                                                                                                            |
| disabled_reason                           | core | array<string> | Output only. If the instance state is DISABLED, the reason for disabling the instance.                                                                                                                                               |
| enable_rbac                               | core | bool          | Optional. Option to enable granular role-based access control.                                                                                                                                                                       |
| enable_stackdriver_logging                | core | bool          | Optional. Option to enable Dataproc Stackdriver Logging.                                                                                                                                                                             |
| enable_stackdriver_monitoring             | core | bool          | Optional. Option to enable Stackdriver Monitoring.                                                                                                                                                                                   |
| enable_zone_separation                    | core | bool          | Output only. Option to enable granular zone separation.                                                                                                                                                                              |
| event_publish_config                      | core | json          | Optional. Option to enable and pass metadata for event publishing.                                                                                                                                                                   |
| gcp_display_name                          | core | string        | Optional. Display name for an instance.                                                                                                                                                                                              |
| gcs_bucket                                | core | string        | Output only. Cloud Storage bucket generated by Data Fusion in the customer project.                                                                                                                                                  |
| labels                                    | core | array<string> | The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.                                                      |
| logging_config                            | core | json          | Optional. The logging configuration for this instance. This field is supported only in CDF versions 6.11.0 and above.                                                                                                                |
| maintenance_events                        | core | json          | Output only. The maintenance events for this instance.                                                                                                                                                                               |
| maintenance_policy                        | core | json          | Optional. Configure the maintenance policy for this instance.                                                                                                                                                                        |
| name                                      | core | string        | Output only. The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}.                                                                                                               |
| network_config                            | core | json          | Optional. Network configuration options. These are required when a private Data Fusion instance is to be created.                                                                                                                    |
| organization_id                           | core | string        |
| p4_service_account                        | core | string        | Output only. Service agent for the customer project.                                                                                                                                                                                 |
| parent                                    | core | string        |
| patch_revision                            | core | string        | Optional. Current patch revision of the Data Fusion.                                                                                                                                                                                 |
| private_instance                          | core | bool          | Optional. Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet.                                     |
| project_id                                | core | string        |
| project_number                            | core | string        |
| region_id                                 | core | string        |
| resource_name                             | core | string        |
| satisfies_pzi                             | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                |
| satisfies_pzs                             | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                |
| service_account                           | core | string        | Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID.                                                                                                                                             |
| service_endpoint                          | core | string        | Output only. Endpoint on which the Data Fusion UI is accessible.                                                                                                                                                                     |
| state                                     | core | string        | Output only. The current state of this Data Fusion instance.                                                                                                                                                                         |
| state_message                             | core | string        | Output only. Additional information about the current state of this Data Fusion instance if available.                                                                                                                               |
| tags                                      | core | hstore_csv    |
| tenant_project_id                         | core | string        | Output only. The name of the tenant project.                                                                                                                                                                                         |
| type                                      | core | string        | Required. Instance type.                                                                                                                                                                                                             |
| update_time                               | core | timestamp     | Output only. The time the instance was last updated.                                                                                                                                                                                 |
| version                                   | core | string        | Optional. Current version of the Data Fusion. Only specifiable in Update.                                                                                                                                                            |
| workforce_identity_service_endpoint       | core | string        | Output only. Endpoint on which the Data Fusion UI is accessible to third-party users                                                                                                                                                 |
| zone                                      | core | string        | Optional. Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field.                                                                                                               |
| zone_id                                   | core | string        |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.healthlake_datastore.dataset.md

---
title: HealthLake Data Store Properties
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > HealthLake Data Store Properties
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.healthlake_datastore.dataset/index.html
---

# HealthLake Data Store Properties

HealthLake Data Store Properties describe the configuration and status details of an Amazon HealthLake data store. This includes information such as the data store's name, type, creation time, status, and associated metadata. It helps users understand the setup and operational state of their HealthLake data stores, which are used to securely store, transform, and query healthcare data in FHIR format.

```
aws.healthlake_datastore
```

## Fields

| Title                           | ID   | Type      | Data Type                                                                                                                | Description |
| ------------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                            | core | string    |
| account_id                      | core | string    |
| created_at                      | core | timestamp | The time that a data store was created.                                                                                  |
| datastore_arn                   | core | string    | The Amazon Resource Name used in the creation of the data store.                                                         |
| datastore_endpoint              | core | string    | The AWS endpoint for the data store. Each data store will have it's own endpoint with data store ID in the endpoint URL. |
| datastore_id                    | core | string    | The AWS-generated ID number for the data store.                                                                          |
| datastore_name                  | core | string    | The user-generated name for the data store.                                                                              |
| datastore_status                | core | string    | The status of the data store.                                                                                            |
| datastore_type_version          | core | string    | The FHIR version. Only R4 version data is supported.                                                                     |
| error_cause                     | core | json      | The error cause for the current data store operation.                                                                    |
| identity_provider_configuration | core | json      | The identity provider that you selected when you created the data store.                                                 |
| preload_data_config             | core | json      | The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.                      |
| sse_configuration               | core | json      | The server-side encryption key configuration for a customer provided encryption key (CMK).                               |
| tags                            | core | hstore    |

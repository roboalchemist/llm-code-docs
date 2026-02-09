# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.healthlake_datastore.dataset.md

---
title: HealthLake Data Store Properties
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > HealthLake Data Store Properties
---

# HealthLake Data Store Properties

HealthLake Data Store Properties describe the configuration and status details of an Amazon HealthLake data store. This includes information such as the data store's name, type, creation time, status, and associated metadata. It helps users understand the setup and operational state of their HealthLake data stores, which are used to securely store, transform, and query healthcare data in FHIR format.

```
aws.healthlake_datastore
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                | Description |
| ------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| created_at                      | core | timestamp  | The time the data store was created.                                                     |
| datastore_arn                   | core | string     | The Amazon Resource Name (ARN) used in the creation of the data store.                   |
| datastore_endpoint              | core | string     | The AWS endpoint for the data store.                                                     |
| datastore_id                    | core | string     | The data store identifier.                                                               |
| datastore_name                  | core | string     | The data store name.                                                                     |
| datastore_status                | core | string     | The data store status.                                                                   |
| datastore_type_version          | core | string     | The FHIR release version supported by the data store. Current support is for version R4. |
| error_cause                     | core | json       | The error cause for the current data store operation.                                    |
| identity_provider_configuration | core | json       | The identity provider selected during data store creation.                               |
| preload_data_config             | core | json       | The preloaded Synthea data configuration for the data store.                             |
| sse_configuration               | core | json       | The server-side encryption key configuration for a customer provided encryption key.     |
| tags                            | core | hstore_csv |

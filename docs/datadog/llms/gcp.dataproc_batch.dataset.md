# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataproc_batch.dataset.md

---
title: Dataproc Batch
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataproc Batch
---

# Dataproc Batch

Dataproc Batch in Google Cloud is a managed service for running batch workloads using open-source data processing frameworks like Spark, Hive, and PySpark. It allows you to submit jobs without managing clusters directly, as resources are provisioned and scaled automatically for the duration of the job. This makes it efficient for running data transformations, analytics, and machine learning tasks on demand.

```
gcp.dataproc_batch
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time when the batch was created.                                                                                                                                                                                                                                                                                                                            |
| creator              | core | string        | Output only. The email address of the user who created the batch.                                                                                                                                                                                                                                                                                                            |
| datadog_display_name | core | string        |
| environment_config   | core | json          | Optional. Environment configuration for the batch execution.                                                                                                                                                                                                                                                                                                                 |
| labels               | core | array<string> | Optional. The labels to associate with this batch. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a batch. |
| name                 | core | string        | Output only. The resource name of the batch.                                                                                                                                                                                                                                                                                                                                 |
| operation            | core | string        | Output only. The resource name of the operation associated with this batch.                                                                                                                                                                                                                                                                                                  |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| pyspark_batch        | core | json          | Optional. PySpark batch config.                                                                                                                                                                                                                                                                                                                                              |
| region_id            | core | string        |
| resource_name        | core | string        |
| runtime_config       | core | json          | Optional. Runtime configuration for the batch execution.                                                                                                                                                                                                                                                                                                                     |
| runtime_info         | core | json          | Output only. Runtime information about batch execution.                                                                                                                                                                                                                                                                                                                      |
| spark_batch          | core | json          | Optional. Spark batch config.                                                                                                                                                                                                                                                                                                                                                |
| spark_r_batch        | core | json          | Optional. SparkR batch config.                                                                                                                                                                                                                                                                                                                                               |
| spark_sql_batch      | core | json          | Optional. SparkSql batch config.                                                                                                                                                                                                                                                                                                                                             |
| state                | core | string        | Output only. The state of the batch.                                                                                                                                                                                                                                                                                                                                         |
| state_history        | core | json          | Output only. Historical state information for the batch.                                                                                                                                                                                                                                                                                                                     |
| state_message        | core | string        | Output only. Batch state details, such as a failure description if the state is FAILED.                                                                                                                                                                                                                                                                                      |
| state_time           | core | timestamp     | Output only. The time when the batch entered a current state.                                                                                                                                                                                                                                                                                                                |
| tags                 | core | hstore_csv    |
| uuid                 | core | string        | Output only. A batch UUID (Unique Universal Identifier). The service generates this value when it creates the batch.                                                                                                                                                                                                                                                         |
| zone_id              | core | string        |

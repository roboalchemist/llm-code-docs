# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_ingestion_job.dataset.md

---
title: Bedrock Ingestion Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Ingestion Job
---

# Bedrock Ingestion Job

This table represents the Bedrock Ingestion Job resource from Amazon Web Services.

```
aws.bedrock_ingestion_job
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                              | Description |
| ----------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| account_id        | core | string        |
| data_source_id    | core | string        | The unique identifier of the data source for the data ingestion job.                                                                                                   |
| description       | core | string        | The description of the data ingestion job.                                                                                                                             |
| failure_reasons   | core | array<string> | A list of reasons that the data ingestion job failed.                                                                                                                  |
| ingestion_job_id  | core | string        | The unique identifier of the data ingestion job.                                                                                                                       |
| knowledge_base_id | core | string        | The unique identifier of the knowledge for the data ingestion job.                                                                                                     |
| started_at        | core | timestamp     | The time the data ingestion job started. If you stop a data ingestion job, the <code>startedAt</code> time is the time the job was started before the job was stopped. |
| statistics        | core | json          | Contains statistics about the data ingestion job.                                                                                                                      |
| status            | core | string        | The status of the data ingestion job.                                                                                                                                  |
| tags              | core | hstore_csv    |
| updated_at        | core | timestamp     | The time the data ingestion job was last updated. If you stop a data ingestion job, the <code>updatedAt</code> time is the time the job was stopped.                   |

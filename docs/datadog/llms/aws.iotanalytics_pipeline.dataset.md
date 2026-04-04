# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotanalytics_pipeline.dataset.md

---
title: Iotanalytics Pipeline
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iotanalytics Pipeline
---

# Iotanalytics Pipeline

This table represents the iotanalytics_pipeline resource from Amazon Web Services.

```
aws.iotanalytics_pipeline
```

## Fields

| Title                  | ID   | Type       | Data Type                                                    | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| activities             | core | json       | The activities that perform transformations on the messages. |
| arn                    | core | string     | The ARN of the pipeline.                                     |
| creation_time          | core | timestamp  | When the pipeline was created.                               |
| last_update_time       | core | timestamp  | The last time the pipeline was updated.                      |
| name                   | core | string     | The name of the pipeline.                                    |
| reprocessing_summaries | core | json       | A summary of information about the pipeline reprocessing.    |
| tags                   | core | hstore_csv |

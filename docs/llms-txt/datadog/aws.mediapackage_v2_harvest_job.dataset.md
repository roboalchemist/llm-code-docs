# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_v2_harvest_job.dataset.md

---
title: Mediapackage V2 Harvest Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage V2 Harvest Job
---

# Mediapackage V2 Harvest Job

This table represents the mediapackage_v2_harvest_job resource from Amazon Web Services.

```
aws.mediapackage_v2_harvest_job
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                        | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of the harvest job.                                               |
| channel_group_name     | core | string     | The name of the channel group containing the channel associated with this harvest job.           |
| channel_name           | core | string     | The name of the channel associated with this harvest job.                                        |
| created_at             | core | timestamp  | The date and time when the harvest job was created.                                              |
| description            | core | string     | An optional description of the harvest job.                                                      |
| destination            | core | json       | The S3 destination where the harvested content will be placed.                                   |
| e_tag                  | core | string     | The current version of the harvest job. Used for concurrency control.                            |
| error_message          | core | string     | An error message if the harvest job encountered any issues.                                      |
| harvest_job_name       | core | string     | The name of the harvest job.                                                                     |
| harvested_manifests    | core | json       | A list of manifests that are being or have been harvested.                                       |
| modified_at            | core | timestamp  | The date and time when the harvest job was last modified.                                        |
| origin_endpoint_name   | core | string     | The name of the origin endpoint associated with this harvest job.                                |
| schedule_configuration | core | json       | The configuration for when the harvest job is scheduled to run.                                  |
| status                 | core | string     | The current status of the harvest job (e.g., QUEUED, IN_PROGRESS, CANCELLED, COMPLETED, FAILED). |
| tags                   | core | hstore_csv |

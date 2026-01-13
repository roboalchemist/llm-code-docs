# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_job.dataset.md

---
title: IoT Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Job
source_url: https://docs.datadoghq.com/data_directory/aws/aws.iot_job.dataset/index.html
---

# IoT Job

An AWS IoT Job is a managed resource that lets you define and manage remote operations on IoT devices, such as software updates, configuration changes, or running specific tasks. Jobs can be scheduled, monitored, and tracked across fleets of devices, ensuring consistent execution and visibility into progress and outcomes.

```
aws.iot_job
```

## Fields

| Title           | ID   | Type   | Data Type                       | Description |
| --------------- | ---- | ------ | ------------------------------- | ----------- |
| _key            | core | string |
| account_id      | core | string |
| document_source | core | string | An S3 link to the job document. |
| job             | core | json   | Information about the job.      |
| tags            | core | hstore |

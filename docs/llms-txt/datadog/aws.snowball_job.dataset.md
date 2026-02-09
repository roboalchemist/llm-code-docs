# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.snowball_job.dataset.md

---
title: Snowball Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Snowball Job
---

# Snowball Job

Snowball Job in AWS refers to a data transfer task using the AWS Snowball service. It represents the process of moving large amounts of data into or out of AWS using a physical Snowball device. A job tracks details such as device shipment, status, and progress of data transfer, helping customers securely and efficiently migrate data without relying on network bandwidth.

```
aws.snowball_job
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                       | Description |
| ---------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| job_metadata     | core | json       | Information about a specific job, including shipping information, job status, and other important metadata.                                     |
| sub_job_metadata | core | json       | Information about a specific job part (in the case of an export job), including shipping information, job status, and other important metadata. |
| tags             | core | hstore_csv |

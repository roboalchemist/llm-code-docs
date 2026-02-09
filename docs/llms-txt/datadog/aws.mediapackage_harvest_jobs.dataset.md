# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediapackage_harvest_jobs.dataset.md

---
title: Mediapackage Harvest Jobs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediapackage Harvest Jobs
---

# Mediapackage Harvest Jobs

This table represents the mediapackage_harvest_jobs resource from Amazon Web Services.

```
aws.mediapackage_harvest_jobs
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                             | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Name (ARN) assigned to the HarvestJob.                                                                                                                                                                            |
| channel_id         | core | string     | The ID of the Channel that the HarvestJob will harvest from.                                                                                                                                                                          |
| created_at         | core | string     | The date and time the HarvestJob was submitted.                                                                                                                                                                                       |
| end_time           | core | string     | The end of the time-window which will be harvested.                                                                                                                                                                                   |
| id                 | core | string     | The ID of the HarvestJob. The ID must be unique within the regionand it cannot be changed after the HarvestJob is submitted.                                                                                                          |
| origin_endpoint_id | core | string     | The ID of the OriginEndpoint that the HarvestJob will harvest from.This cannot be changed after the HarvestJob is submitted.                                                                                                          |
| s3_destination     | core | json       |
| start_time         | core | string     | The start of the time-window which will be harvested.                                                                                                                                                                                 |
| status             | core | string     | The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen forHarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event willinclude an explanation of why the HarvestJob failed. |
| tags               | core | hstore_csv |

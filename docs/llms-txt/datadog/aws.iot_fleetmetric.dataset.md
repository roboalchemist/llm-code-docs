# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_fleetmetric.dataset.md

---
title: Iot Fleetmetric
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Fleetmetric
---

# Iot Fleetmetric

This table represents the iot_fleetmetric resource from Amazon Web Services.

```
aws.iot_fleetmetric
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                         | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| aggregation_field  | core | string     | The field to aggregate.                                                                                                                                                                                           |
| aggregation_type   | core | json       | The type of the aggregation query.                                                                                                                                                                                |
| creation_date      | core | timestamp  | The date when the fleet metric is created.                                                                                                                                                                        |
| description        | core | string     | The fleet metric description.                                                                                                                                                                                     |
| index_name         | core | string     | The name of the index to search.                                                                                                                                                                                  |
| last_modified_date | core | timestamp  | The date when the fleet metric is last modified.                                                                                                                                                                  |
| metric_arn         | core | string     | The ARN of the fleet metric to describe.                                                                                                                                                                          |
| metric_name        | core | string     | The name of the fleet metric to describe.                                                                                                                                                                         |
| period             | core | int64      | The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.                                                                                                   |
| query_string       | core | string     | The search query string.                                                                                                                                                                                          |
| query_version      | core | string     | The query version.                                                                                                                                                                                                |
| tags               | core | hstore_csv |
| unit               | core | string     | Used to support unit transformation such as milliseconds to seconds. The unit must be supported by <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html">CW metric</a>. |
| version            | core | int64      | The version of the fleet metric.                                                                                                                                                                                  |

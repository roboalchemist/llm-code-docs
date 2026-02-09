# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_cloudwatch_alarm_template.dataset.md

---
title: Medialive Cloudwatch Alarm Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Medialive Cloudwatch Alarm Template
---

# Medialive Cloudwatch Alarm Template

This table represents the medialive_cloudwatch_alarm_template resource from Amazon Web Services.

```
aws.medialive_cloudwatch_alarm_template
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                            | Description |
| -------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| arn                  | core | string     | A cloudwatch alarm template's ARN (Amazon Resource Name)                                             |
| comparison_operator  | core | string     |
| created_at           | core | timestamp  |
| datapoints_to_alarm  | core | int64      | The number of datapoints within the evaluation period that must be breaching to trigger the alarm.   |
| description          | core | string     | A resource's optional description.                                                                   |
| evaluation_periods   | core | int64      | The number of periods over which data is compared to the specified threshold.                        |
| group_id             | core | string     | A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-` |
| id                   | core | string     | A cloudwatch alarm template's id. AWS provided templates have ids that start with `aws-`             |
| metric_name          | core | string     | The name of the metric associated with the alarm. Must be compatible with targetResourceType.        |
| modified_at          | core | timestamp  |
| name                 | core | string     | A resource's name. Names must be unique within the scope of a resource type in a specific region.    |
| period               | core | int64      | The period, in seconds, over which the specified statistic is applied.                               |
| statistic            | core | string     |
| tags                 | core | hstore_csv |
| target_resource_type | core | string     |
| threshold            | core | float64    | The threshold value to compare with the specified statistic.                                         |
| treat_missing_data   | core | string     |

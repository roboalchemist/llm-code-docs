# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_cloudwatch_alarm_template_group.dataset.md

---
title: Medialive Cloudwatch Alarm Template Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Medialive Cloudwatch Alarm Template
  Group
---

# Medialive Cloudwatch Alarm Template Group

This table represents the medialive_cloudwatch_alarm_template_group resource from Amazon Web Services.

```
aws.medialive_cloudwatch_alarm_template_group
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                            | Description |
| -------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| arn            | core | string     | A cloudwatch alarm template group's ARN (Amazon Resource Name)                                       |
| created_at     | core | timestamp  |
| description    | core | string     | A resource's optional description.                                                                   |
| id             | core | string     | A cloudwatch alarm template group's id. AWS provided template groups have ids that start with `aws-` |
| modified_at    | core | timestamp  |
| name           | core | string     | A resource's name. Names must be unique within the scope of a resource type in a specific region.    |
| tags           | core | hstore_csv |
| template_count | core | int64      | The number of templates in a group.                                                                  |

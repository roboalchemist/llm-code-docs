# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_eventbridge_rule_template.dataset.md

---
title: Medialive Eventbridge Rule Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Medialive Eventbridge Rule Template
---

# Medialive Eventbridge Rule Template

This table represents the medialive_eventbridge_rule_template resource from Amazon Web Services.

```
aws.medialive_eventbridge_rule_template
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                             | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | An eventbridge rule template's ARN (Amazon Resource Name)                                             |
| created_at         | core | timestamp  |
| description        | core | string     | A resource's optional description.                                                                    |
| event_target_count | core | int64      | The number of targets configured to send matching events.                                             |
| event_type         | core | string     |
| group_id           | core | string     | An eventbridge rule template group's id. AWS provided template groups have ids that start with `aws-` |
| id                 | core | string     | An eventbridge rule template's id. AWS provided templates have ids that start with `aws-`             |
| modified_at        | core | timestamp  |
| name               | core | string     | A resource's name. Names must be unique within the scope of a resource type in a specific region.     |
| tags               | core | hstore_csv |

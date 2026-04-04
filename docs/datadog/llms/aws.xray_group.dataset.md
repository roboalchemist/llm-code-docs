# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.xray_group.dataset.md

---
title: X-Ray Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > X-Ray Group
---

# X-Ray Group

An X-Ray Group in AWS is a logical grouping of traces that share specific criteria, such as a filter expression. It allows you to organize and analyze subsets of trace data for applications monitored with AWS X-Ray. Groups help you focus on particular services, users, or request patterns, and you can configure them to generate insights and metrics for performance and error analysis.

```
aws.xray_group
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                     | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| filter_expression      | core | string     | The filter expression defining the parameters to include traces.                                                                                                                                                                                                                                                                                              |
| group_arn              | core | string     | The ARN of the group generated based on the GroupName.                                                                                                                                                                                                                                                                                                        |
| group_name             | core | string     | The unique case-sensitive name of the group.                                                                                                                                                                                                                                                                                                                  |
| insights_configuration | core | json       | The structure containing configurations related to insights. The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group. The NotificationsEnabled boolean can be set to true to enable insights notifications. Notifications can only be enabled on a group with InsightsEnabled set to true. |
| tags                   | core | hstore_csv |

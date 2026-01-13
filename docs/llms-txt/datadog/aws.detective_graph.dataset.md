# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.detective_graph.dataset.md

---
title: Detective Graph
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Detective Graph
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.detective_graph.dataset/index.html
---

# Detective Graph

Amazon Detective Graph is the core resource that represents a behavior graph in Amazon Detective. A behavior graph collects and organizes data from AWS resources, such as CloudTrail logs, VPC Flow Logs, and GuardDuty findings, to help analyze and visualize security-related activities. It enables security teams to investigate potential security issues, uncover relationships between entities, and identify root causes more efficiently.

```
aws.detective_graph
```

## Fields

| Title        | ID   | Type      | Data Type                                                                                                                               | Description |
| ------------ | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key         | core | string    |
| account_id   | core | string    |
| arn          | core | string    | The ARN of the behavior graph.                                                                                                          |
| created_time | core | timestamp | The date and time that the behavior graph was created. The value is an ISO8601 formatted string. For example, 2021-08-18T16:35:56.284Z. |
| tags         | core | hstore    |

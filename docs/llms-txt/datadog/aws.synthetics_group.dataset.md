# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.synthetics_group.dataset.md

---
title: CloudWatch Synthetics Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudWatch Synthetics Group
---

# CloudWatch Synthetics Group

CloudWatch Synthetics Group is a resource in AWS that represents a collection of canaries, which are configurable scripts that monitor endpoints and APIs by simulating user interactions. This group allows you to organize and manage multiple canaries together, making it easier to track performance, availability, and errors across related synthetic tests. It helps streamline monitoring and troubleshooting by grouping canaries with similar purposes or applications.

```
aws.synthetics_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                   | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the group.                                       |
| created_time       | core | timestamp  | The date and time that the group was created.               |
| id                 | core | string     | The unique ID of the group.                                 |
| last_modified_time | core | timestamp  | The date and time that the group was most recently updated. |
| name               | core | string     | The name of the group.                                      |
| tags               | core | hstore_csv |

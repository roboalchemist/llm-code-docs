# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_group.dataset.md

---
title: QuickSight Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Group
---

# QuickSight Group

An AWS QuickSight Group is a collection of users within Amazon QuickSight that allows administrators to manage permissions and access at scale. By organizing users into groups, you can assign datasets, dashboards, and analyses to multiple users at once, simplifying governance and collaboration. Groups help ensure consistent access control and make it easier to manage large numbers of users in an enterprise environment.

```
aws.quicksight_group
```

## Fields

| Title        | ID   | Type       | Data Type                                     | Description |
| ------------ | ---- | ---------- | --------------------------------------------- | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| arn          | core | string     | The Amazon Resource Name (ARN) for the group. |
| description  | core | string     | The group description.                        |
| group_name   | core | string     | The name of the group.                        |
| principal_id | core | string     | The principal ID of the group.                |
| tags         | core | hstore_csv |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_ip_group.dataset.md

---
title: WorkSpaces IP Access Control Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > WorkSpaces IP Access Control Group
---

# WorkSpaces IP Access Control Group

An AWS WorkSpaces IP Access Control Group is a resource that lets you define and manage sets of trusted IP address ranges for Amazon WorkSpaces. By associating these groups with your WorkSpaces directories, you can restrict access so that users can only connect from approved networks, enhancing security and compliance.

```
aws.workspaces_ip_group
```

## Fields

| Title      | ID   | Type       | Data Type                     | Description |
| ---------- | ---- | ---------- | ----------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| group_desc | core | string     | The description of the group. |
| group_id   | core | string     | The identifier of the group.  |
| group_name | core | string     | The name of the group.        |
| tags       | core | hstore_csv |
| user_rules | core | json       | The rules.                    |

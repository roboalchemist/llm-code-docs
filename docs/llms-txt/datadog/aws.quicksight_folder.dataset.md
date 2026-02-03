# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_folder.dataset.md

---
title: QuickSight Folder
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Folder
---

# QuickSight Folder

QuickSight Folder in AWS is a container used to organize and manage QuickSight assets such as dashboards, analyses, and datasets. It helps structure content for easier navigation, access control, and sharing within an organization. Folders support permissions, allowing administrators to control who can view or modify the assets inside.

```
aws.quicksight_folder
```

## Fields

| Title      | ID   | Type       | Data Type                                              | Description |
| ---------- | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| folder     | core | json       | Information about the folder.                          |
| request_id | core | string     | The Amazon Web Services request ID for this operation. |
| status     | core | int64      | The HTTP status of the request.                        |
| tags       | core | hstore_csv |

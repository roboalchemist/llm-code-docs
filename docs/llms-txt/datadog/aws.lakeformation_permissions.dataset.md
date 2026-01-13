# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lakeformation_permissions.dataset.md

---
title: Lake Formation Permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lake Formation Permissions
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.lakeformation_permissions.dataset/index.html
---

# Lake Formation Permissions

Lake Formation Permissions in AWS define the access rights granted to principals for data stored in the Data Lake. They control which users or roles can perform actions such as reading, writing, or managing metadata on databases, tables, and data locations. This resource helps enforce fine-grained security and governance across data assets.

```
aws.lakeformation_permissions
```

## Fields

| Title                          | ID   | Type   | Data Type                                                                                                  | Description |
| ------------------------------ | ---- | ------ | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string |
| account_id                     | core | string |
| principal_resource_permissions | core | json   | A list of principals and their permissions on the resource for the specified principal and resource types. |
| tags                           | core | hstore |

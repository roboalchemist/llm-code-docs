# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_thinggroup.dataset.md

---
title: Iot Thinggroup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Thinggroup
---

# Iot Thinggroup

This table represents the iot_thinggroup resource from Amazon Web Services.

```
aws.iot_thinggroup
```

## Fields

| Title                  | ID   | Type       | Data Type                                    | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| index_name             | core | string     | The dynamic thing group index name.          |
| query_string           | core | string     | The dynamic thing group search query string. |
| query_version          | core | string     | The dynamic thing group query version.       |
| status                 | core | string     | The dynamic thing group status.              |
| tags                   | core | hstore_csv |
| thing_group_arn        | core | string     | The thing group ARN.                         |
| thing_group_id         | core | string     | The thing group ID.                          |
| thing_group_metadata   | core | json       | Thing group metadata.                        |
| thing_group_name       | core | string     | The name of the thing group.                 |
| thing_group_properties | core | json       | The thing group properties.                  |
| version                | core | int64      | The version of the thing group.              |

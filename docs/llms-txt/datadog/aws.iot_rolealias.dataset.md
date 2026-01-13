# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_rolealias.dataset.md

---
title: Iot Rolealias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Rolealias
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iot_rolealias.dataset/index.html
---

# Iot Rolealias

This table represents the iot_rolealias resource from Amazon Web Services.

```
aws.iot_rolealias
```

## Fields

| Title                       | ID   | Type      | Data Type                                                    | Description |
| --------------------------- | ---- | --------- | ------------------------------------------------------------ | ----------- |
| _key                        | core | string    |
| account_id                  | core | string    |
| creation_date               | core | timestamp | The UNIX timestamp of when the role alias was created.       |
| credential_duration_seconds | core | int64     | The number of seconds for which the credential is valid.     |
| last_modified_date          | core | timestamp | The UNIX timestamp of when the role alias was last modified. |
| owner                       | core | string    | The role alias owner.                                        |
| role_alias                  | core | string    | The role alias.                                              |
| role_alias_arn              | core | string    | The ARN of the role alias.                                   |
| role_arn                    | core | string    | The role ARN.                                                |
| tags                        | core | hstore    |

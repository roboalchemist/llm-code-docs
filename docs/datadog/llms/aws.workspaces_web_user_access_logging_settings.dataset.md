# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_user_access_logging_settings.dataset.md

---
title: Workspaces Web User Access Logging Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Workspaces Web User Access Logging
  Settings
---

# Workspaces Web User Access Logging Settings

This table represents the workspaces_web_user_access_logging_settings resource from Amazon Web Services.

```
aws.workspaces_web_user_access_logging_settings
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                            | Description |
| -------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------ | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| associated_portal_arns           | core | array<string> | A list of web portal ARNs that this user access logging settings is associated with. |
| kinesis_stream_arn               | core | string        | The ARN of the Kinesis stream.                                                       |
| tags                             | core | hstore_csv    |
| user_access_logging_settings_arn | core | string        | The ARN of the user access logging settings.                                         |

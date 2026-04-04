# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_data_protection_settings.dataset.md

---
title: Workspaces Web Data Protection Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Workspaces Web Data Protection
  Settings
---

# Workspaces Web Data Protection Settings

This table represents the workspaces_web_data_protection_settings resource from Amazon Web Services.

```
aws.workspaces_web_data_protection_settings
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                 | Description |
| ------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| account_id                     | core | string        |
| additional_encryption_context  | core | hstore        | The additional encryption context of the data protection settings.                        |
| associated_portal_arns         | core | array<string> | A list of web portal ARNs that this data protection settings resource is associated with. |
| creation_date                  | core | timestamp     | The creation date timestamp of the data protection settings.                              |
| data_protection_settings_arn   | core | string        | The ARN of the data protection settings resource.                                         |
| description                    | core | string        | The description of the data protection settings.                                          |
| inline_redaction_configuration | core | json          | The inline redaction configuration for the data protection settings.                      |
| tags                           | core | hstore_csv    |

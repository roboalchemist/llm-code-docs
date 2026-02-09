# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_browser_settings.dataset.md

---
title: Workspaces Web Browser Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workspaces Web Browser Settings
---

# Workspaces Web Browser Settings

This table represents the workspaces_web_browser_settings resource from Amazon Web Services.

```
aws.workspaces_web_browser_settings
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                           | Description |
| ----------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| account_id                    | core | string        |
| additional_encryption_context | core | hstore        | The additional encryption context of the browser settings.                                          |
| associated_portal_arns        | core | array<string> | A list of web portal ARNs that this browser settings is associated with.                            |
| browser_policy                | core | string        | A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions. |
| browser_settings_arn          | core | string        | The ARN of the browser settings.                                                                    |
| tags                          | core | hstore_csv    |

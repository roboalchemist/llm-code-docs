# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_user_settings.dataset.md

---
title: Workspaces Web User Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workspaces Web User Settings
---

# Workspaces Web User Settings

This table represents the workspaces_web_user_settings resource from Amazon Web Services.

```
aws.workspaces_web_user_settings
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string        |
| account_id                           | core | string        |
| additional_encryption_context        | core | hstore        | The additional encryption context of the user settings.                                                                                                                                                                                                                                                                               |
| associated_portal_arns               | core | array<string> | A list of web portal ARNs that this user settings is associated with.                                                                                                                                                                                                                                                                 |
| cookie_synchronization_configuration | core | json          | The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.                                                                                                                                                                                                        |
| copy_allowed                         | core | string        | Specifies whether the user can copy text from the streaming session to the local device.                                                                                                                                                                                                                                              |
| deep_link_allowed                    | core | string        | Specifies whether the user can use deep links that open automatically when connecting to a session.                                                                                                                                                                                                                                   |
| disconnect_timeout_in_minutes        | core | int64         | The amount of time that a streaming session remains active after users disconnect.                                                                                                                                                                                                                                                    |
| download_allowed                     | core | string        | Specifies whether the user can download files from the streaming session to the local device.                                                                                                                                                                                                                                         |
| idle_disconnect_timeout_in_minutes   | core | int64         | The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.                                                                                                                                                                            |
| paste_allowed                        | core | string        | Specifies whether the user can paste text from the local device to the streaming session.                                                                                                                                                                                                                                             |
| print_allowed                        | core | string        | Specifies whether the user can print to the local device.                                                                                                                                                                                                                                                                             |
| tags                                 | core | hstore_csv    |
| toolbar_configuration                | core | json          | The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences. |
| upload_allowed                       | core | string        | Specifies whether the user can upload files from the local device to the streaming session.                                                                                                                                                                                                                                           |
| user_settings_arn                    | core | string        | The ARN of the user settings.                                                                                                                                                                                                                                                                                                         |

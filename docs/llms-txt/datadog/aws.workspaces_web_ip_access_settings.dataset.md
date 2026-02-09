# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_web_ip_access_settings.dataset.md

---
title: Workspaces Web Ip Access Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workspaces Web Ip Access Settings
---

# Workspaces Web Ip Access Settings

This table represents the workspaces_web_ip_access_settings resource from Amazon Web Services.

```
aws.workspaces_web_ip_access_settings
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                           | Description |
| ----------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| account_id                    | core | string        |
| additional_encryption_context | core | hstore        | The additional encryption context of the IP access settings.                        |
| associated_portal_arns        | core | array<string> | A list of web portal ARNs that this IP access settings resource is associated with. |
| creation_date                 | core | timestamp     | The creation date timestamp of the IP access settings.                              |
| description                   | core | string        | The description of the IP access settings.                                          |
| ip_access_settings_arn        | core | string        | The ARN of the IP access settings resource.                                         |
| ip_rules                      | core | json          | The IP rules of the IP access settings.                                             |
| tags                          | core | hstore_csv    |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appconfig_extensionassociation.dataset.md

---
title: Appconfig Extensionassociation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Appconfig Extensionassociation
---

# Appconfig Extensionassociation

This table represents the appconfig_extensionassociation resource from Amazon Web Services.

```
aws.appconfig_extensionassociation
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                     | Description |
| ------------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| arn                      | core | string     | The system-generated Amazon Resource Name (ARN) for the extension.                            |
| extension_arn            | core | string     | The ARN of the extension defined in the association.                                          |
| extension_version_number | core | int64      | The version number for the extension defined in the association.                              |
| id                       | core | string     | The system-generated ID for the association.                                                  |
| parameters               | core | hstore     | The parameter names and values defined in the association.                                    |
| resource_arn             | core | string     | The ARNs of applications, configuration profiles, or environments defined in the association. |
| tags                     | core | hstore_csv |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.workspaces_application.dataset.md

---
title: Workspaces Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Workspaces Application
---

# Workspaces Application

This table represents the workspaces_application resource from Amazon Web Services.

```
aws.workspaces_application
```

## Fields

| Title                            | ID   | Type          | Data Type                                                     | Description |
| -------------------------------- | ---- | ------------- | ------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| application_id                   | core | string        | The identifier of the application.                            |
| created                          | core | timestamp     | The time the application is created.                          |
| description                      | core | string        | The description of the WorkSpace application.                 |
| license_type                     | core | string        | The license availability for the applications.                |
| name                             | core | string        | The name of the WorkSpace application.                        |
| owner                            | core | string        | The owner of the WorkSpace application.                       |
| state                            | core | string        | The status of WorkSpace application.                          |
| supported_compute_type_names     | core | array<string> | The supported compute types of the WorkSpace application.     |
| supported_operating_system_names | core | array<string> | The supported operating systems of the WorkSpace application. |
| tags                             | core | hstore_csv    |

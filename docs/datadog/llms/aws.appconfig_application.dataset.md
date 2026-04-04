# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appconfig_application.dataset.md

---
title: AWS AppConfig Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS AppConfig Application
---

# AWS AppConfig Application

AWS AppConfig Application is a logical container within AWS AppConfig used to manage configuration data for one or more environments. It helps you define, validate, and deploy configuration changes safely and quickly across applications, reducing the risk of errors during updates.

```
aws.appconfig_application
```

## Fields

| Title       | ID   | Type       | Data Type                           | Description |
| ----------- | ---- | ---------- | ----------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| description | core | string     | The description of the application. |
| id          | core | string     | The application ID.                 |
| name        | core | string     | The application name.               |
| tags        | core | hstore_csv |

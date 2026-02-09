# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appconfig_extension.dataset.md

---
title: AWS AppConfig Extension
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS AppConfig Extension
---

# AWS AppConfig Extension

AWS AppConfig Extension is a component that allows you to extend the functionality of AWS AppConfig by integrating with other AWS services or third-party tools. It enables custom logic to run during configuration deployments, such as validating configurations, sending notifications, or triggering workflows. Extensions help automate and enhance the configuration management process within AppConfig environments.

```
aws.appconfig_extension
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                      | Description |
| -------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| actions        | core | string     | The actions defined in the extension.                                                                                                                                                                                                                                          |
| arn            | core | string     | The system-generated Amazon Resource Name (ARN) for the extension.                                                                                                                                                                                                             |
| description    | core | string     | Information about the extension.                                                                                                                                                                                                                                               |
| id             | core | string     | The system-generated ID of the extension.                                                                                                                                                                                                                                      |
| name           | core | string     | The extension name.                                                                                                                                                                                                                                                            |
| parameters     | core | string     | The parameters accepted by the extension. You specify parameter values when you associate the extension to an AppConfig resource by using the CreateExtensionAssociation API action. For Lambda extension actions, these parameters are included in the Lambda request object. |
| tags           | core | hstore_csv |
| version_number | core | int64      | The extension version number.                                                                                                                                                                                                                                                  |

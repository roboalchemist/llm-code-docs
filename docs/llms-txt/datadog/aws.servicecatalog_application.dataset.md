# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.servicecatalog_application.dataset.md

---
title: Service Catalog Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Catalog Application
---

# Service Catalog Application

Service Catalog Application in AWS AppRegistry represents a registered application that helps organize and manage resources across environments. It provides metadata, associations, and insights into how resources are grouped, enabling better governance, visibility, and lifecycle management of applications within AWS Service Catalog.

```
aws.servicecatalog_application
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                     | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| application_tag           | core | hstore     | A key-value pair that identifies an associated resource.                                                      |
| arn                       | core | string     | The Amazon resource name (ARN) that specifies the application across services.                                |
| associated_resource_count | core | int64      | The number of top-level resources that were registered as part of this application.                           |
| creation_time             | core | timestamp  | The ISO-8601 formatted timestamp of the moment when the application was created.                              |
| description               | core | string     | The description of the application.                                                                           |
| id                        | core | string     | The identifier of the application.                                                                            |
| integrations              | core | json       | The information about the integration of the application with other services, such as Resource Groups.        |
| last_update_time          | core | timestamp  | The ISO-8601 formatted timestamp of the moment when the application was last updated.                         |
| name                      | core | string     | The name of the application. The name must be unique in the region in which you are creating the application. |
| tags                      | core | hstore_csv |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_service.dataset.md

---
title: Proton Service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Service
---

# Proton Service

Proton Service in AWS Proton represents a deployable application composed of infrastructure and code defined by a service template. It allows platform teams to define standardized architectures while enabling developers to provision and manage services consistently. This resource provides details about a specific service, including its configuration, status, and outputs, helping teams manage lifecycle operations such as deployment, updates, and monitoring.

```
aws.proton_service
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                              | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The Amazon Resource Name (ARN) of the service.                                                                                                         |
| branch_name               | core | string     | The name of the code repository branch that holds the code that's deployed in Proton.                                                                  |
| created_at                | core | timestamp  | The time when the service was created.                                                                                                                 |
| description               | core | string     | A description of the service.                                                                                                                          |
| last_modified_at          | core | timestamp  | The time when the service was last modified.                                                                                                           |
| name                      | core | string     | The name of the service.                                                                                                                               |
| pipeline                  | core | json       | The service pipeline detail data.                                                                                                                      |
| repository_connection_arn | core | string     | The Amazon Resource Name (ARN) of the repository connection. For more information, see Setting up an AWS CodeStar connection in the Proton User Guide. |
| repository_id             | core | string     | The ID of the source code repository.                                                                                                                  |
| spec                      | core | string     | The formatted specification that defines the service.                                                                                                  |
| status                    | core | string     | The status of the service.                                                                                                                             |
| status_message            | core | string     | A service status message.                                                                                                                              |
| tags                      | core | hstore_csv |
| template_name             | core | string     | The name of the service template.                                                                                                                      |

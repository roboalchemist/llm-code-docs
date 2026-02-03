# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_service_instance.dataset.md

---
title: Proton Service Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Service Instance
---

# Proton Service Instance

An AWS Proton Service Instance is a deployed copy of a service within Proton, AWS's fully managed application delivery service. It represents a running version of a service that uses predefined infrastructure and CI/CD templates. Service instances allow teams to consistently provision and manage applications across environments, ensuring standardized deployments and easier lifecycle management.

```
aws.proton_service_instance
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                               | Description |
| ---------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| arn                          | core | string     | The Amazon Resource Name (ARN) of the service instance.                                 |
| created_at                   | core | timestamp  | The time when the service instance was created.                                         |
| deployment_status            | core | string     | The service instance deployment status.                                                 |
| deployment_status_message    | core | string     | The message associated with the service instance deployment status.                     |
| environment_name             | core | string     | The name of the environment that the service instance was deployed into.                |
| last_attempted_deployment_id | core | string     | The ID of the last attempted deployment of this service instance.                       |
| last_client_request_token    | core | string     | The last client request token received.                                                 |
| last_deployment_attempted_at | core | timestamp  | The time when a deployment of the service instance was last attempted.                  |
| last_deployment_succeeded_at | core | timestamp  | The time when the service instance was last deployed successfully.                      |
| last_succeeded_deployment_id | core | string     | The ID of the last successful deployment of this service instance.                      |
| name                         | core | string     | The name of the service instance.                                                       |
| service_name                 | core | string     | The name of the service that the service instance belongs to.                           |
| spec                         | core | string     | The service spec that was used to create the service instance.                          |
| tags                         | core | hstore_csv |
| template_major_version       | core | string     | The major version of the service template that was used to create the service instance. |
| template_minor_version       | core | string     | The minor version of the service template that was used to create the service instance. |
| template_name                | core | string     | The name of the service template that was used to create the service instance.          |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_deployment.dataset.md

---
title: Proton Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Deployment
---

# Proton Deployment

Proton Deployment in AWS Proton represents the process of rolling out infrastructure or application changes defined in a Proton service or environment. It manages the deployment lifecycle, tracks status, and provides outputs related to the deployment execution. This helps teams standardize and automate deployments across multiple environments while ensuring consistency and visibility.

```
aws.proton_deployment
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                      | Description |
| ---------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| arn                          | core | string     | The Amazon Resource Name (ARN) of the deployment.                                                              |
| completed_at                 | core | timestamp  | The date and time the deployment was completed.                                                                |
| component_name               | core | string     | The name of the component associated with this deployment.                                                     |
| created_at                   | core | timestamp  | The date and time the deployment was created.                                                                  |
| deployment_status            | core | string     | The status of the deployment.                                                                                  |
| deployment_status_message    | core | string     | The deployment status message.                                                                                 |
| environment_name             | core | string     | The name of the environment associated with this deployment.                                                   |
| id                           | core | string     | The ID of the deployment.                                                                                      |
| initial_state                | core | json       | The initial state of the target resource at the time of the deployment.                                        |
| last_attempted_deployment_id | core | string     | The ID of the last attempted deployment.                                                                       |
| last_modified_at             | core | timestamp  | The date and time the deployment was last modified.                                                            |
| last_succeeded_deployment_id | core | string     | The ID of the last successful deployment.                                                                      |
| service_instance_name        | core | string     | The name of the deployment's service instance.                                                                 |
| service_name                 | core | string     | The name of the service in this deployment.                                                                    |
| tags                         | core | hstore_csv |
| target_arn                   | core | string     | The Amazon Resource Name (ARN) of the target of the deployment.                                                |
| target_resource_created_at   | core | timestamp  | The date and time the depoyment target was created.                                                            |
| target_resource_type         | core | string     | The resource type of the deployment target. It can be an environment, service, service instance, or component. |
| target_state                 | core | json       | The target state of the target resource at the time of the deployment.                                         |

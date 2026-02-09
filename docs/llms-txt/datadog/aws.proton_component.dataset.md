# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_component.dataset.md

---
title: Proton Component
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Component
---

# Proton Component

Proton Component in AWS Proton represents a building block of infrastructure or application resources that can be created, managed, and deployed as part of an environment or service. It allows teams to define reusable infrastructure templates and standardize deployments across applications. Components help enforce consistency, security, and compliance by encapsulating infrastructure definitions and making them available for use in Proton-managed services.

```
aws.proton_component
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                         | Description |
| ---------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| arn                          | core | string     | The Amazon Resource Name (ARN) of the component.                                                                                  |
| created_at                   | core | timestamp  | The time when the component was created.                                                                                          |
| deployment_status            | core | string     | The component deployment status.                                                                                                  |
| deployment_status_message    | core | string     | The message associated with the component deployment status.                                                                      |
| description                  | core | string     | A description of the component.                                                                                                   |
| environment_name             | core | string     | The name of the Proton environment that this component is associated with.                                                        |
| last_attempted_deployment_id | core | string     | The ID of the last attempted deployment of this component.                                                                        |
| last_client_request_token    | core | string     | The last token the client requested.                                                                                              |
| last_deployment_attempted_at | core | timestamp  | The time when a deployment of the component was last attempted.                                                                   |
| last_deployment_succeeded_at | core | timestamp  | The time when the component was last deployed successfully.                                                                       |
| last_modified_at             | core | timestamp  | The time when the component was last modified.                                                                                    |
| last_succeeded_deployment_id | core | string     | The ID of the last successful deployment of this component.                                                                       |
| name                         | core | string     | The name of the component.                                                                                                        |
| service_instance_name        | core | string     | The name of the service instance that this component is attached to. Provided when a component is attached to a service instance. |
| service_name                 | core | string     | The name of the service that serviceInstanceName is associated with. Provided when a component is attached to a service instance. |
| service_spec                 | core | string     | The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.   |
| tags                         | core | hstore_csv |

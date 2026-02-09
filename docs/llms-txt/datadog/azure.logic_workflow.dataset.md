# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.logic_workflow.dataset.md

---
title: Logic Apps Workflow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Logic Apps Workflow
---

# Logic Apps Workflow

Logic Apps Workflow in Azure is a serverless resource that enables you to automate workflows and integrate applications, data, and services across cloud and on-premises environments. It provides a visual designer to build workflows using prebuilt connectors, triggers, and actions, making it easier to orchestrate business processes without writing extensive code.

```
azure.logic_workflow
```

## Fields

| Title                           | ID   | Type       | Data Type                            | Description |
| ------------------------------- | ---- | ---------- | ------------------------------------ | ----------- |
| _key                            | core | string     |
| access_control                  | core | json       | The access control configuration.    |
| access_endpoint                 | core | string     | Gets the access endpoint.            |
| changed_time                    | core | string     | Gets the changed time.               |
| created_time                    | core | string     | Gets the created time.               |
| definition                      | core | json       | The definition.                      |
| endpoints_configuration         | core | json       | The endpoints configuration.         |
| id                              | core | string     | The resource id.                     |
| identity                        | core | json       | Managed service identity properties. |
| integration_account             | core | json       | The resource reference.              |
| integration_service_environment | core | json       | The resource reference.              |
| location                        | core | string     | The resource location.               |
| name                            | core | string     | Gets the resource name.              |
| provisioning_state              | core | string     | The workflow provisioning state.     |
| resource_group                  | core | string     |
| sku                             | core | json       | The sku type.                        |
| state                           | core | string     | The workflow state.                  |
| subscription_id                 | core | string     |
| subscription_name               | core | string     |
| tags                            | core | hstore_csv |
| type                            | core | string     | Gets the resource type.              |
| version                         | core | string     | Gets the version.                    |

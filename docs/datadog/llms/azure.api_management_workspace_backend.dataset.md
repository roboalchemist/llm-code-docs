# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.api_management_workspace_backend.dataset.md

---
title: Api Management Workspace Backend
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Api Management Workspace Backend
---

# Api Management Workspace Backend

This table represents the api_management_workspace_backend resource from Microsoft Azure.

```
azure.api_management_workspace_backend
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ---------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| circuit_breaker        | core | json       | Backend Circuit Breaker Configuration                                                                                                                                                     |
| credentials            | core | json       | Backend Credentials Contract Properties                                                                                                                                                   |
| description            | core | string     | Backend Description.                                                                                                                                                                      |
| id                     | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| location               | core | string     |
| name                   | core | string     | The name of the resource                                                                                                                                                                  |
| pool                   | core | json       |
| protocol               | core | string     | Backend communication protocol. Required when backend type is 'Single'.                                                                                                                   |
| proxy                  | core | json       | Backend gateway Contract Properties                                                                                                                                                       |
| resource_group         | core | string     |
| resource_id            | core | string     | Management Uri of the Resource in External System. This URL can be the Arm Resource Id of Logic Apps, Function Apps or API Apps.                                                          |
| service_fabric_cluster | core | json       | Backend Service Fabric Cluster Properties                                                                                                                                                 |
| subscription_id        | core | string     |
| subscription_name      | core | string     |
| tags                   | core | hstore_csv |
| title                  | core | string     | Backend Title.                                                                                                                                                                            |
| tls                    | core | json       | Backend TLS Properties                                                                                                                                                                    |
| type                   | core | string     | Type of the backend. A backend can be either Single or Pool.                                                                                                                              |
| url                    | core | string     | Runtime Url of the Backend. Required when backend type is 'Single'.                                                                                                                       |

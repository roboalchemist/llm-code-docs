# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.app_managed_environment.dataset.md

---
title: App Managed Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Managed Environment
---

# App Managed Environment

This table represents the app_managed_environment resource from Microsoft Azure.

```
azure.app_managed_environment
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                                                                 | Description |
| ----------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| app_logs_configuration        | core | json       | Cluster configuration which enables the log daemon to export app logs to configured destination.                                                                                                                          |
| custom_domain_configuration   | core | json       | Custom domain configuration for the environment                                                                                                                                                                           |
| dapr_ai_connection_string     | core | string     | Application Insights connection string used by Dapr to export Service to Service communication telemetry                                                                                                                  |
| dapr_configuration            | core | json       | The configuration of Dapr component.                                                                                                                                                                                      |
| default_domain                | core | string     | Default Domain Name for the cluster                                                                                                                                                                                       |
| deployment_errors             | core | string     | Any errors that occurred during deployment or deployment validation                                                                                                                                                       |
| event_stream_endpoint         | core | string     | The endpoint of the eventstream of the Environment.                                                                                                                                                                       |
| id                            | core | string     | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"                               |
| identity                      | core | json       | Managed identities for the Managed Environment to interact with other Azure services without maintaining any secrets or credentials in code.                                                                              |
| infrastructure_resource_group | core | string     | Name of the platform-managed resource group created for the Managed Environment to host infrastructure resources. If a subnet ID is provided, this resource group will be created in the same subscription as the subnet. |
| keda_configuration            | core | json       | The configuration of Keda component.                                                                                                                                                                                      |
| kind                          | core | string     | Kind of the Environment.                                                                                                                                                                                                  |
| location                      | core | string     | The geo-location where the resource lives                                                                                                                                                                                 |
| name                          | core | string     | The name of the resource                                                                                                                                                                                                  |
| peer_authentication           | core | json       | Peer authentication settings for the Managed Environment                                                                                                                                                                  |
| peer_traffic_configuration    | core | json       | Peer traffic settings for the Managed Environment                                                                                                                                                                         |
| provisioning_state            | core | string     | Provisioning state of the Environment.                                                                                                                                                                                    |
| resource_group                | core | string     |
| static_ip                     | core | string     | Static IP of the Environment                                                                                                                                                                                              |
| subscription_id               | core | string     |
| subscription_name             | core | string     |
| system_data                   | core | json       | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                                                          |
| tags                          | core | hstore_csv |
| type                          | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                                                 |
| vnet_configuration            | core | json       | Vnet configuration for the environment                                                                                                                                                                                    |
| workload_profiles             | core | json       | Workload profiles configured for the Managed Environment.                                                                                                                                                                 |
| zone_redundant                | core | bool       | Whether or not this Managed Environment is zone-redundant.                                                                                                                                                                |

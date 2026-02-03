# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.machine_learning_services_workspace.dataset.md

---
title: Machine Learning Services Workspace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Machine Learning Services Workspace
---

# Machine Learning Services Workspace

This table represents the machine_learning_services_workspace resource from Microsoft Azure.

```
azure.machine_learning_services_workspace
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                                                                                                                                 | Description |
| ------------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string        |
| allow_public_access_when_behind_vnet | core | bool          | The flag to indicate whether to allow public access when behind VNet.                                                                                                                     |
| application_insights                 | core | string        | ARM id of the application insights associated with this workspace.                                                                                                                        |
| associated_workspaces                | core | array<string> |
| container_registry                   | core | string        | ARM id of the container registry associated with this workspace.                                                                                                                          |
| description                          | core | string        | The description of this workspace.                                                                                                                                                        |
| discovery_url                        | core | string        | Url for the discovery service to identify regional endpoints for machine learning experimentation services                                                                                |
| enable_data_isolation                | core | bool          |
| encryption                           | core | json          | The encryption settings of Azure ML workspace.                                                                                                                                            |
| feature_store_settings               | core | json          | Settings for feature store type workspace.                                                                                                                                                |
| friendly_name                        | core | string        | The friendly name for this workspace. This name in mutable                                                                                                                                |
| hbi_workspace                        | core | bool          | The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service                                                                                          |
| hub_resource_id                      | core | string        |
| id                                   | core | string        | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                             | core | json          | The identity of the resource.                                                                                                                                                             |
| image_build_compute                  | core | string        | The compute name for image build                                                                                                                                                          |
| key_vault                            | core | string        | ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created                                                                        |
| kind                                 | core | string        |
| location                             | core | string        | Specifies the location of the resource.                                                                                                                                                   |
| managed_network                      | core | json          |
| ml_flow_tracking_uri                 | core | string        | The URI associated with this workspace that machine learning flow must point at to set up tracking.                                                                                       |
| name                                 | core | string        | The name of the resource                                                                                                                                                                  |
| notebook_info                        | core | json          | The notebook info of Azure ML workspace.                                                                                                                                                  |
| primary_user_assigned_identity       | core | string        | The user assigned identity resource id that represents the workspace identity.                                                                                                            |
| private_endpoint_connections         | core | json          | The list of private endpoint connections in the workspace.                                                                                                                                |
| private_link_count                   | core | int64         | Count of private connections in the workspace                                                                                                                                             |
| provisioning_state                   | core | string        | The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning.                                                                |
| public_network_access                | core | string        | Whether requests from Public Network are allowed.                                                                                                                                         |
| resource_group                       | core | string        |
| serverless_compute_settings          | core | json          | Settings for serverless compute created in the workspace                                                                                                                                  |
| service_managed_resources_settings   | core | json          | The service managed resource settings.                                                                                                                                                    |
| service_provisioned_resource_group   | core | string        | The name of the managed resource group created by workspace RP in customer subscription if the workspace is CMK workspace                                                                 |
| shared_private_link_resources        | core | json          | The list of shared private link resources in this workspace.                                                                                                                              |
| sku                                  | core | json          | The sku of the workspace.                                                                                                                                                                 |
| storage_account                      | core | string        | ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created                                                                  |
| storage_hns_enabled                  | core | bool          | If the storage associated with the workspace has hierarchical namespace(HNS) enabled.                                                                                                     |
| subscription_id                      | core | string        |
| subscription_name                    | core | string        |
| system_data                          | core | json          | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                          |
| tags                                 | core | hstore_csv    |
| tenant_id                            | core | string        | The tenant id associated with this workspace.                                                                                                                                             |
| type                                 | core | string        | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| v1_legacy_mode                       | core | bool          | Enabling v1_legacy_mode may prevent you from using features provided by the v2 API.                                                                                                       |
| workspace_hub_config                 | core | json          | WorkspaceHub's configuration object.                                                                                                                                                      |
| workspace_id                         | core | string        | The immutable id associated with this workspace.                                                                                                                                          |

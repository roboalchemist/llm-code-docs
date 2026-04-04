# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.machine_learning_services_workspace_compute.dataset.md

---
title: Machine Learning Services Workspace Compute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Machine Learning Services Workspace
  Compute
---

# Machine Learning Services Workspace Compute

This table represents the machine_learning_services_workspace_compute resource from Microsoft Azure.

```
azure.machine_learning_services_workspace_compute
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| compute_location    | core | string     | Location for the underlying compute                                                                                                                                                       |
| compute_type        | core | string     | The type of compute                                                                                                                                                                       |
| created_on          | core | string     | The time at which the compute was created.                                                                                                                                                |
| description         | core | string     | The description of the Machine Learning compute.                                                                                                                                          |
| disable_local_auth  | core | bool       | Opt-out of local authentication and ensure customers can use only MSI and AAD exclusively for authentication.                                                                             |
| id                  | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity            | core | json       | The identity of the resource.                                                                                                                                                             |
| is_attached_compute | core | bool       | Indicating whether the compute was provisioned by user and brought from outside if true, or machine learning service provisioned it if false.                                             |
| location            | core | string     | Specifies the location of the resource.                                                                                                                                                   |
| modified_on         | core | string     | The time at which the compute was last modified.                                                                                                                                          |
| name                | core | string     | The name of the resource                                                                                                                                                                  |
| provisioning_errors | core | json       | Errors during provisioning                                                                                                                                                                |
| provisioning_state  | core | string     | The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed.                                                                              |
| resource_group      | core | string     |
| resource_id         | core | string     | ARM resource id of the underlying compute                                                                                                                                                 |
| sku                 | core | json       | The sku of the workspace.                                                                                                                                                                 |
| subscription_id     | core | string     |
| subscription_name   | core | string     |
| system_data         | core | json       | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                          |
| tags                | core | hstore_csv |
| type                | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |

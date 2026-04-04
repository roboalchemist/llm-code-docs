# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.stack_hci_cluster.dataset.md

---
title: Stack Hci Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Stack Hci Cluster
---

# Stack Hci Cluster

This table represents the stack_hci_cluster resource from Microsoft Azure.

```
azure.stack_hci_cluster
```

## Fields

| Title                                 | ID   | Type       | Data Type                                                                                                                                                                                   | Description |
| ------------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string     |
| aad_application_object_id             | core | string     | Object id of cluster AAD identity.                                                                                                                                                          |
| aad_client_id                         | core | string     | App id of cluster AAD identity.                                                                                                                                                             |
| aad_service_principal_object_id       | core | string     | Id of cluster identity service principal.                                                                                                                                                   |
| aad_tenant_id                         | core | string     | Tenant id of cluster AAD identity.                                                                                                                                                          |
| billing_model                         | core | string     | Type of billing applied to the resource.                                                                                                                                                    |
| cloud_id                              | core | string     | Unique, immutable resource id.                                                                                                                                                              |
| cloud_management_endpoint             | core | string     | Endpoint configured for management from the Azure portal.                                                                                                                                   |
| connectivity_status                   | core | string     | Overall connectivity status for the cluster resource.                                                                                                                                       |
| desired_properties                    | core | json       | Desired properties of the cluster.                                                                                                                                                          |
| id                                    | core | string     | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| identity                              | core | json       | Identity of Cluster resource                                                                                                                                                                |
| isolated_vm_attestation_configuration | core | json       | Attestation configurations for isolated VM (e.g. TVM, CVM) of the cluster.                                                                                                                  |
| last_billing_timestamp                | core | string     | Most recent billing meter timestamp.                                                                                                                                                        |
| last_sync_timestamp                   | core | string     | Most recent cluster sync timestamp.                                                                                                                                                         |
| location                              | core | string     | The geo-location where the resource lives                                                                                                                                                   |
| log_collection_properties             | core | json       | Log Collection properties of the cluster.                                                                                                                                                   |
| name                                  | core | string     | The name of the resource                                                                                                                                                                    |
| provisioning_state                    | core | string     | Provisioning state.                                                                                                                                                                         |
| registration_timestamp                | core | string     | First cluster sync timestamp.                                                                                                                                                               |
| remote_support_properties             | core | json       | RemoteSupport properties of the cluster.                                                                                                                                                    |
| reported_properties                   | core | json       | Properties reported by cluster agent.                                                                                                                                                       |
| resource_group                        | core | string     |
| resource_provider_object_id           | core | string     | Object id of RP Service Principal                                                                                                                                                           |
| service_endpoint                      | core | string     | Region specific DataPath Endpoint of the cluster.                                                                                                                                           |
| software_assurance_properties         | core | json       | Software Assurance properties of the cluster.                                                                                                                                               |
| status                                | core | string     | Status of the cluster agent.                                                                                                                                                                |
| subscription_id                       | core | string     |
| subscription_name                     | core | string     |
| system_data                           | core | json       | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                            |
| tags                                  | core | hstore_csv |
| trial_days_remaining                  | core | float64    | Number of days remaining in the trial period.                                                                                                                                               |
| type                                  | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                   |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.hybrid_compute_machine.dataset.md

---
title: Hybrid Compute Machine
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Hybrid Compute Machine
---

# Hybrid Compute Machine

This table represents the hybrid_compute_machine resource from Microsoft Azure.

```
azure.hybrid_compute_machine
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| ------------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| ad_fqdn                        | core | string     | Specifies the AD fully qualified display name.                                                                                                                                            |
| agent_configuration            | core | json       | Configurable properties that the user can set locally via the azcmagent config command, or remotely via ARM.                                                                              |
| agent_upgrade                  | core | json       | The info of the machine w.r.t Agent Upgrade                                                                                                                                               |
| agent_version                  | core | string     | The hybrid machine agent full version.                                                                                                                                                    |
| cloud_metadata                 | core | json       | The metadata of the cloud environment (Azure/GCP/AWS/OCI...).                                                                                                                             |
| dns_fqdn                       | core | string     | Specifies the DNS fully qualified display name.                                                                                                                                           |
| domain_name                    | core | string     | Specifies the Windows domain name.                                                                                                                                                        |
| error_details                  | core | json       | Details about the error state.                                                                                                                                                            |
| extensions                     | core | json       | Machine Extensions information (deprecated field)                                                                                                                                         |
| id                             | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                       | core | json       |
| kind                           | core | string     |
| last_status_change             | core | string     | The time of the last status change.                                                                                                                                                       |
| license_profile                | core | json       | Specifies the License related properties for a machine.                                                                                                                                   |
| location                       | core | string     | The geo-location where the resource lives                                                                                                                                                 |
| location_data                  | core | json       |
| machine_fqdn                   | core | string     | Specifies the hybrid machine FQDN.                                                                                                                                                        |
| mssql_discovered               | core | string     | Specifies whether any MS SQL instance is discovered on the machine.                                                                                                                       |
| name                           | core | string     | The name of the resource                                                                                                                                                                  |
| network_profile                | core | json       | Information about the network the machine is on.                                                                                                                                          |
| os_edition                     | core | string     | The edition of the Operating System.                                                                                                                                                      |
| os_name                        | core | string     | The Operating System running on the hybrid machine.                                                                                                                                       |
| os_profile                     | core | json       | Specifies the operating system settings for the hybrid machine.                                                                                                                           |
| os_sku                         | core | string     | Specifies the Operating System product SKU.                                                                                                                                               |
| os_type                        | core | string     | The type of Operating System (windows/linux).                                                                                                                                             |
| os_version                     | core | string     | The version of Operating System running on the hybrid machine.                                                                                                                            |
| parent_cluster_resource_id     | core | string     | The resource id of the parent cluster (Azure HCI) this machine is assigned to, if any.                                                                                                    |
| private_link_scope_resource_id | core | string     | The resource id of the private link scope this machine is assigned to, if any.                                                                                                            |
| provisioning_state             | core | string     | The provisioning state, which only appears in the response.                                                                                                                               |
| resource_group                 | core | string     |
| resources                      | core | json       | The list of extensions affiliated to the machine                                                                                                                                          |
| service_statuses               | core | json       | Statuses of dependent services that are reported back to ARM.                                                                                                                             |
| status                         | core | string     | The status of the hybrid machine agent.                                                                                                                                                   |
| subscription_id                | core | string     |
| subscription_name              | core | string     |
| system_data                    | core | json       | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                          |
| tags                           | core | hstore_csv |
| type                           | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| vm_id                          | core | string     | Specifies the hybrid machine unique ID.                                                                                                                                                   |
| vm_uuid                        | core | string     | Specifies the Arc Machine's unique SMBIOS ID                                                                                                                                              |

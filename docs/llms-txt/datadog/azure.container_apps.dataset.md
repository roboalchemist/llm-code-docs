# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.container_apps.dataset.md

---
title: Container Apps
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Container Apps
---

# Container Apps

This table represents the Container Apps resource from Microsoft Azure.

```
azure.container_apps
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                          | Description |
| ----------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| configuration                 | core | json          | Non versioned Container App configuration properties.                                                                                                                                                                                                                                              |
| custom_domain_verification_id | core | string        | Id used to verify domain name ownership                                                                                                                                                                                                                                                            |
| environment_id                | core | string        | Resource ID of environment.                                                                                                                                                                                                                                                                        |
| event_stream_endpoint         | core | string        | The endpoint of the eventstream of the container app.                                                                                                                                                                                                                                              |
| extended_location             | core | json          |
| id                            | core | string        | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"                                                                                                        |
| identity                      | core | json          | managed identities for the Container App to interact with other Azure services without maintaining any secrets or credentials in code.                                                                                                                                                             |
| latest_ready_revision_name    | core | string        | Name of the latest ready revision of the Container App.                                                                                                                                                                                                                                            |
| latest_revision_fqdn          | core | string        | Fully Qualified Domain Name of the latest revision of the Container App.                                                                                                                                                                                                                           |
| latest_revision_name          | core | string        | Name of the latest revision of the Container App.                                                                                                                                                                                                                                                  |
| location                      | core | string        | The geo-location where the resource lives                                                                                                                                                                                                                                                          |
| managed_by                    | core | string        | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| managed_environment_id        | core | string        | Deprecated. Resource ID of the Container App's environment.                                                                                                                                                                                                                                        |
| name                          | core | string        | The name of the resource                                                                                                                                                                                                                                                                           |
| outbound_ip_addresses         | core | array<string> | Outbound IP Addresses for container app.                                                                                                                                                                                                                                                           |
| provisioning_state            | core | string        | Provisioning state of the Container App.                                                                                                                                                                                                                                                           |
| resource_group                | core | string        |
| subscription_id               | core | string        |
| subscription_name             | core | string        |
| system_data                   | core | json          | Azure Resource Manager metadata containing createdBy and modifiedBy information.                                                                                                                                                                                                                   |
| tags                          | core | hstore_csv    |
| template                      | core | json          | Container App versioned application definition.                                                                                                                                                                                                                                                    |
| type                          | core | string        | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                                                                                                                          |
| workload_profile_name         | core | string        | Workload profile name to pin for container app execution.                                                                                                                                                                                                                                          |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.cognitive_services_account.dataset.md

---
title: Cognitive Services Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cognitive Services Account
---

# Cognitive Services Account

This table represents the cognitive_services_account resource from Microsoft Azure.

```
azure.cognitive_services_account
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                 | Description |
| -------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| abuse_penalty                    | core | json          |
| allowed_fqdn_list                | core | array<string> |
| aml_workspace                    | core | json          | The user owned AML workspace properties.                                                                                                                                                  |
| api_properties                   | core | json          | The api properties for special APIs.                                                                                                                                                      |
| call_rate_limit                  | core | json          |
| capabilities                     | core | json          | Gets the capabilities of the cognitive services account. Each item indicates the capability of a specific feature. The values are read-only and for reference only.                       |
| commitment_plan_associations     | core | json          | The commitment plan associations of Cognitive Services account.                                                                                                                           |
| custom_sub_domain_name           | core | string        | Optional subdomain name used for token-based authentication.                                                                                                                              |
| date_created                     | core | string        | Gets the date of cognitive services account creation.                                                                                                                                     |
| deletion_date                    | core | string        | The deletion date, only available for deleted account.                                                                                                                                    |
| disable_local_auth               | core | bool          |
| dynamic_throttling_enabled       | core | bool          | The flag to enable dynamic throttling.                                                                                                                                                    |
| encryption                       | core | json          | The encryption properties for this resource.                                                                                                                                              |
| endpoint                         | core | string        | Endpoint of the created account.                                                                                                                                                          |
| etag                             | core | string        | Resource Etag.                                                                                                                                                                            |
| id                               | core | string        | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| identity                         | core | json          |
| internal_id                      | core | string        | The internal identifier (deprecated, do not use this property).                                                                                                                           |
| is_migrated                      | core | bool          | If the resource is migrated from an existing key.                                                                                                                                         |
| kind                             | core | string        | The Kind of the resource.                                                                                                                                                                 |
| location                         | core | string        | The geo-location where the resource lives                                                                                                                                                 |
| locations                        | core | json          | The multiregion settings of Cognitive Services account.                                                                                                                                   |
| migration_token                  | core | string        | Resource migration token.                                                                                                                                                                 |
| name                             | core | string        | The name of the resource                                                                                                                                                                  |
| network_acls                     | core | json          | A collection of rules governing the accessibility from specific network locations.                                                                                                        |
| private_endpoint_connections     | core | json          | The private endpoint connection associated with the Cognitive Services account.                                                                                                           |
| provisioning_state               | core | string        | Gets the status of the cognitive services account at the time the operation was called.                                                                                                   |
| public_network_access            | core | string        | Whether or not public endpoint access is allowed for this account.                                                                                                                        |
| quota_limit                      | core | json          |
| rai_monitor_config               | core | json          |
| resource_group                   | core | string        |
| restore                          | core | bool          |
| restrict_outbound_network_access | core | bool          |
| scheduled_purge_date             | core | string        | The scheduled purge date, only available for deleted account.                                                                                                                             |
| sku                              | core | json          |
| sku_change_info                  | core | json          | Sku change info of account.                                                                                                                                                               |
| subscription_id                  | core | string        |
| subscription_name                | core | string        |
| system_data                      | core | json          |
| tags                             | core | hstore_csv    |
| type                             | core | string        | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                 |
| user_owned_storage               | core | json          | The storage accounts for this resource.                                                                                                                                                   |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.storage_blob_container.dataset.md

---
title: Storage Blob Container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Blob Container
---

# Storage Blob Container

This table represents the Storage Blob Container resource from Microsoft Azure.

```
azure.storage_blob_container
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                          | Description |
| ------------------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| default_encryption_scope       | core | string     | Default the container to use specified encryption scope for all writes.                                                                                                                                                                                                                            |
| deleted                        | core | bool       | Indicates whether the blob container was deleted.                                                                                                                                                                                                                                                  |
| deleted_time                   | core | string     | Blob container deletion time.                                                                                                                                                                                                                                                                      |
| deny_encryption_scope_override | core | bool       | Block override of encryption scope from the container default.                                                                                                                                                                                                                                     |
| etag                           | core | string     | Resource Etag.                                                                                                                                                                                                                                                                                     |
| has_immutability_policy        | core | bool       | The hasImmutabilityPolicy public property is set to true by SRP if ImmutabilityPolicy has been created for this container. The hasImmutabilityPolicy public property is set to false by SRP if ImmutabilityPolicy has not been created for this container.                                         |
| has_legal_hold                 | core | bool       | The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold=true for a given account. |
| id                             | core | string     | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}                                                                                                          |
| last_modified_time             | core | string     | Returns the date and time the container was last modified.                                                                                                                                                                                                                                         |
| lease_duration                 | core | string     | Specifies whether the lease on a container is of infinite or fixed duration, only when the container is leased.                                                                                                                                                                                    |
| lease_state                    | core | string     | Lease state of the container.                                                                                                                                                                                                                                                                      |
| lease_status                   | core | string     | The lease status of the container.                                                                                                                                                                                                                                                                 |
| location                       | core | string     |
| name                           | core | string     | The name of the resource                                                                                                                                                                                                                                                                           |
| public_access                  | core | string     | Specifies whether data in the container may be accessed publicly and the level of access.                                                                                                                                                                                                          |
| remaining_retention_days       | core | int64      | Remaining retention days for soft deleted blob container.                                                                                                                                                                                                                                          |
| resource_group                 | core | string     |
| subscription_id                | core | string     |
| subscription_name              | core | string     |
| tags                           | core | hstore_csv |
| type                           | core | string     | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                                                                                                                          |
| version                        | core | string     | The version of the deleted blob container.                                                                                                                                                                                                                                                         |

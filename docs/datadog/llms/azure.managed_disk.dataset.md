# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.managed_disk.dataset.md

---
title: Managed Disk
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Disk
---

# Managed Disk

This table represents the Managed Disk resource from Microsoft Azure.

```
azure.managed_disk
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                       | Description |
| ------------------------------ | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string        |
| bursting_enabled               | core | bool          | Set to true to enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default. Does not apply to Ultra disks.                                           |
| creation_data                  | core | json          | Disk source information. CreationData information cannot be changed after the disk has been created.                                                                                            |
| disk_access_id                 | core | string        | ARM id of the DiskAccess resource for using private endpoints on disks.                                                                                                                         |
| disk_iops_read_only            | core | int64         | The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.                                        |
| disk_iops_read_write           | core | int64         | The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.                                                               |
| disk_mbps_read_only            | core | int64         | The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10. |
| disk_mbps_read_write           | core | int64         | The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.                                |
| disk_size_bytes                | core | int64         | The size of the disk in bytes. This field is read only.                                                                                                                                         |
| disk_state                     | core | string        | The state of the disk.                                                                                                                                                                          |
| encryption                     | core | json          | Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.                                                                                    |
| encryption_settings_collection | core | json          | Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.                                                                   |
| extended_location              | core | json          | The extended location where the disk will be created. Extended location cannot be changed.                                                                                                      |
| hyper_v_generation             | core | string        | The hypervisor generation of the Virtual Machine. Applicable to OS disks only.                                                                                                                  |
| id                             | core | string        | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}       |
| location                       | core | string        | The geo-location where the resource lives                                                                                                                                                       |
| managed_by                     | core | string        | A relative URI containing the ID of the VM that has the disk attached.                                                                                                                          |
| managed_by_extended            | core | array<string> | List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.         |
| max_shares                     | core | int64         | The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.                           |
| name                           | core | string        | The name of the resource                                                                                                                                                                        |
| network_access_policy          | core | string        | Policy for accessing the disk via network.                                                                                                                                                      |
| os_type                        | core | string        | The Operating System type.                                                                                                                                                                      |
| property_updates_in_progress   | core | json          | Properties of the disk for which update is pending.                                                                                                                                             |
| provisioning_state             | core | string        | The disk provisioning state.                                                                                                                                                                    |
| purchase_plan                  | core | json          | Purchase plan information for the the image from which the OS disk was created. E.g. - {name: 2019-Datacenter, publisher: MicrosoftWindowsServer, product: WindowsServer}                       |
| resource_group                 | core | string        |
| security_profile               | core | json          | Contains the security related information for the resource.                                                                                                                                     |
| share_info                     | core | json          | Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.                              |
| sku                            | core | json          | The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, StandardSSD_ZRS, or PremiumV2_LRS.                                                            |
| subscription_id                | core | string        |
| subscription_name              | core | string        |
| supports_hibernation           | core | bool          | Indicates the OS on a disk supports hibernation.                                                                                                                                                |
| tags                           | core | hstore_csv    |
| tier                           | core | string        | Performance tier of the disk (e.g, P4, S10) as described here: https://azure.microsoft.com/en-us/pricing/details/managed-disks/. Does not apply to Ultra disks.                                 |
| time_created                   | core | string        | The time when the disk was created.                                                                                                                                                             |
| type                           | core | string        | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"                                                                                       |
| unique_id                      | core | string        | Unique Guid identifying the resource.                                                                                                                                                           |
| zones                          | core | array<string> | The Logical zone list for Disk.                                                                                                                                                                 |

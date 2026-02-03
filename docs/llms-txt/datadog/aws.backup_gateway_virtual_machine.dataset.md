# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.backup_gateway_virtual_machine.dataset.md

---
title: Backup Gateway Virtual Machine
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Gateway Virtual Machine
---

# Backup Gateway Virtual Machine

This table represents the Backup Gateway Virtual Machine resource from Amazon Web Services.

```
aws.backup_gateway_virtual_machine
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                              | Description |
| ---------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| host_name        | core | string     | The host name of the virtual machine.                                                                                                                  |
| hypervisor_id    | core | string     | The ID of the virtual machine's hypervisor.                                                                                                            |
| last_backup_date | core | timestamp  | The most recent date a virtual machine was backed up, in Unix format and UTC time.                                                                     |
| name             | core | string     | The name of the virtual machine.                                                                                                                       |
| path             | core | string     | The path of the virtual machine.                                                                                                                       |
| resource_arn     | core | string     | The Amazon Resource Name (ARN) of the virtual machine. For example, <code>arn:aws:backup-gateway:us-west-1:0000000000000:vm/vm-0000ABCDEFGIJKL</code>. |
| tags             | core | hstore_csv |
| vmware_tags      | core | json       | These are the details of the VMware tags associated with the specified virtual machine.                                                                |

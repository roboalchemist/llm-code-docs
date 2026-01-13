# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.fsx_storage_virtual_machine.dataset.md

---
title: FSx Storage Virtual Machine
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > FSx Storage Virtual Machine
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.fsx_storage_virtual_machine.dataset/index.html
---

# FSx Storage Virtual Machine

FSx Storage Virtual Machine in AWS is a virtualized file server environment within Amazon FSx for ONTAP. It provides isolated namespaces, user authentication, and data management capabilities, allowing you to create and manage file systems with multi-protocol access such as NFS, SMB, and iSCSI. This enables secure, scalable, and flexible storage for applications and users.

```
aws.fsx_storage_virtual_machine
```

## Fields

| Title                          | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------------------------ | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string    |
| account_id                     | core | string    |
| active_directory_configuration | core | json      | Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.                                                                                                                                                                                                                                                            |
| creation_time                  | core | timestamp | The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.                                                                                                                                                                                                                                                    |
| endpoints                      | core | json      | The endpoints that are used to access data or to manage the SVM using the NetApp ONTAP CLI, REST API, or NetApp CloudManager. They are the Iscsi, Management, Nfs, and Smb endpoints.                                                                                                                                                                        |
| file_system_id                 | core | string    | The globally unique ID of the file system, assigned by Amazon FSx.                                                                                                                                                                                                                                                                                           |
| lifecycle                      | core | string    | Describes the SVM's lifecycle status. CREATED - The SVM is fully available for use. CREATING - Amazon FSx is creating the new SVM. DELETING - Amazon FSx is deleting an existing SVM. FAILED - Amazon FSx was unable to create the SVM. MISCONFIGURED - The SVM is in a failed but recoverable state. PENDING - Amazon FSx has not started creating the SVM. |
| lifecycle_transition_reason    | core | json      | Describes why the SVM lifecycle state changed.                                                                                                                                                                                                                                                                                                               |
| name                           | core | string    | The name of the SVM, if provisioned.                                                                                                                                                                                                                                                                                                                         |
| resource_arn                   | core | string    | The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.                                       |
| root_volume_security_style     | core | string    | The security style of the root volume of the SVM.                                                                                                                                                                                                                                                                                                            |
| storage_virtual_machine_id     | core | string    | The SVM's system generated unique ID.                                                                                                                                                                                                                                                                                                                        |
| subtype                        | core | string    | Describes the SVM's subtype.                                                                                                                                                                                                                                                                                                                                 |
| tags                           | core | hstore    |
| uuid                           | core | string    | The SVM's UUID (universally unique identifier).                                                                                                                                                                                                                                                                                                              |

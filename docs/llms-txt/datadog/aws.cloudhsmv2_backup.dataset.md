# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudhsmv2_backup.dataset.md

---
title: CloudHSM Backup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudHSM Backup
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cloudhsmv2_backup.dataset/index.html
---

# CloudHSM Backup

CloudHSM Backup in AWS represents a saved copy of a hardware security module cluster's state. It allows you to securely preserve cryptographic keys and configurations, enabling recovery or duplication of CloudHSM clusters. Backups are automatically encrypted and can be restored only within the same AWS account and region, ensuring both security and compliance.

```
aws.cloudhsmv2_backup
```

## Fields

| Title            | ID   | Type      | Data Type                                                                                                                                                                                                                            | Description |
| ---------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key             | core | string    |
| account_id       | core | string    |
| backup_arn       | core | string    | The Amazon Resource Name (ARN) of the backup.                                                                                                                                                                                        |
| backup_id        | core | string    | The identifier (ID) of the backup.                                                                                                                                                                                                   |
| backup_state     | core | string    | The state of the backup.                                                                                                                                                                                                             |
| cluster_id       | core | string    | The identifier (ID) of the cluster that was backed up.                                                                                                                                                                               |
| copy_timestamp   | core | timestamp | The date and time when the backup was copied from a source backup.                                                                                                                                                                   |
| create_timestamp | core | timestamp | The date and time when the backup was created.                                                                                                                                                                                       |
| delete_timestamp | core | timestamp | The date and time when the backup will be permanently deleted.                                                                                                                                                                       |
| hsm_type         | core | string    | The HSM type used to create the backup.                                                                                                                                                                                              |
| mode             | core | string    | The mode of the cluster that was backed up.                                                                                                                                                                                          |
| never_expires    | core | bool      | Specifies whether the service should exempt a backup from the retention policy for the cluster. True exempts a backup from the retention policy. False means the service applies the backup retention policy defined at the cluster. |
| source_backup    | core | string    | The identifier (ID) of the source backup from which the new backup was copied.                                                                                                                                                       |
| source_cluster   | core | string    | The identifier (ID) of the cluster containing the source backup from which the new backup was copied.                                                                                                                                |
| source_region    | core | string    | The AWS Region that contains the source backup from which the new backup was copied.                                                                                                                                                 |
| tags             | core | hstore    |

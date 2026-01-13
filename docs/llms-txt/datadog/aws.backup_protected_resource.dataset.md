# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.backup_protected_resource.dataset.md

---
title: Backup Protected Resource
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Backup Protected Resource
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.backup_protected_resource.dataset/index.html
---

# Backup Protected Resource

A Backup Protected Resource in AWS represents an item, such as an Amazon EC2 instance, RDS database, or EFS file system, that is associated with AWS Backup and has backup protection enabled. It identifies resources that are being managed under backup plans, allowing you to track, manage, and restore them as needed.

```
aws.backup_protected_resource
```

## Fields

| Title                   | ID   | Type      | Data Type                                                                                                                                                                                                                                                                      | Description |
| ----------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string    |
| account_id              | core | string    |
| last_backup_time        | core | timestamp | The date and time a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of LastBackupTime is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.                      |
| last_backup_vault_arn   | core | string    | The ARN (Amazon Resource Name) of the backup vault that contains the most recent backup recovery point.                                                                                                                                                                        |
| last_recovery_point_arn | core | string    | The ARN (Amazon Resource Name) of the most recent recovery point.                                                                                                                                                                                                              |
| resource_arn            | core | string    | An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.                                                                                                                                                         |
| resource_name           | core | string    | The non-unique name of the resource that belongs to the specified backup.                                                                                                                                                                                                      |
| resource_type           | core | string    | The type of Amazon Web Services resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For Windows Volume Shadow Copy Service (VSS) backups, the only supported resource type is Amazon EC2. |
| tags                    | core | hstore    |

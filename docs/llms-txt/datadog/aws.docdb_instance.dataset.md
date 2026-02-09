# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.docdb_instance.dataset.md

---
title: DocDB Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DocDB Instance
---

# DocDB Instance

This table represents the DocDB Instance resource from Amazon Web Services.

```
aws.docdb_instance
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                  | Description |
| ------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                            | core | string        |
| account_id                      | core | string        |
| auto_minor_version_upgrade      | core | bool          | Does not apply. This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.                                 |
| availability_zone               | core | string        | Specifies the name of the Availability Zone that the instance is located in.                                                                                                               |
| backup_retention_period         | core | int64         | Specifies the number of days for which automatic snapshots are retained.                                                                                                                   |
| ca_certificate_identifier       | core | string        | The identifier of the CA certificate for this DB instance.                                                                                                                                 |
| certificate_details             | core | json          | The details of the DB instance's server certificate.                                                                                                                                       |
| copy_tags_to_snapshot           | core | bool          | A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.                                                         |
| db_cluster_identifier           | core | string        | Contains the name of the cluster that the instance is a member of if the instance is a member of a cluster.                                                                                |
| db_instance_arn                 | core | string        | The Amazon Resource Name (ARN) for the instance.                                                                                                                                           |
| db_instance_class               | core | string        | Contains the name of the compute and memory capacity class of the instance.                                                                                                                |
| db_instance_identifier          | core | string        | Contains a user-provided database identifier. This identifier is the unique key that identifies an instance.                                                                               |
| db_instance_status              | core | string        | Specifies the current state of this database.                                                                                                                                              |
| db_subnet_group                 | core | json          | Specifies information on the subnet group that is associated with the instance, including the name, description, and subnets in the subnet group.                                          |
| dbi_resource_id                 | core | string        | The Amazon Web Services Region-unique, immutable identifier for the instance. This identifier is found in CloudTrail log entries whenever the KMS key for the instance is accessed.        |
| enabled_cloudwatch_logs_exports | core | array<string> | A list of log types that this instance is configured to export to CloudWatch Logs.                                                                                                         |
| endpoint                        | core | json          | Specifies the connection endpoint.                                                                                                                                                         |
| engine                          | core | string        | Provides the name of the database engine to be used for this instance.                                                                                                                     |
| engine_version                  | core | string        | Indicates the database engine version.                                                                                                                                                     |
| instance_create_time            | core | timestamp     | Provides the date and time that the instance was created.                                                                                                                                  |
| kms_key_id                      | core | string        | If <code>StorageEncrypted</code> is <code>true</code>, the KMS key identifier for the encrypted instance.                                                                                  |
| latest_restorable_time          | core | timestamp     | Specifies the latest time to which a database can be restored with point-in-time restore.                                                                                                  |
| pending_modified_values         | core | json          | Specifies that changes to the instance are pending. This element is included only when changes are pending. Specific changes are identified by subelements.                                |
| performance_insights_enabled    | core | bool          | Set to <code>true</code> if Amazon RDS Performance Insights is enabled for the DB instance, and otherwise <code>false</code>.                                                              |
| performance_insights_kms_key_id | core | string        | The KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key. |
| preferred_backup_window         | core | string        | Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the <code>BackupRetentionPeriod</code>.                       |
| preferred_maintenance_window    | core | string        | Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).                                                                            |
| promotion_tier                  | core | int64         | A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.                               |
| publicly_accessible             | core | bool          | Not supported. Amazon DocumentDB does not currently support public endpoints. The value of <code>PubliclyAccessible</code> is always <code>false</code>.                                   |
| status_infos                    | core | json          | The status of a read replica. If the instance is not a read replica, this is blank.                                                                                                        |
| storage_encrypted               | core | bool          | Specifies whether or not the instance is encrypted.                                                                                                                                        |
| tags                            | core | hstore_csv    |
| vpc_security_groups             | core | json          | Provides a list of VPC security group elements that the instance belongs to.                                                                                                               |

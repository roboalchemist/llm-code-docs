# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_option_group.dataset.md

---
title: RDS Option Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Option Group
---

# RDS Option Group

An RDS Option Group in AWS allows you to enable and manage additional features for Amazon RDS instances that are not available by default. These options can include features like Oracle Transparent Data Encryption, SQL Server Audit, or advanced monitoring tools. By assigning an option group to a database instance, you can customize its functionality without changing the underlying database engine.

```
aws.rds_option_group
```

## Fields

| Title                                       | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                        | core | string     |
| account_id                                  | core | string     |
| allows_vpc_and_non_vpc_instance_memberships | core | bool       | Indicates whether this option group can be applied to both VPC and non-VPC instances. The value true indicates the option group can be applied to both VPC and non-VPC instances.                                                                                                                                                                               |
| copy_timestamp                              | core | timestamp  | Indicates when the option group was copied.                                                                                                                                                                                                                                                                                                                     |
| engine_name                                 | core | string     | Indicates the name of the engine that this option group can be applied to.                                                                                                                                                                                                                                                                                      |
| major_engine_version                        | core | string     | Indicates the major engine version associated with this option group.                                                                                                                                                                                                                                                                                           |
| option_group_arn                            | core | string     | Specifies the Amazon Resource Name (ARN) for the option group.                                                                                                                                                                                                                                                                                                  |
| option_group_description                    | core | string     | Provides a description of the option group.                                                                                                                                                                                                                                                                                                                     |
| option_group_name                           | core | string     | Specifies the name of the option group.                                                                                                                                                                                                                                                                                                                         |
| options                                     | core | json       | Indicates what options are available in the option group.                                                                                                                                                                                                                                                                                                       |
| source_account_id                           | core | string     | Specifies the Amazon Web Services account ID for the option group from which this option group is copied.                                                                                                                                                                                                                                                       |
| source_option_group                         | core | string     | Specifies the name of the option group from which this option group is copied.                                                                                                                                                                                                                                                                                  |
| tags                                        | core | hstore_csv |
| vpc_id                                      | core | string     | If AllowsVpcAndNonVpcInstanceMemberships is false, this field is blank. If AllowsVpcAndNonVpcInstanceMemberships is true and this field is blank, then this option group can be applied to both VPC and non-VPC instances. If this field contains a value, then this option group can only be applied to instances that are in the VPC indicated by this field. |

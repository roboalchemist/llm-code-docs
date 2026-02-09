# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_security_group.dataset.md

---
title: RDS Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Security Group
---

# RDS Security Group

This table represents the RDS Security Group resource from Amazon Web Services.

```
aws.rds_security_group
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                         | Description |
| ----------------------------- | ---- | ---------- | --------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| db_security_group_arn         | core | string     | The Amazon Resource Name (ARN) for the DB security group.                         |
| db_security_group_description | core | string     | Provides the description of the DB security group.                                |
| db_security_group_name        | core | string     | Specifies the name of the DB security group.                                      |
| ec2_security_groups           | core | json       | Contains a list of <code>EC2SecurityGroup</code> elements.                        |
| ip_ranges                     | core | json       | Contains a list of <code>IPRange</code> elements.                                 |
| owner_id                      | core | string     | Provides the Amazon Web Services ID of the owner of a specific DB security group. |
| tags                          | core | hstore_csv |
| vpc_id                        | core | string     | Provides the VpcId of the DB security group.                                      |

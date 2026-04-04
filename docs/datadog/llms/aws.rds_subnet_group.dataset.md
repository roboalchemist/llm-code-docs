# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_subnet_group.dataset.md

---
title: RDS Subnet Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Subnet Group
---

# RDS Subnet Group

This table represents the RDS Subnet Group resource from Amazon Web Services.

```
aws.rds_subnet_group
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| --------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| db_subnet_group_arn         | core | string        | The Amazon Resource Name (ARN) for the DB subnet group.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| db_subnet_group_description | core | string        | Provides the description of the DB subnet group.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| db_subnet_group_name        | core | string        | The name of the DB subnet group.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| subnet_group_status         | core | string        | Provides the status of the DB subnet group.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| subnets                     | core | json          | Contains a list of <code>Subnet</code> elements.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| supported_network_types     | core | array<string> | The network type of the DB subnet group. Valid values: <ul> <li> <code>IPV4</code> </li> <li> <code>DUAL</code> </li> </ul> A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>). For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> |
| tags                        | core | hstore_csv    |
| vpc_id                      | core | string        | Provides the VpcId of the DB subnet group.                                                                                                                                                                                                                                                                                                                                                                                                                              |

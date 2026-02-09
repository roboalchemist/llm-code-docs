# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_cluster_security_group.dataset.md

---
title: Redshift Cluster Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Cluster Security Group
---

# Redshift Cluster Security Group

An Amazon Redshift Cluster Security Group acts as a virtual firewall that controls network access to Redshift clusters. It defines inbound rules that specify which IP ranges or Amazon EC2 security groups can connect to the cluster. This resource is used in the EC2-Classic network model and helps manage secure connectivity to Redshift without relying on VPC security groups.

```
aws.redshift_cluster_security_group
```

## Fields

| Title                               | ID   | Type       | Data Type                                                                                                            | Description |
| ----------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| cluster_security_group_name         | core | string     | The name of the cluster security group to which the operation was applied.                                           |
| description                         | core | string     | A description of the security group.                                                                                 |
| ec2_security_groups                 | core | json       | A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.     |
| ip_ranges                           | core | json       | A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group. |
| redshift_cluster_security_group_arn | core | string     |
| tags                                | core | hstore_csv |

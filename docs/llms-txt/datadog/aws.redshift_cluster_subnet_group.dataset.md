# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_cluster_subnet_group.dataset.md

---
title: Redshift Cluster Subnet Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Cluster Subnet Group
---

# Redshift Cluster Subnet Group

An Amazon Redshift Cluster Subnet Group is a collection of subnets within a Virtual Private Cloud (VPC) that you designate for your Redshift clusters. It defines the network boundaries where the cluster's nodes can be launched, ensuring they are placed in subnets with proper connectivity and availability. This allows you to control which Availability Zones your Redshift cluster can use, supporting high availability and compliance with networking requirements.

```
aws.redshift_cluster_subnet_group
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                            | Description |
| ---------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string        |
| account_id                         | core | string        |
| cluster_subnet_group_name          | core | string        | The name of the cluster subnet group.                                                                |
| description                        | core | string        | The description of the cluster subnet group.                                                         |
| redshift_cluster_subnet_group_arn  | core | string        |
| subnet_group_status                | core | string        | The status of the cluster subnet group. Possible values are Complete, Incomplete and Invalid.        |
| subnets                            | core | json          | A list of the VPC Subnet elements.                                                                   |
| supported_cluster_ip_address_types | core | array<string> | The IP address types supported by this cluster subnet group. Possible values are ipv4 and dualstack. |
| tags                               | core | hstore_csv    |
| vpc_id                             | core | string        | The VPC ID of the cluster subnet group.                                                              |

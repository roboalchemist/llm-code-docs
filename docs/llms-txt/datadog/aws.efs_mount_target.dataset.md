# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.efs_mount_target.dataset.md

---
title: EFS Mount Target
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EFS Mount Target
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.efs_mount_target.dataset/index.html
---

# EFS Mount Target

An EFS Mount Target in AWS provides a network endpoint in a specific subnet that allows Amazon EC2 instances or other resources within a VPC to access an Amazon Elastic File System. Each mount target is associated with a subnet and an IP address, enabling secure and scalable file system access across Availability Zones.

```
aws.efs_mount_target
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                   | Description |
| ---------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| availability_zone_id   | core | string        | The unique and consistent identifier of the Availability Zone that the mount target resides in. For example, use1-az1 is an AZ ID for the us-east-1 Region and it has the same location in every Amazon Web Services account.                                                                                                               |
| availability_zone_name | core | string        | The name of the Availability Zone in which the mount target is located. Availability Zones are independently mapped to names for each Amazon Web Services account. For example, the Availability Zone us-east-1a for your Amazon Web Services account might not be the same location as us-east-1a for another Amazon Web Services account. |
| file_system_id         | core | string        | The ID of the file system for which the mount target is intended.                                                                                                                                                                                                                                                                           |
| ip_address             | core | string        | Address at which the file system can be mounted by using the mount target.                                                                                                                                                                                                                                                                  |
| life_cycle_state       | core | string        | Lifecycle state of the mount target.                                                                                                                                                                                                                                                                                                        |
| mount_target_arn       | core | string        |
| mount_target_id        | core | string        | System-assigned mount target ID.                                                                                                                                                                                                                                                                                                            |
| network_interface_id   | core | string        | The ID of the network interface that Amazon EFS created when it created the mount target.                                                                                                                                                                                                                                                   |
| owner_id               | core | string        | Amazon Web Services account ID that owns the resource.                                                                                                                                                                                                                                                                                      |
| security_groups        | core | array<string> | An array of security groups.                                                                                                                                                                                                                                                                                                                |
| subnet_id              | core | string        | The ID of the mount target's subnet.                                                                                                                                                                                                                                                                                                        |
| tags                   | core | hstore        |
| vpc_id                 | core | string        | The virtual private cloud (VPC) ID that the mount target is configured in.                                                                                                                                                                                                                                                                  |

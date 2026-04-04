# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_instance_profile.dataset.md

---
title: DMS Instance Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Instance Profile
---

# DMS Instance Profile

An AWS DMS Instance Profile defines the compute and memory resources used by a Database Migration Service replication instance. It specifies the instance class and related capacity that determines performance for migration tasks, such as moving data between databases or to AWS cloud services.

```
aws.dms_instance_profile
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string        |
| account_id                     | core | string        |
| availability_zone              | core | string        | The Availability Zone where the instance profile runs.                                                                                                                                                                                                                                                                                                                               |
| description                    | core | string        | A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.                                                                                                                    |
| instance_profile_arn           | core | string        | The Amazon Resource Name (ARN) string that uniquely identifies the instance profile.                                                                                                                                                                                                                                                                                                 |
| instance_profile_creation_time | core | timestamp     | The time the instance profile was created.                                                                                                                                                                                                                                                                                                                                           |
| instance_profile_name          | core | string        | The user-friendly name for the instance profile.                                                                                                                                                                                                                                                                                                                                     |
| kms_key_arn                    | core | string        | The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile. If you don't specify a value for the KmsKeyArn parameter, then DMS uses an Amazon Web Services owned encryption key to encrypt your resources.                                                                                                             |
| network_type                   | core | string        | Specifies the network type for the instance profile. A value of IPV4 represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of IPV6 represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of DUAL represents an instance profile with dual network type that supports IPv4 and IPv6 addressing. |
| publicly_accessible            | core | bool          | Specifies the accessibility options for the instance profile. A value of true represents an instance profile with a public IP address. A value of false represents an instance profile with a private IP address. The default value is true.                                                                                                                                         |
| subnet_group_identifier        | core | string        | The identifier of the subnet group that is associated with the instance profile.                                                                                                                                                                                                                                                                                                     |
| tags                           | core | hstore_csv    |
| vpc_security_groups            | core | array<string> | The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.                                                                                                                                                                                                                                      |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_settings.dataset.md

---
title: EC2 Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Settings
---

# EC2 Settings

EC2 Settings in AWS provide configuration options that control security, encryption, and access behaviors for EC2 resources. These settings include managing VPC public access exclusions and options, defining allowed AMI usage, setting default EBS encryption and KMS keys, controlling image and snapshot public access, configuring instance metadata defaults, and enabling or disabling serial console access. They help enforce compliance, improve security posture, and standardize resource behavior across an AWS environment.

```
aws.ec2_settings
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                        | Description |
| ---------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| allowed_amis                       | core | json       |
| ebs_default_kms_key_id             | core | string     | The Amazon Resource Name (ARN) of the default KMS key for encryption by default. |
| ebs_encryption_by_default          | core | bool       | Indicates whether encryption by default is enabled.                              |
| image_block_public_access          | core | json       |
| imds_defaults                      | core | json       | The account-level default IMDS settings.                                         |
| serial_console                     | core | json       |
| snapshot_block_public_access       | core | json       |
| sse_type                           | core | string     | Reserved for future use.                                                         |
| tags                               | core | hstore_csv |
| vpc_block_public_access_exclusions | core | json       | Details related to the exclusions.                                               |
| vpc_block_public_access_options    | core | json       | Details related to the options.                                                  |

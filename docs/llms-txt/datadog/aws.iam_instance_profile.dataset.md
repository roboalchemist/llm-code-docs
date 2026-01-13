# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_instance_profile.dataset.md

---
title: IAM Instance Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Instance Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iam_instance_profile.dataset/index.html
---

# IAM Instance Profile

An IAM Instance Profile in AWS is a container for an IAM role that can be attached to an EC2 instance. It allows the instance to obtain temporary security credentials and access AWS services without embedding long-term credentials in the instance. This provides secure and manageable access control for applications running on EC2.

```
aws.iam_instance_profile
```

## Fields

| Title                 | ID   | Type      | Data Type                                                                                                                                                                   | Description |
| --------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string    |
| account_id            | core | string    |
| arn                   | core | string    | The Amazon Resource Name (ARN) specifying the instance profile. For more information about ARNs and how to use them in policies, see IAM identifiers in the IAM User Guide. |
| create_date           | core | timestamp | The date when the instance profile was created.                                                                                                                             |
| instance_profile      | core | json      | A structure containing details about the instance profile.                                                                                                                  |
| instance_profile_id   | core | string    | The stable and unique string identifying the instance profile. For more information about IDs, see IAM identifiers in the IAM User Guide.                                   |
| instance_profile_name | core | string    | The name identifying the instance profile.                                                                                                                                  |
| path                  | core | string    | The path to the instance profile. For more information about paths, see IAM identifiers in the IAM User Guide.                                                              |
| roles                 | core | json      | The role associated with the instance profile.                                                                                                                              |
| tags                  | core | hstore    |

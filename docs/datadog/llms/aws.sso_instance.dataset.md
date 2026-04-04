# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sso_instance.dataset.md

---
title: IAM Identity Center Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Identity Center Instance
---

# IAM Identity Center Instance

IAM Identity Center Instance in AWS represents a dedicated configuration of AWS IAM Identity Center (formerly AWS SSO). It provides the foundation for managing workforce identities, enabling centralized access to multiple AWS accounts and applications. This instance stores metadata and settings that define how users, groups, and permissions are managed across the environment.

```
aws.sso_instance
```

## Fields

| Title                                           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                        | Description |
| ----------------------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                            | core | string     |
| account_id                                      | core | string     |
| created_date                                    | core | timestamp  | The date and time that the Identity Center instance was created.                                                                                                                                                                                                                                                                                                 |
| identity_store_id                               | core | string     | The identifier of the identity store that is connected to the Identity Center instance.                                                                                                                                                                                                                                                                          |
| instance_access_control_attribute_configuration | core | json       | Gets the list of IAM Identity Center identity store attributes that have been added to your ABAC configuration.                                                                                                                                                                                                                                                  |
| instance_arn                                    | core | string     | The ARN of the Identity Center instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces in the Amazon Web Services General Reference.                                                                                                                   |
| name                                            | core | string     | The name of the Identity Center instance.                                                                                                                                                                                                                                                                                                                        |
| owner_account_id                                | core | string     | The Amazon Web Services account ID number of the owner of the Identity Center instance.                                                                                                                                                                                                                                                                          |
| status                                          | core | string     | The current status of this Identity Center instance.                                                                                                                                                                                                                                                                                                             |
| status_reason                                   | core | string     | Provides additional context about the current status of the IAM Identity Center instance. This field is particularly useful when an instance is in a non-ACTIVE state, such as CREATE_FAILED. When an instance creation fails, this field contains information about the cause, which may include issues with KMS key configuration or insufficient permissions. |
| tags                                            | core | hstore_csv |

# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_account.dataset.md

---
title: Account Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Account Alias
---

# Account Alias

Account Alias in AWS IAM is a user-friendly name that you can assign to your AWS account. Instead of using the default account ID, which is a numeric string, the alias provides a simpler way to reference your account, especially in sign-in URLs. This makes it easier for users to remember and access the account securely.

```
aws.iam_account
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ------------------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| access_keys_per_user_quota           | core | int64      |
| account_access_keys_present          | core | int64      |
| account_id                           | core | string     |
| account_mfa_enabled                  | core | int64      |
| account_password_present             | core | int64      |
| account_signing_certificates_present | core | int64      |
| assume_role_policy_size_quota        | core | int64      |
| attached_policies_per_group_quota    | core | int64      |
| attached_policies_per_role_quota     | core | int64      |
| attached_policies_per_user_quota     | core | int64      |
| global_endpoint_token_version        | core | int64      |
| group_policy_size_quota              | core | int64      |
| groups                               | core | int64      |
| groups_per_user_quota                | core | int64      |
| groups_quota                         | core | int64      |
| instance_profiles                    | core | int64      |
| instance_profiles_quota              | core | int64      |
| mfa_devices                          | core | int64      |
| mfa_devices_in_use                   | core | int64      |
| organization                         | core | json       | A structure that contains information about the organization. The AvailablePolicyTypes part of the response is deprecated, and you shouldn't use it in your apps. It doesn't include any policy type supported by Organizations other than SCPs. In the China (Ningxia) Region, no policy type is included. To determine which policy types are enabled in your organization, use the ListRoots operation. |
| password_policy                      | core | json       | A structure that contains details about the account's password policy.                                                                                                                                                                                                                                                                                                                                     |
| password_policy_v2                   | core | json       |
| policies                             | core | int64      |
| policies_quota                       | core | int64      |
| policy_size_quota                    | core | int64      |
| policy_versions_in_use               | core | int64      |
| policy_versions_in_use_quota         | core | int64      |
| providers                            | core | int64      |
| role_policy_size_quota               | core | int64      |
| roles                                | core | int64      |
| roles_quota                          | core | int64      |
| server_certificates                  | core | int64      |
| server_certificates_quota            | core | int64      |
| signing_certificates_per_user_quota  | core | int64      |
| tags                                 | core | hstore_csv |
| user_policy_size_quota               | core | int64      |
| users                                | core | int64      |
| users_quota                          | core | int64      |
| versions_per_policy_quota            | core | int64      |

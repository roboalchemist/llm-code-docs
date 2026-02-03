# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sso_permission_set.dataset.md

---
title: SSO Permission Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SSO Permission Set
---

# SSO Permission Set

An AWS SSO Permission Set is a collection of policies that define a set of permissions for users and groups when accessing AWS accounts through AWS IAM Identity Center (formerly AWS SSO). It simplifies access management by allowing administrators to centrally create and manage permission sets, which are then assigned to identities. This ensures consistent and scalable access control across multiple accounts without needing to manage individual IAM roles and policies in each account.

```
aws.sso_permission_set
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                                                                                                    | Description |
| ---------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| attached_managed_policies          | core | json       | An array of the AttachedManagedPolicy data type object.                                                                                                                                      |
| created_date                       | core | timestamp  | The date that the permission set was created.                                                                                                                                                |
| customer_managed_policy_references | core | json       | Specifies the names and paths of the customer managed policies that you have attached to your permission set.                                                                                |
| description                        | core | string     | The description of the PermissionSet.                                                                                                                                                        |
| inline_policy                      | core | string     | The inline policy that is attached to the permission set. For Length Constraints, if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned. |
| name                               | core | string     | The name of the permission set.                                                                                                                                                              |
| permission_set_arn                 | core | string     | The ARN of the permission set. For more information about ARNs, see Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces in the Amazon Web Services General Reference.    |
| permissions_boundary               | core | json       | The permissions boundary attached to the specified permission set.                                                                                                                           |
| relay_state                        | core | string     | Used to redirect users within the application during the federation authentication process.                                                                                                  |
| session_duration                   | core | string     | The length of time that the application user sessions are valid for in the ISO-8601 standard.                                                                                                |
| tags                               | core | hstore_csv |

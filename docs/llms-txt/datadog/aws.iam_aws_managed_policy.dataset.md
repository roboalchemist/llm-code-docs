# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_aws_managed_policy.dataset.md

---
title: Managed Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Policy
---

# Managed Policy

A Managed Policy in AWS is a standalone IAM policy created and maintained either by AWS or by the user. It defines a set of permissions that can be attached to multiple IAM users, groups, or roles, making it easier to manage access consistently across resources. AWS-managed policies are maintained and updated by AWS, while customer-managed policies give full control to the user.

```
aws.iam_aws_managed_policy
```

## Fields

| Title                            | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                 | Description |
| -------------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string    |
| arn                              | core | string    | The Amazon Resource Name (ARN). ARNs are unique identifiers for Amazon Web Services resources. For more information about ARNs, go to Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.                                                                                                          |
| attachment_count                 | core | int64     | The number of entities (users, groups, and roles) that the policy is attached to.                                                                                                                                                                                                                                         |
| create_date                      | core | timestamp | The date and time, in ISO 8601 date-time format, when the policy was created.                                                                                                                                                                                                                                             |
| default_version_id               | core | string    | The identifier for the version of the policy that is set as the default version.                                                                                                                                                                                                                                          |
| description                      | core | string    | A friendly description of the policy. This element is included in the response to the GetPolicy operation. It is not included in the response to the ListPolicies operation.                                                                                                                                              |
| is_attachable                    | core | bool      | Specifies whether the policy can be attached to an IAM user, group, or role.                                                                                                                                                                                                                                              |
| path                             | core | string    | The path to the policy. For more information about paths, see IAM identifiers in the IAM User Guide.                                                                                                                                                                                                                      |
| permissions_boundary_usage_count | core | int64     | The number of entities (users and roles) for which the policy is used to set the permissions boundary. For more information about permissions boundaries, see Permissions boundaries for IAM identities in the IAM User Guide.                                                                                            |
| policy_id                        | core | string    | The stable and unique string identifying the policy. For more information about IDs, see IAM identifiers in the IAM User Guide.                                                                                                                                                                                           |
| policy_name                      | core | string    | The friendly name (not ARN) identifying the policy.                                                                                                                                                                                                                                                                       |
| policy_version                   | core | json      |
| update_date                      | core | timestamp | The date and time, in ISO 8601 date-time format, when the policy was last updated. When a policy has only one version, this field contains the date and time when the policy was created. When a policy has more than one version, this field contains the date and time when the most recent policy version was created. |

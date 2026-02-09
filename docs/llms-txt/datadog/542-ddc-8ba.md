# Source: https://docs.datadoghq.com/security/default_rules/542-ddc-8ba.md

---
title: IAM users should not have the 'AdministratorAccess' policy attached
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM users should not have the
  'AdministratorAccess' policy attached
---

# IAM users should not have the 'AdministratorAccess' policy attached
 
## Description{% #description %}

Confirm there are no [Amazon IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) (privileged users) with administrator permissions for your AWS account.

## Rationale{% #rationale %}

A privileged IAM user can access all AWS services and control resources through the [AdministratorAccess IAM managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator). Any user with administrator access that should not have access can potentially, whether unknowingly or purposefully, cause security issues or data leaks.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Removing a permissions policy from a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-remove-policy-console) docs to revoke AdministratorAccess for a user.

### From the command line{% #from-the-command-line %}

1. Run `list-users` to get [a list of current IAM users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html).

   ```
   aws iam list-users
   ```

1. Run the `list-user-policies` command find the [users attached policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html#examples).

   ```
    aws iam list-user-policies --user-name Name
   ```

1. Run the `detach-user-policy` command to [revoke Administrator access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html).

   ```
    aws iam detach-user-policy \
    --user-name insert-username-here \
    --policy-arn insert-policy-arn-here
   ```

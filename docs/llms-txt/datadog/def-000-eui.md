# Source: https://docs.datadoghq.com/security/default_rules/def-000-eui.md

---
title: AWS IAM user has administrative privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM user has administrative
  privileges
---

# AWS IAM user has administrative privileges
 
## Description{% #description %}

This rule ensures that none of your IAM users have highly privileged policies or administrative policies attached to them.

## Rationale{% #rationale %}

An IAM user with highly privileged or administrative permissions can access all AWS services and resources in the account. A user with these privileges could potentially, whether unknowingly or purposefully, cause security issues or data leaks. Users with these level of access may also be targeted by an adversary to compromise the entire AWS account.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Removing a permissions policy from a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-remove-policy-console) docs to revoke policies from a user.

### From the command line{% #from-the-command-line %}

1. Run `list-users` to get [a list of current IAM users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html).

   ```
   aws iam list-users
   ```

1. Run the `list-user-policies` command find the [users attached policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html#examples).

   ```
    aws iam list-user-policies --user-name Name
   ```

1. Run the `detach-user-policy` command to [remove policies from the user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html).

   ```
    aws iam detach-user-policy \
    --user-name insert-username-here \
    --policy-arn insert-policy-arn-here
   ```

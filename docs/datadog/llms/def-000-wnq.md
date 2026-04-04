# Source: https://docs.datadoghq.com/security/default_rules/def-000-wnq.md

---
title: AWS IAM AdministratorAccess policy was applied to a group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM AdministratorAccess policy was
  applied to a group
---

# AWS IAM AdministratorAccess policy was applied to a group
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when the `AdministratorAccess` policy is attached to an AWS IAM group.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect if an attacker has attached the AWS managed policy [`AdministratorAccess`](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) to an AWS IAM group using the [`AttachGroupPolicy`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachGroupPolicy.html) API call.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Remove the `AdministratorAccess` policy from the `{{@requestParameters.groupName}}` group using the `aws-cli` command [detach-group-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/detach-group-policy.html).
If the API call was made legitimately by the user:
- Determine if the group `{{@requestParameters.groupName}}` requires the `AdministratorAccess` policy to perform the intended function.
- Advise the user to find the [least privileged](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) policy that allows the group to operate as intended.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-sd5.md

---
title: AWS IAM AdministratorAccess policy was applied to a user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM AdministratorAccess policy was
  applied to a user
---

# AWS IAM AdministratorAccess policy was applied to a user
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when the `AdministratorAccess` policy is attached to an AWS IAM user.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect if an attacker has attached the AWS managed policy [`AdministratorAccess`](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) to an AWS IAM user using the [`AttachUserPolicy`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachUserPolicy.html) API call.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Remove the `AdministratorAccess` policy from the `{{@requestParameters.userName}}` user using the `aws-cli` command [detach-user-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/detach-user-policy.html).
If the API call was made legitimately by the user:
- Determine if the user `{{@requestParameters.userName}}` requires the AdministratorAccess policy to perform the intended function.
- Advise the user to find the [least privileged](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) policy that allows the user to operate as intended.

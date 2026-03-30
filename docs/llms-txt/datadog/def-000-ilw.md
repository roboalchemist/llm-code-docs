# Source: https://docs.datadoghq.com/security/default_rules/def-000-ilw.md

---
title: AWS IAM User created with AdministratorAccess policy attached
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM User created with
  AdministratorAccess policy attached
---

# AWS IAM User created with AdministratorAccess policy attached
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136)
## Goal{% #goal %}

Detect when an AWS IAM user is created and the managed AdministratorAccess policy is attached shortly after.

## Strategy{% #strategy %}

This rule leverages CloudTrail and triggers if an [`CreateUser`](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateUser.html) API call is followed by the AWS managed policy [`AdministratorAccess`](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) being attached for the requested IAM user within 10 minutes. This can be an indicator of an attacker trying to preserve access to the AWS environment and to ensure the level of privileges required to achieve their objectives.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should have carried out this operation.
1. If the API calls were not made by the user:

- Rotate user credentials.
- Remove the newly created IAM user `{{@requestParameters.userName}}`.
- Determine what other API calls were made by the user and the newly created user `{{@requestParameters.userName}}`.
- Begin your organization's incident response process and investigate.
If the API call was made legitimately by the user:
- It is recommended that IAM roles are used for human users and workloads so that they use temporary credentials.
- If an IAM user is required, advise the user to find the [least privileged](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) policy that allows the user to operate as intended.
- If not, see if other API calls were made by the user and determine if they warrant further investigation.

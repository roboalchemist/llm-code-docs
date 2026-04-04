# Source: https://docs.datadoghq.com/security/default_rules/def-000-jtm.md

---
title: AWS IAM Roles Anywhere User Profile Creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM Roles Anywhere User Profile
  Creation
---

# AWS IAM Roles Anywhere User Profile Creation
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when an IAM Roles Anywhere profile is created.

## Strategy{% #strategy %}

This rule monitors CloudTrail logs for `CreateProfile` API calls. An attacker may attempt to [create a profile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateProfile.html), a list of the roles that the AWS IAM Roles Anywhere service is trusted to assume. Profiles are used to intersect permissions with IAM managed policies.

## Triage & response{% #triage--response %}

1. Determine if the API call `{{@evt.name}}` should have been performed by the user `{{@userIdentity.arn}}`:
   - Contact the user to confirm if they made the API call.
1. If the API call was not made by the user:
   - Rotate the user credentials.
   - Determine what actions the user took and which new access keys the user created.
   - Begin your organization's incident response process and investigate.

## References{% #references %}

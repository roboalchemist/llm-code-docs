# Source: https://docs.datadoghq.com/security/default_rules/def-000-iye.md

---
title: Unfamiliar IAM user retrieved SSM parameter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unfamiliar IAM user retrieved SSM
  parameter
---

# Unfamiliar IAM user retrieved SSM parameter
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detect when data about one or more parameters is retrieved from AWS Systems Manager.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail and detect when data about one or more parameters is retrieved from AWS Systems Manager with one of the following API calls:

- [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameter.html)
- [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html)

This rule uses the New Value detection method. Datadog learns the historical behavior of the identities within your environment, then creates a signal when unfamiliar values appear.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` is expected to perform the `{{@evt.name}}` API call on the parameter `{{@resource.ARN}}`.
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#customize-security-signal-messages-to-fit-your-environment) for more information.
1. Otherwise, if the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

# Source: https://docs.datadoghq.com/security/default_rules/fwu-obr-c9n.md

---
title: Anomalous number of assumed roles from user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of assumed roles from
  user
---

# Anomalous number of assumed roles from user
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when a user has attempted to assume an anomalous number of unique roles.

## Strategy{% #strategy %}

This rule sets a baseline for user activity for the [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API call, and enables detection of potentially anomalous activity.

An attacker may attempt this for the following reasons:

- To identify which roles the user account has access to.
- To identify what AWS services are being used internally.
- To identify third party integrations and internal software.

## Triage and response{% #triage-and-response %}

1. Investigate activity for the following ARN `{{@userIdentity.arn}}` using `{{@userIdentity.session_name}}`.
1. Review any other security signals for `{{@userIdentity.arn}}`.
1. If the activity is deemed malicious:
   - Rotate user credentials.
   - Determine what other API calls were made by the user.
   - Begin your organization's incident response process and investigate.

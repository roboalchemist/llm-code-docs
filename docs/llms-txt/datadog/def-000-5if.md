# Source: https://docs.datadoghq.com/security/default_rules/def-000-5if.md

---
title: Password recovery request completed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Password recovery request completed
---

# Password recovery request completed
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when an API request to reset the password of the root user is made from a suspicious IP address.

## Strategy{% #strategy %}

Monitor CloudTrail logs to detect the API call PasswordRecoveryCompleted from a suspicious IP address. This indicates that the [root user password was reset](https://docs.aws.amazon.com/IAM/latest/UserGuide/reset-root-password.html).

## Triage and response{% #triage-and-response %}

1. Determine if the request to reset the root user password should have been made.
1. If not, investigate the action performed by `{{@userIdentity.arn}}` for indicators of account compromise, and rotate credentials if necessary.

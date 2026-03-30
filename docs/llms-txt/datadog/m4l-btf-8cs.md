# Source: https://docs.datadoghq.com/security/default_rules/m4l-btf-8cs.md

---
title: AWS Security Hub disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS Security Hub disabled
---

# AWS Security Hub disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a user disables AWS Security Hub.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if a user has disabled AWS Security Hub:

- [DisableSecurityHub](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHub.html)

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` is expected to perform the `{{@evt.name}}` API call on the account: `{{@userIdentity.accountId}}`.
1. Contact the principal owner and see if this was an API call that was made by the user.
1. If the API call was not made by the user, rotate the user credentials and investigate what other APIs were successfully accessed.
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.

## Changelog{% #changelog %}

- 7 April 2022 - Updated rule query and signal message.
- 20 January 2022 - Updated rule severity.

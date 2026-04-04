# Source: https://docs.datadoghq.com/security/default_rules/moj-p98-l67.md

---
title: AWS WAF web access control list modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS WAF web access control list
  modified
---

# AWS WAF web access control list modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when an AWS Web Application Firewall (WAF) Access Control List (ACL) is updated.

## Strategy{% #strategy %}

The rule monitors AWS WAF logs `@eventSource:waf*.amazonaws.com` and detects when the `@evt.name` is `UpdateWebACL`.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` is expected to perform the `{{@evt.name}}` API call on the account: `{{@userIdentity.accountId}}`.
1. If the API call was not made legitimately by the user, rotate the user's credentials and investigate what other APIs were successfully accessed.

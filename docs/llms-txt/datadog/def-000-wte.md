# Source: https://docs.datadoghq.com/security/default_rules/def-000-wte.md

---
title: Okta user's MFA factors reset followed by access to the administrative console
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta user's MFA factors reset followed
  by access to the administrative console
---

# Okta user's MFA factors reset followed by access to the administrative console
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detect when the multi-factor authentication (MFA) factors for an enrolled Okta user are reset followed by that user accessing the administrative console.

## Strategy{% #strategy %}

This rule lets you monitor the following Okta events to determine when a user's MFA factors are reset and they access the administrative console:

- `user.mfa.factor.reset_all`
- `user.session.access_admin_app`

[Okta's security team reported](https://sec.okta.com/articles/2023/08/cross-tenant-impersonation-prevention-and-detection) a series of social engineering attacks in which attackers would convince service desk staff to reset the MFA factors of highly-privileged users, and leverage this to access administrative features within an Okta tenant.

## Triage and response{% #triage-and-response %}

1. Contact the user `{{@usr.email}}` to ensure the change to their MFA factors was authorized and it was them accessing the administrative console.
1. If the user was unaware of the activity:
   - Determine if any other activity occurred from this user. Look for deviations in user agents, IP addresses, and network metadata.
   - Begin your organization's incident response process and investigate for any account takeovers.

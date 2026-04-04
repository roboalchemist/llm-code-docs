# Source: https://docs.datadoghq.com/security/default_rules/w6m-rmy-hra.md

---
title: Azure Login Explicitly Denied MFA
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Login Explicitly Denied MFA
---

# Azure Login Explicitly Denied MFA
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect and identify the network IP address when multiple user accounts failed to complete the MFA process.

## Strategy{% #strategy %}

Monitor Azure Active Directory Sign-in logs and detect when any `@evt.category` is equal to `SignInLogs`, `@properties.authenticationRequirement` is equal to `multiFactorAuthentication` and `@evt.outcome` is equal to `failure`.

## Triage and response{% #triage-and-response %}

1. Inspect the log and determine if this was a valid login attempt.
1. If the user was compromised, rotate user credentials.

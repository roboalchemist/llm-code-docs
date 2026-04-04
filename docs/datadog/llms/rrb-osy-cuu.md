# Source: https://docs.datadoghq.com/security/default_rules/rrb-osy-cuu.md

---
title: Azure AD brute force login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure AD brute force login
---

# Azure AD brute force login
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect when a user is a victim of an Account Take Over (ATO) by a brute force attack.

## Strategy{% #strategy %}

Monitor Azure Active Directory Sign-in logs and detect when any `@evt.category` is equal to `SignInLogs`, and `@evt.outcome` is equal to `failure`.

## Triage and response{% #triage-and-response %}

1. Inspect the log and determine if this was a valid login attempt.
1. If the user was compromised, rotate user credentials.

## Changelog{% #changelog %}

- 26 October 2022 - Updated query.

# Source: https://docs.datadoghq.com/security/default_rules/ljt-3f4-8ty.md

---
title: Credential Stuffing Attack on Azure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Credential Stuffing Attack on Azure
---

# Credential Stuffing Attack on Azure
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110)
## Goal{% #goal %}

Detect and identify the network IP address or user agent when multiple user accounts have login attempt activities recorded.

## Strategy{% #strategy %}

Monitor Azure Active Directory and detect when any `@evt.category` is equal to `SignInLogs` and at least 5 of the `@evt.outcome` are equal to `false` by the same network IP address or user agent.

Security Signal returns **MEDIUM** [if`@evt.outcome](mailto:if%60@evt.outcome)`has value of`success` after 5 multiple failed logins by the same network IP address or user agent.

## Triage and response{% #triage-and-response %}

1. Inspect the log and determine if this was a valid login attempt.
1. If the user was compromised, rotate user credentials.

## Changelog{% #changelog %}

- 14 June 2022 - Updated triggering cases to align with other credential stuffing rules. Also updated other backend options to reduce noise levels.
- 26 October 2022 - Updated query.

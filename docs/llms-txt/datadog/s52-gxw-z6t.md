# Source: https://docs.datadoghq.com/security/default_rules/s52-gxw-z6t.md

---
title: Multiple Okta push notifications denied followed by a successful login
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Multiple Okta push notifications denied
  followed by a successful login
---

# Multiple Okta push notifications denied followed by a successful login
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1621-multi-factor-authentication-request-generation](https://attack.mitre.org/techniques/T1621) 
## Goal{% #goal %}

Detect Okta Multi-factor Authentication (MFA) fatigue attacks.

## Strategy{% #strategy %}

This rule lets you monitor the following Okta events to determine when a user has rejected Okta MFA push verify more than once:

- `user.mfa.okta_verify.deny_push` for Okta Classic
- `user.authentication.auth_via_mfa` with `debugContext.debugData.factor` of `OKTA_VERIFY_PUSH` and `@evt.outcome` of `FAILURE` for Okta Identity Engine

An attacker may attempt to bombard users with repeated MFA push notifications in order to fatigue them, thereby forcing them into verifying their malicious authentication attempts.

## Triage and response{% #triage-and-response %}

1. Verify if the user: `{{@usr.email}}` made the observed authentication attempts.
1. If the user did not make the observed authentication attempts:
   - Rotate user credentials
   - Confirm that no successful authentication attempts have been made.
   - Investigate the source IP: `{{@network.client.ip}}` using the Cloud SIEM - IP Investigation dashboard to determine if the IP address has taken other actions.

## Changelog{% #changelog %}

- 12 September 2023 - Updated query to add distinction between Okta Classic and Okta Identity Engine.
- 14 July 2025 - Updated queries to include abandoned push events and consolidated detection to fire when a successful login is observed after the failed push events. Severity has also been updated to `Medium`.

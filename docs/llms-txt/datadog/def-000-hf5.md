# Source: https://docs.datadoghq.com/security/default_rules/def-000-hf5.md

---
title: Okta User Identity Verification failure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Okta User Identity Verification failure
---

# Okta User Identity Verification failure
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detects failed Okta user identity verification attempts. Alerts when an identity verification challenge results in `DENY`.

## Strategy{% #strategy %}

This rule monitors [Okta identity verification](https://www.okta.com/identity-proofing/) events, highlighted by the team at [Okta](https://www.okta.com/identity-proofing/). It triggers when `@evt.name` is `user.identity_verification` and `@evt.outcome` is `DENY`. Identity verification failures during authentication or recovery workflows warrant review to distinguish user error from potential account takeover activity.

Adversaries may try to bypass ID Verification in order to reset a password, enroll a factor for a user with admin permissions, or unlock an account.

This detection has been adopted from rules published by the [Okta team](https://github.com/okta/customer-detections).

## Triage & Response{% #triage--response %}

1. Examine the identity verification context for `{{@usr.email}}` to confirm the prompt was expected (authentication challenge, recovery, or risk-based step).
1. Review recent authentication activity for `{{@usr.email}}` around the alert time, including failed logins, MFA challenges, and password reset attempts.
1. Identify the source IP `{{@network.client.ip}}` and geo-location and determine whether they align with normal usage patterns or corporate egress.
1. Check device and client details to verify whether the attempt originated from a recognized device for the user.
1. Analyze subsequent events to see if the identity verification later succeeded or if access attempts continued without resolution.
1. If user activity is suspicious, begin your organization's incident response process and investigate for any account takeovers.

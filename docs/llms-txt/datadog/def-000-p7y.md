# Source: https://docs.datadoghq.com/security/default_rules/def-000-p7y.md

---
title: Azure AD possible MFA fatigue attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure AD possible MFA fatigue attack
---

# Azure AD possible MFA fatigue attack
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1621-multi-factor-authentication-request-generation](https://attack.mitre.org/techniques/T1621) 
## Goal{% #goal %}

Detects when multiple Azure AD multi-factor authentication (MFA) push notifications have been rejected or not responded to by a user.

## Strategy{% #strategy %}

This rule allows you to monitor Azure AD sign-in logs and detect when multiple MFA push notifications have been rejected or not responded to by a user. Attackers may attempt to bypass MFA mechanisms and gain access to accounts by generating MFA requests sent to users. Bombarding users with MFA push notifications may result in the user finally accepting the authentication request.

## Triage and response{% #triage-and-response %}

1. Speak with the user `{{@usr.id}}` to understand the context of push rejections, and whether or not the push notifications were initiated by the user.
1. If the user did not initate the push notifications:
   - Filter for the specific `@usr.id` and `@properties.status.additionalDetails:("MFA denied; user declined the authentication\" OR "MFA denied; user did not respond to mobile app notification")` to highlight failed push notifications. Compare previous geo-locations, user-agents, and IP addresses for the user to determine if this is abnormal activity.
   - If it is believed to be malicious activity, then disable the user, invalidate any active sessions, and rotate their credentials.
   - Begin your organization's incident response process and investigate.

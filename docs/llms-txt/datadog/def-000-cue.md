# Source: https://docs.datadoghq.com/security/default_rules/def-000-cue.md

---
title: Auth0 Guardian MFA push notifications rejected by user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Auth0 Guardian MFA push notifications
  rejected by user
---

# Auth0 Guardian MFA push notifications rejected by user
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1621-multi-factor-authentication-request-generation](https://attack.mitre.org/techniques/T1621)
## Goal{% #goal %}

Detects when multiple Auth0 Guardian multi-factor authentication (MFA) push notifications have been rejected by a user.

## Strategy{% #strategy %}

This rule allows you to monitor Auth0 logs and detect when multiple Auth0 Guardian MFA push notifications have been rejected by a user. Attackers may attempt to bypass MFA mechanisms and gain access to accounts by generating MFA requests sent to users. Bombarding users with MFA push notifications may result in the user finally accepting the authentication request.

## Triage and response{% #triage-and-response %}

1. Speak with the user `{{@usr.id}}` to understand the context of push rejections, if the push notifications were initiated by the user.
1. If the user did not initate the push notifications:
   - Filter for `@evt.name:multifactor_push_notification_sent` and the specific `@usr.id` to highlight push notifications. Compare previous geo-locations, user-agents and IP addresses for the user to determine if this is abnormal activity.
   - If it is believed to be malicious activity then disable the user, invalidate any active sessions and rotate their credentials.
   - Begin your organization's incident response process and investigate.

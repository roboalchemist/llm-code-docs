# Source: https://docs.datadoghq.com/security/default_rules/def-002-oxv.md

---
title: Slack user logout due to suspicious activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Slack user logout due to suspicious
  activity
---

# Slack user logout due to suspicious activity
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Alert when a Slack user is logged out due to a detected compromised account.

## Strategy{% #strategy %}

This rule monitors Slack events for when a user is logged out as a result of a detected compromise. Slack may log out users if they detect suspicious behavior indicative of account takeover. This could involve actions like unusual login patterns or unauthorized access attempts.

## Triage and response{% #triage-and-response %}

1. Determine if the behavior is expected by:

   - Contacting the user to confirm if they initiated any recent unusual actions.
   - Checking Slack logs and other relevant logs for the user `{{@usr.email}}`, focusing on: Geolocation, IP address, and ASN.
   - Determine if other actions were taken before being logged out such as file downloads and channel messages.

1. If the activity is deemed malicious:

   - Begin your organization's incident response process and investigate.
   - Force a password reset for the user.
   - Review and revoke any suspicious OAuth integrations tied to the user's account.
   - Enable or enforce multi-factor authentication (MFA) if not already implemented for the user.

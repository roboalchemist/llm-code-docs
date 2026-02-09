# Source: https://docs.datadoghq.com/security/default_rules/def-000-bjq.md

---
title: Multiple GitLab OTP attempts denied
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Multiple GitLab OTP attempts denied
---

# Multiple GitLab OTP attempts denied

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1621-multi-factor-authentication-request-generation](https://attack.mitre.org/techniques/T1621) 
## Goal{% #goal %}

Detects multiple failed GitLab OTP authentication attempts that may indicate brute force attacks against user accounts. Alerts when users experience repeated OTP failures, account lockouts, or suspicious authentication patterns.

## Strategy{% #strategy %}

This rule monitors GitLab audit events for failed OTP authentication attempts through `login_failed_with_otp_authentication` events, user account lockouts via `user_access_locked`, and successful authentication activities. The rule creates different severity levels based on the authentication pattern: high severity for multiple failures followed by successful login (indicating potential account compromise), medium severity for account lockouts (indicating sustained attack attempts), and low severity for repeated failures without success.

## Triage & Response{% #triage--response %}

- Examine the failed OTP attempts for `{{@usr.name}}` to determine if the authentication failures align with legitimate user behavior or indicate malicious activity.
- If the user did not make the observed authentication attempts:
  - Rotate user credentials
  - Confirm that no successful authentication attempts have been made.
  - Investigate the source IP: {{@network.client.ip}} to determine if the IP address has taken other actions.

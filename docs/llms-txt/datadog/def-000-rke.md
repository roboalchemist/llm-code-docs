# Source: https://docs.datadoghq.com/security/default_rules/def-000-rke.md

---
title: Unusual password reset rate activity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Unusual password reset rate activity
---

# Unusual password reset rate activity
Tactic:[TA0042-resource_development](https://attack.mitre.org/tactics/TA0042)Technique:[T1586-compromise-accounts](https://attack.mitre.org/techniques/T1586)
### Goal{% #goal %}

Detect excessive password reset requests activity.

This may be caused by a malicious actor trying to use the feature to list existing users, or compromise some.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `users.password_reset`

### Strategy{% #strategy %}

Count the number password reset requests and detect deviations from historical patterns.

Require the password reset to be flagged using either [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) or a custom WAF rule.

A `Low` signal is then generated if more the password reset requests for a single service over 5 minutes deviates too far from the baseline.

### Triage and response{% #triage-and-response %}

1. Investigate the IP activity over the flagged time window and validate that it is legitimate.
1. Review your password reset process to ensure it's not leaking whether the user existed or not.
1. Consider blocking the IPs to slow down the attacker.

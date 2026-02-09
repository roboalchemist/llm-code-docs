# Source: https://docs.datadoghq.com/security/default_rules/def-000-m3m.md

---
title: Password reset token bruteforce
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Password reset token bruteforce
---

# Password reset token bruteforce
Tactic:[TA0042-resource_development](https://attack.mitre.org/tactics/TA0042)Technique:[T1586-compromise-accounts](https://attack.mitre.org/techniques/T1586) 
### Goal{% #goal %}

Detect excessive password reset requests for a user.

This may be caused by a malicious actor trying to guess the right password reset token for this user.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `users.password_reset`

### Strategy{% #strategy %}

Count the number of password reset attempts for a given user.

Requires the password reset to be flagged using [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) with a `usr.login` metadata field set to the user receiving the password reset.

The instrumentation should be added on the route processing the password reset request (instead of the one sending the email with the password reset link).

`usr.login` must be provided and unique, even if the user does not exist.

A `Medium` signal is then generated if more than 10 password resets for a single user over 5 minutes are found.

### Triage and response{% #triage-and-response %}

1. Investigate the IP activity and validate that it is legitimate.
1. Review your password reset process to ensure it's not possible to guess the secret.
1. Consider blocking the IP to slow down the attacker.

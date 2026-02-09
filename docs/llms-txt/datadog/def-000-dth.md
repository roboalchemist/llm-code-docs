# Source: https://docs.datadoghq.com/security/default_rules/def-000-dth.md

---
title: User enumeration through password reset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > User enumeration through password reset
---

# User enumeration through password reset
Tactic:[TA0043-reconnaissance](https://attack.mitre.org/tactics/TA0043)Technique:[T1589-gather-victim-identity-information](https://attack.mitre.org/techniques/T1589) 
### Goal{% #goal %}

Detect excessive password reset requests from an IP.

This may be caused by a malicious actor trying to use the feature to list existing users, or compromise some.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `users.password_reset`

### Strategy{% #strategy %}

Count the number of users to which an IP requested password resets.

Require the password reset to be flagged using [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) with a `usr.login` metadata field set to the user receiving the password reset and a `exists` field set to `true` or `false` whether the user existed or not.

`usr.login` must be provided and unique, even if the user didn't exist.

A `Medium` signal is then generated if more than 5 password resets from a single IP over 5 minutes are found for users that exist. A `Low` signal is generated if the user didn't exist.

### Triage and response{% #triage-and-response %}

1. Investigate the IP activity and validate that it is legitimate.
1. Review your password reset process to ensure it's not leaking whether the user existed or not.
1. Consider blocking the IP to slow down the attacker.

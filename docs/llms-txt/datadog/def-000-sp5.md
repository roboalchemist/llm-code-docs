# Source: https://docs.datadoghq.com/security/default_rules/def-000-sp5.md

---
title: Excessive account deletion from an IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Excessive account deletion from an IP
---

# Excessive account deletion from an IP
Tactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1531-account-access-removal](https://attack.mitre.org/techniques/T1531) 
### Goal{% #goal %}

Detect excessive account deletions from an IP.

This may be caused by a malicious actor who found an exploit to damage your platform.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `users.delete`

### Strategy{% #strategy %}

Count the number of users that were deleted by an IP.

Require the account deletion to be flagged using [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) with a `usr.id` metadata field set to the user being deleted.

`usr.id` must be provided and unique, even if the user didn't exist.

A `Medium` signal is then generated if more than 5 accounts are deleted within 5 minutes.

### Triage and response{% #triage-and-response %}

1. Investigate the user activity and validate that it is legitimate.
1. Review your account deletion process to ensure users can't be impersonated.
1. Consider blocking the IP to slow down the attacker, or disable the account deletion route.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-ibd.md

---
title: Unusual account creations from an IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Unusual account creations from an IP
---

# Unusual account creations from an IP
Tactic:[TA0042-resource_development](https://attack.mitre.org/tactics/TA0042)Technique:[T1585-establish-accounts](https://attack.mitre.org/techniques/T1585) 
### Goal{% #goal %}

Detect excessive account creations from an IP.

This may be caused by a malicious actor trying to create bots on your platform or abuse discounts to new users.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `users.signup`

### Strategy{% #strategy %}

Count the number of user signups generated coming from a single IP.

Require the signup to be flagged using [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces).

The rule determines the standard rate for IPs to create new users.If an IP is seen significantly exceeding the normal rate, a `Medium` signal will be generated.

#### Note{% #note %}

This rule is using a new feature of App & API Protection that isn't yet available in custom detection rules.This will prevent you from cloning this rule and having it work the same way as the Datadog version.We're working toward solving this limitation.

### Triage and response{% #triage-and-response %}

1. Investigate the IP activity and validate that it is legitimate.
1. Extract the list of created account to lock/delete them.
1. Consider blocking the IP if the account creations are malicious.

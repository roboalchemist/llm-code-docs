# Source: https://docs.datadoghq.com/security/default_rules/def-000-zwj.md

---
title: Excessive payment failures from IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Excessive payment failures from IP
---

# Excessive payment failures from IP
Tactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496)
### Goal{% #goal %}

Detect excessive payment failures from an IP.

This may be caused by a malicious actor trying to use stolen payment cards to buy products from you. Those payments will lead to expensive chargebacks and unpaid but shipped products.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `payment.failure`

### Strategy{% #strategy %}

Count the number of payment failures generated coming from a single IP.

Require the payment failure to be flagged using [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) with a `status` metadata field set to `success` or `failed`.

A `Medium` signal is then generated if more than 3 signups from a single IP over 5 minutes are found.

### Triage and response{% #triage-and-response %}

1. Investigate the IP activity and validate that it is legitimate.
1. Flag transactions from this IP for advanced review and require a captcha to perform payment until the attack is over.
1. Consider blocking the IP to slow down the attacker.

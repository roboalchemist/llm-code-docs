# Source: https://docs.datadoghq.com/security/default_rules/def-000-hio.md

---
title: User activity from Tor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > User activity from Tor
---

# User activity from Tor

### Goal{% #goal %}

Detect user activity from suspicious IPs, specifically the [Tor anonymisation network](https://en.wikipedia.org/wiki/Tor_%28network%29).

This may highlight malicious activity that a user doesn't want to be linked to their real IP address.

### Strategy{% #strategy %}

Correlate traces [tagged with a user](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-authenticated-user-information-to-traces-and-enabling-user-blocking-capability) with the Threat Intelligence qualification of their IP address.

Require the trace to be flagged, either by [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) or by an In-App WAF attack.

A `Low` signal is then generated.

### Triage and response{% #triage-and-response %}

1. Investigate the activity and validate that it is legitimate.
1. Review activity from Tor IPs (`@threat_intel.results.category:tor`) to evaluate if you're under attack.
1. Consider blocking the user if the activity is suspicious.

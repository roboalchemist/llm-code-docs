# Source: https://docs.datadoghq.com/security/default_rules/def-000-l8r.md

---
title: Excessive sensitive activity from an IP (SDK instrumented)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Excessive sensitive activity from an IP
  (SDK instrumented)
---

# Excessive sensitive activity from an IP (SDK instrumented)
 
### Goal{% #goal %}

Detect excessive activity performed from an IP.

This may be caused by a malicious actor trying to cause issues in your platform, create spam content, or similar.

You can read more about the purpose of rate limiting [there](https://cloud.google.com/architecture/rate-limiting-strategies-techniques).

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented event:

- `activity.sensitive`

### Strategy{% #strategy %}

Count the number of a given activity generated coming from a single IP.

Require the activity to be flagged using [a user event](https://docs.datadoghq.com/security/application_security/threats/add-user-info/?tab=set_user#adding-user-events-login-success-login-failure-any-business-logic-to-traces) named `activity.sensitive`. User authentication isn't necessary.

**However, it is very important that the event be given a name in the metadata**.

The rule will count the number of events sharing the same names. This enables you to rate limit multiple activities separately without one counting for another (60 activity named A + 60 activity named B won't trigger the rate limit). The rule won't run if no name is provided.

The rule determines the standard rate for IPs to trigger this activity. If an IP is seen significantly exceeding the normal rate, a `Medium` signal will be generated.

#### Note{% #note %}

This rule is using a new feature of App & API Protection that isn't yet available in custom detection rules.This will prevent you from cloning this rule and having it work the same way as the Datadog version.We're working toward solving this limitation.

### Triage and response{% #triage-and-response %}

1. Investigate the IP activity and validate that it is legitimate.
1. Consider blocking the IP if the activity are malicious.
1. Consider introducing your own rate limiting features.

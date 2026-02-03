# Source: https://docs.datadoghq.com/security/default_rules/def-000-xv1.md

---
title: Admin endpoint without authentication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Admin endpoint without authentication
---

# Admin endpoint without authentication
 
## Description{% #description %}

An administrative endpoint is exposed without authentication, allowing unauthorized users to access sensitive functionality.

## Rationale{% #rationale %}

This finding detects when an endpoint:

- Is identified as a potential administrative route
- Lacks an [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication).

## Remediation{% #remediation %}

- Validate that the code isn't expecting the user to be authenticated to have access to this resource (AuthN). If this API is, in fact, authenticated, ensure your code is [instrumented correctly](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info). Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events.

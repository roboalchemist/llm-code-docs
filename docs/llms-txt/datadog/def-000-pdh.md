# Source: https://docs.datadoghq.com/security/default_rules/def-000-pdh.md

---
title: Unauthenticated route without rate limit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthenticated route without rate
  limit
---

# Unauthenticated route without rate limit
 
## Description{% #description %}

Unauthenticated users are allowed to consume this exposed endpoint, which does not implement any rate-limiting protection.

A malicious user could abuse this endpoint to incur significant resources consumtion and potentially disrupt your application.

## Rationale{% #rationale %}

This finding works by:

- Identifying an API that lacks an [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication)
- Is processing traffic from the internet.
- There is no business logic rate limiting rule associated with this endpoint

## Remediation{% #remediation %}

- Set up rate-limiting using a [detection rule](https://docs.datadoghq.com/security/application_security/policies/custom_rules/#business-logic-abuse-detection-rule) on this API
- Implement authentication to prevent non-intended users interaction with the API
- Require a challenge to prevent automated traffic and slow down resource exhaustion
- Keep track of this business flow by [adding business logic information](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#adding-business-logic-information-login-success-login-failure-any-business-logic-to-traces) to the endpoint

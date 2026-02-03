# Source: https://docs.datadoghq.com/security/default_rules/def-000-jdx.md

---
title: Unauthenticated route use expensive APIs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthenticated route use expensive
  APIs
---

# Unauthenticated route use expensive APIs
 
## Description{% #description %}

An exposed API allows unauthenticated users to make use of paid third-party services, which may not be intended.

A malicious user could abuse this endpoint to incur significant costs, exceed your quota, and potentially disrupt your application.

## Rationale{% #rationale %}

This finding works by:

- Identifying an API that lacks an [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication)
- Is processing traffic from the internet.
- It was detected using a third-party paid service as a part of its operations. See the [list of services](https://docs.datadoghq.com/security/default_rules/appsec-expensive_apis/#strategy) that fall in this category.

## Remediation{% #remediation %}

- Implement authentication to prevent non-intended users' interaction with the API

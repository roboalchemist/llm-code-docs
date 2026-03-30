# Source: https://docs.datadoghq.com/security/default_rules/def-000-k3g.md

---
title: User signup endpoint without HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > User signup endpoint without HTTPS
---

# User signup endpoint without HTTPS

## Description{% #description %}

This API endpoint allows the registration of new users into an application over a non-encrypted channel.

Using plain HTTP for APIs is a significant security risk because it exposes sensitive data to potential interception, manipulation, and unauthorized access. Services must only provide HTTPS endpoints.

## Rationale{% #rationale %}

This finding works by identifying an API that:

- Is tracking a user signup [business logic event](https://app.datadoghq.com/security/appsec/business-logic) (tag `user.signup`).
- Uses an HTTP connection, sending data in the clear over the wire.

## Remediation{% #remediation %}

- Implement the HTTP Strict Transport Security (HSTS) header to instruct the user's browser to always request the site over HTTPS.

### References{% #references %}

| Reference                                                                                                                                | Description                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html) | Transport Layer Security Cheat Sheet: guidance implementing transport layer protection for applications using Transport Layer Security (TLS). |

# Source: https://docs.datadoghq.com/security/default_rules/def-000-1ev.md

---
title: User preferences endpoint without HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > User preferences endpoint without HTTPS
---

# User preferences endpoint without HTTPS
 
## Description{% #description %}

This API endpoint handles user profile settings over an unencrypted channel.

Using plain HTTP for APIs is a significant security risk because it exposes sensitive data to potential interception, manipulation, and unauthorized access. Services must only provide HTTPS endpoints.

## Remediation{% #remediation %}

- Implement the HTTP Strict Transport Security (HSTS) header to instruct the user's browser to always request the site over HTTPS.

### References{% #references %}

| Reference                                                                                                                                | Description                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [OWASP - Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html) | Transport Layer Security Cheat Sheet: guidance implementing transport layer protection for applications using Transport Layer Security (TLS). |

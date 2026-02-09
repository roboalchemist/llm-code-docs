# Source: https://docs.datadoghq.com/security/default_rules/def-000-4fb.md

---
title: Endpoint exposes stack trace errors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Endpoint exposes stack trace errors
---

# Endpoint exposes stack trace errors
 
## Description{% #description %}

An API endpoint was found [exposing stack trace errors](https://app.datadoghq.com/security/appsec/vm/code?query=status%3A%28Open%20OR%20%22In%20progress%22%29%20type%3A%22Stacktrace%20Leak%22&column=score&detection=runtime&order=desc). Stack trace leaks occur when an application displays detailed error messages that include internal code paths, function names, and line numbers when an error occurs.

When stack traces are exposed to users, attackers can gain valuable insights into the application's architecture, libraries, and potential vulnerabilities that can be exploited in further attacks.

## Remediation{% #remediation %}

- Implement proper error handling to catch exceptions before they propagate to users
- Configure production environments to disable detailed error messages

### References{% #references %}

| Reference                                                                                                                         | Description                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [OWASP - REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html#error-handling) | REST Security Cheat Sheet: guidance on the best practices in REST services implementation. |

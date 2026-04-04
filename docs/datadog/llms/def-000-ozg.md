# Source: https://docs.datadoghq.com/security/default_rules/def-000-ozg.md

---
title: Missing Content-Security-Policy HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Missing Content-Security-Policy HTTP
  header
---

# Missing Content-Security-Policy HTTP header

## Description{% #description %}

This publicly exposed API endpoint was found responding with HTML or browser-rendered content and does not implement the Content Security Policy (CSP) header. Since the response content of this API can be rendered by a browser, this header specifies which domains the browser should consider as valid sources and prevent unwanted executable scripts, and other resources.

## Remediation{% #remediation %}

Implement the Content Security Policy (CSP) header in all API responses that return browser-rendered content.

Examples when this header is useful:

```
# Swagger UI docs
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; img-src 'self' data:; connect-src 'self' https://api.example.com
```

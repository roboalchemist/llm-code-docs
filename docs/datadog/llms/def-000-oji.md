# Source: https://docs.datadoghq.com/security/default_rules/def-000-oji.md

---
title: Missing Strict Transport Security HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Missing Strict Transport Security HTTP
  header
---

# Missing Strict Transport Security HTTP header

## Description{% #description %}

This publicly exposed API endpoint does not implement the HTTP Strict-Transport-Security (HSTS) header. This header is crucial for security as it instructs browsers to only interact with the application over HTTPS, protecting against protocol downgrade attacks and cookie hijacking. Without this header, users may be vulnerable to man-in-the-middle attacks where an attacker could intercept and modify traffic or steal sensitive information by forcing connections over unencrypted HTTP.

## Remediation{% #remediation %}

Implement the HTTP Strict-Transport-Security (HSTS) header in all API responses with appropriate values:

- Set a long max-age directive (recommended to at least 31536000 seconds, which is one year).
- Include the includeSubDomains directive to protect all subdomains.
- Consider adding the preload directive for maximum protection.

Example header value:

```gdscript3
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

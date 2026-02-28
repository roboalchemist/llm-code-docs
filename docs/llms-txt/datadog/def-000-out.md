# Source: https://docs.datadoghq.com/security/default_rules/def-000-out.md

---
title: Missing Access-Control-Allow-Origin HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Missing Access-Control-Allow-Origin
  HTTP header
---

# Missing Access-Control-Allow-Origin HTTP header

## Description{% #description %}

This publicly exposed API endpoint does not implement the Access-Control-Allow-Origin (ACAO) header, which may allow attackers to exploit Cross-Origin Resource Sharing (CORS) vulnerabilities. Without this header properly configured, the API may be vulnerable to cross-site request forgery (CSRF) attacks where malicious websites could make unauthorized requests to the API using the user's credentials.

## Remediation{% #remediation %}

Implement the Access-Control-Allow-Origin (ACAO) header in all API responses with appropriate values:

- Use specific origins instead of the wildcard '*' .
- Only allow trusted domains that need access to the API.

Example header value:

```
Access-Control-Allow-Origin: https://trusted-domain.com
```

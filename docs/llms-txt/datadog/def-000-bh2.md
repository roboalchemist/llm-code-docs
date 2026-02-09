# Source: https://docs.datadoghq.com/security/default_rules/def-000-bh2.md

---
title: Missing X-Frame-Options HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Missing X-Frame-Options HTTP header
---

# Missing X-Frame-Options HTTP header
 
## Description{% #description %}

This publicly exposed API endpoint does not implement the X-Frame-Options header. This header allows to control whether a browser should be allowed to render the response in a frame, iframe, embed, or object. Without this header, the API response could be vulnerable to clickjacking attacks.

## Remediation{% #remediation %}

Implement the X-Frame-Options header in all API responses with appropriate values.

Example header values:

```
# Use DENY to prevent any domain from framing the content
X-Frame-Options: DENY

# Use SAMEORIGIN to allow framing only by the same site
X-Frame-Options: SAMEORIGIN
```

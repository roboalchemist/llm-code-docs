# Source: https://docs.datadoghq.com/security/default_rules/def-000-vvh.md

---
title: Missing Content Type HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Missing Content Type HTTP header
---

# Missing Content Type HTTP header
 
## Description{% #description %}

This publicly exposed API endpoint does not implement the `Content-Type` and `X-Content-Type-Options` HTTP headers. These headers declare the resource's media type, preventing browsers from performing MIME type sniffing. Without the headers, browsers may interpret the content in unexpected ways.

## Remediation{% #remediation %}

- Implement the `Content-Type` HTTP header with the appropriate value.

Example header value:

  ```
  Content-Type: application/json; charset=utf-8
  ```

- Add the `X-Content-Type-Options` header with the "nosniff" value to prevent MIME type sniffing.

Example header value:

  ```
  X-Content-Type-Options: nosniff
  ```

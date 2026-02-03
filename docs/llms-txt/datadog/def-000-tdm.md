# Source: https://docs.datadoghq.com/security/default_rules/def-000-tdm.md

---
title: Route returns non-sensitive PII without setting Cache-Control HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns non-sensitive PII without
  setting Cache-Control HTTP header
---

# Route returns non-sensitive PII without setting Cache-Control HTTP header
 
## Description{% #description %}

This publicly exposed API endpoint returns non-sensitive personally identifiable information (PII) without implementing the Cache-Control header. This header instructs browsers how to cache HTTP responses. Without this header, sensitive API responses might be cached inappropriately, potentially exposing confidential information to unintended users through shared browsers.

### What are considered non-sensitive personally identifiable information (PII)?{% #what-are-considered-non-sensitive-personally-identifiable-information-pii %}

PII is information that can identify a user but, in isolation, cannot cause significant harm to a person if leaked or stolen. This information includes full name, email address, and phone numbers. **Note**: Datadog is only able to detect certain types of PII.

## Remediation{% #remediation %}

Implement the Cache-Control header in all API responses. Use the 'no-store' value to prevent caching of sensitive data.

Example header values:

```
Cache-Control: no-store
```

# Source: https://docs.datadoghq.com/security/default_rules/def-000-f8l.md

---
title: Route returns sensitive PII without setting Cache-Control HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns sensitive PII without
  setting Cache-Control HTTP header
---

# Route returns sensitive PII without setting Cache-Control HTTP header
 
## Description{% #description %}

This publicly exposed API endpoint returns non-sensitive personally identifiable information (PII) without implementing the Cache-Control header. This header instructs browsers how to cache HTTP responses. Without this header, sensitive API responses might be cached inappropriately, potentially exposing confidential information to unintended users through shared browsers.

### What are considered sensitive personally identifiable information (PII)?{% #what-are-considered-sensitive-personally-identifiable-information-pii %}

Sensitive PII is information that, if inadvertently disclosed, could have significant consequences for the data subject. Sensitive PII data can encompass a wide range of information, including:

- Health information, which includes medical records or insurance information.
- Government information, which includes social security information or other government related data.
- Proprietary information, which includes secrets or intellectual property (IP).

**Note**: Datadog is only able to detect certain types of PII.

## Remediation{% #remediation %}

Implement the Cache-Control header in all API responses. Use the 'no-store' value to prevent caching of sensitive data.

Example header values:

```
Cache-Control: no-store
```

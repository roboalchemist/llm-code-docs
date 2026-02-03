# Source: https://docs.datadoghq.com/security/default_rules/def-000-kxa.md

---
title: Route returns non-sensitive PII data without HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns non-sensitive PII data
  without HTTPS
---

# Route returns non-sensitive PII data without HTTPS
 
## Description{% #description %}

The API transmits non-sensitive personally identifiable information (PII) over a non-encrypted channel.

### What are considered non-sensitive personally identifiable information (PII)?{% #what-are-considered-non-sensitive-personally-identifiable-information-pii %}

PII is information that can identify a user but, in isolation, could not cause significant harm to a person if leaked or stolen. This information includes full name, email address or phone numbers. **Note**: Datadog is only able to detect certain types of PII.

## Rationale{% #rationale %}

This finding works by identifying an API that both:

- Replies with or accepts requests containing email addresses or phone numbers.
- Uses an HTTP connection, sending data in the clear over the wire

## Remediation{% #remediation %}

- Validate whether the API is intended to return PII.
- Implement the HTTP Strict Transport Security (HSTS) header to instruct the user's browser to always request the site over HTTPS.

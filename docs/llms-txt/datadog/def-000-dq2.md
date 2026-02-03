# Source: https://docs.datadoghq.com/security/default_rules/def-000-dq2.md

---
title: Route returns sensitive PII data without HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns sensitive PII data
  without HTTPS
---

# Route returns sensitive PII data without HTTPS
 
## Description{% #description %}

The API transmits sensitive personally identifiable information (PII) over a non encrypted channel.

### What are considered sensitive personally identifiable information (PII)?{% #what-are-considered-sensitive-personally-identifiable-information-pii %}

Sensitive PII is information that, if inadvertently disclosed, could have significant consequences for the data subject. Sensitive PII data can encompass a wide range of information, including:

- Health information, which includes medical records or insurance information.
- Government information, which includes social security information or other government related data.
- Proprietary information, which includes secrets or intellectual property (IP).

**Note**: Datadog is only able to detect certain types of PII.

## Rationale{% #rationale %}

This finding works by identifying an API that both:

- Replies with or accepts requests containing one or more of the following:
  - Social Security Number (US)
  - Social Insurance Number (UK)
  - Passport Number
  - Vehicle Identification Number
- Uses an HTTP connection, sending data in the clear over the wire

## Remediation{% #remediation %}

- Validate whether the API is intended to return PII.
- Implement the HTTP Strict Transport Security (HSTS) header to instruct the user's browser to always request the site over HTTPS.

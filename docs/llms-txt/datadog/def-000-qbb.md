# Source: https://docs.datadoghq.com/security/default_rules/def-000-qbb.md

---
title: Route returns non-sensitive PII data without rate limit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns non-sensitive PII data
  without rate limit
---

# Route returns non-sensitive PII data without rate limit
 
## Description{% #description %}

The API returns non-sensitive personally identifiable information (PII) and does not implement any rate-limiting protection.

### What are considered non-sensitive personally identifiable information (PII)?{% #what-are-considered-non-sensitive-personally-identifiable-information-pii %}

PII is information that can identify a user but, in isolation, could not cause significant harm to a person if leaked or stolen. This information includes full name, email address or phone numbers. **Note**: Datadog is only able to detect certain types of PII.

## Rationale{% #rationale %}

This finding works by identifying an API where both of the following conditions are fulfilled:

- The API replies with or accepts requests containing email addresses or phone numbers.
- There is no business logic rate-limiting rule associated with this endpoint.

## Remediation{% #remediation %}

- Validate whether the API is intended to return PII.
- Set up rate-limiting using a [detection rule](https://docs.datadoghq.com/security/application_security/policies/custom_rules/#business-logic-abuse-detection-rule) on this API.

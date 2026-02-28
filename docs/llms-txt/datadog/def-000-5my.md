# Source: https://docs.datadoghq.com/security/default_rules/def-000-5my.md

---
title: Route returns sensitive PII data without rate limit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns sensitive PII data
  without rate limit
---

# Route returns sensitive PII data without rate limit

## Description{% #description %}

The API returns sensitive personally identifiable information (PII) and does not implement any rate-limiting protection.

### What are considered sensitive personally identifiable information (PII)?{% #what-are-considered-sensitive-personally-identifiable-information-pii %}

Sensitive PII is information that, if inadvertently disclosed, could have significant consequences for the data subject. Sensitive PII data can encompass a wide range of information, including:

- Health information, which includes medical records or insurance information.
- Government information, which includes social security information or other government related data.
- Proprietary information, which includes secrets or intellectual property (IP).

**Note**: Datadog is only able to detect certain types of PII.

## Rationale{% #rationale %}

This finding works by identifying an API where both of the following conditions are fulfilled:

- Replies with or accepts requests containing one or more of the following:
  - Social Security Number (US)
  - Social Insurance Number (UK)
  - Passport Number
  - Vehicle Identification Number
- There is no business logic rate-limiting rule associated with this endpoint.

## Remediation{% #remediation %}

- Validate whether the API is intended to return PII.
- Set up rate-limiting using a [detection rule](https://docs.datadoghq.com/security/application_security/policies/custom_rules/#business-logic-abuse-detection-rule) on this API.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-ubv.md

---
title: Unauthenticated route returns sensitive PII
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthenticated route returns sensitive
  PII
---

# Unauthenticated route returns sensitive PII

## Description{% #description %}

The API allows unauthenticated users to access sensitive personally identifiable information (PII), which may not be intended.

### What are considered sensitive personally identifiable information (PII)?{% #what-are-considered-sensitive-personally-identifiable-information-pii %}

Sensitive PII is information that, if inadvertently disclosed, could have significant consequences for the data subject. Sensitive PII data can encompass a wide range of information, including:

- Health information, covering medical records or insurance information.
- Government information, which includes social security information or other government related data.
- Proprietary information, which includes secrets or intellectual property (IP).

**Note**: Datadog is only able to detect certain types of PII.

## Rationale{% #rationale %}

This finding works by identifying an API that:

- Lacks an [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication).
- Replies with or accepts requests containing one or more of the following:
  - Social Security Number (US)
  - Social Insurance Number (UK)
  - Passport Number
  - Vehicle Identification Number

## Remediation{% #remediation %}

- Validate that the code isn't expecting the user to be authenticated to have access to this resource (AuthN). In case this API it is in fact authenticated, ensure your code is [instrumented correctly](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info). Datadog auto-instruments many event types, [review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events.
- Validate whether the API is intended to return PII.

### References{% #references %}

| Reference                                                                                                            | Description                                                                            |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [OWASP - Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Authentication Cheat Sheet: guidance on the best practices in the authentication area. |

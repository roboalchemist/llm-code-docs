# Source: https://docs.datadoghq.com/security/default_rules/def-000-rps.md

---
title: Unauthenticated route returns PCI regulated data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthenticated route returns PCI
  regulated data
---

# Unauthenticated route returns PCI regulated data

## Description{% #description %}

The API allows unauthenticated users to access PCI regulated data, which may not be intended.

### What are considered payment card industry (PCI) data?{% #what-are-considered-payment-card-industry-pci-data %}

It refers to any sensitive information associated with payment cards that must be protected under the PCI Data Security Standard (PCI DSS). The standard ensures that businesses handling payment data implement security measures to protect against fraud and breaches. This data includes credit cards, bank account numbers, security code (CVV/CVC), expiration date, etc.

**Note**: Datadog is only able to detect certain types of PCI data.

## Rationale{% #rationale %}

This finding works by identifying an API that both:

- Lacks an [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication).
- Replies with or accepts requests containing one or more of the following:
  - Credit Card Numbers (American Express, Mastercard, VISA, etc)
  - International Bank Account Number (IBAN)

## Remediation{% #remediation %}

- Validate that the code isn't expecting the user to be authenticated to have access to this resource (AuthN). In case this API it is in fact authenticated, ensure your code is [instrumented correctly](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info). Datadog auto-instruments many event types, [review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events.
- Validate whether the API is intended to return PCI regulated data.

### References{% #references %}

| Reference                                                                                                            | Description                                                                            |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [OWASP - Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Authentication Cheat Sheet: guidance on the best practices in the authentication area. |

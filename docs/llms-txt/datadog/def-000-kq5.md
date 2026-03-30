# Source: https://docs.datadoghq.com/security/default_rules/def-000-kq5.md

---
title: Route returns PCI regulated data without HTTPS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns PCI regulated data
  without HTTPS
---

# Route returns PCI regulated data without HTTPS

## Description{% #description %}

The API transmits PCI regulated data over a non encrypted channel.

### What are considered payment card industry (PCI) data?{% #what-are-considered-payment-card-industry-pci-data %}

It refers to any sensitive information associated with payment cards that must be protected under the PCI Data Security Standard (PCI DSS). The standard ensures that businesses handling payment data implement security measures to protect against fraud and breaches. This data includes credit cards, bank account numbers, security code (CVV/CVC), expiration date, etc.

**Note**: Datadog is only able to detect certain types of PCI data.

## Rationale{% #rationale %}

This finding works by identifying an API that both:

- Replies with or accepts requests containing one or more of the following:
  - Credit Card Numbers (American Express, Mastercard, VISA, etc)
  - International Bank Account Number (IBAN)
- Uses an HTTP connection, sending data in the clear over the wire

## Remediation{% #remediation %}

- Validate whether the API is intended to return PCI regulated data.
- Implement the HTTP Strict Transport Security (HSTS) header to instruct the user's browser to always request the site over HTTPS.

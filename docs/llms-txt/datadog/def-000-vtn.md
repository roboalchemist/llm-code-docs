# Source: https://docs.datadoghq.com/security/default_rules/def-000-vtn.md

---
title: Route returns PCI regulated data without setting Cache-Control HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route returns PCI regulated data
  without setting Cache-Control HTTP header
---

# Route returns PCI regulated data without setting Cache-Control HTTP header
 
## Description{% #description %}

This publicly exposed API endpoint returns PCI regulated data without implementing the Cache-Control header. This header instructs browsers how to cache HTTP responses. Without this header, sensitive API responses might be cached inappropriately, potentially exposing regulated data to unintended users through shared browsers.

### What are considered payment card industry (PCI) data?{% #what-are-considered-payment-card-industry-pci-data %}

It refers to any sensitive information associated with payment cards that must be protected under the PCI Data Security Standard (PCI DSS). The standard ensures that businesses handling payment data implement security measures to protect against fraud and breaches. This data includes credit cards, bank account numbers, security code (CVV/CVC), expiration date, etc.

**Note**: Datadog is only able to detect certain types of PCI data.

## Remediation{% #remediation %}

Implement the Cache-Control header in all API responses. Use the 'no-store' value to prevent caching of sensitive data.

Example header values:

```
Cache-Control: no-store
```

# Source: https://docs.datadoghq.com/security/default_rules/r88-a34-ppx.md

---
title: IAM password policy should require at least one symbol
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM password policy should require at
  least one symbol
---

# IAM password policy should require at least one symbol
 
## Description{% #description %}

Password policies are, in part, used to enforce password complexity requirements. IAM password policies can be used to ensure passwords are comprised of different character sets. It is recommended that the password policy require at least one symbol.

## Rationale{% #rationale %}

Setting a password complexity policy increases account resiliency against brute force login attempts.

## Remediation{% #remediation %}

See the [CIS AWS Foundations Benchmark controls docs](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls.html#securityhub-cis-controls-1.7) for console remediation steps.

## Impact{% #impact %}

None

## Default value{% #default-value %}

None

## References{% #references %}

1. CCE-78905-7

## CIS controls{% #cis-controls %}

16 Account Monitoring and Control Account Monitoring and Control

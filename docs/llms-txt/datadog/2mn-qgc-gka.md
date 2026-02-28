# Source: https://docs.datadoghq.com/security/default_rules/2mn-qgc-gka.md

---
title: IAM password policy should require at least one number in passwords
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM password policy should require at
  least one number in passwords
---

# IAM password policy should require at least one number in passwords

## Description{% #description %}

Password policies are, in part, used to enforce password complexity requirements. Use IAM password policies to ensure passwords are comprised of different character sets. The password policy should require at least one number.

## Rationale{% #rationale %}

Setting a password complexity policy increases account resiliency against brute force login attempts.

## Remediation{% #remediation %}

See the [CIS AWS Foundations Benchmark controls docs](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls.html#securityhub-cis-controls-1.8) for console remediation steps.

## Impact{% #impact %}

None

## Default value{% #default-value %}

None

## References{% #references %}

1. CCE-78906-5

## CIS controls{% #cis-controls %}

16 Account Monitoring and Control

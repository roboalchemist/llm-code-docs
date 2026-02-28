# Source: https://docs.datadoghq.com/security/default_rules/ptg-n4i-d7q.md

---
title: IAM password policy should require at least one lowercase letter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM password policy should require at
  least one lowercase letter
---

# IAM password policy should require at least one lowercase letter

## Description{% #description %}

Password policies are, in part, used to enforce password complexity requirements. IAM password policies can be used to ensure password are comprised of different character sets. It is recommended that the password policy require at least one lowercase letter.

## Rationale{% #rationale %}

Setting a password complexity policy increases account resiliency against brute force login attempts.

## Remediation{% #remediation %}

See the [CIS AWS Foundations Benchmark controls docs](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls.html#securityhub-cis-controls-1.6) for console remediation steps.

## Impact{% #impact %}

None

## Default value{% #default-value %}

None

## References{% #references %}

1. CCE-78904-0

## CIS controls{% #cis-controls %}

16 Account Monitoring and Control

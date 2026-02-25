# Source: https://docs.datadoghq.com/security/default_rules/ziw-w2v-e6z.md

---
title: IAM password policy should require uppercase characters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM password policy should require
  uppercase characters
---

# IAM password policy should require uppercase characters

## Description{% #description %}

Password policies are, in part, used to enforce password complexity requirements. Use IAM password policies to ensure passwords are comprised of different character sets. The password policy should require at least one uppercase letter.

## Rationale{% #rationale %}

Setting a password complexity policy increases account resiliency against brute force login attempts.

## Remediation{% #remediation %}

See the [CIS AWS Foundations Benchmark controls docs](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls.html#securityhub-cis-controls-1.5) for console remediation steps.

## Impact{% #impact %}

None

## Default value{% #default-value %}

None

## References{% #references %}

1. CCE-78903-2

## CIS controls{% #cis-controls %}

16 Account Monitoring and Control

# Source: https://docs.datadoghq.com/security/default_rules/def-000-ill.md

---
title: >-
  Bedrock Agent Guardrails should have the Sensitive Information filter enabled
  and BLOCK highly sensitive PII entities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Bedrock Agent Guardrails should have
  the Sensitive Information filter enabled and BLOCK highly sensitive PII
  entities
---

# Bedrock Agent Guardrails should have the Sensitive Information filter enabled and BLOCK highly sensitive PII entities
 
## Description{% #description %}

This control verifies that all Amazon Bedrock Agent aliases point to Agent versions with an Amazon Guardrail policy attached, specifically ensuring that the Sensitive Information filter is enabled and configured to **BLOCK** all highly sensitive PII entities.

Amazon Bedrock Agents can have multiple aliases, each referencing different immutable versions, and each version may have a unique guardrail configuration. Guardrails are essential for enforcing data privacy and regulatory compliance in AI/ML environments by preventing the model from generating or exposing sensitive personal, financial, or credential information.

Without these guardrail settings, there is a heightened risk of data leakage, regulatory violations, or unauthorized disclosure of critical personal data.

Datadog requires using `BLOCK` rather than `MASK` to prevent sensitive data from being logged, and to ensure compliance with data protection policies and standards.

## Remediation{% #remediation %}

For detailed guidance on creating and attaching guardrail policies, see the [Create a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html) documentation.

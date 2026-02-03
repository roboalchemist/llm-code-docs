# Source: https://docs.datadoghq.com/security/default_rules/def-000-fkp.md

---
title: >-
  Bedrock Agent Guardrails should have the Prompt Attack filter enabled and
  BLOCK prompt attacks at HIGH sensitivity
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Bedrock Agent Guardrails should have
  the Prompt Attack filter enabled and BLOCK prompt attacks at HIGH sensitivity
---

# Bedrock Agent Guardrails should have the Prompt Attack filter enabled and BLOCK prompt attacks at HIGH sensitivity
 
## Description{% #description %}

This control verifies that all Amazon Bedrock Agent aliases point to Agent versions with an Amazon Guardrail policy that has the Prompt Attack filter enabled and configured to **block** prompt attacks at **high** sensitivity, for both text and image.

Amazon Bedrock Agents can support multiple aliases, each pointing to a different immutable versions with its own guardrail configuration. Guardrails are crucial in maintaining the integrity and security of AI/ML environments by detecting and blocking prompt injection attacks that could manipulate model behavior or output.

Failing to implement these guardrail settings increases the risk of model exploitation, unauthorized access to confidential data, and potential security breaches, adversely affecting the integrity and reliability of your AI/ML workflows.

## Remediation{% #remediation %}

For comprehensive guidance on implementing and connecting guardrail policies with the required configurations, refer to the [Create a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html) documentation.

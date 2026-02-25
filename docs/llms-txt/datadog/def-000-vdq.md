# Source: https://docs.datadoghq.com/security/default_rules/def-000-vdq.md

---
title: ECS cluster logging should be enabled and encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS cluster logging should be enabled
  and encrypted
---

# ECS cluster logging should be enabled and encrypted

## Description{% #description %}

ECS clusters should have encrypted logging enabled for execute command sessions to protect sensitive data in transit and at rest.

## Remediation{% #remediation %}

Configure your ECS cluster's execute command logging with proper encryption by setting a KMS key ID and enabling encryption for CloudWatch Logs or S3 destinations in the log configuration. Refer to the [Encryption best practices for Amazon ECS](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/ecs.html).

# Source: https://docs.datadoghq.com/security/default_rules/def-000-as4.md

---
title: ECS services should have volume encryption for mounted EFS volumes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS services should have volume
  encryption for mounted EFS volumes
---

# ECS services should have volume encryption for mounted EFS volumes

## Description{% #description %}

ECS services that mount EFS volumes should ensure that all mounted EFS file systems have encryption enabled to protect data at rest.

## Remediation{% #remediation %}

Enable encryption on all EFS file systems mounted by ECS services by setting the `encrypted` parameter to `true` when creating the EFS file system, and optionally specify a KMS key for encryption. Refer to the [Encryption best practices for Amazon ECS](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/ecs.html).

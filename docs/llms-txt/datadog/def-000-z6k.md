# Source: https://docs.datadoghq.com/security/default_rules/def-000-z6k.md

---
title: >-
  Secrets Manager secrets configured with automatic rotation should rotate
  successfully
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Secrets Manager secrets configured with
  automatic rotation should rotate successfully
---

# Secrets Manager secrets configured with automatic rotation should rotate successfully

## Description{% #description %}

This check verifies if a secret managed by AWS Secrets Manager has been rotated according to its defined schedule. The check applies only to secrets with rotation enabled.

AWS Secrets Manager allows for centralized storage of sensitive information, with built-in encryption, access control, and automated rotation. The rotation process can replace long-term secrets with short-term alternatives, reducing the window of opportunity for unauthorized access if a secret is compromised.

To enhance security, it's important not only to enable automatic rotation but also to ensure that the rotation is completed successfully as per the schedule.

## Remediation{% #remediation %}

For guidance on troubleshooting issues with secret rotation, please refer to the [Troubleshooting AWS Secrets Manager rotation of secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot_rotation.html) section of the AWS Secrets Manager User Guide.

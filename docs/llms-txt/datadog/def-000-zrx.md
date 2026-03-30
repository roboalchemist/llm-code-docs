# Source: https://docs.datadoghq.com/security/default_rules/def-000-zrx.md

---
title: Secrets Manager secrets should be rotated within 90 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Secrets Manager secrets should be
  rotated within 90 days
---

# Secrets Manager secrets should be rotated within 90 days

## Description{% #description %}

This control verifies whether an AWS Secrets Manager secret is rotated at least once within 90 days. The control will fail if the secret is not rotated within this period. This control does not apply to secrets created within the last 90 days.

Regularly rotating secrets helps reduce the risk of unauthorized access to sensitive information, such as database credentials, passwords, third-party API keys, or other confidential data. The longer a secret remains unchanged, the higher the risk of it being compromised.

As the number of users with access to a secret increases, so does the likelihood of accidental exposure to unauthorized parties, through means such as logs, cache data, or shared debugging processes. For these reasons, frequent rotation of secrets is essential.

## Remediation{% #remediation %}

For guidance on rotating secrets, please refer to the [Rotating your AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) section in the AWS Secrets Manager User Guide.

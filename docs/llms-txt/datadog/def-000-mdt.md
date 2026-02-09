# Source: https://docs.datadoghq.com/security/default_rules/def-000-mdt.md

---
title: Remove unused Secrets Manager secrets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Remove unused Secrets Manager secrets
---

# Remove unused Secrets Manager secrets
 
## Description{% #description %}

This control checks if an AWS Secrets Manager secret has been accessed within the last 90 days. The control will fail if the secret remains unused beyond this defined period.

Unused secrets may be exploited by individuals who no longer require access. Additionally, the more users that have access to a secret, the higher the risk that it could be mishandled or exposed to unauthorized parties. Removing unused secrets helps prevent access by users who no longer need it and can also reduce the costs associated with Secrets Manager. Regularly deleting unused secrets is a vital part of maintaining a secure environment.

## Remediation{% #remediation %}

For guidance on deleting secrets, please refer to the [Delete an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html) section of the AWS Secrets Manager User Guide

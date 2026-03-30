# Source: https://docs.datadoghq.com/security/default_rules/ayr-n9s-q87.md

---
title: Password policy should require at least 14 characters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Password policy should require at least
  14 characters
---

# Password policy should require at least 14 characters

## Description{% #description %}

Password policies are employed to enforce password complexity requirements, ensuring passwords have a minimum length. Datadog recommends that the password policy requires a minimum password length of 14 characters to enhance security.

Enforcing a password complexity policy increases account resiliency against brute force login attempts and improves the overall security posture of your AWS account.

## Remediation{% #remediation %}

For instructions on setting a minimum password length in IAM password policies, refer to [Managing an IAM User Password Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html).

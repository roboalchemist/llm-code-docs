# Source: https://docs.datadoghq.com/security/default_rules/def-000-er4.md

---
title: Cognito user pool password policies should have strong configurations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cognito user pool password policies
  should have strong configurations
---

# Cognito user pool password policies should have strong configurations

## Description{% #description %}

Password policies for Amazon Cognito user pools should enforce strong configurations to protect user credentials against brute force attacks and unauthorized access. Strong password requirements include minimum length, character complexity requirements, and appropriate temporary password validity periods. These settings help ensure that user passwords meet security standards and comply with organizational security requirements.

## Remediation{% #remediation %}

Configure your Cognito user pool password policy to require strong passwords with a minimum length of 8 characters, require lowercase letters, uppercase letters, numbers, and symbols, and limit temporary password validity to 7 days or less. For guidance on configuring password policies, refer to the [Adding user pool password requirements](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html) section of the Amazon Cognito Developer Guide.

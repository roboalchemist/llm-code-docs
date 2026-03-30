# Source: https://docs.datadoghq.com/security/default_rules/def-000-a1d.md

---
title: Cognito user pools should have deletion protection enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cognito user pools should have deletion
  protection enabled
---

# Cognito user pools should have deletion protection enabled

## Description{% #description %}

Amazon Cognito user pools should have deletion protection enabled. Deletion protection prevents accidental deletion of user pools containing user data, providing an additional layer of protection for identity management infrastructure.

## Remediation{% #remediation %}

Enable deletion protection for your Amazon Cognito user pool. Visit [AWS Cognito documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-deletion-protection.html) for specific instructions to enable deletion protection.

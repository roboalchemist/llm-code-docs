# Source: https://docs.datadoghq.com/security/default_rules/def-000-vxv.md

---
title: MFA should be enabled for Cognito user pools
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > MFA should be enabled for Cognito user
  pools
---

# MFA should be enabled for Cognito user pools

## Description{% #description %}

Multi-factor authentication (MFA) should be enabled for Amazon Cognito user pools. MFA provides an additional layer of security by requiring users to provide a second form of verification during sign-in, reducing the risk of unauthorized access.

## Remediation{% #remediation %}

Enable MFA for the Amazon Cognito user pool. Visit [AWS Cognito documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) for specific instructions to enable MFA in Amazon Cognito user pools.

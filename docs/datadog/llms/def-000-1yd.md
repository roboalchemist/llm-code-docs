# Source: https://docs.datadoghq.com/security/default_rules/def-000-1yd.md

---
title: Cognito identity pools should only allow authenticated identities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cognito identity pools should only
  allow authenticated identities
---

# Cognito identity pools should only allow authenticated identities

## Description{% #description %}

Cognito identity pools should not allow unauthenticated identities to assume IAM roles. When this parameter is enabled, it allows anonymous users to access AWS resources through the identity pool, which can introduce security risks by providing unauthorized access to your AWS environment.

## Remediation{% #remediation %}

Set the `AllowUnauthenticatedIdentities` parameter to `false` when creating or updating Cognito identity pools. For guidance on managing identity pool authentication settings, refer to the [Amazon Cognito Identity Pools documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html).

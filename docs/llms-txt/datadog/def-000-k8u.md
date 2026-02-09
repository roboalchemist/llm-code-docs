# Source: https://docs.datadoghq.com/security/default_rules/def-000-k8u.md

---
title: Cognito identity pool should not have the classic authentication flow enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cognito identity pool should not have
  the classic authentication flow enabled
---

# Cognito identity pool should not have the classic authentication flow enabled
 
## Description{% #description %}

In Amazon Cognito, there are [two different flows](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html) for authentication; enhanced and basic. This detection will trigger when a [Cognito identity pool](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) is configured to use the basic flow.

## Rationale{% #rationale %}

The basic (also referred to as classic) flow introduces the risk that an adversary could abuse [sts:AssumeRoleWithWebIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-web-identity.html) to assume IAM roles with misconfigured role trust policies for the Cognito Identity service. For this reason, it is recommended to use the Enhanced flow, which also offers additional protections.

## Remediation{% #remediation %}

Disable the basic authflow for your identity pool and update your clients to make use of the enhanced auth flow.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-rf2.md

---
title: AWS IAM user has administrative privileges and is inactive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM user has administrative
  privileges and is inactive
---

# AWS IAM user has administrative privileges and is inactive
 
## Description{% #description %}

If an IAM user is highly privileged or has administrative privileges and is inactive, this may indicate the role is not regularly used and may be removed.

## Rationale{% #rationale %}

An IAM user with highly privileged or administrative permissions can access all AWS services and resources in the account. A role with these privileges could potentially, whether unknowingly or purposefully, cause security issues or data leaks. IAM users with this level of access may also be targeted by an adversary to compromise the entire AWS account. In the event a user has not be active for an extended period of time, this may indicate that the role is no longer needed and can be removed.

## Remediation{% #remediation %}

Determine if the user is needed for a particular function and if not, remove it.

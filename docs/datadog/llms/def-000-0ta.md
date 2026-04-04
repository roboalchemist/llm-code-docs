# Source: https://docs.datadoghq.com/security/default_rules/def-000-0ta.md

---
title: AWS IAM role has administrative privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM role has administrative
  privileges
---

# AWS IAM role has administrative privileges

## Description{% #description %}

This rule ensures that none of your IAM roles have highly-privileged policies or administrative policies attached to them.

## Rationale{% #rationale %}

An IAM role with highly privileged or administrative permissions can access all AWS services and resources in the account. A role with these privileges could potentially, whether unknowingly or purposefully, cause security issues or data leaks. Roles with these level of access may also be targeted by an adversary to compromise the entire AWS account.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an IAM role to the minimum necessary for it to fulfill its function. You can use AWS Access Advisor to identify effective permissions used by your instances, and use AWS IAM Access Analyzer to generate an IAM policy based on past CloudTrail events.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-k6r.md

---
title: >-
  AWS IAM role with administrative privileges has a trust relationship with a
  wildcard principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM role with administrative
  privileges has a trust relationship with a wildcard principal
---

# AWS IAM role with administrative privileges has a trust relationship with a wildcard principal

## Description{% #description %}

This rule ensures that none of your IAM roles have highly-privileged policies or administrative policies attached to them and a trust policy which includes a [wildcard](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous) as a `Principal`. It is possible to specify a wildcard principal which permits any principal, including those outside your AWS organization, the ability to assume the role. It is strongly discouraged to use the wildcard principal in a trust policy unless there is a [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) element to restrict access.

## Rationale{% #rationale %}

An IAM role with highly privileged or administrative permissions can access all AWS services and resources in the account. A role with these privileges could potentially, whether unknowingly or purposefully, cause security issues or data leaks. Roles with this level of access may also be targeted by an adversary to compromise the entire AWS account. When a role has a trust relationship with a [wildcard](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous) `Principal`, this means that any AWS account (including those outside your AWS organization) can assume that role.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an IAM role to the minimum required for it to fulfill its function. You can use AWS Access Advisor to identify effective permissions used by your instances, and use AWS IAM Access Analyzer to generate an IAM policy based on past CloudTrail events.

Any role with a trust relationship involving a wildcard should be audited to ensure their validity and compliance with any security requirements set in place by your organization. In addition, the use of a [Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) element is strongly encouraged.

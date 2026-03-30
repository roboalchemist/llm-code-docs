# Source: https://docs.datadoghq.com/security/default_rules/def-000-lil.md

---
title: AWS IAM group has administrative privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM group has administrative
  privileges
---

# AWS IAM group has administrative privileges

## Description{% #description %}

Confirm there are no IAM Groups with administrative privileges for your AWS account.

## Rationale{% #rationale %}

An IAM group with administratative privileges can access all services and resources in an AWS account. Any groups with IAM users that should not have access can potentially, whether unknowingly or purposefully, cause security issues or data leaks.

## Remediation{% #remediation %}

Determine the proper permissions needed for the group and modify the IAM policy to better match that need.

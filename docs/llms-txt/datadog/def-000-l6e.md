# Source: https://docs.datadoghq.com/security/default_rules/def-000-l6e.md

---
title: AWS IAM policy with administrative privileges is not attached to any principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM policy with administrative
  privileges is not attached to any principal
---

# AWS IAM policy with administrative privileges is not attached to any principal
 
## Description{% #description %}

A privileged IAM policy exists but is not attached to any principal.

## Rationale{% #rationale %}

If an IAM policy is not in use it may indicate that it is no longer needed. Highly privileged policies may accidentally be attached to principals, providing them full access to all services and resources in the AWS account. Unused policies should be removed to mitigate this risk.

## Remediation{% #remediation %}

Determine if the policy is needed for a particular function and if not, remove it.

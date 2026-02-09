# Source: https://docs.datadoghq.com/security/default_rules/def-000-njg.md

---
title: AWS IAM user has access to a large number of resources
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM user has access to a large
  number of resources
---

# AWS IAM user has access to a large number of resources
 
## Description{% #description %}

This rule identifies when an IAM user has a policy attached which permits access to a significant number of resources in the account.

## Rationale{% #rationale %}

IAM policies should be scoped down to have the fewest permissions needed to perform their function. In the event the IAM user is compromised, if the associated policies are too broadly scoped, this would permit an adversary to access a significant number of resources in the account.

## Remediation{% #remediation %}

Review the policies attached to the IAM user and ensure the `Resource` policy element is scoped down to only what is needed.

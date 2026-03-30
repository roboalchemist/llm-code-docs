# Source: https://docs.datadoghq.com/security/default_rules/kp3-9yr-ube.md

---
title: IAM policies should be attached and managed at the group level
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM policies should be attached and
  managed at the group level
---

# IAM policies should be attached and managed at the group level

## Description{% #description %}

By default, IAM users, groups, and roles have no access to AWS resources. IAM policies are the mechanism through which privileges are granted. Datadog recommends that you apply IAM policies directly to groups, not to individual users or roles.

Assigning IAM policies through groups unifies permissions management to a single, flexible layer that aligns with organizational functional roles. This approach reduces the likelihood of granting excessive permissions and simplifies the management of user privileges.

## Remediation{% #remediation %}

For instructions on properly applying IAM policies to groups, refer to [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#convert-inline-to-managed-policy).

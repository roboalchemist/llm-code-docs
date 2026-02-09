# Source: https://docs.datadoghq.com/security/default_rules/def-000-sdh.md

---
title: >-
  AWS IAM role can update the trust policy for a role with administrative
  privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM role can update the trust
  policy for a role with administrative privileges
---

# AWS IAM role can update the trust policy for a role with administrative privileges
 
## Description{% #description %}

In AWS environments, some IAM permissions can lead to privilege escalation, where an identity can gain access to another more privileged identity. This rule identifies when a given role can use `iam:UpdateAssumeRolePolicy` to modify an existing trust policy for an IAM role with administrative privileges. By modifying the role trust policy, an adversary could assume that role and leverage their privileges.

## Rationale{% #rationale %}

The identity which triggered this detection can update the trust policy for a role with administrative privileges, giving them access to the privileges of that role.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an IAM role to the minimum required for the role to fulfill its function. To remediate the issue, either remove the `iam:UpdateAssumeRolePolicy` permission entirely or modify the resource specified in the IAM policy.

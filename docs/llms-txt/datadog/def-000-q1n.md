# Source: https://docs.datadoghq.com/security/default_rules/def-000-q1n.md

---
title: >-
  AWS IAM role can create a login profile for an IAM user with administrative
  privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM role can create a login profile
  for an IAM user with administrative privileges
---

# AWS IAM role can create a login profile for an IAM user with administrative privileges

## Description{% #description %}

In AWS environments, some IAM permissions can lead to privilege escalation, where an identity can gain access to another more privileged identity. This rule identifies when a given role can use `iam:CreateLoginProfile` to create a new login profile for an IAM user with administrative privileges. By creating a new login profile for another user, an adversary could log in as that user and leverage their privileges.

## Rationale{% #rationale %}

In this scenario, there exists at least one privileged IAM user in the account who does not have a login profile set. The identity which triggered this detection can create a login profile for that IAM user, giving them access to the privileges of the compromised user.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an IAM role to the minimum necessary for the role to fulfill its function. To remediate the issue, either remove the `iam:CreateLoginProfile` permission entirely or modify the resource the IAM policy specifies.

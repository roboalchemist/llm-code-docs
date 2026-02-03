# Source: https://docs.datadoghq.com/security/default_rules/def-000-0cb.md

---
title: >-
  AWS IAM user can create access keys for an IAM user with administrative
  privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM user can create access keys for
  an IAM user with administrative privileges
---

# AWS IAM user can create access keys for an IAM user with administrative privileges
 
## Description{% #description %}

In AWS environments, some IAM permissions can lead to privilege escalation, where an identity can gain access to another more privileged identity. This rule identifies when a given user can use `iam:CreateAccessKey` to create a new access keys for an IAM user with administrative privileges. By creating a new access key pair for another user, an adversary could use those credentials to operate as that user and leverage their privileges.

## Rationale{% #rationale %}

The identity which triggered this detection can create an access key pair for an IAM user with administrative privileges, giving them access to the privileges of the compromised user.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an IAM user to the minimum required for the user to fulfill their function. To remediate the issue, either remove the `sts:CreateAccessKey` permission entirely or modify the resource specified in the IAM policy.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-kfe.md

---
title: AWS EC2 instance can assume a role with administrative privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS EC2 instance can assume a role with
  administrative privileges
---

# AWS EC2 instance can assume a role with administrative privileges

## Description{% #description %}

In AWS environments, some IAM permissions can lead to privilege escalation, where an identity can gain access to another more privileged identity. This rule identifies when an EC2 instance has an IAM role that can use `sts:AssumeRole` to assume a role with administrative privileges in the same account inside your AWS Organization. By assuming this more privileged role, an adversary can leverage their permissions for further access.

## Rationale{% #rationale %}

The identity which triggered this detection can assume a role with administrative privileges, giving them access to the privileges of that role.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an EC2 instance to the minimum required for it to fulfill its function. To remediate the issue, either remove the `sts:AssumeRole` permission entirely or modify the resource specified in the IAM policy.

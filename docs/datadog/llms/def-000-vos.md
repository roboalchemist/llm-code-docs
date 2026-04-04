# Source: https://docs.datadoghq.com/security/default_rules/def-000-vos.md

---
title: EC2 instance should not have a highly-privileged IAM role attached to it
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 instance should not have a
  highly-privileged IAM role attached to it
---

# EC2 instance should not have a highly-privileged IAM role attached to it

## Description{% #description %}

This rule ensures that none of your EC2 instances is attached to a highly-privileged [instance role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

## Rationale{% #rationale %}

EC2 instance roles are the recommended method to grant applications running on an EC2 instance privileges to access the AWS API. However, an EC2 instance attached to a privileged IAM role is considered risky, since an attacker compromising the instance can compromise your whole AWS account.

## Remediation{% #remediation %}

EC2 instances typically do not require privileged IAM roles. It is recommended to reduce the permissions attached to the instance role. You can use [AWS Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) to identify effective permissions used by your instances, and use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to generate an IAM policy based on past CloudTrail events.

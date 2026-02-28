# Source: https://docs.datadoghq.com/security/default_rules/def-000-u5t.md

---
title: Publicly accessible EC2 instances should not have highly-privileged IAM roles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible EC2 instances
  should not have highly-privileged IAM roles
---

# Publicly accessible EC2 instances should not have highly-privileged IAM roles

## Description{% #description %}

This rule verifies that publicly accessible EC2 instances are not attached to a highly-privileged, risky [instance role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

## Rationale{% #rationale %}

An EC2 instance is publicly accessible if it exists within infrastructure that could provide an access route from the internet for an attacker.

EC2 instance roles are the recommended method to grant applications running on an EC2 instance privileges to access the AWS API. However, an EC2 instance attached to a privileged IAM role is considered risky, since an attacker compromising the instance can compromise your whole AWS account.

## Remediation{% #remediation %}

You can use the [AWS Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to identify the path to your EC2 instance that is allowing it to be accessed via the internet. If possible, don't open your instance security group to the Internet, or don't assign it a public IP so it's only accessible from within the VPC.

EC2 instances typically do not require privileged IAM roles. It is recommended to reduce the permissions attached to the instance role. You can use [AWS Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) to identify effective permissions used by your instances, and use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to generate an IAM policy based on past CloudTrail events.

## References{% #references %}

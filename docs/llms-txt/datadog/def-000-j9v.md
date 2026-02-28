# Source: https://docs.datadoghq.com/security/default_rules/def-000-j9v.md

---
title: Lambda functions should not be configured with a privileged execution role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Lambda functions should not be
  configured with a privileged execution role
---

# Lambda functions should not be configured with a privileged execution role

## Description{% #description %}

This control ensures that none of your Lambda functions are attached to a highly-privileged execution role. Reducing privileges for these roles minimizes security risks and potential vulnerabilities in your AWS environment.

**Note:** Lambda execution roles are the preferred way to grant Lambda functions access to AWS APIs. However, associating a function with a privileged IAM role is risky because an attacker, exploiting an application-level vulnerability, could compromise your entire AWS account.

## Remediation{% #remediation %}

Lambda functions typically do not require privileged IAM roles. It is recommended to reduce the permissions attached to the execution role. You can use [AWS Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) to identify the effective permissions used by your Lambda functions and use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to generate an IAM policy based on past CloudTrail events.

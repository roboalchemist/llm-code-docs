# Source: https://docs.datadoghq.com/security/default_rules/def-000-ph2.md

---
title: Publicly accessible Lambda function uses a privileged IAM role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Lambda function
  uses a privileged IAM role
---

# Publicly accessible Lambda function uses a privileged IAM role

## Description{% #description %}

A misconfigured Lambda execution role contains risky privileges. A privileged IAM role attached to a Lambda function can lead to an AWS account compromise if the underlying function code has an application-level vulnerability or can be modified by the attacker. This Lambda function is publicly accessible, making it easier for attackers to exploit the function.

## Remediation{% #remediation %}

1. Reduce the permissions attached to the Lambda execution role using the concept of least-privileged access. You can use [AWS Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html).
1. Once you identify effective permissions used by your Lambda function, use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to generate an IAM policy based on past CloudTrail events.
1. Redeploy the role to the Lambda Function.

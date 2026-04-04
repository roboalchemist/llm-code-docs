# Source: https://docs.datadoghq.com/security/default_rules/def-001-hec.md

---
title: >-
  Publicly accessible Lambda function with a critical vulnerability uses a
  privileged IAM role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Publicly accessible Lambda function
  with a critical vulnerability uses a privileged IAM role
---

# Publicly accessible Lambda function with a critical vulnerability uses a privileged IAM role

## Description{% #description %}

A misconfigured Lambda execution role contains risky privileges. This Lambda function is also publicly accessible and has one or more critical-severity vulnerabilities. A privileged IAM role attached to a Lambda function can lead to an AWS account compromise or privilege escalation if the underlying vulnerability is exploited. The public accessibility of this Lambda function makes it easier for attackers to exploit.

## Remediation{% #remediation %}

1. Reduce the permissions attached to the Lambda execution role using the concept of least-privileged access. You can use [AWS Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html).
1. Once you identify effective permissions used by your Lambda function, use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to generate an IAM policy based on past CloudTrail events.
1. Prioritize and apply security patches or updates to address the identified vulnerabilities. If patches are not available, consider implementing alternative security measures.
1. Evaluate the need for public accessibility of the Lambda function. If unnecessary, modify the function's access settings to restrict public access.

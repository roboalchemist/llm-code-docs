# Source: https://docs.datadoghq.com/security/default_rules/9ga-poq-w7v.md

---
title: Lambda function should have access to VPC resources in configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Lambda function should have access to
  VPC resources in configuration
---

# Lambda function should have access to VPC resources in configuration

## Description{% #description %}

Ensure your Amazon Lambda Function is configured to access VPC-only resources, enhancing the security of your connection to private resources.

**Note:** By default, Amazon Lambda functions operate within a secure VPC with internet and AWS service access. By selecting specific resources for access, you can enhance the security of connections within your private VPC.

## Remediation{% #remediation %}

To configure VPC access for an existing Lambda function, please refer to the [Configuring VPC access (console) documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-configuring).

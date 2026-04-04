# Source: https://docs.datadoghq.com/security/default_rules/def-000-aw4.md

---
title: CloudFormation stacks should have termination protection enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFormation stacks should have
  termination protection enabled
---

# CloudFormation stacks should have termination protection enabled

## Description{% #description %}

CloudFormation stacks should have termination protection enabled to prevent accidental deletion. Termination protection helps protect critical infrastructure from unintended removal, which could cause service outages or data loss.

## Remediation{% #remediation %}

Enable termination protection for your CloudFormation stack using the AWS Console or CLI.

### From the console{% #from-the-console %}

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).
1. Select the stack you want to protect.
1. Choose **Stack actions**, then **Edit termination protection**.
1. Select **Enabled** and choose **Save**.

### From the command line{% #from-the-command-line %}

```bash
aws cloudformation update-termination-protection \
    --stack-name <stack-name> \
    --enable-termination-protection
```

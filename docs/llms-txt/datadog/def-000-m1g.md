# Source: https://docs.datadoghq.com/security/default_rules/def-000-m1g.md

---
title: CloudFormation stacks should have associated service roles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFormation stacks should have
  associated service roles
---

# CloudFormation stacks should have associated service roles

## Description{% #description %}

CloudFormation stacks should use service roles (IAM roles) instead of user credentials. Using a service role allows you to specify which actions CloudFormation can perform, following the principle of least privilege. This provides better security control and auditability for stack operations.

## Remediation{% #remediation %}

Associate an IAM service role with your CloudFormation stack.

### From the console{% #from-the-console %}

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).
1. Select the stack you want to update.
1. Choose **Stack actions**, then **Update stack**.
1. In the **Permissions** section, select an existing IAM role or create a new one.
1. Complete the stack update wizard.

### From the command line{% #from-the-command-line %}

```bash
aws cloudformation update-stack \
    --stack-name <stack-name> \
    --role-arn arn:aws:iam::123456789012:role/CloudFormationServiceRole \
    --use-previous-template
```

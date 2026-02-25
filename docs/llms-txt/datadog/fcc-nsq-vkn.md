# Source: https://docs.datadoghq.com/security/default_rules/fcc-nsq-vkn.md

---
title: SNS topic should not be accessible over the public internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SNS topic should not be accessible over
  the public internet
---

# SNS topic should not be accessible over the public internet

## Description{% #description %}

Update your Amazon Simple Notification Service (SNS) topic permissions.

## Rationale{% #rationale %}

Publicly-accessible topics allow unauthorized users access to receive and publish messages and subscribe to exposed topics.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Using identity-based policies with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-using-identity-based-policies.html#iam-and-sns-policies) docs to learn how to create or add to a policy in the AWS Console.

### From the command line{% #from-the-command-line %}

If you do not have an access control policy, [create one](https://awspolicygen.s3.amazonaws.com/policygen.html).

1. Select `SNS Topic Policy` as the type of policy.

1. Add a statement to allow only specific IAM users and roles to have access to the topic. For example:

   ```text
       Effect: `Allow`
       Principal: `arn:aws:iam::123456789012:root`
       Action: `Add permission`
       Amazon Resource Name: `arn:aws:iam::123456789012:root`

```

If you do have an access control policy, follow the [add-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/add-permission.html) docs to add a permission to your existing policy.

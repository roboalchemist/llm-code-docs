# Source: https://docs.datadoghq.com/security/default_rules/npo-qzo-yjo.md

---
title: SNS Topic should have restrictions set for publishing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SNS Topic should have restrictions set
  for publishing
---

# SNS Topic should have restrictions set for publishing
 
## Description{% #description %}

Update your Amazon Simple Notification Service (SNS) topic publishing permissions.

## Rationale{% #rationale %}

A resource-based policy attached to an SNS topic with a Principal of `*` and an Action of `sns:Publish` allows anyone to publish to a topic. Unauthenticated users can publish arbitrary messages, potentially leading to an impact for downstream applications.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Preventative best practices](https://docs.aws.amazon.com/sns/latest/dg/sns-security-best-practices.html#preventative-best-practices) docs to learn how to implement least-privilege access or use IAM roles for your applications and AWS services.

### From the command line{% #from-the-command-line %}

1. Update your [access control policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) with an appropriate `Principal` ARN. Save the file as `policy.json`.

```
{
  ...
  "Statement": [
    ...
    {
      "Sid": "console_pub",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": [
        "SNS:Publish"
      ],
      ...
    }
  ]
}
```
Run `set-topic-attributes` with the [ARN of the SNS topic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-topic-attributes.html#set-topic-attributes).
```bash
aws sns set-topic-attributes
  --topic-arn arn:aws:sns:region:123456789012:YourTopic
  --attribute-name Policy
  --attribute-value file://policy.json
```

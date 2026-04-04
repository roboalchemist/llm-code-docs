# Source: https://docs.datadoghq.com/security/default_rules/7b7-txn-jj2.md

---
title: SNS Topic should have server-side encryption enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SNS Topic should have server-side
  encryption enabled
---

# SNS Topic should have server-side encryption enabled

## Description{% #description %}

Enable Server-Side Encryption for your AWS Simple Notification Service (SNS) topics.

## Rationale{% #rationale %}

Server-Side Encryption (SSE) protects the data of published messages within your SNS topics, which can help adhere to compliance and regulatory requirements.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Enabling server-side encryption (SSE) for an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html) docs to learn how to enable encryption from the AWS Management Console.

### From the command line{% #from-the-command-line %}

Run `set-topic-attributes` with the [ARN of the SNS topic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-topic-attributes.html#set-topic-attributes) and the [KmsMasterKeyId](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms).

In the `set-topic-attributes.sh` file:

```bash
aws sns set-topic-attributes
  --topic-arn arn:aws:sns:region:123456789012:YourTopic
  --attribute-name KmsMasterKeyId
  --attribute-value YourTopicDisplayName
```

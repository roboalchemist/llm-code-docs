# Source: https://docs.datadoghq.com/security/default_rules/nmb-c7a-8rv.md

---
title: SQS queue should have server-side encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQS queue should have server-side
  encryption
---

# SQS queue should have server-side encryption

## Description{% #description %}

Secure your Amazon Simple Queue Service (SQS) messages with server-side encryption.

## Rationale{% #rationale %}

Encryption ensures that Amazon SQS messages, which may contain sensitive data, are not available to anonymous or unauthorized users.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Configuring service-side encryption for a queue(console)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html) docs to learn how to create and use AWS Key Management Service (AWS KMS) to manage customer master keys (CMK) for server-side encryption.

### From the command line{% #from-the-command-line %}

1. Define `set-queue-attributes` in [a file](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html). Use your custom KMS Master Key ARN for `KmsMasterKeyID`. Save the file.

   ```
   {
     "KmsMasterKeyId": "custom_key_arn",
     "KmsDataKeyReusePeriodSeconds": "300"
   }
   ```

1. Run `set-queue-attributes` with the [queue URL and the file](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html) created in step 1.

   ```
   aws sqs set-queue-attributes
     --queue-url https://us-west-2.queue.amazonaws.com/<insert-account-id>/<insert-sqs-queue-name>
     --attributes file://sqs-sse-enabled.json
   ```

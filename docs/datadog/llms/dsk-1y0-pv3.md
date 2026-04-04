# Source: https://docs.datadoghq.com/security/default_rules/dsk-1y0-pv3.md

---
title: SQS queue should not be accessible over the public internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQS queue should not be accessible over
  the public internet
---

# SQS queue should not be accessible over the public internet

## Description{% #description %}

Update Amazon Simple Queue Service (SQS) queue permissions.

## Rationale{% #rationale %}

Publicly-available Amazon SQS queues give unauthorized users access to potentially intercept, delete, or send queue messages, which can lead to data leaks.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Managing access to resources](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html#sqs-managing-access-to-resources) docs to learn how to implement a permissions policy in the AWS console.

### From the command line{% #from-the-command-line %}

1. Run the `list-queues` command to get a list of queue URLs.

   ```
   aws sqs list-queues --region insert-your-region-here
   ```

1. Run the `get-queue-attributes` command with a [queue URL](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html) returned in step 1.

   ```
   aws sqs get-queue-attributes \
       --queue-url https://queue.amazonaws.com/123456789012/YourQueue \
       --attribute-names Policy
   ```

1. Run the `remove-permission` command to [remove any unwanted permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html) from your queue policy.

   ```zed
   aws sqs remove-permission \
       --region insert-your-region-here \
       --queue-url https://queue.amazonaws.com/YourAccountID/YourQueue \
       --label insert-label-name \
       --aws-account-ids insert-aws-account-ids-here \
       --actions insert-action-to-remove
   ```

1. Run the `add-permission` command to [add a new permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/add-permission.html) to your queue policy.

   ```zed
   aws sqs add-permission \
       --queue-url https://queue.amazonaws.com/YourAccountID/YourQueue \
       --label insert-label-name \
       --aws-account-ids insert-aws-account-ids-here \
       --actions insert-action-to-add
   ```

1. Complete steps 2 through 4 for any remaining queue URLs returned from step 1 for each region you have SQS enabled.

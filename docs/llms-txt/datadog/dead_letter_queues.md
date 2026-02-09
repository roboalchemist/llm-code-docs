# Source: https://docs.datadoghq.com/data_streams/dead_letter_queues.md

---
title: Dead Letter Queues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Data Streams Monitoring > Dead Letter Queues
---

# Dead Letter Queues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Data Streams Monitoring is not available for the  site.
{% /alert %}


{% /callout %}

Data Streams Monitoring (DSM) provides visibility into your non-empty dead letter queues (DLQs), enabling you to monitor and inspect message processing failures. DSM also enables you to remediate these message processing failures directly within Datadog.

{% alert level="info" %}
Monitoring dead letter queues is available for Amazon SQS queues.
{% /alert %}

## Monitor DLQs{% #monitor-dlqs %}

### Setup{% #setup %}

- Enable [Data Streams Monitoring](https://docs.datadoghq.com/data_streams/setup) for your messaging services.
- Install the [Datadog-AWS integration](https://docs.datadoghq.com/integrations/amazon-web-services/). Use this integration to manage permissions.
- To remediate message processing failures within Datadog, additional setup is required. See the Remediate DLQ issues section.

### Usage{% #usage %}

#### Create a monitor for a dead letter queue{% #create-a-monitor-for-a-dead-letter-queue %}

To track if your queue is rerouting messages to its DLQ, you can create a [metric monitors](https://docs.datadoghq.com/monitors/types/metric/) that alerts on the [`data_streams.sqs.dead_letter_queue.messages`](https://docs.datadoghq.com/monitors/types/metric/) metric.

To create a monitor for a queue's DLQ:

1. In Datadog, navigate to [Data Streams Monitoring](https://app.datadoghq.com/data-streams/).
1. Select the **Explore** tab (default).
1. Click on a supported queue to open its side panel.
1. Select the **Dead Letter Queue** tab.
1. Click **Create Monitor** to open a monitor setup page. The default inputs are sufficient to create a monitor that alerts when your DLQ is non-empty, but you can also make additional configurations on this page if you wish.
1. Click **Create** at the bottom of the page.

#### Detect message processing issues{% #detect-message-processing-issues %}

Data Streams Monitoring helps you detect where messages couldn't be processed and what downstream services could be affected:

- The DSM [**Service Map**](https://app.datadoghq.com/data-streams/map) highlights queues with messages in their DLQs, helping you to visually identify where failures occur

- The DSM [**Issues**](https://app.datadoghq.com/data-streams/issues) page lists all queues that are experiencing message processing issues

## Remediate DLQ issues{% #remediate-dlq-issues %}

You can inspect and resolve non-empty DLQs directly in Datadog by using [Datadog Actions](https://app.datadoghq.com/actions).

### Setup{% #setup-1 %}

In Datadog, create a [Connection](https://app.datadoghq.com/actions/connections). You need an IAM entity to perform the actions. This IAM entity can be an IAM User (with a secret access key) or IAM Role (assumed by using `sts:AssumeRole`) and have the following permissions:

- `sqs:ReceiveMessage` (for *peek*)
- `sqs:StartMessageMoveTask` (for *redrive*)
- `sqs:PurgeQueue` (for *purge*)

These permissions can be applied globally to all SQS queues, or restricted to specific queues.

### Usage{% #usage-1 %}

After you set up the connection, you can click on a supported queue to open its side panel, where you can use the following actions:

- **Peek** to inspect failed message content and identify the root cause
- **Redrive** to requeue messages for another processing attempt
- **Purge** to clear messages that no longer need processing

## Troubleshooting{% #troubleshooting %}

If you are unable to see dead letter queue information:

- Confirm that you have installed the [Datadog-AWS integration](https://docs.datadoghq.com/integrations/amazon-web-services/)
- Confirm that your AWS role uses the AWS-managed `AmazonSQSReadOnlyAccess` policy
- Confirm that your role has `sqs:ListQueues` and `sqs:GetQueueAttributes` permissions

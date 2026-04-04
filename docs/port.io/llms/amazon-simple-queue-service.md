# Source: https://docs.port.io/build-your-software-catalog/sync-data-to-catalog/cloud-providers/aws-v3/resource-and-property-reference/amazon-simple-queue-service.md

# Amazon Simple Queue Service (SQS)

<!-- -->

## AWS::SQS::Queue[â](#awssqsqueue "Direct link to AWS::SQS::Queue")

The following example demonstrates how to ingest your AWS SQS queues to Port.

#### SQS Queue supported actions[â](#sqs-queue-supported-actions "Direct link to SQS Queue supported actions")

The table below summarizes the available actions for ingesting Amazon SQS Queue resources in Port:

| Action                                                                                                                        | Description                                                                               | Type     | Required AWS Permission  |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------- | ------------------------ |
| [ListQueuesAction](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html)                 | Discover all SQS queues across your AWS account.                                          | Default  | `sqs:ListQueues`         |
| [GetQueueAttributesAction](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) | Retrieve detailed configuration and operational data for each queue.                      | Default  | `sqs:GetQueueAttributes` |
| [ListQueueTagsAction](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html)           | Bring in custom tags assigned to your queues for advanced catalog filtering and grouping. | Optional | `sqs:ListQueueTags`      |

Optional Properties Note

Properties of optional actions will not appear in the response unless you explicitly include the action that provides them in your configuration.

You can use the following Port blueprint definitions and integration configuration:

**SQS Queue blueprint (click to expand)**

Create in Port

```
{
  "identifier": "sqsQueue",
  "title": "SQS Queue",
  "icon": "AWS",
  "schema": {
    "properties": {
      "arn": {
        "type": "string",
        "title": "ARN",
        "description": "The Amazon Resource Name (ARN) of the SQS queue"
      },
      "region": {
        "type": "string",
        "title": "Region",
        "description": "The AWS region where the SQS queue is located"
      },
      "queueUrl": {
        "type": "string",
        "title": "Queue URL",
        "description": "The URL of the SQS queue"
      },
      "approximateNumberOfMessages": {
        "type": "number",
        "title": "Approx Number of Messages",
        "description": "The approximate number of messages available for retrieval from the queue"
      },
      "visibilityTimeout": {
        "type": "number",
        "title": "Visibility Timeout (seconds)",
        "description": "The visibility timeout for the queue in seconds"
      },
      "messageRetentionPeriod": {
        "type": "number",
        "title": "Message Retention Period",
        "description": "The length of time, in seconds, for which Amazon SQS retains a message"
      },
      "sqsManagedSseEnabled": {
        "type": "boolean",
        "title": "SQS Managed SSE Enabled",
        "description": "Whether SQS managed server-side encryption is enabled"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "aggregationProperties": {},
  "relations": {
    "account": {
      "title": "Account",
      "target": "awsAccount",
      "required": false,
      "many": false
    }
  }
}
```

**SQS Queue mapping configuration (click to expand)**

```
- kind: AWS::SQS::Queue
  selector:
    query: 'true'
  port:
    entity:
      mappings:
        identifier: .Properties.QueueArn
        title: .Properties.QueueUrl | split("/") | .[-1]
        blueprint: '"sqsQueue"'
        properties:
          arn: .Properties.QueueArn
          region: .__ExtraContext.Region
          queueUrl: .Properties.QueueUrl
          approximateNumberOfMessages: .Properties.ApproximateNumberOfMessages
          visibilityTimeout: .Properties.VisibilityTimeout
          messageRetentionPeriod: .Properties.MessageRetentionPeriod
          sqsManagedSseEnabled: .Properties.SqsManagedSseEnabled
        relations:
          account: .__ExtraContext.AccountId
```

For more details about SQS queue properties, refer to the [AWS SQS API documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html).

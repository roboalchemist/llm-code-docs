# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sqs_with_sse_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/sqs_with_sse_disabled.md

---
title: SQS with SSE disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SQS with SSE disabled
---

# SQS with SSE disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `12726829-93ed-4d51-9cbe-13423f4299e1`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.html#aws-sqs-queue-kmsmasterkeyid)

### Description{% #description %}

SQS queues should encrypt message contents at rest to prevent unauthorized disclosure if storage, backups, or snapshots are compromised and to meet data protection and compliance requirements.

In CloudFormation, `AWS::SQS::Queue` resources must either define `Properties.KmsMasterKeyId` (a customer-managed KMS key ID, ARN, or alias) or set `Properties.SqsManagedSseEnabled` to `true` to enable server-side encryption. Resources that omit `KmsMasterKeyId` and either omit `SqsManagedSseEnabled` or set it to `false` will be flagged.

Secure configurations:

```yaml
MyQueue:
  Type: AWS::SQS::Queue
  Properties:
    SqsManagedSseEnabled: true
```

```yaml
MyQueueWithKms:
  Type: AWS::SQS::Queue
  Properties:
    KmsMasterKeyId: arn:aws:kms:us-west-2:123456789012:key/EXAMPLE-KEY-ID
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: "SampleQueue"
      KmsMasterKeyId: wewewewewewe
  MyQueue2:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: "SampleQueue"
      SqsManagedSseEnabled: true

```

```json
{
  "Resources": {
    "MyQueue": {
      "Type": "AWS::SQS::Queue",
      "Properties": {
        "QueueName": "SampleQueue",
        "KmsMasterKeyId": "wewewewewewe"
      }
    },
    "MyQueue2": {
      "Type": "AWS::SQS::Queue",
      "Properties": {
        "QueueName": "SampleQueue",
        "SqsManagedSseEnabled": "true"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "MyQueue": {
      "Type": "AWS::SQS::Queue",
      "Properties": {
        "QueueName": "SampleQueue"
      }
    },
    "MyQueue2": {
      "Type": "AWS::SQS::Queue",
      "Properties": {
        "QueueName": "SampleQueue",
        "SqsManagedSseEnabled": "false"
      }
    }
  }
}
```

```yaml
Resources:
  MyQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: "SampleQueue"
  MyQueue2:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: "SampleQueue"
      SqsManagedSseEnabled: false
```

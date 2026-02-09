# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/sns_topic_without_kms_master_key_id.md

---
title: SNS topic without KmsMasterKeyId
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SNS topic without KmsMasterKeyId
---

# SNS topic without KmsMasterKeyId

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9d13b150-a2ab-42a1-b6f4-142e41f81e52`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html)

### Description{% #description %}

SNS topics should use a customer-managed AWS KMS key for server-side encryption to protect published messages at rest and to enable controllable key access, rotation, and auditability.

In CloudFormation, `AWS::SNS::Topic` resources must define `Properties.KmsMasterKeyId` and set it to a KMS key identifier (key ARN, key ID, alias such as `alias/your-alias`, or a `Ref`/`Fn::GetAtt` to an `AWS::KMS::Key`). Resources missing this property will be flagged. When `KmsMasterKeyId` is undefined, SNS falls back to the AWS-managed key (`aws/sns`), which you cannot fully manage via custom key policies or rotation and which may not meet compliance or cross-account access requirements.

Secure configuration example (CloudFormation YAML):

```yaml
MyKey:
  Type: AWS::KMS::Key
  Properties:
    Description: "CMK for SNS topic encryption"

MyTopic:
  Type: AWS::SNS::Topic
  Properties:
    TopicName: my-topic
    KmsMasterKeyId: !Ref MyKey
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MySNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      Subscription:
        - Endpoint:
            Fn::GetAtt:
              - "MyQueue1"
              - "Arn"
          Protocol: "sqs"
        - Endpoint:
            Fn::GetAtt:
              - "MyQueue2"
              - "Arn"
          Protocol: "sqs"
      TopicName: "SampleTopic"
      KmsMasterKeyId: "kmsMasterKeyId"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MySNSTopic": {
      "Type": "AWS::SNS::Topic",
      "Properties": {
        "Subscription": [
          {
            "Endpoint": {
              "Fn::GetAtt": [
                "MyQueue1",
                "Arn"
              ]
            },
            "Protocol": "sqs"
          },
          {
            "Endpoint": {
              "Fn::GetAtt": [
                "MyQueue2",
                "Arn"
              ]
            },
            "Protocol": "sqs"
          }
        ],
        "TopicName": "SampleTopic",
        "KmsMasterKeyId": "kmsMasterKeyId"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MySNSTopic": {
      "Type": "AWS::SNS::Topic",
      "Properties": {
        "Subscription": [
          {
            "Endpoint": {
              "Fn::GetAtt": [
                "MyQueue1",
                "Arn"
              ]
            },
            "Protocol": "sqs"
          },
          {
            "Endpoint": {
              "Fn::GetAtt": [
                "MyQueue2",
                "Arn"
              ]
            },
            "Protocol": "sqs"
          }
        ],
        "TopicName": "SampleTopic"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MySNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      Subscription:
        - Endpoint:
            Fn::GetAtt:
              - "MyQueue1"
              - "Arn"
          Protocol: "sqs"
        - Endpoint:
            Fn::GetAtt:
              - "MyQueue2"
              - "Arn"
          Protocol: "sqs"
      TopicName: "SampleTopic"
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/kinesis_sse_not_configured.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/kinesis_sse_not_configured.md

---
title: Kinesis SSE not configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Kinesis SSE not configured
---

# Kinesis SSE not configured

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7f65be75-90ab-4036-8c2a-410aef7bb650`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html)

### Description{% #description %}

Kinesis streams must have server-side encryption enabled to protect data at rest and reduce the risk of sensitive records being exposed through compromised storage, snapshots, or insider access. In AWS CloudFormation, `AWS::Kinesis::Stream` resources must include the `Properties.StreamEncryption` object with `EncryptionType` and `KeyId` defined. Resources missing `StreamEncryption` or with `StreamEncryption.EncryptionType` or `StreamEncryption.KeyId` undefined will be flagged as insecure.

Secure CloudFormation example:

```yaml
MyKinesisStream:
  Type: AWS::Kinesis::Stream
  Properties:
    Name: my-stream
    ShardCount: 1
    StreamEncryption:
      EncryptionType: KMS
      KeyId: arn:aws:kms:us-east-1:123456789012:key/abcd1234-ef56-7890-ab12-3456cdef7890
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  EventStream:
    Type: AWS::Kinesis::Stream
    Properties:
      Name: EventStream
      RetentionPeriodHours: 24
      ShardCount: 1
      StreamEncryption:
            EncryptionType: KMS
            KeyId: !Ref myKey
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-EventStream-${AWS::Region}
```

```json
{
  "Resources": {
    "EventStream": {
      "Type": "AWS::Kinesis::Stream",
      "Properties": {
        "Tags": [
          {
            "Key": "Name",
            "Value": "${EnvironmentName}-EventStream-${AWS::Region}"
          }
        ],
        "Name": "EventStream",
        "RetentionPeriodHours": 24,
        "ShardCount": 1,
        "StreamEncryption": {
          "EncryptionType": "KMS",
          "KeyId": "myKey"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "EventStream1": {
      "Type": "AWS::Kinesis::Stream",
      "Properties": {
        "Name": "EventStream",
        "RetentionPeriodHours": 24,
        "ShardCount": 1,
        "StreamEncryption": {
          "EncryptionType": "KMS"
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "${EnvironmentName}-EventStream-${AWS::Region}"
          }
        ]
      }
    },
    "EventStream2": {
      "Type": "AWS::Kinesis::Stream",
      "Properties": {
        "Name": "EventStream",
        "RetentionPeriodHours": 24,
        "ShardCount": 1,
        "StreamEncryption": {
          "KeyId": "myKey"
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "${EnvironmentName}-EventStream-${AWS::Region}"
          }
        ]
      }
    },
    "EventStream3": {
      "Type": "AWS::Kinesis::Stream",
      "Properties": {
        "Name": "EventStream",
        "RetentionPeriodHours": 24,
        "ShardCount": 1,
        "Tags": [
          {
            "Key": "Name",
            "Value": "${EnvironmentName}-EventStream-${AWS::Region}"
          }
        ]
      }
    }
  }
}
```

```yaml
Resources:
  EventStream1:
    Type: AWS::Kinesis::Stream
    Properties:
      Name: EventStream
      RetentionPeriodHours: 24
      ShardCount: 1
      StreamEncryption:
            EncryptionType: KMS
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-EventStream-${AWS::Region}
  EventStream2:
    Type: AWS::Kinesis::Stream
    Properties:
      Name: EventStream
      RetentionPeriodHours: 24
      ShardCount: 1
      StreamEncryption:
            KeyId: !Ref myKey
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-EventStream-${AWS::Region}
  EventStream3:
    Type: AWS::Kinesis::Stream
    Properties:
      Name: EventStream
      RetentionPeriodHours: 24
      ShardCount: 1
      Tags:
        - Key: Name
          Value: !Sub ${EnvironmentName}-EventStream-${AWS::Region}
```

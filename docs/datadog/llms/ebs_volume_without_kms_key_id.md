# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ebs_volume_without_kms_key_id.md

---
title: EBS volume without KmsKeyId
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EBS volume without KmsKeyId
---

# EBS volume without KmsKeyId

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b7063015-6c31-4658-a8e7-14f98f37fd42`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html)

### Description{% #description %}

Amazon EBS volumes should specify a customer-managed AWS KMS key (`KmsKeyId`) so data at rest is encrypted under keys you control and access to decrypt volumes and snapshots can be restricted via key policies.

In CloudFormation, the `AWS::EC2::Volume` resource must include the `Properties.KmsKeyId` property, and it should reference a key ARN, key ID, or alias for a customer-managed CMK. Resources missing `KmsKeyId` will be flagged. If account-level default EBS encryption is not enabled, this omission can result in unencrypted volumes. If default encryption is enabled, it may cause the AWS-managed key to be used instead of a customer-managed key.

Secure configuration example:

```yaml
MyVolume:
  Type: AWS::EC2::Volume
  Properties:
    AvailabilityZone: us-west-2a
    Size: 100
    KmsKeyId: arn:aws:kms:us-west-2:123456789012:key/01234567-89ab-cdef-0123-456789abcdef
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: Creating ECS service
Resources:
  MyKey:
    Type: "AWS::KMS::Key"
    Properties:
      KeyPolicy:
        Version: 2012-10-17
        Id: key-default-1
        Statement:
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !Join
                - ""
                - - "arn:aws:iam::"
                  - !Ref "AWS::AccountId"
                  - ":root"
            Action: "kms:*"
            Resource: "*"
  NewVolume:
      Type: AWS::EC2::Volume
      Properties:
        Size: 100
        Encrypted: true
        AvailabilityZone: !GetAtt Ec2Instance.AvailabilityZone
        Tags:
          - Key: MyTag
            Value: TagValue
        KmsKeyId: !Ref MyKey
      DeletionPolicy: Snapshot
```

```json
{
  "Resources": {
    "MyKey": {
      "Type": "AWS::KMS::Key",
      "Properties": {
        "KeyPolicy": {
          "Version": "2012-10-17T00:00:00Z",
          "Id": "key-default-1",
          "Statement": [
            {
              "Sid": "Enable IAM User Permissions",
              "Effect": "Allow",
              "Principal": {
                "AWS": [
                  "",
                  [
                    "arn:aws:iam::",
                    "AWS::AccountId",
                    ":root"
                  ]
                ]
              },
              "Action": "kms:*",
              "Resource": "*"
            }
          ]
        }
      }
    },
    "NewVolume": {
      "DeletionPolicy": "Snapshot",
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "KmsKeyId": "MyKey",
        "Size": 100,
        "Encrypted": true,
        "AvailabilityZone": "Ec2Instance.AvailabilityZone",
        "Tags": [
          {
            "Key": "MyTag",
            "Value": "TagValue"
          }
        ]
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "Creating ECS service"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Description": "Creating ECS service",
  "Resources": {
    "NewVolume": {
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "Size": 100,
        "Encrypted": true,
        "AvailabilityZone": "Ec2Instance.AvailabilityZone",
        "Tags": [
          {
            "Key": "MyTag",
            "Value": "TagValue"
          }
        ]
      },
      "DeletionPolicy": "Snapshot"
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: Creating ECS service
Resources:
  NewVolume:
      Type: AWS::EC2::Volume
      Properties:
        Size: 100
        Encrypted: true
        AvailabilityZone: !GetAtt Ec2Instance.AvailabilityZone
        Tags:
          - Key: MyTag
            Value: TagValue
      DeletionPolicy: Snapshot
```

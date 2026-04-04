# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ebs_volume_encryption_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ebs_volume_encryption_disabled.md

---
title: EBS volume encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EBS volume encryption disabled
---

# EBS volume encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `80b7ac3f-d2b7-4577-9b10-df7913497162`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html)

### Description{% #description %}

Amazon EBS volumes must be encrypted to protect data at rest from unauthorized access and to prevent sensitive information from being exposed via unencrypted snapshots or compromised storage. In CloudFormation, the `Encrypted` property on `AWS::EC2::Volume` resources must be defined and set to `true`. Resources that omit the `Encrypted` property or have `Encrypted` set to `false` will be flagged. Optionally specify `KmsKeyId` to use a customer-managed AWS KMS key for encryption and key rotation policies.

Secure configuration example:

```yaml
MyVolume:
  Type: AWS::EC2::Volume
  Properties:
    AvailabilityZone: us-east-1a
    Size: 100
    Encrypted: true
    KmsKeyId: arn:aws:kms:us-east-1:123456789012:key/abcd-1234-ef56-...
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Volume"
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

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Volume",
  "Resources": {
    "NewVolume": {
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "Encrypted": true,
        "AvailabilityZone": "Ec2Instance.AvailabilityZone",
        "Tags": [
          {
            "Key": "MyTag",
            "Value": "TagValue"
          }
        ],
        "Size": 100
      },
      "DeletionPolicy": "Snapshot"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Volume 02"
Resources:
  NewVolume02:
    Type: AWS::EC2::Volume
    Properties:
      Size: 100
      AvailabilityZone: !GetAtt Ec2Instance.AvailabilityZone
      Tags:
        - Key: MyTag
          Value: TagValue
    DeletionPolicy: Snapshot
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Volume",
  "Resources": {
    "NewVolume": {
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "Tags": [
          {
            "Key": "MyTag",
            "Value": "TagValue"
          }
        ],
        "Size": 100,
        "Encrypted": false,
        "AvailabilityZone": "Ec2Instance.AvailabilityZone"
      },
      "DeletionPolicy": "Snapshot"
    }
  }
}
```

```json
{
  "Description": "Volume 02",
  "Resources": {
    "NewVolume02": {
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "Size": 100,
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
  },
  "AWSTemplateFormatVersion": "2010-09-09"
}
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ec2_not_ebs_optimized.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ec2_not_ebs_optimized.md

---
title: EC2 not EBS optimized
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EC2 not EBS optimized
---

# EC2 not EBS optimized

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8dd0ff1f-0da4-48df-9bb3-7f338ae36a40`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ebsoptimized)

### Description{% #description %}

EC2 instances should be EBS-optimized to ensure dedicated throughput and reduced I/O contention between instance network traffic and Amazon EBS volumes. This improves disk performance, lowers latency spikes, and helps maintain application availability under load.

For `AWS::EC2::Instance` resources, the `Properties.EbsOptimized` property must be defined and set to `true` for instance types that are not EBS-optimized by default. Resources missing `EbsOptimized` or with `EbsOptimized` set to `false` will be flagged. Instance types that are EBS-optimized by default are exempt.

**Note**: If `InstanceType` is omitted, CloudFormation defaults to `m1.small`, which is not EBS-optimized by default and should have `EbsOptimized` set to `true` explicitly set.

Secure configuration example:

```yaml
MyInstance:
  Type: AWS::EC2::Instance
  Properties:
    InstanceType: m5.large
    EbsOptimized: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: "ami-79fd7eee"
      KeyName: "testkey"
      BlockDeviceMappings:
        - DeviceName: "/dev/sdm"
          Ebs:
            VolumeType: "io1"
            Iops: "200"
            DeleteOnTermination: "false"
            VolumeSize: "20"
        - DeviceName: "/dev/sdk"
          NoDevice: {}
      EbsOptimized: true
```

```json
{
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "InstanceType": "t3.nano",
        "ImageId": "ami-79fd7eee",
        "KeyName": "testkey",
        "BlockDeviceMappings": [
          {
            "DeviceName": "/dev/sdm",
            "Ebs": {
              "VolumeType": "io1",
              "Iops": "200",
              "DeleteOnTermination": "false",
              "VolumeSize": "20"
            }
          },
          {
            "DeviceName": "/dev/sdk",
            "NoDevice": {}
          }
        ]
      }
    }
  }
}
```

```json
{
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-79fd7eee",
        "KeyName": "testkey",
        "BlockDeviceMappings": [
          {
            "DeviceName": "/dev/sdm",
            "Ebs": {
              "VolumeType": "io1",
              "Iops": "200",
              "DeleteOnTermination": "false",
              "VolumeSize": "20"
            }
          },
          {
            "DeviceName": "/dev/sdk",
            "NoDevice": {}
          }
        ],
        "EbsOptimized": true
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-79fd7eee",
        "KeyName": "testkey",
        "BlockDeviceMappings": [
          {
            "DeviceName": "/dev/sdm",
            "Ebs": {
              "VolumeType": "io1",
              "Iops": "200",
              "DeleteOnTermination": "false",
              "VolumeSize": "20"
            }
          },
          {
            "DeviceName": "/dev/sdk",
            "NoDevice": {}
          }
        ]
      }
    }
  }
}
```

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: "ami-79fd7eee"
      KeyName: "testkey"
      BlockDeviceMappings:
        - DeviceName: "/dev/sdm"
          Ebs:
            VolumeType: "io1"
            Iops: "200"
            DeleteOnTermination: "false"
            VolumeSize: "20"
        - DeviceName: "/dev/sdk"
          NoDevice: {}
      EbsOptimized: false
```

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.small
      ImageId: "ami-79fd7eee"
      KeyName: "testkey"
      BlockDeviceMappings:
        - DeviceName: "/dev/sdm"
          Ebs:
            VolumeType: "io1"
            Iops: "200"
            DeleteOnTermination: "false"
            VolumeSize: "20"
        - DeviceName: "/dev/sdk"
          NoDevice: {}
```

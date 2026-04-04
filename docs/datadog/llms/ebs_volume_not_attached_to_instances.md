# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ebs_volume_not_attached_to_instances.md

---
title: EBS volume not attached to instances
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EBS volume not attached to instances
---

# EBS volume not attached to instances

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1819ac03-542b-4026-976b-f37addd59f3b`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Availability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html)

### Description{% #description %}

Unattached Amazon EBS volumes can retain sensitive data at rest and therefore increase the risk of data exposure or unauthorized access if snapshots are created, shared, or the storage is otherwise misused. In CloudFormation, each `AWS::EC2::Volume` should be associated with an `AWS::EC2::VolumeAttachment` whose `Properties.VolumeId` references the volume (typically using `Ref` to the volume logical ID). Resources missing a corresponding `AWS::EC2::VolumeAttachment` or where no `AWS::EC2::VolumeAttachment` resource's `Properties.VolumeId` equals the volume's `Ref` will be flagged.

Note: This rule detects explicit `AWS::EC2::VolumeAttachment` resources and may not catch attachments made via instance block device mappings, LaunchConfigurations, or Auto Scaling constructs.

Secure example with an explicit attachment:

```yaml
MyVolume:
  Type: AWS::EC2::Volume
  Properties:
    AvailabilityZone: us-east-1a
    Size: 100
    Encrypted: true

AttachVolume:
  Type: AWS::EC2::VolumeAttachment
  Properties:
    InstanceId: !Ref MyInstance
    VolumeId: !Ref MyVolume
    Device: /dev/sdf
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    NewVolume:
        Type: AWS::EC2::Volume
        Properties:
            Size: 100
            AvailabilityZone: us-west-1
    MountPoint:
        Type: AWS::EC2::VolumeAttachment
        Properties:
            InstanceId: !Ref Ec2Instance
            VolumeId: !Ref NewVolume
            Device: /dev/sdh
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "NewVolume": {
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "Size": 100,
        "AvailabilityZone": "us-west-1"
      }
    },
    "MountPoint": {
      "Type": "AWS::EC2::VolumeAttachment",
      "Properties": {
        "VolumeId": "NewVolume",
        "Device": "/dev/sdh",
        "InstanceId": "Ec2Instance"
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
    "NewVolume": {
      "Type": "AWS::EC2::Volume",
      "Properties": {
        "AvailabilityZone": "us-west-1",
        "Size": 100
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    NewVolume:
        Type: AWS::EC2::Volume
        Properties:
            Size: 100
            AvailabilityZone: us-west-1
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/default_security_groups_with_unrestricted_traffic.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/default_security_groups_with_unrestricted_traffic.md

---
title: Default security groups with unrestricted traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Default security groups with unrestricted
  traffic
---

# Default security groups with unrestricted traffic

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ea33fcf7-394b-4d11-a228-985c5d08f205`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)

### Description{% #description %}

The default Amazon EC2 security group must not define inbound or outbound rules because permissive rules on the default group can expose instances to unauthorized access and enable lateral movement between resources.

In CloudFormation, this rule checks `AWS::EC2::SecurityGroup` resources with `Properties.GroupName` set to `"default"` and requires that `Properties.SecurityGroupIngress` and `Properties.SecurityGroupEgress` are either absent or empty. Resources with non-empty ingress or egress arrays will be flagged.

If you need to allow specific traffic, create a separate security group with explicit least-privilege rules and attach that group to instances instead of modifying the default group.

Secure example:

```yaml
DefaultSecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupName: default
    VpcId: vpc-01234567
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Parameters:
  KeyName:
    Description: The EC2 Key Pair to allow SSH access to the instance
    Type: 'AWS::EC2::KeyPair::KeyName'
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroups:
        - !Ref InstanceSecurityGroup
        - MyExistingSecurityGroup
      KeyName: !Ref KeyName
      ImageId: ami-7a11e213
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupName: default
      GroupDescription: Enable SSH access via port 22
```

```json
{
  "Parameters": {
    "KeyName": {
      "Description": "The EC2 Key Pair to allow SSH access to the instance",
      "Type": "AWS::EC2::KeyPair::KeyName"
    }
  },
  "Resources": {
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "SecurityGroups": [
          "InstanceSecurityGroup",
          "MyExistingSecurityGroup"
        ],
        "KeyName": "KeyName",
        "ImageId": "ami-7a11e213"
      }
    },
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupName": "default",
        "GroupDescription": "Enable SSH access via port 22"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Parameters": {
    "KeyName": {
      "Description": "The EC2 Key Pair to allow SSH access to the instance",
      "Type": "AWS::EC2::KeyPair::KeyName"
    }
  },
  "Resources": {
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "SecurityGroups": [
          "InstanceSecurityGroup",
          "MyExistingSecurityGroup"
        ],
        "KeyName": "KeyName",
        "ImageId": "ami-7a11e213"
      }
    },
    "InstanceSecurityGroup": {
      "Properties": {
        "GroupName": "default",
        "GroupDescription": "Enable SSH access via port 22",
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": "22",
            "ToPort": "22",
            "CidrIp": "0.0.0.0/0"
          }
        ],
        "SecurityGroupEgress": [
          {
            "FromPort": "22",
            "ToPort": "22",
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp"
          }
        ]
      },
      "Type": "AWS::EC2::SecurityGroup"
    }
  }
}
```

```yaml
Parameters:
  KeyName:
    Description: The EC2 Key Pair to allow SSH access to the instance
    Type: 'AWS::EC2::KeyPair::KeyName'
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroups:
        - !Ref InstanceSecurityGroup
        - MyExistingSecurityGroup
      KeyName: !Ref KeyName
      ImageId: ami-7a11e213
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupName: default
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
```

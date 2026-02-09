# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/security_groups_with_unrestricted_access_to_ssh.md

---
title: Security group with unrestricted access to SSH
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security group with unrestricted access to SSH
---

# Security group with unrestricted access to SSH

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `6e856af2-62d7-4ba2-adc1-73b62cef9cc1`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)

### Description{% #description %}

Allowing SSH (TCP port `22`) from the public internet (`0.0.0.0/0`) exposes instances to brute-force attacks, credential theft, lateral movement, and unauthorized access. In CloudFormation `AWS::EC2::SecurityGroup` resources, any `Properties.SecurityGroupIngress` entry with `CidrIp: 0.0.0.0/0` and `FromPort` or `ToPort` equal to `22` will be flagged.

To remediate, restrict SSH ingress to specific trusted IP ranges, use a bastion/jump host, or adopt AWS Systems Manager Session Manager instead of opening port `22`. Resources containing the insecure ingress entry will be reported.

Secure configuration example (restrict SSH to a single IP):

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Allow SSH from admin IP only
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: 203.0.113.4/32
```

Note: this rule specifically matches ingress entries where `FromPort == 22` or `ToPort == 22`; port ranges that include 22 but do not have 22 as an endpoint may not be detected by this check.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroups:
        - !Ref InstanceSecurityGroup
      KeyName: mykey
      ImageId: ''
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow http to client host
        VpcId:
          Ref: myVPC
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 127.0.0.1/32
        SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 127.0.0.1/33
```

```json
{
  "Resources": {
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Allow http to client host",
        "VpcId": {
          "Ref": "myVPC"
        },
        "SecurityGroupIngress": [
          {
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "127.0.0.1/32",
            "IpProtocol": "tcp"
          }
        ],
        "SecurityGroupEgress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "127.0.0.1/33"
          }
        ]
      }
    },
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "SecurityGroups": [
          "InstanceSecurityGroup"
        ],
        "KeyName": "mykey",
        "ImageId": ""
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "",
        "SecurityGroups": [
          "InstanceSecurityGroup"
        ],
        "KeyName": "mykey"
      }
    },
    "InstanceSecurityGroup": {
      "Properties": {
        "SecurityGroupEgress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ],
        "GroupDescription": "Allow http to client host",
        "VpcId": {
          "Ref": "myVPC"
        },
        "SecurityGroupIngress": [
          {
            "ToPort": 22,
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp",
            "FromPort": 22
          }
        ]
      },
      "Type": "AWS::EC2::SecurityGroup"
    }
  }
}
```

```yaml
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      SecurityGroups:
        - !Ref InstanceSecurityGroup
      KeyName: mykey
      ImageId: ''
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow http to client host
        VpcId:
          Ref: myVPC
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
        SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
```

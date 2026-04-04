# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/security_groups_unrestricted_access_to_rdp.md

---
title: Security group unrestricted access to RDP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security group unrestricted access to RDP
---

# Security group unrestricted access to RDP

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3ae83918-7ec7-4cb8-80db-b91ef0f94002`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)

### Description{% #description %}

Allowing RDP (TCP port `3389`) from the public internet (`0.0.0.0/0`) exposes hosts to automated scanning, brute-force attacks, and unauthorized remote access. This rule flags `AWS::EC2::SecurityGroup` resources whose `Properties.SecurityGroupIngress` entries have `CidrIp: 0.0.0.0/0` and either `FromPort` or `ToPort` set to `3389`.

To remediate, restrict ingress to specific trusted CIDR ranges or reference a trusted security group (using `SourceSecurityGroupId`), or require access via a bastion host or VPN. Any ingress entry with `CidrIp: "0.0.0.0/0"` for port `3389` will be reported.

Secure configuration examples:

```yaml
MyRdpSg:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: RDP access restricted to corporate network
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 3389
        ToPort: 3389
        CidrIp: 203.0.113.0/24
```

```yaml
MyRdpSg:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: RDP access via internal bastion
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 3389
        ToPort: 3389
        SourceSecurityGroupId: sg-0123456789abcdef0
```

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
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "SecurityGroups": [
          "InstanceSecurityGroup"
        ],
        "KeyName": "mykey",
        "ImageId": ""
      }
    },
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "SecurityGroupEgress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "127.0.0.1/33"
          }
        ],
        "GroupDescription": "Allow http to client host",
        "VpcId": {
          "Ref": "myVPC"
        },
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "127.0.0.1/32"
          }
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

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
            "IpProtocol": "tcp",
            "FromPort": 3389,
            "ToPort": 3389,
            "CidrIp": "0.0.0.0/0"
          }
        ],
        "SecurityGroupEgress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ]
      }
    },
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "KeyName": "mykey",
        "ImageId": "",
        "SecurityGroups": [
          "InstanceSecurityGroup"
        ]
      }
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
          FromPort: 3389
          ToPort: 3389
          CidrIp: 0.0.0.0/0
        SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
```

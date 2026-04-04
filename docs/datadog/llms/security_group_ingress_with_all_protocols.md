# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/security_group_ingress_with_all_protocols.md

---
title: Security group ingress with all protocols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security group ingress with all protocols
---

# Security group ingress with all protocols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1a427b25-2e9e-4298-9530-0499a55e736b`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html)

### Description{% #description %}

Setting `IpProtocol` to `-1` allows all protocols and all ports. This greatly increases attack surface and can expose services or enable lateral movement if an ingress rule is too permissive.

Check `AWS::EC2::SecurityGroupIngress` resources and `AWS::EC2::SecurityGroup` resources' `SecurityGroupIngress` entries. `IpProtocol` must not be set to `-1`. Resources with `IpProtocol: -1` will be flagged. Specify explicit protocols (for example, `tcp`, `udp`, or `icmp`, or their numeric protocol values) and define `FromPort`/`ToPort` where applicable. If broader access is required, restrict the source to a specific CIDR or use a referenced security group.

Secure configuration examples:

```yaml
MyIngressRule:
  Type: AWS::EC2::SecurityGroupIngress
  Properties:
    IpProtocol: tcp
    FromPort: 443
    ToPort: 443
    CidrIp: 10.0.0.0/24
```

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Example SG
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 22
        ToPort: 22
        CidrIp: 203.0.113.5/32
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
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
        CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
  OutboundRule:
    Type: AWS::EC2::SecurityGroupEgress
    Properties:
      IpProtocol: tcp
      FromPort: 0
      ToPort: 65535
      DestinationSecurityGroupId:
        Fn::GetAtt:
        - TargetSG
        - GroupId
      GroupId:
        Fn::GetAtt:
        - SourceSG
        - GroupId
  InboundRule:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      IpProtocol: tcp
      FromPort: 0
      ToPort: 65535
      SourceSecurityGroupId:
        Fn::GetAtt:
        - SourceSG
        - GroupId
      GroupId:
        Fn::GetAtt:
        - TargetSG
        - GroupId
```

```json
{
  "Resources": {
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ],
        "SecurityGroupEgress": [
          {
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp"
          }
        ],
        "GroupDescription": "Allow http to client host",
        "VpcId": {
          "Ref": "myVPC"
        }
      }
    },
    "OutboundRule": {
      "Type": "AWS::EC2::SecurityGroupEgress",
      "Properties": {
        "IpProtocol": "tcp",
        "FromPort": 0,
        "ToPort": 65535,
        "DestinationSecurityGroupId": {
          "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
          ]
        },
        "GroupId": {
          "Fn::GetAtt": [
            "SourceSG",
            "GroupId"
          ]
        }
      }
    },
    "InboundRule": {
      "Type": "AWS::EC2::SecurityGroupIngress",
      "Properties": {
        "ToPort": 65535,
        "SourceSecurityGroupId": {
          "Fn::GetAtt": [
            "SourceSG",
            "GroupId"
          ]
        },
        "GroupId": {
          "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
          ]
        },
        "IpProtocol": "tcp",
        "FromPort": 0
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
        "VpcId": {
          "Ref": "myVPC"
        },
        "SecurityGroupIngress": [
          {
            "IpProtocol": -1,
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ],
        "SecurityGroupEgress": [
          {
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp"
          }
        ],
        "GroupDescription": "Allow http to client host"
      }
    },
    "OutboundRule": {
      "Type": "AWS::EC2::SecurityGroupEgress",
      "Properties": {
        "ToPort": 65535,
        "DestinationSecurityGroupId": {
          "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
          ]
        },
        "GroupId": {
          "Fn::GetAtt": [
            "SourceSG",
            "GroupId"
          ]
        },
        "IpProtocol": "tcp",
        "FromPort": 0
      }
    },
    "InboundRule": {
      "Type": "AWS::EC2::SecurityGroupIngress",
      "Properties": {
        "IpProtocol": -1,
        "FromPort": 0,
        "ToPort": 65535,
        "SourceSecurityGroupId": {
          "Fn::GetAtt": [
            "SourceSG",
            "GroupId"
          ]
        },
        "GroupId": {
          "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
          ]
        }
      }
    }
  }
}
```

```yaml
Resources:
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow http to client host
      VpcId:
         Ref: myVPC
      SecurityGroupIngress:
      - IpProtocol: -1
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
  OutboundRule:
    Type: AWS::EC2::SecurityGroupEgress
    Properties:
      IpProtocol: tcp
      FromPort: 0
      ToPort: 65535
      DestinationSecurityGroupId:
        Fn::GetAtt:
        - TargetSG
        - GroupId
      GroupId:
        Fn::GetAtt:
        - SourceSG
        - GroupId
  InboundRule:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      IpProtocol: -1
      FromPort: 0
      ToPort: 65535
      SourceSecurityGroupId:
        Fn::GetAtt:
        - SourceSG
        - GroupId
      GroupId:
        Fn::GetAtt:
        - TargetSG
        - GroupId
```

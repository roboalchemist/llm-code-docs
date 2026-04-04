# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/security_group_egress_with_port_range.md

---
title: Security group egress with port range
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security group egress with port range
---

# Security group egress with port range

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dae9c373-8287-462f-8746-6f93dad93610`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html)

### Description{% #description %}

Egress rules should restrict outbound traffic to a single explicit port to enforce least privilege. Allowing port ranges expands the attack surface and can enable unintended outbound connections, lateral movement, or data exfiltration.

In CloudFormation, `AWS::EC2::SecurityGroupEgress` resources must have `Properties.FromPort` and `Properties.ToPort` defined and set to the same value. For `AWS::EC2::SecurityGroup` resources, each entry in `Properties.SecurityGroupEgress` must have `FromPort` equal to `ToPort`. Resources missing these properties, or where `FromPort` does not equal `ToPort`, will be flagged. Set both properties to the same explicit port number (for example, `443`) instead of using a range.

Secure configuration examples:

```yaml
MyEgressRule:
  Type: AWS::EC2::SecurityGroupEgress
  Properties:
    GroupId: sg-01234567
    IpProtocol: tcp
    FromPort: 443
    ToPort: 443
    CidrIp: 10.0.0.0/16
```

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Example security group
    SecurityGroupEgress:
      - IpProtocol: tcp
        FromPort: 443
        ToPort: 443
        CidrIp: 10.0.0.0/16
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
        Description: TCP
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
      - IpProtocol: tcp
        Description: TCP
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
  OutboundRule:
    Type: AWS::EC2::SecurityGroupEgress
    Properties:
      Description: TCP
      IpProtocol: tcp
      FromPort: 0
      ToPort: 0
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
      Description: TCP
      IpProtocol: tcp
      FromPort: 0
      ToPort: 0
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
      "Properties": {
        "VpcId": {
          "Ref": "myVPC"
        },
        "SecurityGroupIngress": [
          {
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp",
            "Description": "TCP"
          }
        ],
        "SecurityGroupEgress": [
          {
            "IpProtocol": "tcp",
            "Description": "TCP",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ],
        "GroupDescription": "Allow http to client host"
      },
      "Type": "AWS::EC2::SecurityGroup"
    },
    "OutboundRule": {
      "Properties": {
        "IpProtocol": "tcp",
        "FromPort": 0,
        "ToPort": 0,
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
        "Description": "TCP"
      },
      "Type": "AWS::EC2::SecurityGroupEgress"
    },
    "InboundRule": {
      "Type": "AWS::EC2::SecurityGroupIngress",
      "Properties": {
        "Description": "TCP",
        "IpProtocol": "tcp",
        "FromPort": 0,
        "ToPort": 0,
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
            "Description": "TCP",
            "FromPort": 80,
            "ToPort": 87,
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp"
          }
        ],
        "SecurityGroupEgress": [
          {
            "Description": "TCP",
            "FromPort": 80,
            "ToPort": 87,
            "CidrIp": "0.0.0.0/0",
            "IpProtocol": "tcp"
          }
        ]
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
        },
        "Description": "TCP"
      }
    },
    "InboundRule": {
      "Type": "AWS::EC2::SecurityGroupIngress",
      "Properties": {
        "GroupId": {
          "Fn::GetAtt": [
            "TargetSG",
            "GroupId"
          ]
        },
        "Description": "TCP",
        "IpProtocol": "tcp",
        "FromPort": 0,
        "ToPort": 65535,
        "SourceSecurityGroupId": {
          "Fn::GetAtt": [
            "SourceSG",
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
      - IpProtocol: tcp
        Description: TCP
        FromPort: 80
        ToPort: 87
        CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
      - IpProtocol: tcp
        Description: TCP
        FromPort: 80
        ToPort: 87
        CidrIp: 0.0.0.0/0
  OutboundRule:
    Type: AWS::EC2::SecurityGroupEgress
    Properties:
      Description: TCP
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
      Description: TCP
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

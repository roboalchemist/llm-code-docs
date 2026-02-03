# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ec2_permissive_network_acl_protocols.md

---
title: EC2 permissive network ACL protocols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EC2 permissive network ACL protocols
---

# EC2 permissive network ACL protocols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `03879981-efa2-47a0-a818-c843e1441b88`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html)

### Description{% #description %}

Network ACL entries that permit all protocols or use unsupported protocol values broaden the attack surface and can allow unintended traffic types to reach your instances, increasing risk of reconnaissance, exploitation, and lateral movement. For `AWS::EC2::NetworkAclEntry` resources, the `Protocol` property must be set to one of the numeric values: `6` (TCP), `17` (UDP), `1` (ICMP), or `58` (ICMPv6). Resources missing the `Protocol` property or configured with any other value (for example, `-1`/`all`) will be flagged.

**Note**: ICMPv6 (`58`) entries must also use an IPv6 CIDR block and include an ICMP type and code.

Secure configuration example:

```yaml
MyNetworkAclEntry:
  Type: AWS::EC2::NetworkAclEntry
  Properties:
    NetworkAclId: !Ref MyNetworkAcl
    RuleNumber: 100
    Protocol: 6
    RuleAction: allow
    CidrBlock: 10.0.0.0/16
    PortRange:
      From: 443
      To: 443
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  MyNACL:
    Type: AWS::EC2::NetworkAcl
    Properties:
       VpcId: vpc-1122334455aabbccd
       Tags:
       - Key: Name
         Value: NACLforSSHTraffic
  InboundRule:
    Type: AWS::EC2::NetworkAclEntry
    Properties:
       NetworkAclId:
         Ref: MyNACL
       RuleNumber: 100
       Protocol: 6
       RuleAction: allow
       CidrBlock: 172.16.0.0/24
       PortRange:
         From: 22
         To: 22
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "InboundRule": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "CidrBlock": "172.16.0.0/24",
        "PortRange": {
          "To": 22,
          "From": 22
        },
        "NetworkAclId": {
          "Ref": "MyNACL"
        },
        "RuleNumber": 100,
        "Protocol": 6,
        "RuleAction": "allow"
      }
    },
    "MyNACL": {
      "Properties": {
        "VpcId": "vpc-1122334455aabbccd",
        "Tags": [
          {
            "Key": "Name",
            "Value": "NACLforSSHTraffic"
          }
        ]
      },
      "Type": "AWS::EC2::NetworkAcl"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "MyNACL": {
      "Type": "AWS::EC2::NetworkAcl",
      "Properties": {
        "VpcId": "vpc-1122334455aabbccd",
        "Tags": [
          {
            "Key": "Name",
            "Value": "NACLforSSHTraffic"
          }
        ]
      }
    },
    "OutboundRule": {
      "Properties": {
        "CidrBlock": "0.0.0.0/0",
        "NetworkAclId": {
          "Ref": "MyNACL"
        },
        "RuleNumber": 100,
        "Protocol": -1,
        "Egress": true,
        "RuleAction": "allow"
      },
      "Type": "AWS::EC2::NetworkAclEntry"
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
  MyNACL:
    Type: AWS::EC2::NetworkAcl
    Properties:
       VpcId: vpc-1122334455aabbccd
       Tags:
       - Key: Name
         Value: NACLforSSHTraffic
  OutboundRule:
    Type: AWS::EC2::NetworkAclEntry
    Properties:
       NetworkAclId:
         Ref: MyNACL
       RuleNumber: 100
       Protocol: -1
       Egress: true
       RuleAction: allow
       CidrBlock: 0.0.0.0/0
```

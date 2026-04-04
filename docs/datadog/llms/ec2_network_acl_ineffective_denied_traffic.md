# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ec2_network_acl_ineffective_denied_traffic.md

---
title: EC2 Network ACL Deny rule not blocking all traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EC2 Network ACL Deny rule not blocking all
  traffic
---

# EC2 Network ACL Deny rule not blocking all traffic

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2623d682-dccb-44cd-99d0-54d9fd62f8f2`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html)

### Description{% #description %}

Deny entries in Network ACLs that are intended to block all external traffic must explicitly target all IP addresses (`0.0.0.0/0`). If a deny rule uses a narrower CIDR, it may leave other sources allowed and create a false sense of protection.

For `AWS::EC2::NetworkAclEntry` resources, when `Properties.RuleAction` is `deny`, `Properties.CidrBlock` must be `0.0.0.0/0`. Resources with `RuleAction` set to `deny` and a different or missing `CidrBlock` will be flagged as ineffective for global traffic denial. If you only intend to block specific ranges, use the appropriate CIDRs and verify rule ordering.

Secure example with a global deny entry:

```yaml
DenyAllEntry:
  Type: AWS::EC2::NetworkAclEntry
  Properties:
    NetworkAclId: acl-0123456789abcdef0
    RuleNumber: 100
    Protocol: -1
    RuleAction: deny
    Egress: false
    CidrBlock: 0.0.0.0/0
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
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

```json
{
  "Resources": {
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
    },
    "InboundRule": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "RuleAction": "allow",
        "CidrBlock": "172.16.0.0/24",
        "PortRange": {
          "From": 22,
          "To": 22
        },
        "NetworkAclId": {
          "Ref": "MyNACL"
        },
        "RuleNumber": 100,
        "Protocol": 6
      }
    },
    "OutboundRule": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "MyNACL"
        },
        "RuleNumber": 100,
        "Protocol": -1,
        "Egress": true,
        "RuleAction": "allow",
        "CidrBlock": "0.0.0.0/0"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
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
    "InboundRule": {
      "Properties": {
        "RuleNumber": 100,
        "Protocol": 6,
        "RuleAction": "deny",
        "CidrBlock": "172.16.0.0/24",
        "PortRange": {
          "From": 22,
          "To": 22
        },
        "NetworkAclId": {
          "Ref": "MyNACL"
        }
      },
      "Type": "AWS::EC2::NetworkAclEntry"
    },
    "OutboundRule": {
      "Properties": {
        "RuleAction": "deny",
        "CidrBlock": "0.0.0.0/0",
        "NetworkAclId": {
          "Ref": "MyNACL"
        },
        "RuleNumber": 100,
        "Protocol": -1,
        "Egress": true
      },
      "Type": "AWS::EC2::NetworkAclEntry"
    }
  }
}
```

```yaml
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
       RuleAction: deny
       CidrBlock: 172.16.0.0/24
       PortRange:
         From: 22
         To: 22
  OutboundRule:
    Type: AWS::EC2::NetworkAclEntry
    Properties:
       NetworkAclId:
         Ref: MyNACL
       RuleNumber: 100
       Protocol: -1
       Egress: true
       RuleAction: deny
       CidrBlock: 0.0.0.0/0
```

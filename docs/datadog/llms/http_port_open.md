# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/http_port_open.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/http_port_open.md

---
title: HTTP port open to internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > HTTP port open to internet
---

# HTTP port open to internet

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ddfc4eaa-af23-409f-b96c-bf5c45dc4daa`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)

### Description{% #description %}

Security groups should not allow HTTP (port `80`) ingress from the entire internet because it exposes web services to unauthenticated access and increases the attack surface for automated scanning and exploitation.

In CloudFormation, inspect `AWS::EC2::SecurityGroup` resources' `SecurityGroupIngress` entries and ensure none have `CidrIp` = `0.0.0.0/0` or `CidrIpv6` = `::/0`, combined with `IpProtocol` set to `tcp`, `-1`, or `6`, and a port range that includes `80`. This rule flags ingress entries where `FromPort <= 80` and `ToPort >= 80`, indicating port `80` is open to the world.

To remediate, restrict source CIDRs to trusted ranges, place services behind a load balancer or VPN, or require encrypted access (HTTPS/port `443`) instead of allowing global HTTP.

Secure configuration example (restrict to specific CIDR):

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Web server security group
    VpcId: !Ref MyVPC
    SecurityGroupIngress:
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
          FromPort: 80
          ToPort: 80
          CidrIp: 192.168.0.0/16
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
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "192.168.0.0/16"
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
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ]
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
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
```

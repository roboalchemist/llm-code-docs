# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/remote_desktop_port_open_to_internet.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/remote_desktop_port_open_to_internet.md

---
title: Remote Desktop port open to the internet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Remote Desktop port open to the internet
---

# Remote Desktop port open to the internet

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c9846969-d066-431f-9b34-8c4abafe422a`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)

### Description{% #description %}

Opening the Remote Desktop service (TCP port `3389`) to the public internet exposes Windows hosts to automated scanning and bruteâforce attacks and enables unauthorized remote access that can lead to credential compromise and lateral movement. In AWS CloudFormation, inspect `AWS::EC2::SecurityGroup` resources' `Properties.SecurityGroupIngress` entries and flag any ingress where `CidrIp` is `0.0.0.0/0` or `CidrIpv6` is `::/0`, `IpProtocol` is TCP (`tcp`, `-1`, or `6`), and the port range includes `3389` (`FromPort` <= `3389` and `ToPort` >= `3389`). Replace global access with specific trusted CIDR ranges or remove the rule. Provide remote access via a bastion host, VPN, or AWS Systems Manager Session Manager instead of exposing RDP directly.

Secure example restricting RDP to a single trusted IP:

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Allow RDP from trusted admin network only
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 3389
        ToPort: 3389
        CidrIp: 203.0.113.4/32
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow rdp to client host
        VpcId:
          Ref: myVPC
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 3389
          ToPort: 3389
          CidrIp: 192.168.0.0/16
```

```json
{
  "Resources": {
    "InstanceSecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Allow rdp to client host",
        "VpcId": {
          "Ref": "myVPC"
        },
        "SecurityGroupIngress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 3389,
            "ToPort": 3389,
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
        "GroupDescription": "Allow rdp to client host",
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
        GroupDescription: Allow rdp to client host
        VpcId:
          Ref: myVPC
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 3389
          ToPort: 3389
          CidrIp: 0.0.0.0/0
```

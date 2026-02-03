# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ec2_instance_subnet_has_public_ip_mapping_on_launch.md

---
title: EC2 instance subnet has public IP mapping on launch
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EC2 instance subnet has public IP mapping on
  launch
---

# EC2 instance subnet has public IP mapping on launch

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b3de4e4c-14be-4159-b99d-9ad194365e4c`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-mappubliciponlaunch)

### Description{% #description %}

Subnets must not automatically assign public IPv4 addresses to instances because automatic public IP assignment exposes instances directly to the internet and increases the risk of unauthorized access and data exposure. For CloudFormation, the `AWS::EC2::Subnet` resource's `Properties.MapPublicIpOnLaunch` property must be defined and set to `false`. Resources with `MapPublicIpOnLaunch` set to `true` will be flagged. For private subnets, explicitly set this property to `false` and use NAT gateways, bastion hosts, or load balancers to provide controlled outbound or inbound access.

Secure configuration example:

```yaml
MyPrivateSubnet:
  Type: AWS::EC2::Subnet
  Properties:
    VpcId: !Ref MyVPC
    CidrBlock: 10.0.1.0/24
    MapPublicIpOnLaunch: false
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
   mySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      MapPublicIpOnLaunch: false
      VpcId: myVPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: "us-east-1a"
      Tags:
      - Key: foo
        Value: bar
```

```json
{
  "Resources": {
    "mySubnet": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "Tags": [
          {
            "Key": "foo",
            "Value": "bar"
          }
        ],
        "MapPublicIpOnLaunch": false,
        "VpcId": "myVPC",
        "CidrBlock": "10.0.0.0/24",
        "AvailabilityZone": "us-east-1a"
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A sample template",
  "Resources": {
    "mySubnet": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "MapPublicIpOnLaunch": true,
        "VpcId": "myVPC",
        "CidrBlock": "10.0.0.0/24",
        "AvailabilityZone": "us-east-1a",
        "Tags": [
          {
            "Key": "foo",
            "Value": "bar"
          }
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
   mySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      MapPublicIpOnLaunch: true
      VpcId: myVPC
      CidrBlock: 10.0.0.0/24
      AvailabilityZone: "us-east-1a"
      Tags:
      - Key: foo
        Value: bar
```

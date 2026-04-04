# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/instance_with_no_vpc.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/instance_with_no_vpc.md

---
title: Instance with no VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Instance with no VPC
---

# Instance with no VPC

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8a6d36cd-0bc6-42b7-92c4-67acc8576861`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html)

### Description{% #description %}

EC2 instances must be launched into VPC subnets so they are subject to VPC network controls (routing and security groups) and are not placed in undefined network contexts that can increase exposure risk.

In AWS CloudFormation:

- `AWS::EC2::Instance` resources must define `Properties.NetworkInterfaces`.
- Each `NetworkInterfaces[].SubnetId` that references an `AWS::EC2::Subnet` resource must point to a subnet that defines `Properties.VpcId`.

This rule flags `AWS::EC2::Instance` resources missing `NetworkInterfaces` and flags subnet resources referenced by `SubnetId` when the referenced `AWS::EC2::Subnet` lacks a `VpcId` property. If you supply `SubnetId` as a literal ID or parameter instead of a template resource reference, ensure that the referenced subnet ID belongs to a VPC. The check validates VPC association only when `SubnetId` points to a template resource.

Secure example with a subnet declaring VpcId and an instance using a network interface that references it:

```yaml
MySubnet:
  Type: AWS::EC2::Subnet
  Properties:
    VpcId: !Ref MyVPC
    CidrBlock: 10.0.1.0/24

MyInstance:
  Type: AWS::EC2::Instance
  Properties:
    NetworkInterfaces:
      - DeviceIndex: 0
        SubnetId: !Ref MySubnet
        AssociatePublicIpAddress: false
        GroupSet:
          - !Ref MySecurityGroup
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.1.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
          - Key: Name
            Value:  !Join ['', [!Ref "AWS::StackName", "-VPC" ]]
  InternetGateway:
    Type: AWS::EC2::InternetGateway
    DependsOn: VPC
  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
  PublicSubnetA:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.1.10.0/24
      AvailabilityZone: !Select [ 0, !GetAZs ]    # Obtenha o primeiro AZ na lista
      Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-Public-A
  Ec2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: 'some-ec2-image'
      Fn::FindInMap:
            - "RegionMap"
            - Ref: "AWS::Region"
            - "AMI"
      KeyName: 'some-rsa-key'
      Ref: "KeyName"
      NetworkInterfaces:
        -   AssociatePublicIpAddress: "true"
            DeviceIndex: 0
            SubnetId: !Ref PublicSubnetA
```

```json
{
  "Resources": {
    "VPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "Tags": [
          {
            "Key": "Name",
            "Value": [
              "",
              [
                "AWS::StackName",
                "-VPC"
              ]
            ]
          }
        ],
        "CidrBlock": "10.1.0.0/16",
        "EnableDnsSupport": true,
        "EnableDnsHostnames": true
      }
    },
    "InternetGateway": {
      "Type": "AWS::EC2::InternetGateway",
      "DependsOn": "VPC"
    },
    "AttachGateway": {
      "Type": "AWS::EC2::VPCGatewayAttachment",
      "Properties": {
        "VpcId": "VPC",
        "InternetGatewayId": "InternetGateway"
      }
    },
    "PublicSubnetA": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "CidrBlock": "10.1.10.0/24",
        "AvailabilityZone": [
          0,
          ""
        ],
        "Tags": [
          {
            "Value": "${AWS::StackName}-Public-A",
            "Key": "Name"
          }
        ],
        "VpcId": "VPC"
      }
    },
    "Ec2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "KeyName": "some-rsa-key",
        "Ref": "KeyName",
        "NetworkInterfaces": [
          {
            "AssociatePublicIpAddress": "true",
            "DeviceIndex": 0,
            "SubnetId": "PublicSubnetA"
          }
        ],
        "ImageId": "some-ec2-image",
        "Fn::FindInMap": [
          "RegionMap",
          {
            "Ref": "AWS::Region"
          },
          "AMI"
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  Ec2Instance-02:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: "some-ec2-image"
      Fn::FindInMap:
            - "RegionMap"
            - Ref: "AWS::Region"
            - "AMI"
      KeyName: "some-rsa-key"
      Ref: "KeyName"
```

```json
{
  "Resources": {
    "VPC": {
      "Properties": {
        "Tags": [
          {
            "Value": [
              "",
              [
                "AWS::StackName",
                "-VPC"
              ]
            ],
            "Key": "Name"
          }
        ],
        "CidrBlock": "10.1.0.0/16",
        "EnableDnsSupport": true,
        "EnableDnsHostnames": true
      },
      "Type": "AWS::EC2::VPC"
    },
    "InternetGateway": {
      "Type": "AWS::EC2::InternetGateway",
      "DependsOn": "VPC"
    },
    "AttachGateway": {
      "Type": "AWS::EC2::VPCGatewayAttachment",
      "Properties": {
        "VpcId": "VPC",
        "InternetGatewayId": "InternetGateway"
      }
    },
    "PublicSubnetA": {
      "Properties": {
        "CidrBlock": "10.1.10.0/24",
        "AvailabilityZone": [
          0,
          ""
        ],
        "Tags": [
          {
            "Key": "Name",
            "Value": "${AWS::StackName}-Public-A"
          }
        ]
      },
      "Type": "AWS::EC2::Subnet"
    },
    "Ec2Instance-01": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "Fn::FindInMap": [
          "RegionMap",
          {
            "Ref": "AWS::Region"
          },
          "AMI"
        ],
        "KeyName": "some-rsa-key",
        "Ref": "KeyName",
        "NetworkInterfaces": [
          {
            "AssociatePublicIpAddress": "true",
            "DeviceIndex": 0,
            "SubnetId": "PublicSubnetA"
          }
        ],
        "ImageId": "some-ec2-image"
      }
    }
  }
}
```

```json
{
  "Resources": {
    "Ec2Instance-02": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "some-ec2-image",
        "Fn::FindInMap": [
          "RegionMap",
          {
            "Ref": "AWS::Region"
          },
          "AMI"
        ],
        "KeyName": "some-rsa-key",
        "Ref": "KeyName"
      }
    }
  }
}
```

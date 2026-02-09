# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ec2_instance_using_default_vpc.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ec2_instance_using_default_vpc.md

---
title: EC2 instance using default VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EC2 instance using default VPC
---

# EC2 instance using default VPC

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e42a3ef0-5325-4667-84bf-075ba1c9d58e`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-subnetid)

### Description{% #description %}

EC2 instances placed in a default VPC are more likely to be publicly reachable and lack explicit network segmentation, increasing the risk of unintended exposure and lateral movement. This rule checks `AWS::EC2::Instance` resources and ensures `Properties.SubnetId` does not reference a subnet that is associated with a default VPC. Instances are flagged when their `SubnetId` references an `AWS::EC2::Subnet` whose `Properties.VpcId` resolves to a value or `Ref` name containing `default`. Use an explicit non-default VPC and private subnets. For example, reference a subnet in your own VPC:

```yaml
MyVPC:
  Type: AWS::EC2::VPC
  Properties:
    CidrBlock: 10.0.0.0/16

MySubnet:
  Type: AWS::EC2::Subnet
  Properties:
    VpcId: !Ref MyVPC
    CidrBlock: 10.0.1.0/24

MyInstance:
  Type: AWS::EC2::Instance
  Properties:
    SubnetId: !Ref MySubnet
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  DefaultVPC:
    Type: AWS::EC2::Instance
    Properties: 
      ImageId: "ami-79fd7eee"
      KeyName: "testkey"
      SubnetId: !Ref PublicSubnetA22
  PublicSubnetA22:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref VPC
      CidrBlock: 10.1.10.0/24
      AvailabilityZone: !Select [ 0, !GetAZs ]    # Obtenha o primeiro AZ na lista
      Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-Public-A
```

```json
{
  "Resources": {
    "DefaultVPC": {
      "Properties": {
        "ImageId": "ami-79fd7eee",
        "KeyName": "testkey",
        "SubnetId": "PublicSubnetA22"
      },
      "Type": "AWS::EC2::Instance"
    },
    "PublicSubnetA22": {
      "Properties": {
        "AvailabilityZone": [
          0,
          ""
        ],
        "CidrBlock": "10.1.10.0/24",
        "Tags": [
          {
            "Key": "Name",
            "Value": "${AWS::StackName}-Public-A"
          }
        ],
        "VpcId": "VPC"
      },
      "Type": "AWS::EC2::Subnet"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "DefaultVPC": {
      "Properties": {
        "ImageId": "ami-79fd7eee",
        "KeyName": "testkey",
        "SubnetId": "PublicSubnetA2"
      },
      "Type": "AWS::EC2::Instance"
    },
    "PublicSubnetA2": {
      "Properties": {
        "AvailabilityZone": [
          0,
          ""
        ],
        "CidrBlock": "10.1.10.0/24",
        "Tags": [
          {
            "Key": "Name",
            "Value": "${AWS::StackName}-Public-A"
          }
        ],
        "VpcId": "DefaultVPC"
      },
      "Type": "AWS::EC2::Subnet"
    }
  }
}
```

```yaml
Resources:
  DefaultVPC:
    Type: AWS::EC2::Instance
    Properties: 
      ImageId: "ami-79fd7eee"
      KeyName: "testkey"
      SubnetId: !Ref PublicSubnetA2
  PublicSubnetA2:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref DefaultVPC
      CidrBlock: 10.1.10.0/24
      AvailabilityZone: !Select [ 0, !GetAZs ]    # Obtenha o primeiro AZ na lista
      Tags:
          - Key: Name
            Value: !Sub ${AWS::StackName}-Public-A
```

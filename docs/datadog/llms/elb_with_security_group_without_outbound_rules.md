# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/elb_with_security_group_without_outbound_rules.md

---
title: ELB with security group without outbound rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ELB with security group without outbound rules
---

# ELB with security group without outbound rules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `01d5a458-a6c4-452a-ac50-054d59275b7c`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupegress)

### Description{% #description %}

Load balancers that are attached to security groups with no outbound rules, or without explicitly defined egress, may be unable to reach backend targets, perform health checks, or connect to logging and monitoring services. This can cause availability and operational failures.

For load balancer resources (`AWS::ElasticLoadBalancing::LoadBalancer` and `AWS::ElasticLoadBalancingV2::LoadBalancer`), examine each security group referenced in the resource's `SecurityGroups` list and validate the corresponding `AWS::EC2::SecurityGroup` defines the `SecurityGroupEgress` property. Resources missing `SecurityGroupEgress` or with `SecurityGroupEgress` set to an empty list will be flagged. The `SecurityGroupEgress` list must contain at least one egress rule that permits the required outbound traffic and should use narrow CIDRs, ports, or security-group destinations rather than broad `0.0.0.0/0` when possible.

Secure example with an explicit outbound rule allowing HTTPS egress:

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: Allow load balancer outbound HTTPS to targets
    VpcId: vpc-01234567
    SecurityGroupEgress:
      - IpProtocol: tcp
        FromPort: 443
        ToPort: 443
        CidrIp: 10.0.0.0/16
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    sgwithegress:
        Type: AWS::EC2::SecurityGroup
        Properties:
            GroupDescription: Limits security group egress traffic
            SecurityGroupEgress:
            -   IpProtocol: tcp
                FromPort: 80
                ToPort: 80
                CidrIp: 0.0.0.0/0
    MyLoadBalancer:
        Type: AWS::ElasticLoadBalancing::LoadBalancer
        Properties:
            SecurityGroups:
            -   sgwithegress
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "sgwithegress": {
      "Properties": {
        "GroupDescription": "Limits security group egress traffic",
        "SecurityGroupEgress": [
          {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "CidrIp": "0.0.0.0/0"
          }
        ]
      },
      "Type": "AWS::EC2::SecurityGroup"
    },
    "MyLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "SecurityGroups": [
          "sgwithegress"
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "sgwithoutegress": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Limits security group egress traffic"
      }
    },
    "MyLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "SecurityGroups": [
          "sgwithoutegress"
        ]
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    sgwithoutegress:
        Type: AWS::EC2::SecurityGroup
        Properties:
            GroupDescription: Limits security group egress traffic
    MyLoadBalancer:
        Type: AWS::ElasticLoadBalancing::LoadBalancer
        Properties:
            SecurityGroups:
            -   sgwithoutegress
```

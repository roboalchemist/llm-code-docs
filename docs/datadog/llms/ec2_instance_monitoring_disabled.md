# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ec2_instance_monitoring_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ec2_instance_monitoring_disabled.md

---
title: EC2 instance monitoring disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EC2 instance monitoring disabled
---

# EC2 instance monitoring disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `0264093f-6791-4475-af34-4b8102dcbcd0`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-monitoring)

### Description{% #description %}

EC2 instances should have detailed (1-minute) monitoring enabled to improve detection and response to performance and security incidents and to provide higher-resolution metrics for investigations and alerting. In CloudFormation, the `AWS::EC2::Instance` resource must include the `Monitoring` property set to `true`. Resources missing `Monitoring` or with `Monitoring` set to `false` will be flagged.

```yaml
MyInstance:
  Type: AWS::EC2::Instance
  Properties:
    InstanceType: t3.micro
    ImageId: ami-0123456789abcdef0
    Monitoring: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-12345678
      InstanceType: t2.micro
      Monitoring: true
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-12345678
      InstanceType: t2.micro
```

```yaml
Resources:
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-12345678
      InstanceType: t2.micro
      Monitoring: false
```

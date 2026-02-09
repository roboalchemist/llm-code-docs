# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/stack_notifications_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/stack_notifications_disabled.md

---
title: Stack notifications disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Stack notifications disabled
---

# Stack notifications disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `837e033c-4717-40bd-807e-6abaa30161b7`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html)

### Description{% #description %}

CloudFormation stacks should send notifications for stack events so operators are promptly alerted to failed or unexpected stack creations, updates, or deletions.

For `AWS::CloudFormation::Stack` resources, `Properties.NotificationARNs` must be defined and set to a list of SNS topic ARNs (or CloudFormation references to `AWS::SNS::Topic` resources) so events are forwarded to your alerting channels. Resources missing `NotificationARNs`, or configured with an empty list, will be flagged because lack of notifications delays detection of provisioning failures and security-relevant changes.

Configure `NotificationARNs` with explicit ARNs or `Ref`/`GetAtt` to SNS topics to ensure reliable delivery. For example:

```yaml
NotificationTopic:
  Type: AWS::SNS::Topic

MyStack:
  Type: AWS::CloudFormation::Stack
  Properties:
    TemplateURL: https://s3.amazonaws.com/example/template.yml
    NotificationARNs:
      - !Ref NotificationTopic
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myStackWithParams:
    Type: AWS::CloudFormation::Stack
    Properties:
      NotificationARNs:
        - "String"
      TemplateURL: https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template
      Parameters:
        InstanceType: t1.micro
        KeyName: mykey
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myStackWithParams": {
      "Type": "AWS::CloudFormation::Stack",
      "Properties": {
        "NotificationARNs": [
          "string"
        ],
        "TemplateURL": "https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template",
        "Parameters": {
          "InstanceType": "t1.micro",
          "KeyName": "mykey"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myStackWithParams": {
      "Type": "AWS::CloudFormation::Stack",
      "Properties": {
        "TemplateURL": "https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template",
        "Parameters": {
          "InstanceType": "t1.micro",
          "KeyName": "mykey"
        }
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myStackWithParams:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/cloudformation-templates-us-east-2/EC2ChooseAMI.template
      Parameters:
        InstanceType: t1.micro
        KeyName: mykey
```

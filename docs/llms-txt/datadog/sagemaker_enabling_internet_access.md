# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/sagemaker_enabling_internet_access.md

---
title: SageMaker enabling internet access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SageMaker enabling internet access
---

# SageMaker enabling internet access

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `88d55d94-315d-4564-beee-d2d725feab11`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html#sagemaker-condition-nbi-lockdown)

### Description{% #description %}

SageMaker notebook instances must have direct internet access disabled to prevent notebooks from initiating outbound connections. Outbound access can be used to exfiltrate sensitive data or download and execute malicious code.

In CloudFormation, `AWS::SageMaker::NotebookInstance` resources must include `Properties.DirectInternetAccess` set to `Disabled`. Resources that omit `DirectInternetAccess`, or set it to any other value, will be flagged.

```yaml
MyNotebook:
  Type: AWS::SageMaker::NotebookInstance
  Properties:
    NotebookInstanceName: my-notebook
    InstanceType: ml.t2.medium
    RoleArn: arn:aws:iam::123456789012:role/SageMakerExecutionRole
    DirectInternetAccess: Disabled
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Internet access and root access for Creating Notebook Instances"
Resources:
  Notebook:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      DirectInternetAccess: "Disabled"
      InstanceType: "ml.c4.2xlarge"
      RoleArn: "role"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Internet access and root access for Creating Notebook Instances",
  "Resources": {
    "Notebook": {
      "Type": "AWS::SageMaker::NotebookInstance",
      "Properties": {
        "DirectInternetAccess": "Disabled",
        "InstanceType": "ml.c4.2xlarge",
        "RoleArn": "role"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "Notebook": {
      "Type": "AWS::SageMaker::NotebookInstance",
      "Properties": {
        "InstanceType": "ml.c4.2xlarge",
        "RoleArn": "role",
        "DirectInternetAccess": "Enabled"
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Internet access and root access for Creating Notebook Instances"
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "Internet access and root access for Creating Notebook Instances"
Resources:
  Notebook:
    Type: AWS::SageMaker::NotebookInstance
    Properties:
      DirectInternetAccess: "Enabled"
      InstanceType: "ml.c4.2xlarge"
      RoleArn: "role"
```

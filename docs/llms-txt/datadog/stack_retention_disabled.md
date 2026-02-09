# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/stack_retention_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/stack_retention_disabled.md

---
title: Stack retention disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Stack retention disabled
---

# Stack retention disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fe974ae9-858e-4991-bbd5-e040a834679f`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Backup

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval)

### Description{% #description %}

StackSet AutoDeployment should be enabled and configured to retain stacks when member accounts are removed to prevent unintended deletion of stacks and their resources. Unintended deletions can remove critical security controls, logging, or IAM roles and cause service disruption.

For `AWS::CloudFormation::StackSet` resources, the `Properties.AutoDeployment` object must be present, with `Enabled` set to `true` and `RetainStacksOnAccountRemoval` set to `true`. Resources missing `AutoDeployment`, with `AutoDeployment.Enabled` set to `false`, or with `AutoDeployment.RetainStacksOnAccountRemoval` set to `false` will be flagged.

Secure configuration example:

```yaml
MyStackSet:
  Type: AWS::CloudFormation::StackSet
  Properties:
    StackSetName: my-stackset
    AutoDeployment:
      Enabled: true
      RetainStacksOnAccountRemoval: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  stackset:
    Type: AWS::CloudFormation::StackSet
    Properties:
      PermissionModel: SERVICE_MANAGED
      StackSetName: some_stack_name
      TemplateURL: some_stack_link
      AutoDeployment:
        Enabled: true
        RetainStacksOnAccountRemoval: true
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "stackset2": {
      "Type": "AWS::CloudFormation::Stack",
      "Properties": {
        "PermissionModel": "SERVICE_MANAGED",
        "StackSetName": "some_stack_name",
        "TemplateURL": "some_stack_link",
        "AutoDeployment": {
          "Enabled": true,
          "RetainStacksOnAccountRemoval": true
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
    "stackset8": {
      "Type": "AWS::CloudFormation::StackSet",
      "Properties": {
        "PermissionModel": "SERVICE_MANAGED",
        "StackSetName": "some_stack_name",
        "TemplateURL": "some_stack_link",
        "AutoDeployment": {
          "Enabled": true,
          "RetainStacksOnAccountRemoval": false
        }
      }
    },
    "stackset9": {
      "Type": "AWS::CloudFormation::StackSet",
      "Properties": {
        "PermissionModel": "SERVICE_MANAGED",
        "StackSetName": "some_stack_name",
        "TemplateURL": "some_stack_link",
        "AutoDeployment": {
          "Enabled": true
        }
      }
    },
    "stackset10": {
      "Type": "AWS::CloudFormation::StackSet",
      "Properties": {
        "PermissionModel": "SERVICE_MANAGED",
        "StackSetName": "some_stack_name",
        "TemplateURL": "some_stack_link",
        "AutoDeployment": {
          "Enabled": false,
          "RetainStacksOnAccountRemoval": false
        }
      }
    },
    "stackset11": {
      "Type": "AWS::CloudFormation::StackSet",
      "Properties": {
        "PermissionModel": "SERVICE_MANAGED",
        "StackSetName": "some_stack_name",
        "TemplateURL": "some_stack_link",
        "AutoDeployment": {
          "RetainStacksOnAccountRemoval": false
        }
      }
    },
    "stackset12": {
      "Type": "AWS::CloudFormation::StackSet",
      "Properties": {
        "PermissionModel": "SERVICE_MANAGED",
        "StackSetName": "some_stack_name",
        "TemplateURL": "some_stack_link"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  stackset3:
    Type: AWS::CloudFormation::StackSet
    Properties:
      PermissionModel: SERVICE_MANAGED
      StackSetName: some_stack_name
      TemplateURL: some_stack_link
      AutoDeployment:
        Enabled: true
        RetainStacksOnAccountRemoval: false
  stackset4:
    Type: AWS::CloudFormation::StackSet
    Properties:
      PermissionModel: SERVICE_MANAGED
      StackSetName: some_stack_name
      TemplateURL: some_stack_link
      AutoDeployment:
        Enabled: true
  stackset5:
    Type: AWS::CloudFormation::StackSet
    Properties:
      PermissionModel: SERVICE_MANAGED
      StackSetName: some_stack_name
      TemplateURL: some_stack_link
      AutoDeployment:
        Enabled: false
        RetainStacksOnAccountRemoval: true
  stackset6:
    Type: AWS::CloudFormation::StackSet
    Properties:
      PermissionModel: SERVICE_MANAGED
      StackSetName: some_stack_name
      TemplateURL: some_stack_link
      AutoDeployment:
        RetainStacksOnAccountRemoval: false
  stackset7:
    Type: AWS::CloudFormation::StackSet
    Properties:
      PermissionModel: SERVICE_MANAGED
      StackSetName: some_stack_name
      TemplateURL: some_stack_link
```

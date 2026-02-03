# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/root_account_has_active_access_keys.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/root_account_has_active_access_keys.md

---
title: Root account has active access keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Root account has active access keys
---

# Root account has active access keys

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4c137350-7307-4803-8c04-17c09a7a9fcf`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html)

### Description{% #description %}

Access keys associated with the AWS root account grant persistent, account-wide credentials. If compromised, they can lead to full account takeover and loss of control over all resources.

In CloudFormation, `AWS::IAM::AccessKey` resources must not be associated with the root account. This rule flags `Resources.<name>.Properties.UserName` values that contain `root` (case-insensitive). Instead of creating or using root access keys, delete or deactivate any existing root keys, enable MFA on the root account, and provision IAM users or roles with least privilege for programmatic access.

Secure configuration example (associate access keys with an IAM user rather than the root account):

```yaml
MyUser:
  Type: AWS::IAM::User
  Properties:
    UserName: app-user

MyAccessKey:
  Type: AWS::IAM::AccessKey
  Properties:
    UserName: !Ref MyUser
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  CFNKeys:
    Type: AWS::IAM::AccessKey
    Properties:
      UserName: MyUser
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "CFNKeys": {
      "Type": "AWS::IAM::AccessKey",
      "Properties": {
        "UserName": "MyUser"
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
    "CFNKeys": {
      "Type": "AWS::IAM::AccessKey",
      "Properties": {
        "UserName": "Root"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  CFNKeys:
    Type: AWS::IAM::AccessKey
    Properties:
      UserName: Root
```

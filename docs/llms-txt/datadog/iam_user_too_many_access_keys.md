# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_user_too_many_access_keys.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_user_too_many_access_keys.md

---
title: IAM user has too many access keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM user has too many access keys
---

# IAM user has too many access keys

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `48677914-6fdf-40ec-80c4-2b0e94079f54`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html)

### Description{% #description %}

IAM users should have at most one access key because multiple keys increase the risk of credential exposure and make secure rotation and revocation more difficult. In AWS CloudFormation, each `AWS::IAM::AccessKey` resource's `Properties.UserName` should be unique per IAM user so a user is not associated with more than one access key. This rule flags templates where more than one `AWS::IAM::AccessKey` resource references the same `UserName`. Remove extra keys, consolidate usage, or rotate and delete unused keys to remediate.

Secure example with a single access key for a user:

```yaml
MyUserAccessKey:
  Type: AWS::IAM::AccessKey
  Properties:
    UserName: MyIamUser
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
    myuser:
      Type: AWS::IAM::User
      Properties:
        Path: "/"
        LoginProfile:
          Password: myP@ssW0rd
    firstKey:
      Type: AWS::IAM::AccessKey
      Properties:
        UserName:
          Ref: myuser
```

```json
{
  "Resources": {
    "myuser": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "Path": "/",
        "LoginProfile": {
          "Password": "myP@ssW0rd"
        }
      }
    },
    "firstKey": {
      "Type": "AWS::IAM::AccessKey",
      "Properties": {
        "UserName": {
          "Ref": "myuser"
        }
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
    "secondKey": {
      "Type": "AWS::IAM::AccessKey",
      "Properties": {
        "UserName": "myuser"
      }
    },
    "myuser": {
      "Type": "AWS::IAM::User",
      "Properties": {
        "LoginProfile": {
          "Password": "myP@ssW0rd"
        },
        "Path": "/"
      }
    },
    "firstKey": {
      "Type": "AWS::IAM::AccessKey",
      "Properties": {
        "UserName": "myuser"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template
Resources:
    myuser:
      Type: AWS::IAM::User
      Properties:
        Path: "/"
        LoginProfile:
          Password: myP@ssW0rd
    firstKey:
      Type: AWS::IAM::AccessKey
      Properties:
        UserName: !Ref myuser
    secondKey:
      Type: AWS::IAM::AccessKey
      Properties:
        UserName: !Ref myuser
```

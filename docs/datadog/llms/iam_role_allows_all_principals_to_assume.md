# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_role_allows_all_principals_to_assume.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_role_allows_all_principals_to_assume.md

---
title: IAM role allows all principals to assume
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM role allows all principals to assume
---

# IAM role allows all principals to assume

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f80e3aa7-7b34-4185-954e-440a6894dde6`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument)

### Description{% #description %}

IAM role trust policies must not grant account-root or wildcard principals permission to assume the role, because allowing principals like an account root ARN (`arn:aws:iam::123456789012:root`) or `*` effectively trusts every principal in an account or every AWS account and can enable privilege escalation or unintended cross-account access. Check `AWS::IAM::Role` resources' `Properties.AssumeRolePolicyDocument.Statement[].Principal.AWS`. The principal value must not be `*` or contain `:root`. Only statements with `Effect: Allow` are evaluated. Resources with `Principal.AWS` containing `:root` or `*` will be flagged and should be replaced with explicit principal ARNs or specific service principals.

Secure example with an explicit principal ARN:

```yaml
MyRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Principal:
            AWS: arn:aws:iam::123456789012:role/TrustedRole
          Action: sts:AssumeRole
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  RootRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument: >
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "AWS": "arn:aws:iam::root"
                    },
                    "Effect": "Deny",
                    "Sid": ""
                }
            ]
        }
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "RootRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Deny",
              "Principal": {
                "AWS": [
                  "arn:aws:iam::root"
                ]
              },
              "Action": [
                "sts:AssumeRole"
              ]
            }
          ]
        },
        "Path": "/"
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
    "RootRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": [
                  "arn:aws:iam::root"
                ]
              },
              "Action": [
                "sts:AssumeRole"
              ]
            }
          ]
        },
        "Path": "/"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  RootRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument: >
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Principal": {
                        "AWS": "arn:aws:iam::root"
                    },
                    "Effect": "Allow",
                    "Sid": ""
                }
            ]
        }
```

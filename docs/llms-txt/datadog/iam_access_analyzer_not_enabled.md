# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_access_analyzer_not_enabled.md

---
title: IAM Access Analyzer not enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM Access Analyzer not enabled
---

# IAM Access Analyzer not enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8d29754a-2a18-460d-a1ba-9509f8d359da`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html)

### Description{% #description %}

IAM Access Analyzer provides continuous monitoring of resource-based policies to detect unintended public or cross-account access. If an `AWS::AccessAnalyzer::Analyzer` is not defined, these permission issues can go undetected, increasing the risk of data exposure or privilege escalation.

The CloudFormation template must include an `AWS::AccessAnalyzer::Analyzer` resource. Templates missing this resource will be flagged. Set the `Properties.Type` to `ACCOUNT` to monitor a single account or `ORGANIZATION` to monitor an AWS Organization, and optionally provide an `AnalyzerName` for identification.

Secure configuration example:

```yaml
MyAccessAnalyzer:
  Type: AWS::AccessAnalyzer::Analyzer
  Properties:
    AnalyzerName: my-access-analyzer
    Type: ACCOUNT
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  Analyzer:
    Type: "AWS::AccessAnalyzer::Analyzer"
    Properties:
      AnalyzerName: MyAccountAnalyzer
      Type: ACCOUNT
      Tags:
        - Key: Kind
          Value: Dev
      ArchiveRules:
        - # Archive findings for a trusted AWS account
          RuleName: ArchiveTrustedAccountAccess
          Filter:
            - Property: "principal.AWS"
              Eq:
                - "123456789012"
        - # Archive findings for known public S3 buckets
          RuleName: ArchivePublicS3BucketsAccess
          Filter:
            - Property: "resource"
              Contains:
                - "arn:aws:s3:::docs-bucket"
                - "arn:aws:s3:::clients-bucket"
```

```json
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
      "Analyzer": {
        "Type": "AWS::AccessAnalyzer::Analyzer",
        "Properties": {
          "AnalyzerName": "MyAccountAnalyzer",
          "Type": "ACCOUNT",
          "Tags": [
            {
              "Key": "Kind",
              "Value": "Dev"
            }
          ],
          "ArchiveRules": [
            {
              "RuleName": "ArchiveTrustedAccountAccess",
              "Filter": [
                {
                  "Property": "principal.AWS",
                  "Eq": [
                    "123456789012"
                  ]
                }
              ]
            },
            {
              "RuleName": "ArchivePublicS3BucketsAccess",
              "Filter": [
                {
                  "Property": "resource",
                  "Contains": [
                    "arn:aws:s3:::docs-bucket",
                    "arn:aws:s3:::clients-bucket"
                  ]
                }
              ]
            }
          ]
        }
      }
    }
  }
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "A sample template 2",
    "Resources": {
      "myuseeer": {
        "Type": "AWS::IAM::Group",
        "Properties": {
          "Path": "/",
          "LoginProfile": {
            "Password": "myP@ssW0rd"
          }
        }
      }
    }
  }
  
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A sample template 2
Resources:
  myuseeer:
    Type: AWS::IAM::Group
    Properties:
      Path: "/"
      LoginProfile:
        Password: myP@ssW0rd
```

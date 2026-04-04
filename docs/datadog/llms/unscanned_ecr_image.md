# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/unscanned_ecr_image.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/unscanned_ecr_image.md

---
title: Unscanned ECR image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Unscanned ECR image
---

# Unscanned ECR image

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9025b2b3-e554-4842-ba87-db7aeec36d35`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-imagescanningconfiguration)

### Description{% #description %}

ECR repositories should enable image scanning on push to detect known vulnerabilities before images are deployed. This reduces the risk of running vulnerable or compromised containers.

For `AWS::ECR::Repository` resources, `Properties.ImageScanningConfiguration.ScanOnPush` must be set to `true`. Resources missing `ImageScanningConfiguration`, or with `ScanOnPush` set to `false`, will be flagged.

To remediate, set `ImageScanningConfiguration.ScanOnPush` to `true` on the repository resource.

Secure configuration example:

```yaml
MyEcrRepository:
  Type: AWS::ECR::Repository
  Properties:
    RepositoryName: my-repo
    ImageScanningConfiguration:
      ScanOnPush: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-11"
Resources:
  MyRepository:
    Type: AWS::ECR::Repository
    Properties:
      RepositoryName: "test-repository"
      ImageScanningConfiguration:
        ScanOnPush: "true"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-11T00:00:00Z",
  "Resources": {
    "MyRepository2": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "RepositoryName": "test-repository",
        "ImageScanningConfiguration": {
          "ScanOnPush": "true"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-11"
Resources:
  MyRepository4:
    Type: AWS::ECR::Repository
    Properties:
      RepositoryName: "test-repository"
      ImageScanningConfiguration:
        ScanOnPush: "false"
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyRepository5": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "RepositoryName": "test-repository",
        "RepositoryPolicyText": {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Sid": "AllowPushPull",
              "Effect": "Allow",
              "Principal": {
                "AWS": [
                  "arn:aws:iam::123456789012:user/Bob",
                  "arn:aws:iam::123456789012:user/Alice"
                ]
              },
              "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload"
              ]
            }
          ]
        }
      }
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-11T00:00:00Z",
  "Resources": {
    "MyRepository6": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "RepositoryName": "test-repository",
        "ImageScanningConfiguration": {
          "ScanOnPush": "false"
        }
      }
    }
  }
}
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ecr_image_tag_not_immutable.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ecr_image_tag_not_immutable.md

---
title: ECR image tag not immutable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECR image tag not immutable
---

# ECR image tag not immutable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `33f41d31-86b1-46a4-81f7-9c9a671f59ac`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html)

### Description{% #description %}

Amazon ECR repositories should enforce immutable image tags to prevent tags from being overwritten. This reduces the risk of supply-chain tampering and accidental or malicious replacement of images referenced by deployments.

The `ImageTagMutability` property on `AWS::ECR::Repository` must be defined and set to `IMMUTABLE`. Resources missing this property or with `ImageTagMutability` set to `MUTABLE` will be flagged as a security issue.

Secure configuration example:

```yaml
MyRepository:
  Type: AWS::ECR::Repository
  Properties:
    RepositoryName: my-repo
    ImageTagMutability: IMMUTABLE
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyRepository:
    Type: AWS::ECR::Repository
    Properties:
      ImageTagMutability: "IMMUTABLE"
      RepositoryName: "test-repository"
      RepositoryPolicyText:
        Version: "2012-10-17"
        Statement:
          -
            Sid: AllowPushPull
            Effect: Allow
            Principal:
              AWS:
                - "arn:aws:iam::123456789012:user/Bob"
                - "arn:aws:iam::123456789012:user/Alice"
            Action:
              - "ecr:GetDownloadUrlForLayer"
              - "ecr:BatchGetImage"
              - "ecr:BatchCheckLayerAvailability"
              - "ecr:PutImage"
              - "ecr:InitiateLayerUpload"
              - "ecr:UploadLayerPart"
              - "ecr:CompleteLayerUpload"
```

```json
{
  "Resources": {
    "MyRepository2": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "ImageTagMutability": "IMMUTABLE",
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

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "MyRepository5": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "ImageTagMutability": "MUTABLE",
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
    },
    "MyRepository6": {
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

```yaml
Resources:
  MyRepository3:
    Type: AWS::ECR::Repository
    Properties:
      ImageTagMutability: "MUTABLE"
      RepositoryName: "test-repository"
      RepositoryPolicyText:
        Version: "2012-10-17"
        Statement:
          -
            Sid: AllowPushPull
            Effect: Allow
            Principal:
              AWS:
                - "arn:aws:iam::123456789012:user/Bob"
                - "arn:aws:iam::123456789012:user/Alice"
            Action:
              - "ecr:GetDownloadUrlForLayer"
              - "ecr:BatchGetImage"
              - "ecr:BatchCheckLayerAvailability"
              - "ecr:PutImage"
              - "ecr:InitiateLayerUpload"
              - "ecr:UploadLayerPart"
              - "ecr:CompleteLayerUpload"
  MyRepository4:
    Type: AWS::ECR::Repository
    Properties:
      RepositoryName: "test-repository"
      RepositoryPolicyText:
        Version: "2012-10-17"
        Statement:
          -
            Sid: AllowPushPull
            Effect: Allow
            Principal:
              AWS:
                - "arn:aws:iam::123456789012:user/Bob"
                - "arn:aws:iam::123456789012:user/Alice"
            Action:
              - "ecr:GetDownloadUrlForLayer"
              - "ecr:BatchGetImage"
              - "ecr:BatchCheckLayerAvailability"
              - "ecr:PutImage"
              - "ecr:InitiateLayerUpload"
              - "ecr:UploadLayerPart"
              - "ecr:CompleteLayerUpload"
```

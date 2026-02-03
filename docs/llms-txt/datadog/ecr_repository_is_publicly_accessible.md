# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ecr_repository_is_publicly_accessible.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ecr_repository_is_publicly_accessible.md

---
title: ECR repository is publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECR repository is publicly accessible
---

# ECR repository is publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `75be209d-1948-41f6-a8c8-e22dd0121134`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html)

### Description{% #description %}

Amazon ECR repository policies that allow wildcard principals (`*`) grant public access to container images, enabling any AWS account or unauthenticated user to pull or push images. This increases the risk of data exposure, unauthorized deployments, and supply-chain compromise.

The `RepositoryPolicyText` property of `AWS::ECR::Repository` resources must not contain `Statement` entries where `Effect` is `Allow` and the `Principal` includes `*`. This rule flags repository policy statements with `Principal` set to `*` and `Effect` set to `Allow`. Instead, specify explicit principals such as AWS account ARNs, IAM roles, or service principals and apply least-privilege actions and conditions.

Secure configuration example (restrict to a specific AWS account):

```yaml
MyRepository:
  Type: AWS::ECR::Repository
  Properties:
    RepositoryName: my-repo
    RepositoryPolicyText:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Principal:
            AWS: "arn:aws:iam::123456789012:root"
          Action:
            - "ecr:GetDownloadUrlForLayer"
            - "ecr:BatchGetImage"
            - "ecr:BatchCheckLayerAvailability"
          Resource: !Sub "arn:aws:ecr:${AWS::Region}:${AWS::AccountId}:repository/my-repo"
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyRepository1:
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

```json
{
  "Resources": {
    "MyRepository2": {
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

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "MyRepository4": {
      "Type": "AWS::ECR::Repository",
      "Properties": {
        "RepositoryName": "test-repository",
        "RepositoryPolicyText": {
          "Version": "2008-10-17",
          "Statement": [
            {
              "Sid": "AllowPushPull",
              "Effect": "Allow",
              "Principal": "*",
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
      RepositoryName: "test-repository"
      RepositoryPolicyText:
        Version: "2012-10-17"
        Statement:
          -
            Sid: AllowPushPull
            Effect: Allow
            Principal: "*"
            Action:
              - "ecr:GetDownloadUrlForLayer"
              - "ecr:BatchGetImage"
              - "ecr:BatchCheckLayerAvailability"
              - "ecr:PutImage"
              - "ecr:InitiateLayerUpload"
              - "ecr:UploadLayerPart"
              - "ecr:CompleteLayerUpload"
```

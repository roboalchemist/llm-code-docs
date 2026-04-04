# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/github/github_repository_set_to_public.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/github_repository_set_to_public.md

---
title: GitHub repository set to public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > GitHub repository set to public
---

# GitHub repository set to public

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5906092d-5f74-490d-9a03-78febe0f65e1`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html)

### Description{% #description %}

Public code repositories can expose source code, credentials, and intellectual property, increasing risk of data leakage and supply-chain compromise.

In CloudFormation, `AWS::CodeStar::GitHubRepository` resources must include the `IsPrivate` property and set it to `true`. Resources that omit `IsPrivate` or have `IsPrivate` set to a non-`true` value will be flagged.

Secure configuration example:

```yaml
MyRepo:
  Type: AWS::CodeStar::GitHubRepository
  Properties:
    RepositoryName: my-repo
    IsPrivate: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  MyRepo1:
    Type: AWS::CodeStar::GitHubRepository
    Properties:
      Code:
        S3:
          Bucket: "my-bucket"
          Key: "sourcecode.zip"
          ObjectVersion: "1"
      EnableIssues: true
      IsPrivate: true
      RepositoryAccessToken: '{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}'
      RepositoryDescription: a description
      RepositoryName: my-github-repo
      RepositoryOwner: my-github-account
```

```json
{
  "Resources": {
    "MyRepo2": {
      "Type": "AWS::CodeStar::GitHubRepository",
      "Properties": {
        "Code": {
          "S3": {
            "Bucket": "my-bucket",
            "Key": "sourcecode.zip",
            "ObjectVersion": "1"
          }
        },
        "EnableIssues": true,
        "IsPrivate": true,
        "RepositoryAccessToken": "{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}",
        "RepositoryDescription": "a description",
        "RepositoryName": "my-github-repo",
        "RepositoryOwner": "my-github-account"
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  MyRepo4:
    Type: AWS::CodeStar::GitHubRepository
    Properties:
      Code:
        S3:
          Bucket: "my-bucket"
          Key: "sourcecode.zip"
          ObjectVersion: "1"
      EnableIssues: true
      RepositoryAccessToken: '{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}'
      RepositoryDescription: a description
      RepositoryName: my-github-repo
      RepositoryOwner: my-github-account
```

```json
{
  "Resources": {
    "MyRepo5": {
      "Type": "AWS::CodeStar::GitHubRepository",
      "Properties": {
        "Code": {
          "S3": {
            "Bucket": "my-bucket",
            "Key": "sourcecode.zip",
            "ObjectVersion": "1"
          }
        },
        "EnableIssues": true,
        "RepositoryAccessToken": "{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}",
        "RepositoryDescription": "a description",
        "RepositoryName": "my-github-repo",
        "RepositoryOwner": "my-github-account"
      }
    }
  }
}
```

```json
{
  "Resources": {
    "MyRepo6": {
      "Type": "AWS::CodeStar::GitHubRepository",
      "Properties": {
        "Code": {
          "S3": {
            "Bucket": "my-bucket",
            "Key": "sourcecode.zip",
            "ObjectVersion": "1"
          }
        },
        "EnableIssues": true,
        "IsPrivate": false,
        "RepositoryAccessToken": "{{resolve:secretsmanager:your-secret-manager-name:SecretString:your-secret-manager-key}}",
        "RepositoryDescription": "a description",
        "RepositoryName": "my-github-repo",
        "RepositoryOwner": "my-github-account"
      }
    }
  }
}
```

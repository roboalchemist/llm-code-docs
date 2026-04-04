# Source: https://docs.datadoghq.com/security/default_rules/def-000-jtg.md

---
title: CodeBuild source credentials should be stored and transmitted securely
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CodeBuild source credentials should be
  stored and transmitted securely
---

# CodeBuild source credentials should be stored and transmitted securely

## Description{% #description %}

This control verifies if AWS CodeBuild source credentials include personal access tokens or basic authentication credentials (username and password). It is applicable only to credentials for GitHub or Bitbucket sources, as only these sources support insecure repository access methods.

Using personal access tokens or basic authentication may lead to unintended data exposure or unauthorized access. Secure methods to access source respositories include AWS CodeConnections, AWS Secrets Manager, or OAuth.

## Remediation{% #remediation %}

For guidance on updating CodeBuild source provider settings, refer to the [Access your source provider in CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html) section of the AWS CodeBuild User Guide.

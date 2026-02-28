# Source: https://docs.datadoghq.com/security/default_rules/def-000-nck.md

---
title: >-
  CodeBuild project environment variables should not contain plain text
  credentials
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CodeBuild project environment variables
  should not contain plain text credentials
---

# CodeBuild project environment variables should not contain plain text credentials

## Description{% #description %}

This rule verifies whether the project has plain text environment variables that include the string `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY`. Storing authentication credentials such as these in plain text poses a security risk, as it may result in unauthorized access and potential data exposure.

## Remediation{% #remediation %}

For guidance on updating project environment variables, refer to the [Change a build project's settings in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html) section in the AWS CodeBuild User Guide.

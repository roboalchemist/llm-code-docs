# Source: https://docs.datadoghq.com/security/default_rules/def-000-q4w.md

---
title: Secrets should not be passed as container environment variables
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Secrets should not be passed as
  container environment variables
---

# Secrets should not be passed as container environment variables

## Description{% #description %}

This assessment verifies whether the environment parameter in container definitions includes key values such as AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, or ECS_ENGINE_AUTH_DATA. This evaluation does not extend to environmental variables sourced from external locations like Amazon S3. It is focused solely on the latest active revision of an Amazon ECS task definition.

Utilizing AWS Systems Manager Parameter Store can enhance the security posture of your organization. We recommend leveraging the Parameter Store to securely store secrets and credentials instead of directly embedding them in container instances or hardcoding them in your code.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

To create parameters using SSM, see [Creating Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html) in the AWS Systems Manager User Guide. For more information about creating a task definition that specifies a secret, see [Specifying sensitive data using Secrets Manager](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html#secrets-create-taskdefinition) in the Amazon Elastic Container Service Developer Guide.

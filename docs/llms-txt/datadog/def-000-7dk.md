# Source: https://docs.datadoghq.com/security/default_rules/def-000-7dk.md

---
title: ECS task definitions should maintain unique execution/task roles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS task definitions should maintain
  unique execution/task roles
---

# ECS task definitions should maintain unique execution/task roles
 
## Description{% #description %}

Amazon ECS task definitions should use different IAM roles for task execution and task operations to ensure proper security isolation and least-privilege access. When a task definition uses the same IAM role for both `taskRoleArn` and `executionRoleArn`, it violates the principle of least privilege by granting the application unnecessary permissions to AWS resources required only for container management.

## Remediation{% #remediation %}

Use separate IAM roles for `taskRoleArn` and `executionRoleArn` in your ECS task definitions. Refer to the [Amazon ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) and [task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) documentation for configuration details.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-qq2.md

---
title: ECS containers should be limited to read-only access to root filesystems
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS containers should be limited to
  read-only access to root filesystems
---

# ECS containers should be limited to read-only access to root filesystems
 
## Description{% #description %}

This evaluation examines whether Amazon ECS containers are restricted to read-only access to mounted root filesystems. The evaluation will not succeed if the `readonlyRootFilesystem` parameter is set to false or if the parameter is missing from the container definition in the task definition. This assessment is based on the most recent active revision of an Amazon ECS task definition.

Enabling this setting helps to minimize security vulnerabilities as it prevents unauthorized tampering or writing to the container instance's filesystem unless explicit read-write permissions are granted to its folders and directories. This control also aligns with the principle of least privilege.

For containers that do not function correctly with `readonlyRootFilesystem` enabled, ECS offers various storage options as described in the [Storage options for Amazon ECS tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) section of the Amazon Elastic Container Service Developer Guide. Consult the documentation of the container you are attempting to deploy to confirm which paths require write access and which storage option is appropriate. Once the required storage and mount points have been configured, the container should function correctly with `readonlyRootFilesystem` enabled.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Open the [Amazon ECS classic console](https://console.aws.amazon.com/ecs/)

1. In the left navigation pane, choose **Task definitions**.

1. Select a task definition that has container definitions that need to be updated. For each, complete the following steps:

   - From the drop down, choose **Create new revision with JSON**.

   - Add the `readonlyRootFilesystem` parameter, and set it to `true` in the container definition within the task definition.

   - Choose **Create**.

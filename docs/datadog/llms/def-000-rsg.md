# Source: https://docs.datadoghq.com/security/default_rules/def-000-rsg.md

---
title: >-
  ECS Fargate services should automatically use the latest Fargate platform
  version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS Fargate services should
  automatically use the latest Fargate platform version
---

# ECS Fargate services should automatically use the latest Fargate platform version

## Description{% #description %}

This control verifies whether Amazon ECS Fargate services are configured to automatically utilize the latest Fargate platform version.

Fargate platform versions define a specific runtime environment for Fargate task infrastructure, encompassing kernel and container runtime versions. Updates to platform versions are introduced as the runtime environment evolves, addressing kernel or operating system enhancements, feature additions, bug fixes, or security improvements. Security updates and patches are automatically applied to Fargate tasks.

Configuring ECS Fargate to use `platformVersion = LATEST` ensures that your workloads benefit from the latest security updates, features, and enhancements provided by AWS, reducing the risk of vulnerabilities and improving overall system resilience.

## Remediation{% #remediation %}

For guidance on configuring ECS platform versions, refer to the [Updating a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html) section of the Amazon Elastic Container Service Developer Guide.

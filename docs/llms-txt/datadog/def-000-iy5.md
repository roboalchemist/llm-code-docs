# Source: https://docs.datadoghq.com/security/default_rules/def-000-iy5.md

---
title: ECS task definitions should have a logging configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS task definitions should have a
  logging configuration
---

# ECS task definitions should have a logging configuration

## Description{% #description %}

This assessment examines whether the most recent active Amazon ECS task definition includes a specified logging configuration. The assessment will not pass if the task definition does not have the logConfiguration property defined or if the logDriver value is null in at least one container definition.

Logging plays a vital role in maintaining the reliability, availability, and performance of Amazon ECS. By collecting data from task definitions, you gain visibility that aids in debugging processes and identifying the source of errors. If you are using a logging solution that does not need to be explicitly defined in the ECS task definition (such as a third-party logging solution), you can safely disable this assessment after confirming that your logs are effectively captured and delivered.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

To define a log configuration for your Amazon ECS task definitions, see [Specifying a log configuration in your task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html#specify-log-config) in the Amazon Elastic Container Service Developer Guide.

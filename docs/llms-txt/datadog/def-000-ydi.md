# Source: https://docs.datadoghq.com/security/default_rules/def-000-ydi.md

---
title: ECS containers should run as non-privileged
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS containers should run as
  non-privileged
---

# ECS containers should run as non-privileged
 
## Description{% #description %}

This assessment examines whether the privileged setting in the container definition of Amazon ECS Task Definitions is enabled. The assessment will not pass if the privileged setting is enabled. This evaluation is based on the most recent active revision of an Amazon ECS task definition.

It is advisable to avoid granting elevated privileges in your ECS task definitions. When the privileged setting is enabled, the container is granted elevated privileges on the host container instance, similar to those of the root user.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

To configure the privileged parameter on a task definition, see [Advanced container definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#container_definition_security) in the Amazon Elastic Container Service Developer Guide.

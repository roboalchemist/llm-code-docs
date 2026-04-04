# Source: https://docs.datadoghq.com/security/default_rules/def-000-zbk.md

---
title: ECS task definitions should not share the host's process namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS task definitions should not share
  the host's process namespace
---

# ECS task definitions should not share the host's process namespace

## Description{% #description %}

This assessment verifies whether Amazon ECS task definitions are set up to share a host's process namespace with its containers. The assessment will not pass if the task definition allows the host's process namespace to be shared with the containers it runs. This evaluation is based on the most recent active revision of an Amazon ECS task definition.

A Process ID (PID) namespace serves to isolate processes from one another, preventing system processes from being visible and allowing PIDs, including PID 1, to be reused. If the host's PID namespace is shared with containers, it would grant containers visibility into all processes on the host system. This compromises the intended isolation between the host and its containers at the process level. Such a setup could potentially result in unauthorized access to host processes, enabling unauthorized manipulation or termination. Therefore, it is recommended that customers refrain from sharing the host's process namespace with containers.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

To configure the pidMode on a task definition, see [Task definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_definition_pidmode) in the Amazon Elastic Container Service Developer Guide.

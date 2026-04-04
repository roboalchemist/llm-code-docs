# Source: https://docs.datadoghq.com/security/default_rules/def-000-e0r.md

---
title: DynamoDB tables should scale automatically with demand
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DynamoDB tables should scale
  automatically with demand
---

# DynamoDB tables should scale automatically with demand

## Description{% #description %}

This control verifies if an Amazon DynamoDB table can automatically adjust its read and write capacity based on demand by using either on-demand capacity mode or provisioned mode with auto-scaling enabled.

By scaling capacity according to demand, the risk of throttling exceptions is reduced, supporting consistent application availability. Tables operating in on-demand capacity mode are restricted only by the default throughput quotas set by DynamoDB. To increase these quotas, you can submit a support ticket to AWS Support. DynamoDB tables using provisioned mode with auto-scaling dynamically adjust their provisioned throughput capacity based on traffic patterns.

## Remediation{% #remediation %}

For guidance regarding enabling DynamoDB automatic scaling on existing tables, refer to the [Enabling DynamoDB auto scaling on existing tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.Console.html#AutoScaling.Console.ExistingTable) section of the Amazon DynamoDB Developer Guide.

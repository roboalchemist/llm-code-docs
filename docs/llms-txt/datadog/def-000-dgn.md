# Source: https://docs.datadoghq.com/security/default_rules/def-000-dgn.md

---
title: DynamoDB tables should have point-in-time recovery enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DynamoDB tables should have
  point-in-time recovery enabled
---

# DynamoDB tables should have point-in-time recovery enabled

## Description{% #description %}

This feature verifies if point-in-time recovery (PITR) has been activated for an Amazon DynamoDB table.

Enabling backups can expedite recovery in the event of a security breach and enhance system reliability. DynamoDB's point-in-time recovery feature automates the backup process for tables, speeding up recovery from unintentional data loss. Tables with PITR enabled can be restored to any specific point within the last 35 days.

## Remediation{% #remediation %}

To recover a DynamoDB table to a specific point in time, refer to the section on [Restoring a DynamoDB table to a specific point in time in the Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html).

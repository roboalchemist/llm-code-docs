# Source: https://docs.datadoghq.com/security/default_rules/def-000-3cf.md

---
title: DynamoDB tables should have deletion protection enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DynamoDB tables should have deletion
  protection enabled
---

# DynamoDB tables should have deletion protection enabled

## Description{% #description %}

This check verifies if deletion protection is turned on for an Amazon DynamoDB table. If the table does not have deletion protection enabled, the check will fail.

Setting up deletion protection for a DynamoDB table prevents accidental deletion. By enabling this feature, you can safeguard your tables from unintended deletion during routine table management tasks performed by administrators. This measure helps prevent any interruptions to your regular business activities.

## Remediation{% #remediation %}

To activate deletion protection for a DynamoDB table, refer to the section on [Using deletion protection in the Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.Basics.html#WorkingWithTables.Basics.DeletionProtection).

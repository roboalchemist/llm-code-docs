# Source: https://docs.datadoghq.com/security/default_rules/def-000-u7d.md

---
title: DocumentDB clusters should publish audit logs to CloudWatch Logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DocumentDB clusters should publish
  audit logs to CloudWatch Logs
---

# DocumentDB clusters should publish audit logs to CloudWatch Logs

## Description{% #description %}

This control verifies if an Amazon DocumentDB cluster is configured to send audit logs to Amazon CloudWatch Logs. The control is marked as failed if the cluster does not transmit audit logs to CloudWatch Logs.

Amazon DocumentDB (compatible with MongoDB) enables you to track activities performed within your cluster, such as successful and unsuccessful attempts to authenticate, the removal of a collection in a database, or the creation of an index. Auditing is not enabled by default in Amazon DocumentDB, and you must manually activate it.

## Remediation{% #remediation %}

To publish Amazon DocumentDB audit logs to CloudWatch Logs, see [Enabling auditing in the Amazon DocumentDB Developer Guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/event-auditing.html#event-auditing-enabling-auditing).

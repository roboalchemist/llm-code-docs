# Source: https://docs.datadoghq.com/security/default_rules/def-000-0zv.md

---
title: EKS clusters should have audit logs enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EKS clusters should have audit logs
  enabled
---

# EKS clusters should have audit logs enabled
 
## Description{% #description %}

This control checks if an Amazon EKS cluster has audit logging enabled. It fails if the audit logging is not activated for the cluster. EKS control plane logging sends audit and diagnostic logs directly from the EKS control plane to Amazon CloudWatch Logs in your account. You can choose specific log types, and logs will be sent as log streams to a group for each EKS cluster within CloudWatch. Logging offers insight into the access and performance of EKS clusters. By routing EKS control plane logs for your clusters to CloudWatch Logs, you can centrally record operations for auditing and diagnostic purposes.

## Remediation{% #remediation %}

To enable audit logs for your EKS cluster, see [Enabling and disabling control plane logs in the Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html#enabling-control-plane-log-export).

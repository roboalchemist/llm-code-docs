# Source: https://docs.datadoghq.com/security/default_rules/def-000-c4m.md

---
title: EFS file systems should be in backup plans
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EFS file systems should be in backup
  plans
---

# EFS file systems should be in backup plans
 
## Description{% #description %}

This control verifies whether Amazon EFS file systems are incorporated into AWS Backup plans.

Ensuring EFS file systems are part of backup plans helps safeguard data against loss and accidental deletion. If a third party backup system is in operation, findings from this control can be muted.

## Remediation{% #remediation %}

To learn how to enable create a backup plan, see the [Create a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) section of the AWS Backup Developer Guide.

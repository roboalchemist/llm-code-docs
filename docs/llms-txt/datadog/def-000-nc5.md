# Source: https://docs.datadoghq.com/security/default_rules/def-000-nc5.md

---
title: Neptune DB clusters should have automated backups enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune DB clusters should have
  automated backups enabled
---

# Neptune DB clusters should have automated backups enabled
 
## Description{% #description %}

This control verifies whether automated backups are enabled for a Neptune DB cluster.

Automating backups enhances system resilience and enables quicker recovery from security incidents. By ensuring backups are in place for your Neptune DB clusters, you can restore your systems to a specific point in time, reducing both downtime and potential data loss.

## Remediation{% #remediation %}

For guidance on configuring automated backups, please refer to the [Overview of backing up and restoring a Neptune DB cluster](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-overview.html#backup-restore-overview-backups) section of the Neptune User Guide.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-m5w.md

---
title: Neptune DB cluster snapshots should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune DB cluster snapshots should be
  encrypted at rest
---

# Neptune DB cluster snapshots should be encrypted at rest
 
## Description{% #description %}

This control verifies whether a Neptune DB cluster snapshot is encrypted while stored.

Data at rest refers to information stored in persistent, non-volatile storage for any period of time. Encrypting data at rest helps protect its confidentiality, reducing the risk of unauthorized access. To enhance security, Neptune DB cluster snapshots should be encrypted while stored.

## Remediation{% #remediation %}

For guidance on securing snapshots, please refer to the [Creating a DB cluster snapshot in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-create-snapshot.html) section of the Neptune User Guide.

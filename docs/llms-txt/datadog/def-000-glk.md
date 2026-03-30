# Source: https://docs.datadoghq.com/security/default_rules/def-000-glk.md

---
title: Neptune DB cluster snapshots should not be public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune DB cluster snapshots should not
  be public
---

# Neptune DB cluster snapshots should not be public

## Description{% #description %}

This control ensures that a Neptune manual DB cluster snapshot is not publicly accessible.

A Neptune DB cluster manual snapshot should remain private unless intentionally made public. When an unencrypted manual snapshot is shared publicly, it becomes accessible to all AWS accounts, which could lead to unintentional data exposure.

## Remediation{% #remediation %}

For guidance on sharing snapshots securely, please refer to the [Sharing a DB cluster snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-share-snapshot.html) section of the Neptune User Guide.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-jhj.md

---
title: Ensure /tmp Located On Separate Partition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure /tmp Located On Separate
  Partition
---

# Ensure /tmp Located On Separate Partition

## Description{% #description %}

The `/tmp` directory is a world-writable directory used for temporary file storage. Ensure it has its own partition or logical volume at installation time, or migrate it using LVM.

## Rationale{% #rationale %}

The `/tmp` partition is used as temporary storage by many programs. Placing `/tmp` in its own partition enables the setting of more restrictive mount options, which can help protect programs which use it.

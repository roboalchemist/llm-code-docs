# Source: https://docs.datadoghq.com/security/default_rules/def-000-a2x.md

---
title: FSx OpenZFS file systems should copy tags to backups and volumes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > FSx OpenZFS file systems should copy
  tags to backups and volumes
---

# FSx OpenZFS file systems should copy tags to backups and volumes

## Description{% #description %}

This control verifies whether an Amazon FSx for OpenZFS file system is set up to copy tags to its backups and volumes.

Maintaining an inventory and identifying your IT assets are key elements of effective governance and security. Tags enable you to categorize AWS resources by various criteria, such as purpose, ownership, or environment. This becomes especially useful when managing multiple resources of the same type, allowing you to quickly locate specific resources based on the tags assigned to them.

## Remediation{% #remediation %}

For guidance on configuring FSx for OpenZFS file systems to copy tags to backups and volumes, refer to the [Updating a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html) section of the Amazon FSx OpenZFS User Guide.

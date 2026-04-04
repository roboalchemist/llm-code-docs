# Source: https://docs.datadoghq.com/security/default_rules/def-000-qza.md

---
title: FSx Lustre file systems should copy tags to backups
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > FSx Lustre file systems should copy
  tags to backups
---

# FSx Lustre file systems should copy tags to backups

## Description{% #description %}

This control verifies whether an Amazon FSx for Lustre file system is set up to copy tags to its backups.

Maintaining an inventory and identifying your IT assets are key elements of effective governance and security. Tags enable you to categorize AWS resources by various criteria, such as purpose, ownership, or environment. This becomes especially useful when managing multiple resources of the same type, allowing you to quickly locate specific resources based on the tags assigned to them.

## Remediation{% #remediation %}

For guidance on configuring FSx for Lustre file systems to copy tags to backups, refer to the [fsx update-file-system](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/update-file-system.html) section of the AWS CLI Command Reference.

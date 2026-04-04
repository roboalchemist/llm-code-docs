# Source: https://docs.datadoghq.com/security/default_rules/def-000-hfj.md

---
title: Amazon Workspaces should enable volume encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon Workspaces should enable volume
  encryption
---

# Amazon Workspaces should enable volume encryption

## Description{% #description %}

Enable volume encryption for Amazon WorkSpaces to protect data at rest by encrypting both root and user volumes using AWS KMS keys.

## Remediation{% #remediation %}

Configure volume encryption when creating WorkSpaces and ensure both root and user volumes are encrypted using the Amazon WorkSpaces console or API. See [Data protection in Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html) for more detailed instructions.

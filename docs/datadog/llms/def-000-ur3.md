# Source: https://docs.datadoghq.com/security/default_rules/def-000-ur3.md

---
title: Backup recovery points should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Backup recovery points should be
  encrypted at rest
---

# Backup recovery points should be encrypted at rest

## Description{% #description %}

This control ensures that AWS Backup recovery points are encrypted at rest, passing only if encryption is enabled.

An AWS Backup recovery point is a saved snapshot of your data at a specific time. Encrypting these recovery points enhances security, guarding against unauthorized access.

## Remediation{% #remediation %}

For instructions on encrypting an AWS Backup recovery point, see [Encryption for backups in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html) in the AWS Backup Developer Guide.

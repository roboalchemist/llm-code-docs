# Source: https://docs.datadoghq.com/security/default_rules/def-000-efs.md

---
title: ECS task definitions should enable in transit encryption for EFS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS task definitions should enable in
  transit encryption for EFS
---

# ECS task definitions should enable in transit encryption for EFS

## Description{% #description %}

Amazon ECS task definitions that mount Amazon Elastic File System (EFS) volumes must enable in transit encryption to ensure data is encrypted between the ECS host and the EFS server. In transit encryption provides an additional layer of security by preventing unauthorized access to data as it moves across the network.

When in transit encryption is disabled (the default), data is transmitted in plaintext, making it vulnerable to interception and unauthorized access. This is particularly important when handling sensitive or regulated data.

## Remediation{% #remediation %}

Enable in transit encryption for all EFS volumes in your ECS task definitions by setting the `transitEncryption` parameter to `"ENABLED"` in the `efsVolumeConfiguration`. Refer to the [Amazon EFS encryption in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) documentation for configuration details.

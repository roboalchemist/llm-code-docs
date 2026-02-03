# Source: https://docs.datadoghq.com/security/default_rules/def-000-pf4.md

---
title: EBS default encryption should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EBS default encryption should be
  enabled
---

# EBS default encryption should be enabled
 
## Description{% #description %}

This rule evaluates whether encryption at the region level is enabled by default for Amazon Elastic Block Store (Amazon EBS).

Once enabled for a Region, encryption applies to all future volumes and snapshots within the region and cannot be disabled on an individual basis.

## Remediation{% #remediation %}

To enable default encryption for Amazon EBS volumes, follow the steps outlined in the [Encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html) section of the Amazon EC2 User Guide.

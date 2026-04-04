# Source: https://docs.datadoghq.com/security/default_rules/def-000-icw.md

---
title: ElastiCache Redis clusters should have auto minor version upgrades enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ElastiCache Redis clusters should have
  auto minor version upgrades enabled
---

# ElastiCache Redis clusters should have auto minor version upgrades enabled

## Description{% #description %}

This evaluation validates that ElastiCache for Redis automatically implements minor version upgrades for cache clusters. It will not pass if cache clusters do not have minor version upgrades applied automatically.

AutoMinorVersionUpgrade is a functionality in ElastiCache for Redis that can be enabled to automatically upgrade cache clusters when a new minor cache engine version becomes available. These upgrades may contain security patches and bug fixes, making it a best practice to stay current with patch installations for system security.

## Remediation{% #remediation %}

For instructions on how to implement automatic minor version upgrades for an existing ElastiCache for Redis cache cluster, refer to the [Upgrading engine versions](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/VersionManagement.html) section in the Amazon ElastiCache User Guide.

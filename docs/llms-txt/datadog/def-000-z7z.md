# Source: https://docs.datadoghq.com/security/default_rules/def-000-z7z.md

---
title: RDS clusters should have Auto Minor Version Upgrade enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS clusters should have Auto Minor
  Version Upgrade enabled
---

# RDS clusters should have Auto Minor Version Upgrade enabled
 
## Description{% #description %}

This check ensures that automatic minor version upgrades are enabled for an Amazon RDS database cluster. Enabling automatic minor version upgrades for RDS clusters ensures your DB cluster remains current, benefiting from new software features, bug fixes, security patches, and performance enhancements. Once enabled, any available minor version updates are automatically applied during the maintenance window, keeping the cluster and its instances up-to-date.

## Remediation{% #remediation %}

To activate automatic minor version upgrades on Multi-AZ DB clusters, refer to the [Modifying a Multi-AZ DB Cluster section in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/modify-multi-az-db-cluster.html).

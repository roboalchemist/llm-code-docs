# Source: https://docs.datadoghq.com/security/default_rules/def-000-2za.md

---
title: RDS databases should have 'Auto Minor Version Upgrade' enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS databases should have 'Auto Minor
  Version Upgrade' enabled
---

# RDS databases should have 'Auto Minor Version Upgrade' enabled
 
## Description{% #description %}

Ensuring that RDS database instances have the Auto Minor Version Upgrade flag enabled allows the instances to automatically receive minor engine upgrades, which include features, bug fixes, and security patches during the specified maintenance window. AWS RDS occasionally deprecates minor engine versions and introduces new ones. By having the Auto Minor Version Upgrade feature enabled, these upgrades occur seamlessly during the specified maintenance window, maintaining database performance and security with minimal administrative intervention.

## Remediation{% #remediation %}

For instructions on enabling Auto Minor Version Upgrade for RDS instances, refer to [Managing an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_RDS_Managing.html).

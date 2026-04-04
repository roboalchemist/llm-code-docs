# Source: https://docs.datadoghq.com/security/default_rules/def-000-1do.md

---
title: RDS instances should have IAM authentication enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instances should have IAM
  authentication enabled
---

# RDS instances should have IAM authentication enabled

## Description{% #description %}

This control checks if an RDS instance has IAM database authentication enabled. The control specifically evaluates RDS instances using the following engine types: `mysql`, `postgres`, `aurora`, `aurora-mysql`, `aurora-postgresql`, and `mariadb`. Additionally, an RDS instance must be in one of these states for a finding to be generated: `available`, `backing-up`, `storage-optimization`, or `storage-full`.

IAM database authentication allows users to authenticate to database instances using an authentication token instead of a password. This mechanism ensures that network traffic to and from the database is encrypted using SSL. For more details, see the [IAM database authentication section in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html).

## Remediation{% #remediation %}

To enable IAM database authentication on RDS instances, see [Enabling and disabling IAM database authentication in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html).

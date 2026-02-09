# Source: https://docs.datadoghq.com/security/default_rules/def-000-m2a.md

---
title: Aurora clusters should have backtracking enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Aurora clusters should have
  backtracking enabled
---

# Aurora clusters should have backtracking enabled
 
## Description{% #description %}

This control verifies backtracking is enabled for an Amazon Aurora cluster. Backups are critical for rapid recovery from security incidents and enhance the resilience of your systems. Aurora backtracking reduces the time needed to revert a database to a previous point in time without necessitating a full database restore.

## Remediation{% #remediation %}

To enable Aurora backtracking, refer to the [Configuring backtracking section in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html).

Please note that it is not possible to enable backtracking on an existing cluster. To accomplish this you will need to create a clone of the cluster with backtracking enabled. For more information on Aurora backtracking, see the [Overview of backtracking section in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Enabling.html).

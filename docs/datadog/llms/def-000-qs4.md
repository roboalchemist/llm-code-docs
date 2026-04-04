# Source: https://docs.datadoghq.com/security/default_rules/def-000-qs4.md

---
title: Redshift clusters should have automatic snapshots enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift clusters should have automatic
  snapshots enabled
---

# Redshift clusters should have automatic snapshots enabled

## Description{% #description %}

This control verifies if automated snapshots are enabled for an Amazon Redshift cluster.

Having backups allows for faster recovery in the event of a security incident and enhances the resilience of your systems. By default, Amazon Redshift creates periodic snapshots. This control ensures that automatic snapshots are activated.

## Remediation{% #remediation %}

For guidance on configuring automatic upgrades, please refer to the [Modifying a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#modify-cluster) section of the Amazon Redshift Management Guide.

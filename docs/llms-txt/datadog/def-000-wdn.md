# Source: https://docs.datadoghq.com/security/default_rules/def-000-wdn.md

---
title: RDS clusters should be configured to use multiple Availability Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS clusters should be configured to
  use multiple Availability Zones
---

# RDS clusters should be configured to use multiple Availability Zones

## Description{% #description %}

This control ensures high availability is enabled for your RDS clusters. The control will fail if an RDS cluster is not deployed across multiple Availability Zones (AZs). RDS clusters should be configured to span multiple AZs to guarantee the availability of stored data. Deploying across multiple AZs provides automated failover capabilities in the event of an AZ availability issue and during regular RDS maintenance events.

## Remediation{% #remediation %}

To information on deploying your DB clusters across multiple Availability Zones, refer to the [Modifying a DB instance to be a Multi-AZ DB instance deployment section in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html#Concepts.MultiAZ.Migrating). For an Aurora global database refer to [Adding Aurora Replicas to a DB cluster in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.html).

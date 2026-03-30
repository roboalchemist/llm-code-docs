# Source: https://docs.datadoghq.com/security/default_rules/def-000-0ld.md

---
title: >-
  DMS replication instances should be configured to use multiple Availability
  Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DMS replication instances should be
  configured to use multiple Availability Zones
---

# DMS replication instances should be configured to use multiple Availability Zones

## Description{% #description %}

AWS Database Migration Service (DMS) replication instances should be configured to use multiple Availability Zones (Multi-AZ deployment) for high availability and resilience. In a Multi-AZ deployment, AWS DMS automatically provisions and maintains a standby replica of a replication instance in a different Availability Zone. The primary replication instance is synchronously replicated to the standby replica, ensuring minimal interruption if the primary instance fails or becomes unresponsive.

## Remediation{% #remediation %}

Configure Multi-AZ deployment for your DMS replication instance by setting the Multi-AZ parameter to `true`. After creating a replication instance, you can modify the Multi-AZ deployment setting. For guidance on changing this setting for an existing replication instance, refer to the [Modifying a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Modifying.html) section of the AWS Database Migration Service User Guide.

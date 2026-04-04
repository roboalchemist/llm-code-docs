# Source: https://docs.datadoghq.com/security/default_rules/def-000-cy0.md

---
title: ElastiCache Redis replication groups should have automatic failover enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ElastiCache Redis replication groups
  should have automatic failover enabled
---

# ElastiCache Redis replication groups should have automatic failover enabled

## Description{% #description %}

Enable automatic failover for your ElastiCache for Redis replication groups

When automatic failover is enabled for a replication group, the primary node's role automatically switches to one of the read replicas. This transition and promotion of the replica ensures that writing to the new primary can resume once the promotion is complete, thereby minimizing overall downtime in the event of a failure.

## Remediation{% #remediation %}

Follow the [Modifying an ElastiCache cluster](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Clusters.Modify.html) docs to learn how to enable automatic failover for your ElastiCache for Redis replication groups.

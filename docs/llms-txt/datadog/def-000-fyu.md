# Source: https://docs.datadoghq.com/security/default_rules/def-000-fyu.md

---
title: ElastiCache Redis clusters should be configured for automatic backup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ElastiCache Redis clusters should be
  configured for automatic backup
---

# ElastiCache Redis clusters should be configured for automatic backup

## Description{% #description %}

This check assesses if an Amazon ElastiCache for Redis cluster has automatic backups scheduled. It will not pass if the SnapshotRetentionLimit for the Redis cluster or replication group is disabled, indicated by a value of 0.

Amazon ElastiCache for Redis clusters have the ability to create backups of their data. These backups can be used to restore a cluster or initialize a new one. Backups contain the cluster's metadata and all of the data within the cluster, and are stored in Amazon Simple Storage Service (Amazon S3) for durability. To restore data, a new Redis cluster can be created and populated with data from a backup. Backup management can be done through the AWS Management Console, AWS Command Line Interface (AWS CLI), and the ElastiCache API.

If this check passes, but the `elasticache` `snapshot_retention_limit` is `0`, it is likely that the `snapshot_retention_limit` is configurated to a `pass` condition in the `aws_elasticache_replication_group`. This configuration can be viewed using `Infrastructure` > `Inventories SQL`.

## Remediation{% #remediation %}

For instructions on setting up automatic backups for an ElastiCache for Redis cluster, refer to the [Scheduling automatic backups](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups-automatic.html) section in the Amazon ElastiCache User Guide.

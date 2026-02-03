# Source: https://docs.datadoghq.com/security/default_rules/9cq-130-xdk.md

---
title: ElastiCache clusters should use the latest engine version available
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ElastiCache clusters should use the
  latest engine version available
---

# ElastiCache clusters should use the latest engine version available
 
## Description{% #description %}

Ensure that your Amazon ElastiCache cluster is running the latest stable version of the Redis, Memcached, or Valkey cache engine. Upgrading to the latest version provides access to essential security patches, bug fixes, enhanced performance, and improved memory management, helping to maintain the reliability and security of your caching infrastructure.

## Remediation{% #remediation %}

To upgrade your ElastiCache cluster or replication group to the latest engine version, please refer to the [Upgrading Engine Versions](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/VersionManagement.html) documentation. This guide provides step-by-step instructions for modifying your cluster settings through the AWS Management Console, ensuring a smooth transition to the updated version.

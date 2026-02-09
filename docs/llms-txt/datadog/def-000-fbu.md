# Source: https://docs.datadoghq.com/security/default_rules/def-000-fbu.md

---
title: ElastiCache Redis clusters before version 6.0 should use Redis AUTH
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ElastiCache Redis clusters before
  version 6.0 should use Redis AUTH
---

# ElastiCache Redis clusters before version 6.0 should use Redis AUTH
 
## Description{% #description %}

ElastiCache for Redis clusters before version 6.0 should use Redis AUTH

When using Redis authentication tokens or passwords, clients must provide a password before executing commands, enhancing data security. For Redis 6.0 and later, it is recommended to use Role-Based Access Control (RBAC). Since RBAC is not available in versions earlier than 6.0, this guideline only applies to those versions that cannot utilize the RBAC feature.

## Remediation{% #remediation %}

Follow the [Authenticating with the Redis OSS AUTH command](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/auth.html) documentation to learn how to enable Redis AUTH.

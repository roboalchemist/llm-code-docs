# Source: https://docs.datadoghq.com/security/default_rules/def-000-rvk.md

---
title: RDS instances should be configured to use a custom administrator name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instances should be configured to
  use a custom administrator name
---

# RDS instances should be configured to use a custom administrator name

## Description{% #description %}

This check determines if the admin username for an Amazon RDS database instance has been altered from its default setting. It's essential to assign a distinct admin username when setting up an Amazon RDS database as default usernames are widely known, this minimizes the risk of unauthorized access.

note: this check excludes Neptune and DocumentDB Databases

## Remediation{% #remediation %}

To update the admin username for an Amazon RDS database instance, initiate the [creation of a new RDS database instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html) and assign a unique admin username during the setup process.

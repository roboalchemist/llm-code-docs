# Source: https://docs.datadoghq.com/security/default_rules/def-000-imu.md

---
title: RDS cluster replicates to a publicly accessible RDS instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS cluster replicates to a publicly
  accessible RDS instance
---

# RDS cluster replicates to a publicly accessible RDS instance

## Description{% #description %}

A private RDS cluster replicating to a publicly accessible RDS read replica instance increases the likelihood of unauthorized data access. If the public RDS read replica instance is accessed, it could lead to unauthorized data access or destruction of sensitive information replicated from the private RDS cluster.

## Remediation{% #remediation %}

1. Modify the database instance to disable public accessibility. Review [Hiding a DB instance in a VPC from the internet](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.HidingInstance) for more information on how to disable public accessibility.

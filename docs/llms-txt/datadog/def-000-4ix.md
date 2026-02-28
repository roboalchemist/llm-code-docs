# Source: https://docs.datadoghq.com/security/default_rules/def-000-4ix.md

---
title: Redshift clusters should use enhanced VPC routing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift clusters should use enhanced
  VPC routing
---

# Redshift clusters should use enhanced VPC routing

## Description{% #description %}

This control verifies if an Amazon Redshift cluster has Enhanced VPC Routing activated.

With Enhanced VPC Routing, all `COPY` and `UNLOAD` operations between the cluster and external data repositories are routed through your VPC. This allows you to leverage VPC features like security groups and network access control lists (ACLs) to secure network traffic. Additionally, you can monitor this traffic using VPC Flow Logs.

## Remediation{% #remediation %}

For guidance on enabling Redshift enhanced VPC routing, please refer to the [Enabling enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-enabling-cluster.html) section of the Amazon Redshift Management Guide.

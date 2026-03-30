# Source: https://docs.datadoghq.com/security/default_rules/def-000-5zp.md

---
title: Classic Load Balancers should span multiple Availability Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Classic Load Balancers should span
  multiple Availability Zones
---

# Classic Load Balancers should span multiple Availability Zones

## Description{% #description %}

This check ensures Classic Load Balancers are configured to operate across at least two Availability Zones (AZs). Load balancers can be set up to distribute traffic across Amazon EC2 instances within either a single Availability Zone or multiple Availability Zones. If a load balancer is not configured to span multiple Availability Zones, it cannot redirect traffic to targets in a different Availability Zone if the sole configured AZ becomes unavailable.

## Remediation{% #remediation %}

To add Availability Zones to a Classic Load Balancer, see [Add or remove subnets for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html).

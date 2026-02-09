# Source: https://docs.datadoghq.com/security/default_rules/def-000-1zq.md

---
title: Load Balancers should span multiple Availability Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Load Balancers should span multiple
  Availability Zones
---

# Load Balancers should span multiple Availability Zones
 
## Description{% #description %}

This check assesses whether load balancers (Application, Network, or Gateway) are configured to operate across at least two Availability Zones (AZs). Load balancers can be set up to distribute traffic across Amazon EC2 instances within either a single Availability Zone or multiple Availability Zones. If a load balancer is not configured to span multiple Availability Zones, it cannot redirect traffic to targets in a different Availability Zone if the sole configured AZ becomes unavailable.

## Remediation{% #remediation %}

To add an Availability Zone to an Application Load Balancer, see [Availability Zones for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html). To add an Availability Zone to a Network Load Balancer, see [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#availability-zones). To add an Availability Zone to a Gateway Load Balancer, see [Create a Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-load-balancer.html).

# Source: https://docs.datadoghq.com/security/default_rules/def-000-g2d.md

---
title: Classic Load Balancers should be configured to use Connection Draining
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Classic Load Balancers should be
  configured to use Connection Draining
---

# Classic Load Balancers should be configured to use Connection Draining

## Description{% #description %}

This control verifies connection draining is enabled for Classic Load Balancers. Enabling connection draining ensures that the load balancer stops routing new requests to instances that are being de-registered or identified as unhealthy, while still allowing existing connections to complete. This feature is especially beneficial for instances within Auto Scaling groups, as it helps prevent abrupt disconnection of active sessions.

## Remediation{% #remediation %}

To enable connection draining on Classic Load Balancers, refer to [Configure Connection Draining for Your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html).

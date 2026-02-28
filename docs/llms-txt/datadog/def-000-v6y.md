# Source: https://docs.datadoghq.com/security/default_rules/def-000-v6y.md

---
title: Application Load Balancers should have deletion protection enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Application Load Balancers should have
  deletion protection enabled
---

# Application Load Balancers should have deletion protection enabled

## Description{% #description %}

This control verifies deletion protection is enabled for Application, Gateway, and Network Load Balancers. To safeguard your Load Balancer from accidental or unauthorized deletion, ensure that deletion protection is enabled.

## Remediation{% #remediation %}

To safeguard your load balancer from accidental deletion, you can activate deletion protection. By default, this feature is turned off for your load balancer.

If deletion protection is enabled, it must be disabled before you can delete the load balancer.

- To enable deletion protection on an Application Load Balancer, refer to the [Deletion Protection](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#deletion-protection) section in the user guide for Application Load Balancers.
- For a Gateway Load Balancer, consult the [Deletion Protection][2] section in the user guide for Gateway Load Balancers.
- For a Network Load Balancer, see the [Deletion Protection][3] section in the user guide for Network Load Balancers.

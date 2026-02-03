# Source: https://docs.datadoghq.com/security/default_rules/def-000-rp8.md

---
title: >-
  Auto Scaling groups associated with a Classic Load Balancer should use ELB
  health checks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Auto Scaling groups associated with a
  Classic Load Balancer should use ELB health checks
---

# Auto Scaling groups associated with a Classic Load Balancer should use ELB health checks
 
## Description{% #description %}

This check verifies if Auto Scaling groups linked to a Classic Load Balancer are using health checks from Elastic Load Balancing (ELB).

The check confirms that the group evaluates the health of its instances using the extended checks available via the load balancer. Employing ELB health checks, rather than EC2, on Classic Load Balancers, can enhance the reliability of applications deployed with EC2 Auto Scaling groups.

## Remediation{% #remediation %}

For instructions on implementing Elastic Load Balancing health checks, refer to the [Add Elastic Load Balancing health checks section in the Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html#as-add-elb-healthcheck-console).

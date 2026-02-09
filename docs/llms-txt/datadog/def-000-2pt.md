# Source: https://docs.datadoghq.com/security/default_rules/def-000-2pt.md

---
title: EC2 Auto Scaling group should use multiple Availability Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 Auto Scaling group should use
  multiple Availability Zones
---

# EC2 Auto Scaling group should use multiple Availability Zones
 
## Description{% #description %}

This check verifies if an Amazon EC2 Auto Scaling group extends across a minimum of two Availability Zones (AZs). Allowed values range from 2 to 6 AZs.

An Auto Scaling group limited to one AZ is not able to initiate instances in a different AZ should the active AZ go down. However, there are scenarios, such as batch processing or situations where minimizing inter-AZ data transfer costs is crucial, and having an Auto Scaling group in a single AZ might be beneficial. In these instances, the check can be turned off or its alerts can be ignored.

## Remediation{% #remediation %}

For instructions on adding AZs to an existing Auto Scaling group, refer to the section on adding and removing Availability Zones in the [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html).

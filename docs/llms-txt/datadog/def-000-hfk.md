# Source: https://docs.datadoghq.com/security/default_rules/def-000-hfk.md

---
title: EC2 Auto Scaling groups should use Amazon EC2 launch templates
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 Auto Scaling groups should use
  Amazon EC2 launch templates
---

# EC2 Auto Scaling groups should use Amazon EC2 launch templates
 
## Description{% #description %}

This check verifies if an Amazon EC2 Auto Scaling group is established using an EC2 launch template. The check does not pass if the Auto Scaling group is created without a launch template, or if a launch template is absent in a mixed instances policy.

An EC2 Auto Scaling group can be formed using either an EC2 launch template or a launch configuration. Opting for a launch template when creating an Auto Scaling group guarantees access to the latest features and enhancements.

## Remediation{% #remediation %}

To establish an Auto Scaling group using an EC2 launch template, consult the section [Create an Auto Scaling group using a launch template in the Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-launch-template.html). Additionally, for details on substituting a launch configuration with a launch template, see [Replace a launch configuration with a launch template in the Amazon EC2 User Guide for Windows Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/migrate-to-launch-templates.html).

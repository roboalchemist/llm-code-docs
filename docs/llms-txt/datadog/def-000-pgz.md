# Source: https://docs.datadoghq.com/security/default_rules/def-000-pgz.md

---
title: >-
  Auto Scaling group launch configuration should configure EC2 instances to
  require IMDSv2
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Auto Scaling group launch configuration
  should configure EC2 instances to require IMDSv2
---

# Auto Scaling group launch configuration should configure EC2 instances to require IMDSv2

## Description{% #description %}

This control verifies if an Amazon EC2 Auto Scaling launch configuration has version 2 of the Instance Metadata Service (IMDS) enforced. The control fails if the `http_tokens` field in the `metadata_options` settings is not set to `required`.

IMDSv2 introduces important additional security features that enhance the protection of your EC2 instances compared to IMDSv1.

## Remediation{% #remediation %}

For guidance on creating secure Auto Scaling launch configurations, refer to the [Configure the instance metadata options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html) section of the Amazon EC2 Auto Scaling User Guide.

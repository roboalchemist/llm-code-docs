# Source: https://docs.datadoghq.com/security/default_rules/def-000-8zx.md

---
title: ECS services should not have public IP addresses assigned
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS services should not have public IP
  addresses assigned
---

# ECS services should not have public IP addresses assigned
 
## Description{% #description %}

A public IP address is an IP address that can be accessed from the internet. When you configure your Amazon ECS instances with a public IP address, they become accessible from the internet. It is not recommended to make Amazon ECS services publicly available to avoid unauthorized access to your container application servers.

Note: This finding should be muted for resources intentionally configured to be publicly accessible.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

To disable automatic public IP assignment, see [To configure VPC and security group settings for your service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) in the Amazon Elastic Container Service Developer Guide.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-qc6.md

---
title: VPC Lambda functions should operate in multiple Availability Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPC Lambda functions should operate in
  multiple Availability Zones
---

# VPC Lambda functions should operate in multiple Availability Zones
 
## Description{% #description %}

This control verifies whether an AWS Lambda function that connects to a Virtual Private Cloud (VPC) is deployed across at least two Availability Zones (AZs). The control will fail if the function does not meet the the minimum of two AZs.

Distributing resources across multiple AZs follows AWS best practices to enhance system resilience and ensure high availability. High availability is essential for maintaining system functionality and is a fundamental aspect of the security principles of confidentiality, integrity, and availability. Lambda functions connected to a VPC should be configured for multi-AZ deployment to avoid service interruptions caused by a failure in a single zone.

## Remediation{% #remediation %}

For guidance on configuring Lambda function VPC settings, refer to the [Configuring VPC access](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html#vpc-configuring) section of the AWS Lambda Developer Guide

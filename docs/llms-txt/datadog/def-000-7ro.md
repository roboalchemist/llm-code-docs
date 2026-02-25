# Source: https://docs.datadoghq.com/security/default_rules/def-000-7ro.md

---
title: ECS clusters should have Container Insights enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > ECS clusters should have Container
  Insights enabled
---

# ECS clusters should have Container Insights enabled

## Description{% #description %}

This control verifies whether ECS clusters have Container Insights enabled.

Monitoring is essential for ensuring the reliability, availability, and performance of Amazon ECS clusters. Container Insights enables the collection, aggregation, and analysis of metrics and logs from containerized applications and microservices. CloudWatch automatically gathers key metrics such as CPU, memory, disk usage, and network activity. Additionally, Container Insights provides diagnostic data, like container restart failures, to aid in identifying and resolving issues efficiently.

## Remediation{% #remediation %}

For guidance on configuring ECS Container Insights, refer to the [Setting up Container Insights on Amazon ECS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html) section of the Amazon CloudWatch User Guide.

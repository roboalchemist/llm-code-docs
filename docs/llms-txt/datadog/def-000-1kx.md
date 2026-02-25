# Source: https://docs.datadoghq.com/security/default_rules/def-000-1kx.md

---
title: RDS logs should be collected and retained for no less than 90 days
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS logs should be collected and
  retained for no less than 90 days
---

# RDS logs should be collected and retained for no less than 90 days

## Description{% #description %}

RDS instances should have CloudWatch Logs exports enabled with log retention configured for no less than 90 days to ensure adequate log retention for security monitoring and compliance requirements.

## Remediation{% #remediation %}

Configure CloudWatch log retention for RDS log groups to retain logs for at least 90 days by setting the retention period on the corresponding CloudWatch log groups for each enabled log export type. Refer to [Logging and monitoring in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.LoggingAndMonitoring.html).

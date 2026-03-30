# Source: https://docs.datadoghq.com/security/default_rules/def-000-wwp.md

---
title: Athena workgroups should have logging enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Athena workgroups should have logging
  enabled
---

# Athena workgroups should have logging enabled

## Description{% #description %}

Amazon Athena workgroups should have logging enabled to track and monitor query activities. Logging provides audit records that help detect security breaches, investigate incidents, and comply with regulations. When enabled, Athena publishes query metrics to Amazon CloudWatch, enhancing accountability and transparency of query operations within the workgroup.

## Remediation{% #remediation %}

Enable CloudWatch query metrics for your Athena workgroup by setting the `PublishCloudWatchMetricsEnabled` parameter to `true` in the workgroup configuration. For guidance on enabling logging for an Athena workgroup, refer to the [Enable CloudWatch query metrics in Athena](https://docs.aws.amazon.com/athena/latest/ug/workgroups-cloudwatch-metrics.html) section of the Amazon Athena User Guide.

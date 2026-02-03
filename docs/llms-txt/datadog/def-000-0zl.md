# Source: https://docs.datadoghq.com/security/default_rules/def-000-0zl.md

---
title: Disabling or deletion of Customer-Managed Keys should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Disabling or deletion of
  Customer-Managed Keys should be monitored
---

# Disabling or deletion of Customer-Managed Keys should be monitored
 
## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for customer-created CMKs that change to a disabled or scheduled deletion state to ensure data accessibility.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for CMK state changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <disable_or_delete_cmk_changes_metric> --metric-transformations \
metricName=<disable_or_delete_cmk_changes_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{($.eventSource = kms.amazonaws.com) && (($.eventName=DisableKey)||($.eventName=ScheduleKeyDeletion))}'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

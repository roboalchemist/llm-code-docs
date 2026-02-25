# Source: https://docs.datadoghq.com/security/default_rules/def-000-4sx.md

---
title: AWS Management Console authentication failures should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Management Console authentication
  failures should be monitored
---

# AWS Management Console authentication failures should be monitored

## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for failed console authentication attempts to decrease the lead time in detecting brute force attempts and identify source IPs for event correlation.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for failed console authentication attempts, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <console_signin_failure_metric> --metric-transformations \
metricName=<console_signin_failure_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{ ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

# Source: https://docs.datadoghq.com/security/default_rules/def-000-m9s.md

---
title: Unauthorized API calls should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unauthorized API calls should be
  monitored
---

# Unauthorized API calls should be monitored

## Description{% #description %}

Real-time monitoring of API calls can be achieved by sending CloudTrail logs to CloudWatch Logs and establishing metric filters and alarms. It is recommended to set up a metric filter and alarm for detecting unauthorized API calls to enhance security awareness and reduce time in identifying potential malicious activity.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for unauthorized API calls, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <trail-log-group-name> \
--filter-name <unauthorized-api-calls-metric> --metric-transformations \
metricName=unauthorized_api_calls_metric,metricNamespace=CISBenchmark,metricValue=1 \
--filter-pattern "{ ($.errorCode =\"*UnauthorizedOperation\") || ($.errorCode =\"AccessDenied*\") && \
($.sourceIPAddress!=\"delivery.logs.amazonaws.com\") && \
($.eventName!=\"HeadBucket\") }"
```

*Note: You can choose your own `metricName` and `metricNamespace` strings. Using the same `metricNamespace` for all Foundations Benchmark metrics will group them together.*

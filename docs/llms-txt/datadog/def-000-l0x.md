# Source: https://docs.datadoghq.com/security/default_rules/def-000-l0x.md

---
title: '''root'' account access should be monitored'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'root' account access should be
  monitored
---

# 'root' account access should be monitored
 
## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for root login attempts to provide visibility into the use of the fully privileged root account and to reduce its usage.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for root login attempts, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <root_usage_metric> --metric-transformations \
metricName=<root_usage_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{ $.userIdentity.type = "Root" && $.userIdentity.invokedBy NOT EXISTS && \
$.eventType != "AwsServiceEvent" }'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

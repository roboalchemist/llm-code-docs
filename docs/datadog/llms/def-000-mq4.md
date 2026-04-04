# Source: https://docs.datadoghq.com/security/default_rules/def-000-mq4.md

---
title: AWS Config configuration changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Config configuration changes should
  be monitored
---

# AWS Config configuration changes should be monitored

## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for detecting changes to AWS Config to ensure sustained visibility of configuration items within the AWS account.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for AWS Config changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <aws_config_changes_metric> --metric-transformations \
metricName=<aws_config_changes_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{($.eventSource = config.amazonaws.com) && (($.eventName=StopConfigurationRecorder)||($.eventName=DeleteDeliveryChannel)||($.eventName=PutDeliveryChannel)||($.eventName=PutConfigurationRecorder))}'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

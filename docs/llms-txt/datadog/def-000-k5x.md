# Source: https://docs.datadoghq.com/security/default_rules/def-000-k5x.md

---
title: Network gateway changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network gateway changes should be
  monitored
---

# Network gateway changes should be monitored
 
## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing AWS CloudTrail logs to AWS CloudWatch logs and establishing corresponding metric filters and alarms. Network gateways are essential for sending and receiving traffic to destinations outside of a VPC. It is recommended to create a metric filter and alarm to monitor changes to network gateways to ensure that all ingress and egress traffic traverses the VPC border using a controlled path.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for network gateway changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <network_gw_changes_metric> --metric-transformations \
metricName=<network_gw_changes_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{($.eventName = CreateCustomerGateway) || ($.eventName = DeleteCustomerGateway) || \
($.eventName = AttachInternetGateway) || ($.eventName = CreateInternetGateway) || ($.eventName = DeleteInternetGateway) || \
($.eventName = DetachInternetGateway)}'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

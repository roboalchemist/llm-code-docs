# Source: https://docs.datadoghq.com/security/default_rules/def-000-i0x.md

---
title: Security group changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Security group changes should be
  monitored
---

# Security group changes should be monitored
 
## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. Security Groups are a stateful packet filter controlling ingress and egress traffic within a VPC. It is recommended to set up a metric filter and alarm for detecting changes to security groups to ensure resources and services are not unintentionally exposed.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for security group changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <security_group_changes_metric> --metric-transformations \
metricName=<security_group_changes_metric>,metricNamespace="CISBenchmark",metricValue=1 \
--filter-pattern '{($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || \
($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || \
($.eventName = DeleteSecurityGroup) }'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

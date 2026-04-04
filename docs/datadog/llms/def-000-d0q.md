# Source: https://docs.datadoghq.com/security/default_rules/def-000-d0q.md

---
title: Network ACL changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Network ACL changes should be monitored
---

# Network ACL changes should be monitored

## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. NACLs are used as a stateless packet filter to control ingress and egress traffic for subnets within a VPC. It is recommended to set up a metric filter and alarm for detecting changes made to NACLs to ensure AWS resources and services are not unintentionally exposed.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for NACL changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <nacl_changes_metric> --metric-transformations \
metricName=<nacl_changes_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{($.eventName = CreateNetworkAcl) || ($.eventName = CreateNetworkAclEntry) || \
($.eventName = DeleteNetworkAcl) || ($.eventName = DeleteNetworkAclEntry) || \
($.eventName = ReplaceNetworkAclEntry) || ($.eventName = ReplaceNetworkAclAssociation)}'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

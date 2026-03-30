# Source: https://docs.datadoghq.com/security/default_rules/def-000-bc0.md

---
title: S3 bucket policy changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket policy changes should be
  monitored
---

# S3 bucket policy changes should be monitored

## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for changes to S3 bucket policies to reduce the time to detect and correct permissive policies on sensitive S3 buckets.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for S3 bucket policy changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <s3_bucket_policy_changes_metric> --metric-transformations \
metricName=<s3_bucket_policy_changes_metric>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{($.eventSource = s3.amazonaws.com) && (($.eventName = PutBucketAcl) || \
($.eventName = PutBucketPolicy) || ($.eventName = PutBucketCors) || ($.eventName = PutBucketLifecycle) || \
($.eventName = PutBucketReplication) || ($.eventName = DeleteBucketPolicy) || ($.eventName = DeleteBucketCors) || \
($.eventName = DeleteBucketLifecycle) || ($.eventName = DeleteBucketReplication))}'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

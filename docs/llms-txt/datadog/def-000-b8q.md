# Source: https://docs.datadoghq.com/security/default_rules/def-000-b8q.md

---
title: AWS Management Console sign-ins without MFA should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Management Console sign-ins without
  MFA should be monitored
---

# AWS Management Console sign-ins without MFA should be monitored
 
## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for console logins not protected by multi-factor authentication (MFA) to increase visibility into potentially at-risk accounts.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for logins without MFA, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter \
    --log-group-name <cloudtrail_log_group_name> \
    --filter-name <no_mfa_console_signin_metric> \
    --metric-transformations metricName=<no_mfa_console_signin_metric>,metricNamespace=CISBenchmark,metricValue=1 \
    --filter-pattern '{ ($.eventName = "ConsoleLogin") && ($.additionalEventData.MFAUsed != "Yes") && \
    ($.userIdentity.type = "IAMUser") && ($.responseElements.ConsoleLogin = "Success") }'
```

```plaintext
aws cloudwatch put-metric-alarm \
    --alarm-name <no_mfa_console_signin_alarm> \
    --metric-name <no_mfa_console_signin_metric> \
    --namespace "CISBenchmark" \
    --statistic "Sum" \
    --period 300 \
    --threshold 1 \
    --evaluation-periods 1 \
    --comparison-operator GreaterThanOrEqualToThreshold \
    --alarm-actions <sns_topic_arn>
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

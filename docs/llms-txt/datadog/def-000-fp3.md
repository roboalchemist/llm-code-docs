# Source: https://docs.datadoghq.com/security/default_rules/def-000-fp3.md

---
title: AWS Organizations changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Organizations changes should be
  monitored
---

# AWS Organizations changes should be monitored

## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. It is recommended to set up a metric filter and alarm for AWS organization changes made in the master AWS Account. This helps prevent any unwanted modifications that may lead to unauthorized access or other security breaches, ensuring that unexpected changes can be investigated and rolled back.

## Remediation{% #remediation %}

For instructions on setting up CloudWatch metric filters and alarms for AWS organization changes, refer to the [AWS CloudWatch Alarms for CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html).

```plaintext
aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> \
--filter-name <organizations_changes> --metric-transformations \
metricName=<organizations_changes>,metricNamespace='CISBenchmark',metricValue=1 \
--filter-pattern '{ ($.eventSource = organizations.amazonaws.com) && (($.eventName = "AcceptHandshake") || \
($.eventName = "AttachPolicy") || ($.eventName = "CreateAccount") || ($.eventName = "CreateOrganizationalUnit") || \
($.eventName = "CreatePolicy") || ($.eventName = "DeclineHandshake") || ($.eventName = "DeleteOrganization") || \
($.eventName = "DeleteOrganizationalUnit") || ($.eventName = "DeletePolicy") || ($.eventName = "DetachPolicy") || \
($.eventName = "DisablePolicyType") || ($.eventName = "EnablePolicyType") || ($.eventName = "InviteAccountToOrganization") || \
($.eventName = "LeaveOrganization") || ($.eventName = "MoveAccount") || ($.eventName = "RemoveAccountFromOrganization") || \
($.eventName = "UpdatePolicy") || ($.eventName = "UpdateOrganizationalUnit")) }'
```

You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

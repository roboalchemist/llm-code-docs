# Source: https://docs.datadoghq.com/security/default_rules/def-000-j0s.md

---
title: Route table changes should be monitored
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Route table changes should be monitored
---

# Route table changes should be monitored
 
## Description{% #description %}

Real-time monitoring of API calls can be achieved by directing CloudTrail logs to CloudWatch logs and establishing corresponding metric filters and alarms. Routing tables are used to route network traffic between subnets and to network gateways. It is recommended that a metric filter and alarm be established for changes to route tables.

## Rationale{% #rationale %}

Monitoring changes to route tables help ensure that all VPC traffic flows through an expected path.

## Remediation{% #remediation %}

Perform the following to set up the metric filter, alarm, SNS topic, and subscription:

### From the command line{% #from-the-command-line %}

1. Retrieve cloudtrail log group name

   ```
   aws cloudtrail describe-trails
   ```

1. Create a metric filter based on the filter pattern provided, which checks for IAM policy changes and the `<cloudtrail_log_group_name>`.

   ```
   aws logs put-metric-filter --log-group-name <cloudtrail_log_group_name> --filter-name `<route_table_changes_metric>` --metric-transformations metricName= `<route_table_changes_metric>`,metricNamespace='CISBenchmark',metricValue=1 --filter-pattern '{($.eventName = CreateRoute) || ($.eventName = CreateRouteTable) || ($.eventName = ReplaceRoute) || ($.eventName = ReplaceRouteTableAssociation) || ($.eventName = DeleteRouteTable) || ($.eventName = DeleteRoute) || ($.eventName = DisassociateRouteTable)}'
   ```

   - Ensure CloudTrail is set to `multi-region` and `isLogging` is set `True`.
   - Ensure there is at least one Event Selector with `IncludeManagementEvents` set to `True` and `ReadWriteType` set to `All`.

**Note**: You can choose your own `metricName` and `metricNamespace` strings. Use the same `metricNamespace` for all Foundations Benchmark metrics to group them together.

1. Create an SNS topic that the alarm notifies.

   ```
   aws sns create-topic --name <sns_topic_name>
   ```

**Note**: You can execute this command once and then re-use the same topic for all monitoring alarms.

1. Create an SNS subscription to the topic created in step 2.

   ```
   aws sns subscribe --topic-arn <sns_topic_arn> --protocol <protocol_for_sns> --notification-endpoint <sns_subscription_endpoints>
   ```

**Note**: You can execute this command once and then re-use the SNS subscription for all monitoring alarms.

1. Create an alarm that is associated with the CloudWatch Logs metric filter created in step 1 and the SNS topic created in step 2.

   ```
   aws cloudwatch put-metric-alarm --alarm-name `<route_table_changes_alarm>` --metric-name `<route_table_changes_metric>` --statistic Sum --period 300 --threshold 1 --comparison-operator GreaterThanOrEqualToThreshold --evaluation-periods 1 --namespace 'CISBenchmark' --alarm-actions<sns_topic_arn>
   ```

## References{% #references %}

1. [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html)
1. [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html)
1. [https://docs.aws.amazon.com/sns/latest/dg/SubscribeTopic.html](https://docs.aws.amazon.com/sns/latest/dg/SubscribeTopic.html)

## Additional information{% #additional-information %}

Configuring log metric filters and alarms on multi-region (global) CloudTrail logs provides the following benefits:

- Ensures that activities from all regions (used as well as unused) are monitored.
- Ensures that activities on all supported global services are monitored.
- Ensures that all management events across all regions are monitored.

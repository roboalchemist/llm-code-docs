# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudwatch_aws_config_configuration_changes_alarm_missing.md

---
title: CloudWatch AWS Config configuration changes alarm missing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudWatch AWS Config configuration changes
  alarm missing
---

# CloudWatch AWS Config configuration changes alarm missing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5b8d7527-de8e-4114-b9dd-9d988f1f418f`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_metric_filter#pattern)

### Description{% #description %}

A log metric filter and alarm should be configured in AWS CloudWatch to detect changes to AWS Config settings, such as stopping the configuration recorder or modifying delivery channels. Without properly linking the `aws_cloudwatch_log_metric_filter` and the `aws_cloudwatch_metric_alarm`âfor example, by incorrectly setting the `metric_name` in the alarmâthe system may fail to alert administrators to unauthorized or unintended configuration changes. This could result in undetected activity that undermines compliance or security auditing, potentially exposing the environment to security risks.

A secure Terraform configuration should reference the correct filter name in the alarm, as shown below:

```
resource "aws_cloudwatch_metric_alarm" "CIS_AWS_Config_Change_CW_Alarm" {
  alarm_name          = "CIS-3.9-AWSConfigChanges"
  metric_name         = aws_cloudwatch_log_metric_filter.CIS_AWS_Config_Change_Metric_Filter.id
  namespace           = "CIS_Metric_Alarm_Namespace"
  // ...other configuration...
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_AWS_Config_Change_Metric_Filter" {
  name           = "CIS-AWSConfigChanges"
  pattern        = "{ ($.eventSource = \"config.amazonaws.com\") && (($.eventName=StopConfigurationRecorder)||($.eventName=DeleteDeliveryChannel)||($.eventName=PutDeliveryChannel)||($.eventName=PutConfigurationRecorder)) }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-AWSConfigChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_AWS_Config_Change_CW_Alarm" {
  alarm_name                = "CIS-3.9-AWSConfigChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.CIS_AWS_Config_Change_Metric_Filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to AWS Config configuration will help ensure sustained visibility of configuration items within the AWS account."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_cloudwatch_log_metric_filter" "cis_no_mfa_console_signin_metric_filter" {
  name           = "CIS-ConsoleSigninWithoutMFA"
  pattern        = "{ ($.eventName = \"ConsoleLogin\") && ($.additionalEventData.MFAUsed != \"Yes\") }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-ConsoleSigninWithoutMFA"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "cis_no_mfa_console_signin_cw_alarm" {
  alarm_name                = "CIS-3.2-ConsoleSigninWithoutMFA"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.cis_no_mfa_console_signin_metric_filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring for single-factor console logins will increase visibility into accounts that are not protected by MFA."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_AWS_Config_Change_Metric_Filter" {
  name           = "CIS-AWSConfigChanges"
  pattern        = "{ ($.eventSource = \"config.amazonaws.com\") && (($.eventName=StopConfigurationRecorder)||($.eventName=PutDeliveryChannel)||($.eventName=PutConfigurationRecorder)) }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-AWSConfigChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_AWS_Config_Change_CW_Alarm" {
  alarm_name                = "CIS-3.9-AWSConfigChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = "XXXX NOT YOUR FILTER XXXX"
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to AWS Config configuration will help ensure sustained visibility of configuration items within the AWS account."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_AWS_Config_Change_Metric_Filter" {
  name           = "CIS-AWSConfigChanges"
  pattern        = "{ ($.eventSource = \"config.amazonaws.com\") || (($.eventName=StopConfigurationRecorder)||($.eventName=DeleteDeliveryChannel)||($.eventName=PutDeliveryChannel)||($.eventName=PutConfigurationRecorder)) }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-AWSConfigChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_AWS_Config_Change_CW_Alarm" {
  alarm_name                = "CIS-3.9-AWSConfigChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = "XXXX NOT YOUR FILTER XXXX"
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to AWS Config configuration will help ensure sustained visibility of configuration items within the AWS account."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

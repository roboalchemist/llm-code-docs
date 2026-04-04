# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudwatch_unauthorized_access_defined_alarm_missing.md

---
title: CloudWatch unauthorized access alarm missing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudWatch unauthorized access alarm missing
---

# CloudWatch unauthorized access alarm missing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4c18a45b-4ab1-4790-9f83-399ac695f1e5`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Critical

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_metric_filter#pattern)

### Description{% #description %}

This check validates that a CloudWatch metric alarm is properly configured to monitor unauthorized API calls, which could indicate potential security breaches or application errors. A properly configured alarm requires the `metric_name` to correctly reference the corresponding metric filter ID. When this reference is incorrect (for example, using a placeholder such as 'XXXX NOT YOUR FILTER XXXX' instead of the actual metric filter ID), the alarm will not trigger when unauthorized access attempts occur, leaving your AWS infrastructure vulnerable to undetected attacks.

To fix this issue, ensure the metric_name references the correct metric filter ID, as shown in this example:

```
metric_name = aws_cloudwatch_log_metric_filter.cis_unauthorized_api_calls_metric_filter.id
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_cloudwatch_metric_alarm" "cis_unauthorized_api_calls_cw_alarm" {
  alarm_name                = "CIS-3.1-UnauthorizedAPICalls"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.cis_unauthorized_api_calls_metric_filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring unauthorized API calls will help reveal application errors and may reduce time to detect malicious activity."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}

resource "aws_cloudwatch_log_metric_filter" "cis_unauthorized_api_calls_metric_filter" {
  name           = "CIS-UnauthorizedAPICalls"
  pattern        = "{ ($.errorCode = \"*UnauthorizedOperation\") || ($.errorCode = \"AccessDenied*\") }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-UnauthorizedAPICalls"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}

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
  alarm_actions             = ["aws_sns_topic.CIS_Alerts_SNS_Topic.arn"]
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
resource "aws_cloudwatch_metric_alarm" "cis_unauthorized_api_calls_cw_alarm" {
  alarm_name                = "CIS-3.1-UnauthorizedAPICalls"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.cis_unauthorized_api_calls_metric_filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring unauthorized API calls will help reveal application errors and may reduce time to detect malicious activity."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}

resource "aws_cloudwatch_log_metric_filter" "cis_unauthorized_api_calls_metric_filter" {
  name           = "CIS-UnauthorizedAPICalls"
  pattern        = "{ $.errorCode = \"AccessDenied*\" }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-UnauthorizedAPICalls"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
```

```terraform
resource "aws_cloudwatch_metric_alarm" "cis_unauthorized_api_calls_cw_alarm" {
  alarm_name                = "CIS-3.1-UnauthorizedAPICalls"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.cis_unauthorized_api_calls_metric_filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring unauthorized API calls will help reveal application errors and may reduce time to detect malicious activity."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}

resource "aws_cloudwatch_log_metric_filter" "cis_unauthorized_api_calls_metric_filter" {
  name           = "CIS-UnauthorizedAPICalls"
  pattern        = "{ ($.errorCode = \"*UnauthorizedOperation\") && ($.errorCode = \"AccessDenied*\") }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-UnauthorizedAPICalls"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
```

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudwatch_security_group_changes_alarm_missing.md

---
title: Cloudwatch security group changes alarm missing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloudwatch security group changes alarm
  missing
---

# Cloudwatch security group changes alarm missing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4beaf898-9f8b-4237-89e2-5ffdc7ee6006`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_metric_filter#pattern)

### Description{% #description %}

This check ensures that log metric filters and corresponding alarms are configured to monitor changes to AWS security groups. Without a properly configured alarm referencing the correct log metric filter, security group changesâsuch as modifications to ingress or egress rules, or the creation and deletion of security groupsâmay go undetected. This lack of visibility can allow unauthorized or accidental changes that could expose sensitive resources or weaken the security posture of your environment. If left unaddressed, such misconfigurations could result in delayed detection of security incidents, increasing the potential for data breaches or service compromise.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_Security_Group_Changes_Metric_Filter" {
  name           = "CIS-SecurityGroupChanges"
  pattern        = "{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup)}"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-SecurityGroupChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_Security_Group_Changes_CW_Alarm" {
  alarm_name                = "CIS-3.10-SecurityGroupChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.CIS_Security_Group_Changes_Metric_Filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to security group will help ensure that resources and services are not unintentionally exposed."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
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
  alarm_actions             = [aws_sns_topic.cis_alerts_sns_topic.arn]
  insufficient_data_actions = []
}
```

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_Security_Group_Changes_Metric_Filter" {
  name           = "CIS-SecurityGroupChanges"
  pattern        = "{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup)}"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-SecurityGroupChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_Security_Group_Changes_CW_Alarm" {
  alarm_name                = "CIS-3.10-SecurityGroupChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.CIS_Security_Group_Changes_Metric_Filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to security group will help ensure that resources and services are not unintentionally exposed."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_Security_Group_Changes_Metric_Filter" {
  name           = "CIS-SecurityGroupChanges"
  pattern        = "{ ($.eventName = AuthorizeSecurityGroupIngress) || ($.eventName = AuthorizeSecurityGroupEgress) || ($.eventName = RevokeSecurityGroupIngress) || ($.eventName = RevokeSecurityGroupEgress) || ($.eventName = CreateSecurityGroup) || ($.eventName = DeleteSecurityGroup)}"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-SecurityGroupChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_Security_Group_Changes_CW_Alarm" {
  alarm_name                = "CIS-3.10-SecurityGroupChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = "XXXX NOT YOUR FILTER XXXX"
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to security group will help ensure that resources and services are not unintentionally exposed."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

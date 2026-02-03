# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/cloudwatch_vpc_changes_alarm_missing.md

---
title: CloudWatch VPC changes alarm missing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CloudWatch VPC changes alarm missing
---

# CloudWatch VPC changes alarm missing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9d0d4512-1959-43a2-a17f-72360ff06d1b`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_metric_filter#pattern)

### Description{% #description %}

To ensure proper monitoring and alerting of changes to Virtual Private Cloud (VPC) configurations, a log metric filter and corresponding CloudWatch alarm should be configured to detect and notify administrators of events such as `CreateVpc`, `DeleteVpc`, or `ModifyVpcAttribute`. If the `metric_name` attribute in the `aws_cloudwatch_metric_alarm` resource does not reference the correct log metric filter (for example, `metric_name = "XXXX NOT YOUR FILTER XXXX"`), the alarm will not trigger on actual VPC changes, leaving unauthorized or accidental modifications undetected. This misconfiguration undermines security monitoring efforts and increases the risk of undetected changes that could impact network segmentation, access control, or data exposure.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_VPC_Changes_Metric_Filter" {
  name           = "CIS-VPCChanges"
  pattern        = "{ ($.eventName = CreateVpc) || ($.eventName = DeleteVpc) || ($.eventName = ModifyVpcAttribute) || ($.eventName = AcceptVpcPeeringConnection) || ($.eventName = CreateVpcPeeringConnection) || ($.eventName = DeleteVpcPeeringConnection) || ($.eventName = RejectVpcPeeringConnection) || ($.eventName = AttachClassicLinkVpc) || ($.eventName = DetachClassicLinkVpc) || ($.eventName = DisableVpcClassicLink) || ($.eventName = EnableVpcClassicLink) }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-VPCChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_VPC_Changes_CW_Alarm" {
  alarm_name                = "CIS-3.14-VPCChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.CIS_VPC_Changes_Metric_Filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to VPC will help ensure that all VPC traffic flows through an expected path."
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
resource "aws_cloudwatch_log_metric_filter" "CIS_VPC_Changes_Metric_Filter" {
  name           = "CIS-VPCChanges"
  pattern        = "{ ($.eventName = CreateVpc) || ($.eventName = ModifyVpcAttribute) || ($.eventName = AcceptVpcPeeringConnection) || ($.eventName = CreateVpcPeeringConnection) || ($.eventName = DeleteVpcPeeringConnection) || ($.eventName = RejectVpcPeeringConnection) || ($.eventName = AttachClassicLinkVpc) || ($.eventName = DetachClassicLinkVpc) || ($.eventName = EnableVpcClassicLink) }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-VPCChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_VPC_Changes_CW_Alarm" {
  alarm_name                = "CIS-3.14-VPCChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = aws_cloudwatch_log_metric_filter.CIS_VPC_Changes_Metric_Filter.id
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to VPC will help ensure that all VPC traffic flows through an expected path."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

```terraform
resource "aws_cloudwatch_log_metric_filter" "CIS_VPC_Changes_Metric_Filter" {
  name           = "CIS-VPCChanges"
  pattern        = "{ ($.eventName = CreateVpc) || ($.eventName = DeleteVpc) || ($.eventName = ModifyVpcAttribute) || ($.eventName = AcceptVpcPeeringConnection) || ($.eventName = CreateVpcPeeringConnection) || ($.eventName = DeleteVpcPeeringConnection) || ($.eventName = RejectVpcPeeringConnection) || ($.eventName = AttachClassicLinkVpc) || ($.eventName = DetachClassicLinkVpc) || ($.eventName = DisableVpcClassicLink) || ($.eventName = EnableVpcClassicLink) }"
  log_group_name = aws_cloudwatch_log_group.CIS_CloudWatch_LogsGroup.name

  metric_transformation {
    name      = "CIS-VPCChanges"
    namespace = "CIS_Metric_Alarm_Namespace"
    value     = "1"
  }
}
resource "aws_cloudwatch_metric_alarm" "CIS_VPC_Changes_CW_Alarm" {
  alarm_name                = "CIS-3.14-VPCChanges"
  comparison_operator       = "GreaterThanOrEqualToThreshold"
  evaluation_periods        = "1"
  metric_name               = "XXXX NOT YOUR FILTER XXXX"
  namespace                 = "CIS_Metric_Alarm_Namespace"
  period                    = "300"
  statistic                 = "Sum"
  threshold                 = "1"
  alarm_description         = "Monitoring changes to VPC will help ensure that all VPC traffic flows through an expected path."
  alarm_actions             = [aws_sns_topic.CIS_Alerts_SNS_Topic.arn]
  insufficient_data_actions = []
}
```

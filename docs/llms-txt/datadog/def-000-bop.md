# Source: https://docs.datadoghq.com/security/default_rules/def-000-bop.md

---
title: CloudTrail trails should be integrated with CloudWatch Logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudTrail trails should be integrated
  with CloudWatch Logs
---

# CloudTrail trails should be integrated with CloudWatch Logs

## Description{% #description %}

It is recommended that CloudTrail logs be sent to CloudWatch Logs. AWS CloudTrail records the identity of the API caller, time of the API call, source IP address of the API caller, request parameters, and the response elements returned by the AWS service. CloudTrail uses Amazon S3 for log file storage and delivery. In addition to capturing CloudTrail logs within a specified S3 bucket for long-term analysis, real-time analysis can be performed by configuring CloudTrail to send logs to CloudWatch Logs. For a trail that is enabled in all regions in an account, CloudTrail sends log files from all those regions to a CloudWatch Logs log group.

**Note**: The intent of this recommendation is to ensure AWS account activity is being captured, monitored, and appropriately alerted on. CloudWatch Logs is a native way to accomplish this using AWS services but does not preclude the use of an alternate solution, such as Datadog Log Management.

## Rationale{% #rationale %}

Sending CloudTrail logs to CloudWatch Logs will facilitate real-time and historic activity logging based on user, API, resource, and IP address, and provides opportunity to establish alarms and notifications for anomalous or sensitive account activity.

### Impact{% #impact %}

**Note**: By default, CloudWatch Logs will store Logs indefinitely unless a specific retention period is defined for the log group. When choosing the number of days to retain, keep in mind it takes an organization an average of 210 days (at the time of writing) to realize they have been breached. Since additional time is required to research a breach, a minimum 365-day retention policy allows time for detection and research. You may also wish to archive the logs to a cheaper storage service rather than simply deleting them.

## Remediation{% #remediation %}

Perform the following to establish the prescribed state:

### From the console{% #from-the-console %}

1. Log in to the [CloudTrail console](https://console.aws.amazon.com/cloudtrail/).
1. Select the **Trail** the needs to be updated.
1. Scroll down to **CloudWatch Logs**.
1. Click **Edit**.
1. Under CloudWatch Logs, check the box for **Enabled**.
1. Under **Log Group**, select New or an existing log group.
1. Edit the **Log group name** to match the CloudTrail or pick the existing CloudWatch Group.
1. Under **IAM Role** Select New or an existing role.
1. Edit the **Role name** to match the CloudTrail or pick the existing IAM Role.
1. Click **Save changes**.

### From the command line{% #from-the-command-line %}

1. Update the trail to send to CloudWatch

   ```
   aws cloudtrail update-trail \
   --name <trail_name> \
   --cloudwatch-logs-log-group-arn <cloudtrail_log_group_arn> \
   --cloudwatch-logs-role-arn <cloudtrail_cloudwatchLogs_role_arn>
   ```

## References{% #references %}

1. [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
1. [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html)

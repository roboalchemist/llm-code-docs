# Source: https://docs.datadoghq.com/security/cloud_siem/guide/aws-config-guide-for-cloud-siem.md

---
title: AWS Configuration Guide for Cloud SIEM
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Cloud SIEM Guides > AWS Configuration
  Guide for Cloud SIEM
---

# AWS Configuration Guide for Cloud SIEM

## Overview{% #overview %}

Cloud SIEM applies detection rules to all processed logs in Datadog to detect threats, like a targeted attack, a threat intel listed IP communicating with your systems, or an insecure configuration. The threats are surfaced as Security Signals in the [Security Signals Explorer](https://app.datadoghq.com/security/signals?query=%40workflow.rule.type%3A%22Log%20Detection%22) for triaging.

This guide walks you through the following steps so that you can start detecting threats with your AWS CloudTrail logs:

1. Set up Datadog's AWS integration
1. Enable AWS CloudTrail logs
1. Send AWS CloudTrail logs to Datadog
1. Use Cloud SIEM to triage Security Signals

## Set up AWS integration using CloudFormation{% #set-up-aws-integration-using-cloudformation %}

{% alert level="danger" %}
Sensitive Data Scanner for cloud storage is in Limited Availability. [Request Access](https://www.datadoghq.com/private-beta/data-security) to enroll.
{% /alert %}

1. Go to Datadog's [AWS integration tile](https://app.datadoghq.com/integrations/amazon-web-services?) to install the integration.
1. Click **Automatically Using CloudFormation**. If there is already an AWS account set up, click **Add Another Account** first.
1. Select the AWS Region where the CloudFormation stack will be launched.
1. Select or create the Datadog API Key used to send data from your AWS account to Datadog.
1. To configure the Datadog Lambda Forwarder, select **Yes** for **Send Logs to Datadog**. This enables AWS CloudTrail logs to be sent to Datadog.
1. To enable Cloud Security, select **Yes** for **Detect security issues**.
1. If you select **Yes** for **Detect security issues**, the **Enable Sensitive Data Scanner for Cloud Storage** option appears. Turn this on to automatically identify and classify sensitive data stored in Amazon S3.
1. Click **Launch CloudFormation Template**. This opens the AWS Console and loads the CloudFormation stack with the parameters filled in based on your selections in the Datadog form.
1. Check the required boxes from AWS and click **Create stack**.
1. After the CloudFormation stack is created, return to the AWS integration tile in Datadog and click **Ready!**

**Notes**:

- The `DatadogAppKey` parameter enables the CloudFormation stack to make API calls to Datadog, allowing it to add and edit the configuration for this AWS account. The key is automatically generated and tied to your Datadog account.
- For more information about Datadog's AWS integration and CloudFormation template, see [Getting Started with AWS](https://docs.datadoghq.com/getting_started/integrations/aws/).
- If you need to set up the AWS integration manually, see [AWS manual setup instructions](https://docs.datadoghq.com/integrations/amazon_web_services/?tab=roledelegation#manual).

## Enable AWS CloudTrail logging{% #enable-aws-cloudtrail-logging %}

Enable AWS CloudTrail logging so that logs are sent to a S3 bucket. If you already have this setup, skip to Send AWS CloudTrail logs to Datadog.

1. Click **Create trail** on the [CloudTrail dashboard](https://console.aws.amazon.com/cloudtrail/home).
1. Enter a name for your trail.
1. Create a new S3 bucket or use an existing S3 bucket to store the CloudTrail logs.
1. Create a new AWS KMS key or use an existing AWS KMS key, then click **Next**.
1. Leave the event type with the default management read and write events, or choose additional event types you want to send to Datadog, then click **Next**.
1. Review and click **Create trail**.

## Send AWS CloudTrail logs to Datadog{% #send-aws-cloudtrail-logs-to-datadog %}

Set up a trigger on your Datadog Forwarder Lambda function to send CloudTrail logs stored in the S3 bucket to Datadog for monitoring.

1. Go to the [Datadog Forwarder Lambda](https://console.aws.amazon.com/lambda/home) that was created during the AWS integration set up.
1. Click **Add trigger**.
1. Select **S3** for the trigger.
1. Select the S3 bucket you are using to collect AWS CloudTrail logs.
1. For Event type, select **All object create events**.
1. Click **Add**.
1. See CloudTrail logs in Datadog's [Log Explorer](https://app.datadoghq.com/logs?query=service%3Acloudtrail).

See [Log Explorer](https://docs.datadoghq.com/logs/explorer/) for more information on how to search and filter, group, and visualize your logs.

## Use Cloud SIEM to triage Security Signals{% #use-cloud-siem-to-triage-security-signals %}

Cloud SIEM applies out of the box detection rules to all processed logs, including the CloudTrail logs you have just set up. When a threat is detected with a Detection Rule, a Security Signal is generated and can be viewed in the Security Signals Explorer.

- Go to the [Cloud SIEM Signals Explorer](https://app.datadoghq.com/security/siem/signals?query=%40workflow.rule.type%3A%28%22Log%20Detection%22%29%20&column=time&order=desc) to view and triage threats. See [Security Signals Explorer](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals) for further details.
- You can also use the [AWS CloudTrail dashboard](https://app.datadoghq.com/dash/integration/30459/aws-cloudtrail) to investigate anomalous activity.
- See [out-of-the-box detection rules](https://docs.datadoghq.com/security/default_rules/#cat-cloud-siem) that are applied to your logs.
- Create [new rules](https://docs.datadoghq.com/security/detection_rules/) to detect threats that match your specific use case.

Since Cloud SIEM applies detection rules to all processed logs, see the [in-app instructions](https://app.datadoghq.com/security/configuration?detect-threats=apache&secure-cloud-environment=amazon-web-services&secure-hosts-and-containers=kubernetes&selected-products=security_monitoring) on how to collect [Kubernetes audit logs](https://docs.datadoghq.com/integrations/kubernetes_audit_logs/) and logs from other sources for threat detection. You can also enable different [AWS services](https://docs.datadoghq.com/logs/guide/send-aws-services-logs-with-the-datadog-lambda-function/?tab=awsconsole#enable-logging-for-your-aws-service) to log to a S3 bucket and send them to Datadog for threat monitoring.

## Further reading{% #further-reading %}

- [Explore Cloud SIEM default detection rules](https://docs.datadoghq.com/security/default_rules/#cat-cloud-siem-log-detection)
- [Learn about the Security Signals Explorer](https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals)
- [Create new detection rules](https://docs.datadoghq.com/security/cloud_siem/detect_and_monitor/custom_detection_rules/)
- [Getting Started with AWS](https://docs.datadoghq.com/getting_started/integrations/aws/)
- [Send AWS services logs with the Datadog Lambda function](https://docs.datadoghq.com/logs/guide/send-aws-services-logs-with-the-datadog-lambda-function/)
- [See how to explore your logs](https://docs.datadoghq.com/logs/explorer/)

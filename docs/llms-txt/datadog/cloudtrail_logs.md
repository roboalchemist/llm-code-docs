# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/cloudtrail_logs.md

---
title: Setting up AWS CloudTrail Logs for Cloud Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security > Setting
  up AWS CloudTrail Logs for Cloud Security
---

# Setting up AWS CloudTrail Logs for Cloud Security

Set up AWS CloudTrail Logs to get the most out of [Cloud Security Identity Risks](https://docs.datadoghq.com/security/cloud_security_management/identity_risks). AWS CloudTrail Logs provides additional insights into the actual usage of cloud resources, helping you identify users and roles with significant gaps between provisioned and utilized permissions.

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

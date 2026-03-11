---
id: Cloudwatch
title: AWS Cloudwatch
---
Amazon CloudWatch is a monitoring and management service built for developers, system operators, site reliability engineers (SRE), and IT managers. To integrate AWS CloudWatch with Zenduty, complete the following steps:

## In Zenduty

1. To add a new AWS CloudWatch integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "AWS CloudWatch" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In AWS CloudWatch

1. Login to your AWS account. Go to your SNS dashboard. On the left panel, click on "Topics". Click on "Create topic". For topic and display names, enter "Zenduty".

![](/img/Integrations/Cloudwatch/1.png)

1. Go back top the SNS dashboard and click on "Create Subscription".

2. In the Topic ARN, choose the topic created in Step 3. Select the protocol as HTTPS. In the endpoint field, past the URL you copied earlier.

![](/img/Integrations/Cloudwatch/2.png)

1. Click on "create subscription" to find a list of your subscriptions. Refresh this page to confirm.

2. You can now create alarms to the topic.

3. While creating Alarm rules, choose the above created SNS topic for notifying in both the ALARM state and OK state as displayed in the screenshot below.

![](/img/Integrations/Cloudwatch/3.png)

![](/img/Integrations/Cloudwatch/4.png)

1. Zenduty will create an incident for each alarm and auto-resolve the incident when Cloudwatch sends the OK notification.

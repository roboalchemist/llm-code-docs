---
id: Stackdriver
title: Google Cloud Platform - Operations
---
Google Stackdriver is a monitoring service that provides IT teams with performance data about applications and virtual machines running on the Google Cloud Platform and Amazon Web Services public cloud. To integrate Google Staackdriver with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Google Stackdriver integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Google Stackdriver" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Google Stackdriver

1. In the Cloud Console, select Monitoring.

![](/img/Integrations/Stackdriver/1.png)

1. In the Monitoring Navigation pane, click on Alerting.

![](/img/Integrations/Stackdriver/2.png)

1. Click Edit notification channels.

![](/img/Integrations/Stackdriver/3.png)

1. The Notification channels dashboard contains a section for each notification channel type. Add a new Webhook notification channel. (Click on ADD NEW button next to Webhook)

![](/img/Integrations/Stackdriver/4.png)

1. Use the URL copied in Step 4.  

![](/img/Integrations/Stackdriver/5.png)

1. Give a suitable name to the webhook and click on TEST CONNECTION. If the test succeeds, click on SAVE. (The save button is not activated until a successful test)

2. You have now created an alerting channel which can be used with any new or existing alert policy.

## Using Notification Channels: 

1. While creating a new alert policy, click on ADD NOTIFICATION CHANNEL

![](/img/Integrations/Stackdriver/6.png)

1. Select “Webhook with Token Authentication” as the Notification Channel type

![](/img/Integrations/Stackdriver/7.png)

1. Select the name of the created notification channel from the dropdown box and then click ADD.

## With an Existing Alert Policy

1. Under the list of all policies in the Alerting tab, select the policy to which the notification channel is to be added.

2. Click EDIT in the top pane

![](/img/Integrations/Stackdriver/8.png)

1. Scroll down to Notifications. Click on ADD NOTIFICATION CHANNELS.

![](/img/Integrations/Stackdriver/9.png)

1. Select Webhook with Token Authentication as the Notification Channel Type

![](/img/Integrations/Stackdriver/10.png)

1. Select the name of the created notification channel from the dropdown box and then click ADD.

2. Your Stackdriver integration is completed.

References:

1) https://cloud.google.com/monitoring/support/notification-options
2) https://cloud.google.com/monitoring/alerts/using-alerting-ui

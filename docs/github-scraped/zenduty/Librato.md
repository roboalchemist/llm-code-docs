---
id: Librato
title: Librato
---
Librato continually tracks down N+1 database queries, sources of memory bloat, performance abnormalities, and more. To integrate Librato with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Librato integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Librato" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Librato

1. Log In to Librato.

2. Click on Settings in the dashboard and then Notification Services.

3. Select Webhook from Notification Services.

![](/img/Integrations/Librato/1.png)

1. Click on Add Configuration under Webhook.

2. Enter the title of the webhook and under URL paste the link copied earlier. Add.

![](/img/Integrations/Librato/2.png)

1. Go back to dashboard and click on Alerts. Click on create new alert.

2. Enter the alert name , alert description, and trigger duration.

![](/img/Integrations/Librato/3.png)

1. Click on create a new condition. Set the condition type and select the metric on which it has to be alerted.

![](/img/Integrations/Librato/4.png)

1. Set the threshold value and the notification duration.

2. Click on add condtion at the top right corner of the screen.

3. Click on Notification services and click on Webhook. Select “Zenduty Webhook”.

![](/img/Integrations/Librato/5.png)

You have successfully integrated Librato with Zenduty.

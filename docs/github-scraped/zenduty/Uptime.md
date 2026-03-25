---
id: Uptime
title: Uptime
---
Uptime provides uptime monitoring for websites and servers. To integrate Uptime with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Uptime integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Uptime" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Uptime

1. Log in to Uptime, and click on the "Drawer" navigation icon located at the top right corner of the screen.

![](/img/Integrations/Uptime/1.png)

1. Go to "Notifications" and select "Integrations".

2. Click on the "New Profile" button. From the "Provider Type" dropdown menu, select the "Custom URL Postback (Webhook)" option.

3. Fill in the name as "Zenduty", or any other easy to remember name, and paste the webhooks url you copied earlier in the "URL" field.

![](/img/Integrations/Uptime/2.png)

1. Save to finish creating the webhook.

2. To set up an endpoint to monitor, go to "Monitoring"->"Checks".

3. Click the "Add New" button, and fill out the form as shown below:

![](/img/Integrations/Uptime/3.png)

1. Click save to allow Zenduty to notify you of the alerts.

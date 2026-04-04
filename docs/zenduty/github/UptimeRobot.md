---
id: UptimeRobot
title: UptimeRobot
---
UptimeRobot is a monitoring service to view uptime, downtime and the response times. To integrate UptimeRobot with Zenduty, complete the following steps:

## In Zenduty

1. To add a new UptimeRobot integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "UptimeRobot" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In UptimeRobot

1. Login to UptimeRobot. Go to "My Settings" and click on the "Add Alert Contact" button.

![](/img/Integrations/UptimeRobot/1.png)

1. Select "Webhook" for "Alert Contact Type" and paste the Zenduty URL in the URL field.

2. Paste the following payload in the POST value field:
 ```
 {
  "alertName":"*monitorFriendlyName*",
  "alertDetails":"*alertDetails*",
  "alertTypeName":"*alertTypeFriendlyName*",
  "id":"*monitorID*"
 }
 ```
3. Then save the webhook.

![](/img/Integrations/UptimeRobot/2.png)

1. To generate alerts, first create a monitor.
 * Click on the "Add New Monitor" button.
 * Fill the form with the necessary details and finally check the box next to the newly created webhook in the "Alert Contacts to Notify" section.

![](/img/Integrations/UptimeRobot/3.png)

1. Once this is saved, any alerts should appear on the Zenduty incidents page.

2. UptimeRobot is now integrated.

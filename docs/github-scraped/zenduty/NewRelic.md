---
id: NewRelic
title: New Relic
---
New Relic is a web application performance service designed to work in a real time with your live web app. To integrate New Relic with Zenduty, complete the following steps:

## In Zenduty

1. To add a new New Relic integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "New Relic" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In New Relic

1. Log in to New Relic. Go to Alerts and create a new Notification Channel.

![](/img/Integrations/NewRelic/1.png)

1. From "Channel Details", select the type of channel as "Webhook". Specify the payload type as "JSON".
Paste the webhooks url you copied earlier.

![](/img/Integrations/NewRelic/2.png)

1. Select "Create Channel". Optional: Select "Send a test notification".

2. Add the notification channel to one or more alert policies.

3. Your New Relic is now setup. Zenduty will create incidents for all New Relic alerts and auto-acknowledge and auto-resolve whenever the incident is resolved in New Relic.

---
id: Scout
title: Scout
---
Scout continually tracks down N+1 database queries, sources of memory bloat, performance abnormalities, and more. To integrate Scout with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Scout integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Scout" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Scout

1. Log In to Scout.

2. Go to "Applications" > "Add Application". Follow the steps given there to add a new application.

![](/img/Integrations/Scout/1.png)

1. Go to "Alerts" > "Notification Channels" > "New Webhook" to configure the new notification channel. Give the name to notification channel and paste the Webhook URL copied earlier.

![](/img/Integrations/Scout/2.png)

![](/img/Integrations/Scout/3.png)

1. Go to "Alerts" > "Notification Groups" > "New Notification group" to add a new notification group. Give a name to the group and select the webhook channel you created in the previous step.

![](/img/Integrations/Scout/4.png)

1. Go to "Alerts" > "Alert Conditions" to set the alert conditions. Select the group that you created in the previous step in the "notify" option in "Alert Condition".

![](/img/Integrations/Scout/5.png)

1. Scout is now integrated with Zenduty.

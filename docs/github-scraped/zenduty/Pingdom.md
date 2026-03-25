---
id: Pingdom
title: Pingdom
---
Pingdom helps you gain instant insights into your website’s availability and performance. To integrate Pingdom with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Pingdom integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Pingdom" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Pingdom

1. Log in to Pingdom. Go to Integrations-> Integrations-> click "Add integration".

![](/img/Integrations/Pingdom/AddIntegration.png)

1. Give it a name, and paste the webhook url (copied in the earlier step).

![](/img/Integrations/Pingdom/IntegrationForm.png)

1. Next, connect the endpoint you want to monitor with the newly added Zenduty integration. For this, go to Experience Monitoring-> Uptime. Click "Add New" to add a new Uptime Check.

![](/img/Integrations/Pingdom/NewCheck.png)

1. Fill form, including the name of the check and the url of the endpoint to be monitored. Select the integration you just added from the dropdown menu.

2. Pingdom is now integrated.

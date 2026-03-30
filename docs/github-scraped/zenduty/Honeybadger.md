---
id: Honeybadger
title: Honeybadger
---
Honeybadger allows you to query, visualize, alert on and understand your metrics no matter where they are stored. To integrate Honeybadger with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Honeybadger integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Honeybadger" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Honeybadger

1. Login to Honeybadger. Click on "Add Project", and give it a name and select a language.

![](/img/Integrations/Honeybadger/add.png)

![](/img/Integrations/Honeybadger/newproject.png)

1. Go to "Project Settings". From the left hand menu, select "Alerts and Integrations". Paste the webhook you copied earlier.

![](/img/Integrations/Honeybadger/webhook1.png)

![](/img/Integrations/Honeybadger/webhook2.png)

1. Add monitoring metrics like Errors and Uptime.

![](/img/Integrations/Honeybadger/errors.png)

![](/img/Integrations/Honeybadger/uptime.png)

1. Your Honeybadger integration is now set up. Zenduty will alert you when something goes wrong.

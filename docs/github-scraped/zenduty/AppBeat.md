---
id: AppBeat
title: AppBeat
---

AppBeat allows you to monitor your online service proactively so you can react before it affects your users. To integrate AppBeat with Zenduty, complete the following steps:

## In Zenduty

1. To add a new AppBeat integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "AppBeat" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In AppBeat

1. Log in to AppBeat, and go to Alerting -> Third Party Service Integration.

2. Under the "Add new integration" dropdown, select the "Dynamic Webhook" option.

![](/img/Integrations/AppBeat/1.png)

1. Fill out the required information (the Zenduty URL must be entered in the "Webhook URL" field) and save the integration.

![](/img/Integrations/AppBeat/2.png)

1. To create a a new check, first goto "Services & Checks" and click on the "Add New Service" button.

2. When creating the new service, in the "Notification types" tab, be sure to select the created webhook.

![](/img/Integrations/AppBeat/3.png)

1. Once the new service is created, click on the "Checks" tab and click on the "Add a New Check" button.

2. Fill in the required information and save the check.

![](/img/Integrations/AppBeat/4.png)

1. AppBeat is now integrated.

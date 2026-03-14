---
id: Atatus
title: Atatus
---
Get deeper insight into performance issues and crashes affecting your apps using Atatus's performance monitoring and error tracking service. To integrate Atatus with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Atatus integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Atatus" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Atatus

1. Login to Atatus.

2. Click on New Project -> Select Infrastructure.

3. Follow the steps to configure the server and click on “I’m done”.

![](/img/Integrations/Atatus/1.png)

1. Click on "Alerting" in the dashboard.

2. Click on "Notification Channels" and click "create new notification channel".

3. Select "Webhook" from the "Channel type" drop-down menu and give your channel a name.

4. Paste the copied link in the "URL" field and click "Create Channel".

![](/img/Integrations/Atatus/2.png)

1. Click on "Alert Policies". Give the Alert policy a name and set the incident preference as “By policy”.

![](/img/Integrations/Atatus/3.png)

1. Select the Notification Channel and click "Create Policy".

2. Select the product and the metric. Set a threshold for "Critical" and "Warning".

![](/img/Integrations/Atatus/4.png)

1. Enter the rule name and click "Create Rule".

![](/img/Integrations/Atatus/5.png)

1. Atatus is now integrated.

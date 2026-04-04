id: Papertrail
title: Papertrail
---

Papertrail helps you monitor your servers, your on-premise network, the global cloud, and cloud platform data, in one thorough, affordable solution. To integrate Papertrail with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Papertrail integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Papertrail" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Papertrail

1. Sign in Papertrail.

2. Under the All Systems column, select the system for which you want to manage logs.

![](/img/Integrations/Papertrail/1.png)

1. Search for the logs for which you want alerts to be triggered. In this case, we are searching for “systemd” logs.

![](/img/Integrations/Papertrail/2.png)

1. Under create a new search, enter the name of search and click on Save and Setup Alert.

![](/img/Integrations/Papertrail/3.png)

1. Click on Webhook.

![](/img/Integrations/Papertrail/4.png)

1. Under Alert Conditions, set the alert frequency and when the alert should be triggered.

![](/img/Integrations/Papertrail/5.png)

1. Under Webhook URL,paste the link copied earlier. Click on Create Alert.

![](/img/Integrations/Papertrail/6.png)

1. Papertrail is now integrated.

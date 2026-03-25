---
id: Panopta
title: Panopta
---
Panopta helps you monitor your servers, your on-premise network, the global cloud, and cloud platform data, in one thorough, affordable solution. To integrate Panopta with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Panopta integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Panopta" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Panopta

1. Sign in Panopta.
2. Go to settings > Integrations. Select "webhook" and click on "configure".
3. Label your webhook and set request as POST, paste the URL copied earlier, select the paylod type as "form variable" and fill the form variable as shown below.

![](/img/Integrations/Panopta/1.png)

![](/img/Integrations/Panopta/2.png)

1. Go to Monitoring > Alert Timeline. Add a new timeline. Add a new event into this timeline. Fill the necessary details and select the integration that you have created earlier. Click add.

![](/img/Integrations/Panopta/3.png)

![](/img/Integrations/Panopta/4.png)

1. Go to "instances" and configure the matrices that you want to monitor. Give threshold and select the severity and in notify with timeline select the alert timeline.

![](/img/Integrations/Panopta/5.png)

1. Panopta is now integrated with Zenduty.

---
id: Humio
title: Humio
---
Humio is a log management software, providing real-time, instant monitoring, analysis, and visibility of log data. To integrate Humio with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Humio integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Humio" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Humio

1. Log into Humio.

2. Go to "Alerts" -> Select "Notifiers".

3. Create a new "Notifier".

![](/img/Integrations/Humio/1.png)

1. Go to "Alerts" and create a new "Alert".

![](/img/Integrations/Humio/2.png)

1. Give a label to "Webhook" and set the request as "POST".

![](/img/Integrations/Humio/3.png)

1. Paste the earlier generated "URL" and then select "New notifier".

![](/img/Integrations/Humio/4.png)

1. Humio is now integrated.

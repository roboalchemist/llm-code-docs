---
id: Logzio
title: Logzio
---
Manage logs and get log analysis services with Logzio's log management and analytics software.  To integrate Logzio with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Logzio integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Logzio" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Logzio

1. Sign into Logzio.

2. Go to "Log shipping" and ship your logs as per your operating system.

![](/img/Integrations/Logzio/1.png)

1. Then go to "Kibana" where you will find the recieved data.

2. Now go to :Alert and events" and select "Create new alert" and fill in all the required details.

![](/img/Integrations/Logzio/2.png)

1. Then go to "Alert endpoint" in "Alerts and events" and select the custom option.

![](/img/Integrations/Logzio/3.png)

1. On the custom option paste the copied URL.

![](/img/Integrations/Logzio/4.png)

1. Logzio is now integrated.

---
id: OpsDash
title: OpsDash
---

OpsDash is an all-in-one solution for server monitoring, uptime monitoring, database monitoring, service monitoring and app metric monitoring. To integrate OpsDash with Zenduty, complete the following steps:

## In Zenduty

1. To add a new OpsDash integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "OpsDash" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In OpsDash

1. Log in to OpsDash.

2. Click on "Sources" under "Dashboards".

3. Select the server which you want to monitor.

4. Select "System Temperatures".

5. Select "sys.hw.temp.zone" and set the alerting thresholds and save the changes.

![](/img/Integrations/OpsDash/1.png)

1. Click on "Notifications" under "Dashboards" and click on “Add Another” under "Notification Rules".

2. Click on "System Settings" and under the "Webhook Integrations", paste the link copied earlier. Click on "Add".

![](/img/Integrations/OpsDash/2.png)

1. Click on "Notifications" under "Dashboards" and add the webhook under "Notification rules".

![](/img/Integrations/OpsDash/3.png)

![](/img/Integrations/OpsDash/4.png)

1. OpsDash is now integrated.

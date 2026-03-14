---
id: Site24x7
title: Site24x7
---

Site24x7 helps you monitor websites, emails, and web apps to get instant alerts. With the Zenduty integration, you will be able to receive context notifications about new code pushes, pull requests, issues and issue comments. New issues will trigger a new incident.

To integrate Site24x7 with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Site24x7 integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Site24x7" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Site24x7

1. Log in to Site24x7. Click on admin on the menu and select "Third Party Integration". Select "Webhooks".

![](/img/Integrations/Site24x7/1.png)

1. Enter the name of the integration, paste the copied link in "Hook URL" and set the "HTTP method" as "POST", select "Post as JSON" and click on "Save".

![](/img/Integrations/Site24x7/2.png)

1. Set Trigger incidents when monitor is "Critical" and "Trouble Status" as “Yes”.

![](/img/Integrations/Site24x7/3.png)

1. Click on the "server" on the menu. Select the server you want to monitor and click "edit".

![](/img/Integrations/Site24x7/4.png)

1. Click on ‘+’ next to "Threshold and Availability".

2. Enter the display name.

3. Under "Threshold Configuration", set notify the process down as “Down”.

![](/img/Integrations/Site24x7/5.png)

1. Set memory utilization threshold for “Trouble” and “Critical” and save it.

2. In Edit monitor server, click on ‘+’ next to "Notification Profile".

3. Enter the display name. Set the downtime notification delay and save it.

![](/img/Integrations/Site24x7/6.png)

1. In Edit monitor server, add the third party integration as "Zenduty Webhook".

2. Click on save.

3. Site24x7 is now integrated.

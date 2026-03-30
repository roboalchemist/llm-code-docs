--
id: Pingometer
title: Pingometer
---

Pingometer helps you gain instant insights into your website’s availability and performance. To integrate Pingometer with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Pingometer integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Pingometer" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Pingometer

1. Log in to Pingometer. Click on Notifications on the menu, and then "Integrations".

2. Click on New Profile on the top right corner of the screen.

3. Set the Provider Type as “Custom Postback URL (Webhook)”.

4. Enter the name of the integration and paste the link copied earlier under URL. Save.

![](/img/Integrations/Pingometer/1.png)

1. Click on Monitoring on the menu. Under Monitoring, click on Check and "Add New".

2. Enter the name of check and set the "Check Interval".

![](/img/Integrations/Pingometer/2.png)
![](/img/Integrations/Pingometer/3.png)

1. Set the "check type" as the application for which we are monitoring. In this case, we set the check type as “API” and then select the locations for which we are monitoring.

2. Set the check steps as follows:
       1.)GET and enter the URL of API.
       2.)Set the conditon as http status should be 200.

![](/img/Integrations/Pingometer/4.png)

1. Click on Save.

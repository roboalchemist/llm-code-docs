---
id: Idera
title: IDERA (Copperegg)
---

IDERA's Uptime Cloud Monitor provides essential monitoring capabilities, giving you everything you need to identify and react to cloud infrastructure issues. To integrate IDERA with Zenduty, complete the following steps:

## In Zenduty

1. To add a new IDERA integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "IDERA" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In IDERA

1. Log in to IDERA, and go to Alerts -> Notification Profiles.

![](/img/Integrations/Idera/1.png)

1. To add a webhook, either click on the "Edit" button under the current user profile or create a new user profile.

2. Select the Webhook notification type in the dropdown and enter the Zenduty URL in the URL field. Then save the current notification.

![](/img/Integrations/Idera/2.png)

1. The user can configure alerts for any service that needs to be monitored.
In this example, we'll look at monitoring the status of a URL.

 * Click the "Configure Alerts" button in the menu on the left-side of the page. Then click on "New Alert" to add new alerts that monitor some endpoint.

 ![](/img/Integrations/Idera/3.png)

 * The type of notification that should be selected to monitor an endpoint is "Probe".
 * Once the notifications are configured and saved, click on the "Probes" tab at the top of the page.
 * Then click on "Add a Probe" and create a probe for the desired URL and save the configuration.

 ![](/img/Integrations/Idera/4.png)

2. IDERA is now integrated, and all alerts will show up as Zenduty Incidents.

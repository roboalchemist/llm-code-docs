---
id: Rollbar
title: Rollbar
---
Rollbar provides real-time error alerting & debugging tools for developers. To integrate Rollbar with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Rollbar integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Rollbar" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Rollbar

1. Log in to Rollbar, and go to Projects-> Create New Project

![](/img/Integrations/Rollbar/1.png)

1. After creating a project, choose a primary SDK. We are using Python as an example.

![](/img/Integrations/Rollbar/2.png)

1. Click on the "Settings" tab located at the top of the page. Choose the "Notifications" options from the left-hand side menu.

![](/img/Integrations/Rollbar/3.png)

1. Click on the "Webhook" option, and then enter the URL you copied earlier.

![](/img/Integrations/Rollbar/4.png)

1. Rollbar is now integrated and all alerts will show up on Zenduty.

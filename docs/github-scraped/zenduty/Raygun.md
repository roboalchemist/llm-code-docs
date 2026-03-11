---
id: Raygun
title: Raygun
---
Raygun gives you a window into how users are really experiencing your software applications. Detect, diagnose and resolve issues that are affecting end users with greater speed and accuracy.
To integrate Raygun with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Raygun integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Raygun" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Raygun

1. Sign in to Raygun, and go to Integrations-> Webhooks

![](/img/Integrations/Raygun/1.png)

1. On the "Webhooks Integrations" page, click on the "Setup" tab and aste the url you copied earlier.
Make sure to check the "Enabled" box and save changes.

![](/img/Integrations/Raygun/2.png)

1. Navigate to the "Setup" page and follow the instructions to set up "Real Time User Monitoring" and or "Crash Reporing".
As an example, we have set up Crash Reporting.

![](/img/Integrations/Raygun/3.png)

1. Raygun is now integrated and corresponding alerts will be sent as Zenduty incidents.

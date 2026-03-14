---
id: Healthchecks
title: Healthchecks.io
---

Healthchecks supports Cron Monitoring to monitor nightly backups, weekly reports, cron jobs and background tasks and receive alerts when your tasks don't run on time. To integrate Healthchecks with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Healthchecks integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Healthchecks" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Healthchecks

1. Login to Healthchecks.

2. Click on Integrations from the dashboard. Select "Add Integration" corresponding to Webhook.

![](/img/Integrations/Healthchecks/1.png)

![](/img/Integrations/Healthchecks/2.png)

1. Paste the link copied earlier in URL for “down” events and “up” events under the Integration settings.

![](/img/Integrations/Healthchecks/3.png)

1. Enter the following code under POST data:

 ```
     {"name":"$NAME","status":"$STATUS","current time":"$NOW","code":"$CODE"}
    ```

 Under Request Headers, set the "Content Type" as JSON and save.

2. Rename the Webhook as “Zenduty Webhook”. Click on "My First Check".

3. Click on "Change Schedule" under Schedule. Set the "Period" and "Grace Time" and save.

![](/img/Integrations/Healthchecks/6.png)

1. Healthchecks is now integrated.  

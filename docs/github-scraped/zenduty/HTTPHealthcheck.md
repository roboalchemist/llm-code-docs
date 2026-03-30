---
id: HTTPHealthcheck
title: HTTP Healthcheck (Zenduty)
---

HTTP Healthcheck supports Cron Monitoring to monitor nightly backups, weekly reports, cron jobs and background tasks and receive alerts when your tasks don't run on time. To integrate HTTP Healthcheck with Zenduty, complete the following steps:

## In Zenduty

1. To add a new HTTP Healthchecks integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "HTTP Healthcheck" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks API KEY generated.

5. To create an alert from your application, send a post request to:

    ```
    https://www.zenduty.com/api/integration/httphealthcheck/<integration-key>/<alert_type>/
    ```

6. Replace the <integration-key> with the Integration key you copied in Step 5. Replace <alert-type> with one of 6 values - **critical**, **acknowledged**, **resolved**, **error**, **warning**, **info**.

7. **critical**, **error** and **warning** alert types will create an incident, depending on your integration settings. **acknowledged** alert type will acknowledge the incident. **resolved** will resolve the incident. **info** will not create any incidents but will add an INFO alert to your alert log.

8. Send an HTTP Post request to the above URL without any payload.

9. HTTP Healthcheck is now integrated.  

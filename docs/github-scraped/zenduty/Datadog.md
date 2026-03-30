---
id: Datadog
title: Datadog
---
Datadog is a monitoring service for cloud-scale applications, providing monitoring of servers, databases, tools, and services. To integrate Datadog with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Datadog integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Datadog" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Datadog

1. Login to Datadog. From the left hand menu, go to Integrations-> Integrations. Search for "Webhooks" from this page, and click the corresponding button.

![](/img/Integrations/Datadog/Webhooks1.png)

1. Scroll down, fill in the name, url (copied above) and custom payload. **Check the "Use Custom Payload" box**.
Paste this in the custom payload box:

```
  {
  "alert_id": "$ALERT_ID",
  "hostname":"$HOSTNAME",
  "date_posix":"$DATE_POSIX",
  "aggreg_key":"$AGGREG_KEY",
  "title": "$EVENT_TITLE", 
  "alert_status":"$ALERT_STATUS",
  "alert_transition":"$ALERT_TRANSITION",
  "link":"$LINK",
  "event_msg":"$TEXT_ONLY_MSG"
  }

```

The page should look as below:

![](/img/Integrations/Datadog/Webhooks2.png)

![](/img/Integrations/Datadog/Webhooks3.png)

1. Click on "Update Configuration".

2. Next, from the left hand side menu, select Monitors-> Manage Monitor.

3. Click on the "Edit" button next to the newly created monitor.

![](/img/Integrations/Datadog/Monitors1.png)

1. Set all the metrics. In the "Notify Team" tab, make sure to select the webhook you have just created.

![](/img/Integrations/Datadog/Monitors2.png)

![](/img/Integrations/Datadog/Monitors3.png)

1. Datadog is now integrated and Zenduty will alert you when Datadof alerts are created and resolved.

---
id: Grafana
title: Grafana
---
Grafana allows you to query, visualize, alert on and understand your metrics no matter where they are stored. To integrate Grafana with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Grafana integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Grafana" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Grafana

1. Log in to Grafana. Go to "Notification Channels". Add New Channel.Select type as "Webhook".

2. Enter the webhook url copied from the previous step. Paste the URL copied and click on Save.

![](/img/Integrations/Grafana/Webhook.png)

```
    IMPORTANT WARNING - Sometimes Grafana may not fire an alert if the "Include Image" parameter is selected. First check if the alert is working with the parameter not selected, and then try selecting the parameter and see if the alerts are fired to Zenduty.
```

1. Go to your Grafana Dashboard and click on the "Alerts" tab. Click on "Create alert". In the alert configuration under "Send to", add Zenduty as a notification method. Add a relevant message for the aalert and save the graph.

![](/img/Integrations/Grafana/EditGraph.png)

1. Your Grafana is now integrated. Zenduty will automatically create incidents from your Grafana rules.

![](/img/Integrations/Grafana/Test.png)

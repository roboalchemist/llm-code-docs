---
id: HostedGraphite
title: Hosted Graphite
---
Hosted Graphite  is an add-on for providing application performance metrics. Hosted Graphite give you a simple, scalable way to measure metric data from your application. To integrate Hosted Graphite with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Hosted Graphite integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.
2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.
3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Hosted Graphite" from the dropdown menu.
4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Hosted Graphite

1. Sign In to Hosted Graphite. Go to "Agent" tab to setup your monitoring agent. You can find instructions for the same within the application.

![](/img/Integrations/HostedGraphite/1.png)

1. Go to dashboard and select "Grafana" to see visualization of metrics values. Go to the "Metrics" tab and type * to see all available metrics

2. Go to the "notification channel" in alert tab and click "add channel" to add new notification channel.

3. Select "webhook" in "notification type" and give name to this channel. Paste the wehook url copied earlier.

![](/img/Integrations/HostedGraphite/2.png)

1. Now, go to "Alerts" and click "add alert" to set the definition of the alert. 

![](/img/Integrations/HostedGraphite/3.png)

1. Fill the name of alert, metric to alert on, and message to be sent. Confirm.

![](/img/Integrations/HostedGraphite/4.png)

1. Then set the "alert criteria" and select the notification channel that you have created earlier. Add alerting notification interval. Save.

![](/img/Integrations/HostedGraphite/5.png)

1. Hosted Graphite is now integrated.

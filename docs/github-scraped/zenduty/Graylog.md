---
id: Graylog
title: Graylog
---
Graylog is a leading centralized log management solution built to open standards for capturing, storing, and enabling real-time analysis of terabytes of machine. To integrate Graylog with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Graylog integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Graylog" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Graylog

1. Log in to Graylog. Go to "Notification Channels"-> Add New Channel. Select type as "Webhook".

2. Select "Inputs" under the "Systems" drop-down menu. From the "Select Input" drop-down list, select "Syslog UDP" and click on "Launch New Input".

![](/img/Integrations/Graylog/1.png)

1. Select the "Node" and enter the title of the input and save it.

![](/img/Integrations/Graylog/2.png)

1. Click on "Alerts" from the menu. Select "Conditons" from the "Manage Alert Conditions" section.

![](/img/Integrations/Graylog/3.png)

1. Select "Message Count Condition" from "Condition" type drop-down list and Add alert.

![](/img/Integrations/Graylog/4.png)

1. Enter the title of the alert, set the time range and threshold type. Set the threshold value, grace period, message backlogs and save.

![](/img/Integrations/Graylog/5.png)

1. Click on "Notifications" under the "Manage Alert Conditions" section.

2. Click on "Add New Notification". Select HTTP Alarm Callback under the Notification type drop-down list.

![](/img/Integrations/Graylog/6.png)

1. Enter the title of the notification and under URL, paste the copied link.

![](/img/Integrations/Graylog/7.png)

1. Graylog is now integrated and Zenduty will create incidents from the alerts.

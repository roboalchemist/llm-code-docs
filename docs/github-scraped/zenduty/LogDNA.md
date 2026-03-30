---
id: LogDNA
title: LogDNA
---
LogDNA provides powerful, centralized logging and log analysis that deploys anywhere. To integrate LogDNA with Zenduty, complete the following steps:

## In Zenduty

1. To add a new LogDNA integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "LogDNA" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In LogDNA

1. Log in to LogDNA.

2. Select the hosts from the ‘All Sources’ drop-down menu.

![](/img/Integrations/LogDNA/1.png)

**To Set Error Alerts:**

1. Select ERROR from the ‘All Levels’ drop-down menu.

![](/img/Integrations/LogDNA/2.png)

1. Click Save as new view under ‘Unsaved View’ drop-down menu. Enter the view name and click on attach an alert.

![](/img/Integrations/LogDNA/3.png)

![](/img/Integrations/LogDNA/4.png)

1. Select "View-Specific Alert" and then "Webhook".

![](/img/Integrations/LogDNA/5.png)

1. Select "Immediately after 1 line" under "Send an Alert" option. Paste the copied link in Webhook URL.

![](/img/Integrations/LogDNA/6.png)

**To Set Warning Alerts**

1. Select WARNING from the ‘All Levels’ drop-down menu.7

![](/img/Integrations/LogDNA/7.png)

1. Click Save as new view under ‘Unsaved View’ drop-down menu.

![](/img/Integrations/LogDNA/8.png)

1. Enter the view name and click on attach an alert.

![](/img/Integrations/LogDNA/9.png)

1. Select "View-Specific Alert" and then "Webhook".

2. Select ‘Immediately after 1 line’ under Send an alert option. Paste the copied link in Webhook URL.

![](/img/Integrations/LogDNA/10.png)

1. LogDNA is now integrated. Zenduty will create incidents from alerts.

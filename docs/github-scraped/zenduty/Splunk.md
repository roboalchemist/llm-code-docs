---
id: Splunk
title: Splunk
---
Splunk is a web-style interface for searching, monitoring, and analyzing machine-generated big data. To integrate Splunk with Zenduty, complete the following steps:

## On the Zenduty Dashboard

1. To add a new Splunk integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Splunk" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Splunk

1. Log in to Splunk. In the "Search and Report" app, search for the monitor metrics for Zenduty incidents to report on. As an example, we monitor "keyring":

![](/img/Integrations/Splunk/1.png)

1. Save this as an "Alert"  from the "Save As" window in the top right corner.

![](/img/Integrations/Splunk/2.png)

1. Fill in the form.

![](/img/Integrations/Splunk/3.png)

1. Click the "Add Actions" button under "Trigger Actions" and select "Webhook".

![](/img/Integrations/Splunk/4.png)

1. Paste the url you copied earlier, and "Save"

![](/img/Integrations/Splunk/5.png)

1. An alert for Zenduty (eg. "Login Alert") has been created and will show up in your "Alerts" tab.

![](/img/Integrations/Splunk/6.png)

Splunk is now Integrated with your Zenduty account.

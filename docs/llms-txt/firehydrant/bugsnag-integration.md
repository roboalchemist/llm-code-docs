# Source: https://docs.firehydrant.com/docs/bugsnag-integration.md

# BugSnag

BugSnag provides error monitoring for your cloud applications. Use alerts from BugSnag to power incidents and notifications in FireHydrant.

> 🚧 BugSnag and Signals
>
> If you're looking to connect BugSnag to FireHydrant to create alerts in Signals, we encourage you to look at creating a [Custom Event Source](https://docs.firehydrant.com/docs/custom-event-source). This document describes Alert Routing, which will not trigger alerts/pages to users.

## Configuration steps

1. First, authorize the BugSnag instance on [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations).

2. You'll see a webhook URL provided once you click **Authorize Application**.

3. From your BugSnag dashboard, use the gear icon to navigate to **Project Settings**, then click the **Data Forwarding** link.

4. On the Data Forwarding page, click **Post to a Webhook URL** and enter the URL shown on the FireHydrant BugSnag Integration page in the BugSnag modal.

<Image alt="BugSnag data forwarding page" align="center" width="650px" src="https://files.readme.io/f76163b-image.png">
  BugSnag data forwarding page
</Image>

<Image alt="BugSnag webhook URL modal" align="center" width="400px" src="https://files.readme.io/43a2b11-image.png">
  BugSnag webhook URL modal
</Image>

5. Click **Save**or the **Test** link to send a test webhook to FireHydrant. You should see the webhook logged on the FireHydrant Bugsnag configuration page (*in the integrations page where you originally got the webhook URL*) under the **Alert Routing** tab.

## Using Alert Routes with BugSnag

Once your BugSnag instance is configured, you can setup Alert Routes to take action on your alerts based on the data included in the alert. You can automatically open new incidents, send alerts to any Slack channel, log an alert in FireHydrant, or simply ignore it. To learn more, read about [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).
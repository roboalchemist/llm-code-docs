# Source: https://docs.firehydrant.com/docs/new-relic-integration.md

# New Relic

New Relic provides a suite of tools for tracking the performance of your cloud services. Use alerts from New Relic to power incidents and notifications in FireHydrant.

> 🚧 New Relic and Signals
>
> If you're looking to connect New Relic to FireHydrant to create alerts in Signals, you can use the generic webhooks integration. Checkout the Signals Integration guide for our [Generic Webhook](https://docs.firehydrant.com/docs/signals-generic-webhook). This document describes setting the integration up for Alert Routing, which does not connect to FireHydrant Signals.

## Configuration steps

1. First, authorize the New Relic integration on [FireHydrant's integrations page](https://app.firehydrant.io/organizations/integrations).

2. You'll see a webhook URL provided once you click **Authorize Application**.

3. In your New Relic account, click the **Alerts & AI** navigation item and, in the sub-navigation, click **Destinations**. In the **Add a destination** section near the top of the page, click the **Webhook** button.

4. Give your webhook a unique name, and paste the **URL** given to you in FireHydrant for the **Endpoint URL** (step 2). Then, click the **Save destination** button at the bottom.

5. From the **Alerts & AI** sub-navigation, click **Alert conditions (policies)** and find the policy for which you'd like to forward alerts to FireHydrant. Open the policy's **Notification settings** page and add a new workflow (or, if you already have an existing workflow, open its configuration form).

6. Click the **Webhook** button in the **Add channel** section to open a slideover form. Give the channel a name, select your FireHydrant webhook in the **Destination** dropdown, and, for the payload, paste in the following:

```jsx Payload
{
  "issue": {
    "id": {{ json issueId }},
    "title": {{ json issueTitle }},
    "description": {{ json annotations.description.[0] }},
    "priority": {{ json priority }},
    "state": {{ json state }},
    "created_at": {{ json createdAt }},
    "closed_at": {{ json closedAt }},
    "url": {{ json issuePageUrl }}
  }
}
```

<Image alt="New Relic channel form" align="center" width="650px" src="https://files.readme.io/f9d7ab1-image.png">
  New Relic channel form
</Image>

7. Click the **Save message** button at the bottom of the page, or the **Send test notification** button to send a test alert to FireHydrant. You should see the alert logged on the New Relic integration page (*where you originally got the webhook URL*) under the **Alert Routing** tab.

## Using Alert Routes with New Relic

Once your New Relic instance is configured, you can set up Alert Routes to take action on your alerts based on the data included in the alert. You can automatically open new incidents, send alerts to any Slack channel, log an alert in FireHydrant, or simply ignore it. To learn more, read about [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).
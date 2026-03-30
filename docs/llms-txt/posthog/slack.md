# Source: https://posthog.com/docs/support/slack.md

# Source: https://posthog.com/docs/self-host/configure/slack.md

# Source: https://posthog.com/docs/cdp/destinations/slack.md

# Source: https://posthog.com/docs/libraries/slack.md

# Slack - Docs

The PostHog app for Slack helps you stay connected to your product data and receive timely updates directly in your workspace.

## Features

The PostHog app for Slack provides three key capabilities:

1.  **Subscribe to product insights and dashboards** – Receive regular digests of your key metrics in chosen Slack channels.

2.  **Set up Slack notifications via PostHog Data Pipelines** – Get timely notifications of any event or action in PostHog.

## Installing the PostHog Slack app

### 1\. Adding the PostHog Slack app to your workspace

Starting in PostHog, you can add the PostHog Slack app to your workspace in [your project settings](https://app.posthog.com/settings/project#integration-slack).

![Allow PostHog Slack app permissions](https://res.cloudinary.com/dmukukwp6/image/upload/allow_slack_bb68272218.png)![Allow PostHog Slack app permissions](https://res.cloudinary.com/dmukukwp6/image/upload/allow_slack_bb68272218.png)

The PostHog Slack app will require some basic permissions which you can grant by clicking the **Allow** button.

### 2\. Adding the PostHog Slack app to specific channels

Then, head to **Slack** and add PostHog to **specific Slack channels**. To do this:

1.  In the Slack [channel header](https://slack.com/help/articles/360059928654-How-to-use-Slack--your-quick-start-guide#channels), click the top right menu and click **Open channel details**
2.  Navigate to the **Integrations** tab
3.  Click the **Add an app** button
4.  Under **In your workspace**, click **PostHog**

You can also try tagging the `@PostHog` bot in the channel to add it to the channel.

## Subscribing to insights and dashboards

You can receive regular updates of your [insights](/docs/product-analytics/insights.md) or [dashboards](/docs/product-analytics/dashboards.md) directly in Slack.

To set up a subscription:

1.  Open the insight or dashboard you want to subscribe to in PostHog
2.  Click the dropdown menu in the top right corner (three dots)
3.  Click **Subscribe**
4.  Click "Add subscription" and select **Slack** as the destination
5.  Choose the Slack channel where you want to receive updates
6.  Set your desired frequency (daily, weekly, monthly, etc.)

For more details, see our [subscriptions documentation](/docs/product-analytics/subscriptions.md).

## Setting up event notifications

You can send custom messages to Slack based on PostHog events or actions using [Data Pipelines destinations](/docs/cdp/destinations/slack.md).

Common use cases include:

-   Notifying your team when a user completes a key action
-   Alerting on errors or issues detected in your product
-   Sharing important user milestones with your team
-   Sending survey responses to a dedicated channel

To set up event notifications:

1.  Go to the [Data pipeline](https://app.posthog.com/data-management/destinations) tab in PostHog
2.  Click the [Destinations](https://app.posthog.com/data-management/destinations?search=slack) tab
3.  Click **\+ New destination** and search for "Slack"
4.  Configure which events or actions should trigger notifications
5.  Select your Slack connection and channel
6.  Template your message using event and person properties

For detailed setup instructions, see our [Slack destination documentation](/docs/cdp/destinations/slack.md).

## What can you do with this integration?

The PostHog Slack integration helps teams stay informed and make data-driven decisions without leaving Slack. You can:

-   **Stay updated on key metrics** – Receive regular reports on user behavior, feature adoption, and conversion rates
-   **React quickly to events** – Be notified immediately when important user actions or errors occur
-   **Share insights with your team** – Make product data accessible to everyone in relevant channels
-   **Monitor product health** – Keep an eye on critical metrics and get alerted to anomalies

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better
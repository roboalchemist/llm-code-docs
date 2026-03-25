# Source: https://posthog.com/docs/product-analytics/subscriptions.md

# Subscriptions - Docs

Subscriptions enable you to send [insights](/docs/product-analytics/insights.md) or [dashboards](/docs/product-analytics/dashboards.md) to your email or Slack on a regular basis.

###### Where is this feature available?

##### Free / Open-source

##### Paid

##### Boost

##### Scale

##### Enterprise

![Not available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDIwIDIwIj48cGF0aCBmaWxsPSIjRkI0RjBEIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMC4wNjQyIDcuODE5Nkw0LjI0NDU5IDJMMiA0LjI0NDU5TDcuODE5NiAxMC4wNjQyTDIuMTI4MzcgMTUuNzU1NEw0LjM3Mjk2IDE4TDEwLjA2NDIgMTIuMzA4OEwxNS40Njc1IDE3LjcxMjFMMTcuNzEyMSAxNS40Njc1TDEyLjMwODggMTAuMDY0MkwxNy44NDA1IDQuNTMyNDhMMTUuNTk1OSAyLjI4Nzg5TDEwLjA2NDIgNy44MTk2WiIgY2xpcC1ydWxlPSJldmVub2RkIi8+PC9zdmc+)![Available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDI4IDI4Ij48cGF0aCBmaWxsPSIjNzFBQTU1IiBkPSJNOS41MTAwMyAyNC4wMjk5TDAuNDEwMDMzIDE0LjkyOTlDLTAuMTM2Njc4IDE0LjM4MzIgLTAuMTM2Njc4IDEzLjQ5NjggMC40MTAwMzMgMTIuOTVMMi4zODk4OCAxMC45NzAxQzIuOTM2NiAxMC40MjMzIDMuODIzMDggMTAuNDIzMyA0LjM2OTc5IDEwLjk3MDFMMTAuNSAxNy4xMDAyTDIzLjYzMDIgMy45NzAwOUMyNC4xNzY5IDMuNDIzMzggMjUuMDYzNCAzLjQyMzM4IDI1LjYxMDEgMy45NzAwOUwyNy41ODk5IDUuOTVDMjguMTM2NyA2LjQ5NjcxIDI4LjEzNjcgNy4zODMxNCAyNy41ODk5IDcuOTI5OUwxMS40ODk5IDI0LjAzQzEwLjk0MzIgMjQuNTc2NyAxMC4wNTY3IDI0LjU3NjcgOS41MTAwMyAyNC4wMjk5VjI0LjAyOTlaIi8+PC9zdmc+)![Available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDI4IDI4Ij48cGF0aCBmaWxsPSIjNzFBQTU1IiBkPSJNOS41MTAwMyAyNC4wMjk5TDAuNDEwMDMzIDE0LjkyOTlDLTAuMTM2Njc4IDE0LjM4MzIgLTAuMTM2Njc4IDEzLjQ5NjggMC40MTAwMzMgMTIuOTVMMi4zODk4OCAxMC45NzAxQzIuOTM2NiAxMC40MjMzIDMuODIzMDggMTAuNDIzMyA0LjM2OTc5IDEwLjk3MDFMMTAuNSAxNy4xMDAyTDIzLjYzMDIgMy45NzAwOUMyNC4xNzY5IDMuNDIzMzggMjUuMDYzNCAzLjQyMzM4IDI1LjYxMDEgMy45NzAwOUwyNy41ODk5IDUuOTVDMjguMTM2NyA2LjQ5NjcxIDI4LjEzNjcgNy4zODMxNCAyNy41ODk5IDcuOTI5OUwxMS40ODk5IDI0LjAzQzEwLjk0MzIgMjQuNTc2NyAxMC4wNTY3IDI0LjU3NjcgOS41MTAwMyAyNC4wMjk5VjI0LjAyOTlaIi8+PC9zdmc+)![Available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDI4IDI4Ij48cGF0aCBmaWxsPSIjNzFBQTU1IiBkPSJNOS41MTAwMyAyNC4wMjk5TDAuNDEwMDMzIDE0LjkyOTlDLTAuMTM2Njc4IDE0LjM4MzIgLTAuMTM2Njc4IDEzLjQ5NjggMC40MTAwMzMgMTIuOTVMMi4zODk4OCAxMC45NzAxQzIuOTM2NiAxMC40MjMzIDMuODIzMDggMTAuNDIzMyA0LjM2OTc5IDEwLjk3MDFMMTAuNSAxNy4xMDAyTDIzLjYzMDIgMy45NzAwOUMyNC4xNzY5IDMuNDIzMzggMjUuMDYzNCAzLjQyMzM4IDI1LjYxMDEgMy45NzAwOUwyNy41ODk5IDUuOTVDMjguMTM2NyA2LjQ5NjcxIDI4LjEzNjcgNy4zODMxNCAyNy41ODk5IDcuOTI5OUwxMS40ODk5IDI0LjAzQzEwLjk0MzIgMjQuNTc2NyAxMC4wNTY3IDI0LjU3NjcgOS41MTAwMyAyNC4wMjk5VjI0LjAyOTlaIi8+PC9zdmc+)![Available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDI4IDI4Ij48cGF0aCBmaWxsPSIjNzFBQTU1IiBkPSJNOS41MTAwMyAyNC4wMjk5TDAuNDEwMDMzIDE0LjkyOTlDLTAuMTM2Njc4IDE0LjM4MzIgLTAuMTM2Njc4IDEzLjQ5NjggMC40MTAwMzMgMTIuOTVMMi4zODk4OCAxMC45NzAxQzIuOTM2NiAxMC40MjMzIDMuODIzMDggMTAuNDIzMyA0LjM2OTc5IDEwLjk3MDFMMTAuNSAxNy4xMDAyTDIzLjYzMDIgMy45NzAwOUMyNC4xNzY5IDMuNDIzMzggMjUuMDYzNCAzLjQyMzM4IDI1LjYxMDEgMy45NzAwOUwyNy41ODk5IDUuOTVDMjguMTM2NyA2LjQ5NjcxIDI4LjEzNjcgNy4zODMxNCAyNy41ODk5IDcuOTI5OUwxMS40ODk5IDI0LjAzQzEwLjk0MzIgMjQuNTc2NyAxMC4wNTY3IDI0LjU3NjcgOS41MTAwMyAyNC4wMjk5VjI0LjAyOTlaIi8+PC9zdmc+)

> **Looking to subscribe to events or actions?** See our [realtime destination docs](/docs/cdp/destinations.md) to learn how to send event or action data to webhooks, Slack, and more.

To get started, open the dropdown menu in the top right of any insight or dashboard and click **Subscribe**.

![New Subscription Button](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/features/subscriptions/new-subscription-button-light-mode.png)![New Subscription Button](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/features/subscriptions/new-subscription-button-dark-mode.png)

## Selecting insights for dashboard subscriptions

When creating a subscription for a dashboard, you can select which specific insights to include. This is useful when different teams subscribe to the same dashboard but only need the insights relevant to them.

-   You can include up to six insights per subscription.
-   New subscriptions automatically pre-select the first six insights from the dashboard.
-   For dashboards with more than 10 insights, a search box appears to help you find specific ones.
-   Selected insights appear in the subscription in the same order as they appear on the dashboard.

## Naming your subscriptions

You can give each subscription a custom name to help distinguish between them. This is especially useful when you have multiple subscriptions to the same dashboard or insight – for example, different reports for different teams or frequencies.

For Slack subscriptions, the custom name appears in the message header. For example, a subscription named "Weekly KPI Report" for a dashboard called "Main Dashboard" displays as **Weekly KPI Report** (dashboard: Main Dashboard) in the Slack message. Without a custom name, the message references the dashboard or insight name directly.

## Email subscriptions

When configuring an email subscription you can subscribe multiple emails at once, whether they are a member of your PostHog team or not and set the frequency of the subscription.

![New Subscription Button](https://res.cloudinary.com/dmukukwp6/image/upload/v1715288461/posthog.com/contents/images/features/subscriptions/email-light.png)![New Subscription Button](https://res.cloudinary.com/dmukukwp6/image/upload/v1715288461/posthog.com/contents/images/features/subscriptions/email-dark.png)

Once saved, any emails not already subscribed receives a notification email informing them what you have subscribed them to. You can optionally include a small personalized message that is sent along to them.

## Slack subscriptions

There are three steps to setting up a Slack subscription:

1.  Adding the PostHog Slack app to your workspace
2.  Adding the PostHog Slack app to specific channels
3.  Creating a new Slack subscription in PostHog

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

### 3\. Creating a new Slack subscription in PostHog

After installing the app, head back to PostHog and add a new subscription. You can do this in any dashboard or insight by clicking the top right menu, then **Subscribe**, and then **Add subscription**.

![Add to Slack button](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/features/subscriptions/slack-subscription-add-light-mode.png)![Add to Slack button](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/features/subscriptions/slack-subscription-add-dark-mode.png)

You can then select any channel the app has access to and set a frequency. **Private channels** are only listed if you have already added PostHog to the relevant channel.

![Slack channel selection](https://res.cloudinary.com/dmukukwp6/image/upload/slack_config_light_b5a1c93ad5.png)![Slack channel selection](https://res.cloudinary.com/dmukukwp6/image/upload/slack_config_dark_3abf83e8fe.png)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better
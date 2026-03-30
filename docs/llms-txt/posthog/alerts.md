# Source: https://posthog.com/docs/error-tracking/alerts.md

# Source: https://posthog.com/docs/alerts.md

# Alerts - Docs

Alerts enable you to monitor your [insights](/product-analytics.md) and get notified when the value of the insight breaches a threshold that you've set (for example, the number of unique visitors to your site increased by 5% week over week). Currently, alerts are supported on all [trends](/docs/product-analytics/trends.md).

## How to create an alert

1.  Alerts are based off of [insights](/docs/product-analytics/insights.md). You can pick any existing trend insight or create a new one.
2.  Click **Actions** in the sidebar and select **Alerts**. This shows you all the alerts for this insight.

![Alert button in actions bar](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/Screenshot_2026_03_13_at_9_50_26_AM_ccce74247b.png)![Alert button in actions bar](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/Screenshot_2026_03_13_at_9_50_34_AM_ee7c2e9444.png)

3.  Click the **New alert** button.

    ![new alert button](https://res.cloudinary.com/dmukukwp6/image/upload/new_alert_button_30d3dde83c.png)![new alert button](https://res.cloudinary.com/dmukukwp6/image/upload/new_alert_dark_19591ee179.png)

4.  Set a name for the alert.

5.  Select a 'series' you want to alert on. These are the different events/values you're plotting in the insight. For example, an insight might have multiple series like `A - $pageview` (total count of page views for a URL) and `B - signed_up` (count of users who signed up on the page). You can select either `A` or `B`, which will determine if the alert gets checked against the value for `A` (total page views) or `B` (signups).

    ![series picker](https://res.cloudinary.com/dmukukwp6/image/upload/series_picker_aa01668862.png)![series picker](https://res.cloudinary.com/dmukukwp6/image/upload/new_alert_options_dark_7adf700d24.png)

6.  Select the alert type:

    -   **has value** - checks the series against a specific value.
    -   **increases by**/**decreases by** - checks if the series has changed by a certain amount.

    ![alert type picker](https://res.cloudinary.com/dmukukwp6/image/upload/alert_type_picker_18909b0b33.png)![alert type picker](https://res.cloudinary.com/dmukukwp6/image/upload/new_alert_type_dark_b3620b34da.png)

7.  Set the threshold. This is the value you want to compare the series value against. For example, you can set a value of 5000 in the "more than" field to check when pageviews have exceeded 5k.

8.  (Optional) For relative alerts (**increases by**/**decreases by**), you can set a percentage threshold. It compares the percentage change in the series value to the thresholds you've set.

    ![percentage threshold](https://res.cloudinary.com/dmukukwp6/image/upload/percentage_threshold_1940ead9e6.png)![percentage threshold](https://res.cloudinary.com/dmukukwp6/image/upload/alert_relative_threshold_dark_02aa4741c3.png)

9.  Select how often you want the alert to be checked (e.g. every hour, every day, every week, every month)

10.  Pick who should be notified when the alert is triggered. You can add email recipients, Slack channels, or webhook URLs directly in the alert form.

     ![filled alert](https://res.cloudinary.com/dmukukwp6/image/upload/filled_alert_627158e6bb.png)![filled alert](https://res.cloudinary.com/dmukukwp6/image/upload/alert_people_dark_0ccd7611bd.png)

11.  Click **Create alert**, and you're done!

     ![insight alerts](https://res.cloudinary.com/dmukukwp6/image/upload/insight_alerts_5k_daef47ade1.png)![insight alerts](https://res.cloudinary.com/dmukukwp6/image/upload/created_alert_dark_1710da74dc.png)

You can now view all the alerts set on the insight. To view all the alerts set, click [Product analytics](https://app.posthog.com/insights) in the sidebar and then click the **Alerts** tab.

![all alerts](https://res.cloudinary.com/dmukukwp6/image/upload/all_alerts_d92386e45a.png)![all alerts](https://res.cloudinary.com/dmukukwp6/image/upload/all_alerts_dark_80be487707.png)

## Create alerts with PostHog AI

You can also create and manage alerts using [PostHog AI](/docs/posthog-ai/overview.md) with natural language commands. Open [PostHog AI](https://app.posthog.com/#panel=max) from anywhere in the app and describe the alert you want.

**Example commands:**

-   "Alert me when daily signups drop below 100"
-   "Create an alert when pageviews increase by more than 50%"
-   "Notify me if revenue drops more than 20% week over week"
-   "Change my alert threshold to 200"
-   "Disable the signups alert"

PostHog AI can create alerts on existing insights or generate new trend insights and set up alerts on them automatically. To update existing alerts, PostHog AI finds the alert by name and applies your changes.

**Note**

PostHog AI can only create alerts on [trends](/docs/product-analytics/trends.md). Other insight types like funnels and retention don't support alerts.

## Relative alerts

Relative alerts check for change in the value of an insight. For example, if a value increases by 5% in a week. To create a relative alert, you just need to change the **has value** option to **increases by** or **decreases by**. This will then also enable you to set a percentage threshold.

![relative alert picker](https://res.cloudinary.com/dmukukwp6/image/upload/relative_alert_picker_fa04215397.png)![relative alert picker](https://res.cloudinary.com/dmukukwp6/image/upload/alert_relative_increase_dark_0855f0afee.png)

### Thresholds

We support both **absolute value** thresholds (insight value more than or less than a certain number) or **percentage** thresholds (insight value changed by a certain percentage). Percentage thresholds are only available for relative alerts (as you need to compare two values to figure out percentage change).

## Notifications

Alerts support email notifications, Slack messages, and webhooks. You can configure these directly when creating or editing an alert.

### Add Slack or webhook notifications

When creating or editing an alert, you can add notification destinations inline:

1.  In the **Destinations** section, select **Slack** or **Webhook** from the dropdown.

2.  For Slack notifications:

    -   If you haven't connected Slack yet, click **Connect to Slack** to set up the integration.
    -   Once connected, select the channel where you want alerts sent.
3.  For webhook notifications:

    -   Enter the webhook URL where you want alerts sent.
4.  Click **Add notification** to add the destination.

5.  Click **Create alert** or **Save** to apply your changes.

You can add multiple notification destinations to a single alert. Each destination appears in the list with its status.

## Advanced options

You can configure alerts to skip checking on weekends. This is useful for daily alerts which would normally trigger on weekends.

### Check ongoing period

Alerts also enable you to check the current/ongoing period. When enabled, this checks the insight value for the ongoing period (current week/month) that hasn't yet completed. Use this if you want to be alerted right away when the insight value rises/increases above threshold

## Alerts on breakdowns

When you set an alert on a trend with a breakdown, the alert will be triggered when any of the breakdown values breaches the thresholds set.

![alert on breakdown](https://res.cloudinary.com/dmukukwp6/image/upload/breakdown_alert_7bd87114cb.png)![alert on breakdown](https://res.cloudinary.com/dmukukwp6/image/upload/alert_with_breakdown_dark_475c3803c3.png)

## Automatically disabled alerts

PostHog automatically disables alerts that have an invalid configuration. When this happens, subscribed users receive an email notification explaining the reason the alert was disabled.

Common reasons an alert may be auto-disabled:

-   The insight was modified and is no longer compatible with the alert configuration (e.g., the insight query type changed from a trend to a funnel)
-   The series referenced by the alert was removed from the insight
-   A relative alert condition (**increases by**/**decreases by**) was set on a non-time-series trend (e.g., a pie chart or number)
-   An absolute value alert was configured with a percentage threshold

**Re-enable manually**

Disabled alerts don't re-enable themselves. After fixing the configuration issue, go to the **Alerts** tab on the insight and manually re-enable the alert.

## Further reading

For more ideas on how to get started with Alerts, check out our [alerts examples](/blog/alerts-examples.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better
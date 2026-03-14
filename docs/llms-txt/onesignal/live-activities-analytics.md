# Source: https://documentation.onesignal.com/docs/en/live-activities-analytics.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Activities Analytics

> Learn how to analyze and measure the performance of your iOS Live Activities with OneSignal. Track delivery rates, clicks, and user engagement to optimize your real-time update strategy.

Understand how your Live Activities are performing by tracking key metrics like delivery rates, clicks, and user engagement. OneSignal provides comprehensive analytics to help you optimize your real-time update strategy.

<Note>
  This guide covers analytics for [Live Activities](./live-activities). Make sure you have Live Activities set up before diving into analytics.
</Note>

***

## Overview

Live Activities analytics help you understand:

* How many users are receiving your updates
* Whether users are engaging with your Live Activities
* Where delivery failures are occurring
* How your subscription base is changing over time

***

## Key metrics

Live Activities offer the following metrics. For more details, see [Engagement Trends](./engagement-analytics).

| Metric                 | Definition                                                                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Sent**               | Live Activities sent from OneSignal to Apple Push Notification service (APNs). Includes push-to-start and push-to-update notifications. |
| **Confirmed Delivery** | Live Activities confirmed delivered to devices. Requires iOS SDK 5.2.15+ and OneSignal setup method.                                    |
| **Failed**             | Live Activities that failed to deliver due to an error.                                                                                 |
| **Unsubscribed**       | Subscriptions marked unsubscribed when users dismiss a Live Activity or disable Live Activities in settings.                            |
| **Clicked**            | Total clicks across all Live Activities. Multiple clicks by the same user are counted separately.                                       |

<Note>
  **Confirmed Delivery** and **Clicked** metrics require iOS SDK version **5.2.15 or higher**. Ensure your app is updated to take advantage of these tracking capabilities.
</Note>

***

## Message reports

Use message reports to analyze the effectiveness of your Live Activities by tracking delivery and click rates.

<Frame caption="Live Activity Report">
  <img src="https://mintcdn.com/onesignal/vW9xDwSIrN3V7agt/images/live-activities/live-activity-report.png?fit=max&auto=format&n=vW9xDwSIrN3V7agt&q=85&s=e9e93614f215a30145dffaf02731fce8" width="1600" height="1171" data-path="images/live-activities/live-activity-report.png" />
</Frame>

### Accessing message reports

1. Navigate to **Sent Messages** in your OneSignal dashboard
2. Filter by **Live Activities** to view only Live Activity messages
3. Click on any Live Activity to view its detailed report

### Statistics and definitions

| Metric                 | Definition                                                                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delivered**          | The number of subscriptions that received the Live Activity.                                                                                       |
| **Confirmed Delivery** | The number of subscriptions that confirmed receiving the activity.                                                                                 |
| **Failed**             | The number of subscriptions that did not receive the Live Activity because of an error.                                                            |
| **Unsubscribed**       | The number of subscriptions that did not receive the Live Activity because they uninstalled the app, opted out, and have not opened the app since. |
| **Clicked**            | Total clicks across all Live Activities. Multiple clicks by the same user are counted separately.                                                  |

***

## Audience activity

The audience activity panel allows you to see the recent activity of users related to the Live Activity, including deliveries, clicks, failures, and unsubscribes.

### Viewing audience activity

1. Open a Live Activity message report
2. Locate the **Audience Activity** panel
3. Select the statistic type you want to view:
   * **Deliveries** — Users who received the Live Activity
   * **Clicks** — Users who tapped on the Live Activity
   * **Failures** — Users who did not receive the Live Activity due to errors
   * **Unsubscribes** — Users who unsubscribed or were removed

### Understanding user behavior

Use the audience activity data to:

* Identify patterns in user engagement
* Troubleshoot delivery issues for specific user segments
* Track the impact of Live Activity content on click rates
* Monitor subscription health over time

***

## Exporting results

You can export the audience activity for your Live Activity by clicking the **Export** button above the audience activity panel.

### Export options

* **Single statistic** — Export only the currently selected activity type (e.g., just clicks or just failures)
* **All statistics** — Export all audience activity data at once

### Receiving your export

Exporting audience activity will send an email with the results directly to the logged-in user's email address. The export includes:

* User identifiers
* Timestamp of the activity
* Activity type
* Device and platform information (where available)

<Note>
  Large exports may take several minutes to process. You'll receive an email notification when your export is ready.
</Note>

***

## Analyzing performance

### Delivery rate

Calculate your delivery rate to understand how effectively your Live Activities are reaching users:

```
Delivery Rate = (Confirmed Delivery / Sent) × 100
```

A healthy delivery rate is typically **95% or higher**. Lower rates may indicate:

* Outdated push tokens
* Users with Live Activities disabled
* Network connectivity issues

### Click-through rate (CTR)

Measure engagement with your Live Activities:

```
CTR = (Clicked / Confirmed Delivery) × 100
```

### Benchmarking your performance

Compare your metrics over time to identify trends:

* **Week-over-week** — Are delivery rates improving?
* **By content type** — Do certain Live Activity types perform better?
* **By time of day** — When are users most engaged?

***

## Troubleshooting common issues

### High failure rates

If you're seeing elevated failure rates:

1. **Check push token validity** — Tokens expire when users uninstall or reinstall your app
2. **Verify APNs configuration** — Ensure your push certificates are up to date
3. **Review error messages** — Check the failure details for specific error codes

### Low confirmed delivery

If confirmed delivery is significantly lower than sent:

1. **Verify SDK version** — Confirmed delivery requires iOS SDK 5.2.15+
2. **Check OneSignal setup** — Ensure the OneSignal setup method is properly implemented
3. **Consider network conditions** — Some users may have intermittent connectivity

### Declining click rates

If click rates are dropping:

1. **Review content relevance** — Are your updates providing value?
2. **Check timing** — Are you sending updates at appropriate times?
3. **Audit UI/UX** — Ensure your Live Activity design encourages interaction

***

## Best practices for analytics

### Regular monitoring

* Review Live Activity performance weekly
* Set up alerts for significant metric changes
* Compare performance across different Live Activity types

### Data-driven optimization

* A/B test different content approaches
* Experiment with update frequency
* Analyze which events drive the most engagement

### Historical analysis

Live Activity data is available in the dashboard for up to **30 days**. For longer-term analysis:

* Export data regularly
* Track trends in a spreadsheet or analytics tool
* Document changes to correlate with performance shifts

***

## FAQ

### How long is Live Activity data retained?

You can view historically sent Live Activities (up to 30 days) in the dashboard under **Sent Messages** after filtering for Live Activities.

### Why is my confirmed delivery lower than sent?

Confirmed delivery requires iOS SDK version 5.2.15 or higher and proper OneSignal setup. If your app has users on older SDK versions, they won't report confirmed delivery.

### Can I track individual user journeys?

Yes, the audience activity panel allows you to see individual user activity. You can also export this data for deeper analysis.

### How do I improve my click-through rate?

Focus on providing timely, relevant updates that offer clear value to users. Ensure your Live Activity design has clear tap targets and compelling content.

***

Built with [Mintlify](https://mintlify.com).

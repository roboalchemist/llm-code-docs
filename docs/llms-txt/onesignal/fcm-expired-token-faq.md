# Source: https://documentation.onesignal.com/docs/en/fcm-expired-token-faq.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FCM expired token FAQ

> Why Android and Chrome push subscriptions get unsubscribed due to FCM token expiry, Google spam suppression, and how to troubleshoot unsubscribe spikes.

Firebase Cloud Messaging (FCM) delivers push notifications to Android devices and Chrome browsers. FCM [expires tokens for devices](https://firebase.google.com/docs/cloud-messaging/manage-tokens#stale-and-expired-tokens) that have been inactive for more than 270 days. These devices may be lost, destroyed, or put into storage and are considered no longer reachable.

When FCM expires a token, OneSignal marks the subscription as **Unsubscribed** the next time you send a push notification to that device.

This is a cleanup exercise from Google — your expected clicks, sessions, and the value you get from OneSignal do not change. You may also see benefits:

* **More accurate analytics** — your CTR reflects your actual reachable audience
* **Faster delivery** — smaller audiences mean campaigns finish delivering faster
* **Less manual work** — no need to manually manage inactive audiences

## Recent changes driving unsubscribe spikes

Seeing sudden spikes in unsubscribes has become more common due to a series of aggressive updates Google has implemented for Chrome and FCM aimed at curbing notification spam and cleaning up inactive data.

These updates include:

* **AI-driven spam suppression (Chrome 143+)** — Chrome actively identifies and suppresses notifications from sites with low engagement.
* **Automatic unsubscription for inactive users** — Introduced in 2024 and ramped up aggressively in late 2025 and early 2026, Chrome's "Safety Check" feature automatically unsubscribes users from sites that send a high volume of notifications but receive very low user engagement.
* **FCM data policy enforcement** — A major FCM policy update on token removal due to data retention has caused peaks in unsubscribes for campaigns targeting all users. Profiles inactive for roughly a year are archived and marked as unsubscribed to keep subscriber bases deliverable.

## Troubleshooting unsubscribe spikes

If you notice a sudden increase in unsubscribes for Android or Chrome subscriptions, follow these steps:

<Steps>
  <Step title="Verify your SDK version">
    Check your site or app to confirm OneSignal is on the latest SDK version and that you have not removed the SDK or made any recent changes to your integration.
  </Step>

  <Step title="Review your engagement trends">
    Navigate to **Dashboard > Analytics > Engagement Trends** to check your send, delivery, and unsubscribe patterns over time. See [Aggregate trends](./analytics-overview#aggregate-trends) for details on reading these charts.
  </Step>

  <Step title="Check your send frequency">
    Due to the way push works, if users uninstall the app, clear browser data, or unsubscribe from notifications in their device settings and never return to the app or site, it takes 2 or more push notifications to detect the unsubscribe. See [When do push subscription statuses update?](./subscriptions#when-do-push-subscription-statuses-update) for more details.

    If you go long periods without sending messages to all your users, you will see spikes in unsubscribes when you resume sending. Send messages to all users at least once or twice a month to detect unsubscribes gradually rather than in large batches.
  </Step>

  <Step title="Evaluate your delivery metrics">
    If you regularly send messages to all users and your confirmed delivery and click metrics are normal, the unsubscribes are likely FCM cleaning up invalid tokens for your app. This does not affect your reachable audience.
  </Step>
</Steps>

## FAQ

### Why did I see a sudden increase in Android and/or Chrome unsubscribes?

FCM expires tokens for devices inactive for more than 270 days. When you send a push notification to those devices, their push subscriptions are marked as unsubscribed. You will see this reflected as increased unsubscribe counts in your dashboard and delivery reports.

Google has also introduced [additional changes](#recent-changes-driving-unsubscribe-spikes) that more aggressively remove inactive or low-engagement subscriptions.

### What happens after a device token is expired?

The expired token is permanently invalid. The subscription is marked as **Unsubscribed** in OneSignal after attempting to send a push notification to the device.

### Does inactivity on my app specifically trigger token expiry?

No. FCM measures inactivity at the **device level**, not per Firebase project. Even if a device has not opened your app in 270+ days, the token remains valid as long as the device itself is active. You will not know a token is expired until you send a notification and see the subscription marked as unsubscribed.

### What if an inactive device comes back online?

When the user opens your app again, the OneSignal SDK automatically retrieves a new push token and updates the existing subscription record. The user keeps their subscribed status and does not need to opt in to push again — push permissions are stored on the device for a given app.

### Can I tell the difference between an active unsubscribe and an FCM token expiry?

No. FCM does not differentiate between these types of unsubscribes, so OneSignal cannot distinguish them either.

***

Built with [Mintlify](https://mintlify.com).

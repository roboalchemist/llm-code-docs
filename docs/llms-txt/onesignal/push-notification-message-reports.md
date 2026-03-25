# Source: https://documentation.onesignal.com/docs/en/push-notification-message-reports.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Push message reports

> Each push notification's delivery report with confirmed delivery, failure diagnostics, CTR, audience activity, and retargeting.

Push message reports help you track the performance of individual push message sends, including delivery outcomes, user engagement (CTR), device-level confirmations, and error diagnostics.

<Frame caption="Push message report high-level stats.">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/7fb7f716c8be4e153110e21fe514e872347188578674781fc75787cbc2f60136-Screenshot_2025-03-11_at_2.48.15_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=3a0aae3f8a7376838920bd16234c6876" width="2292" height="386" data-path="images/docs/7fb7f716c8be4e153110e21fe514e872347188578674781fc75787cbc2f60136-Screenshot_2025-03-11_at_2.48.15_PM.png" />
</Frame>

***

## Delivery metrics

OneSignal sends push notifications to **push services** (Google FCM, Apple APNs, Huawei HMS) which deliver them to your users' devices (Subscriptions). The Delivered, Unsubscribed, and Failed metrics come from these push services. The [Confirmed Delivery](./confirmed-delivery) and Clicked metrics come from the OneSignal SDK on the device.

| Metric               | Definition                                                                                                                                                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Sent**             | The number of messages successfully sent from OneSignal to the provider.                                                                                                                                                                                     |
| **Total Attempted**  | The number of messages we attempted to send. This includes messages successfully sent to the push provider and failures. This is a **derived** metric and is a sum of successes, failures and errors while attempting to send to the provider.               |
| **Audience**         | The number of subscriptions in the targeted segment(s).                                                                                                                                                                                                      |
| **Delivered**        | The number of push subscriptions to which the push service (FCM, APNs, HMS) reported delivering the notification. This is distinct from [Confirmed Delivery](/docs/en/confirmed-delivery), which is verified by the OneSignal SDK on the device.             |
| **Unsubscribed**     | The number of push subscriptions that did not receive the message because they uninstalled the app, cleared browser data, or opted out of push and have not opened the app since. We will **not** attempt to send to these subscriptions in future messages. |
| **Failed**           | The number of push subscriptions that did not receive a notification because of an error. We will attempt to send to these subscriptions in future messages.                                                                                                 |
| **Clicked**          | The number of clicks on a notification.                                                                                                                                                                                                                      |
| **Frequency Capped** | The number of push subscriptions that the notification was not sent to due to frequency cap settings.                                                                                                                                                        |

The following metrics are specific to push message reports:

| Metric                 | Definition                                                                                                                                                             |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Confirmed Delivery** | The number of push Subscriptions that confirmed receiving the message.                                                                                                 |
| **Remaining**          | The number of notifications still queued on the OneSignal side for sending.                                                                                            |
| **Click-Through Rate** | Calculated as `(Clicks / Delivered) * 100%`.                                                                                                                           |
| **Confirmed CTR**      | Calculated as `(Clicks / Confirmed Delivered) * 100%`.                                                                                                                 |
| **Influenced Opens**   | The number of app opens that occurred after receiving the notification, without clicking. Based on time window set in **Settings > Push & In-App > Influenced Opens**. |

<Note>
  For detailed metric definitions across all channels, see the [Metrics Glossary](./analytics-metrics-glossary).
</Note>

### Failure message troubleshooting

These errors prevented OneSignal from delivering the message to the push provider:

| Error                                                                                                                                                                  | Type | Troubleshooting Steps                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **401 Unauthorized**                                                                                                                                                   | Web  | Web push server gave an unclear 401 error. Retry cautiously — it may cause duplicate sends.                                                                                       |
| **404 Not Found**                                                                                                                                                      | Web  | Invalid push subscription endpoint (bad token).                                                                                                                                   |
| **Authentication Error**                                                                                                                                               | FCM  | Check your [FCM credentials](./android-firebase-credentials), re-upload the service account file, and try again.                                                                  |
| **[DeviceTokenNotForTopic](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html)** | APNs | Token’s Bundle ID does not match your APNs key or certificate. Fix in [p8 token](./ios-p8-token-based-connection-to-apns) or [p12 setup](./ios-p12-generate-certificates).        |
| **Expired Certificate**                                                                                                                                                | APNs | Your p12 certificate has expired. See [certificate setup](./ios-p12-generate-certificates).                                                                                       |
| **FcmV1InvalidToken / Not Found**                                                                                                                                      | FCM  | Invalid push token. Check [Firebase credentials](./android-firebase-credentials). Devices must reopen app to refresh tokens.                                                      |
| **None / Missing**                                                                                                                                                     | FCM  | Firebase Cloud Messaging API may not be enabled in your project. Activate in the Firebase Console and retry.                                                                      |
| **Permission Denied**                                                                                                                                                  | FCM  | Check the full error message for which permission is missing. [Update the permission for the Service Account file](./android-firebase-credentials) and re-upload it to OneSignal. |
| **SenderIdMismatch**                                                                                                                                                   | FCM  | FCM v1 Sender ID mismatch. Verify [Firebase credentials](./android-firebase-credentials). Users must reopen the app for updated tokens.                                           |
| **[TopicDisallowed](https://developer.apple.com/documentation/usernotifications/handling-notification-responses-from-apns)**                                           | APNs | APNs token mismatch. Check your Team ID, Key ID, and Bundle ID in [p8 config](./ios-p8-token-based-connection-to-apns).                                                           |

## Delivery status

| Status            | Description                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------- |
| **Delivered**     | Push service has reported delivery of the message to recipients.                                  |
| **Scheduled**     | Message is scheduled for future delivery.                                                         |
| **Sending**       | Message is actively being sent.                                                                   |
| **Queued**        | Message is waiting to be sent.                                                                    |
| **Canceled**      | Message was manually canceled. See [Cancel push notifications](./push#cancel-push-notifications). |
| **No Recipients** | No valid audience at send time (e.g. unsubscribed or out of segment).                             |
| **Failed**        | OneSignal could not send the message due to errors.                                               |

***

## Conversions

<Info>
  **Coming soon** — [Conversion metrics](/docs/en/conversion-metrics) will be available on message reports. Once available, you will see attributed and influenced conversions for each message directly in its report. See [Conversion metrics](/docs/en/conversion-metrics) for details on the attribution model and setup instructions.
</Info>

## Message statistics

The message statistics graph tracks clicks, sessions, and custom outcomes over the 30 days following a send. Use it to see whether engagement occurred immediately after delivery or continued over time.

<Card title="Custom outcomes (legacy)" icon="clock-rotate-left" href="./custom-outcomes"> Track actions like purchases or sign-ups from push and in-app messages. Being replaced by Conversion metrics. </Card>

<Frame caption="Message statistics graph showing clicks, sessions, and custom outcomes over time.">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d3e4db9-Screenshot_2023-07-25_at_2.18.57_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=03607676051399984b2966a93216b3a7" width="1364" height="993" data-path="images/docs/d3e4db9-Screenshot_2023-07-25_at_2.18.57_PM.png" />
</Frame>

<Warning>
  Messages sent via the OneSignal API are only retained for 30 days. Use [Template Analytics](./template-analytics) to track performance over time, or [export your data](./exporting-data) for offline analysis.
</Warning>

## Audience activity

The **Audience activity** report shows how each Subscription interacted with a specific message. Results are grouped into categories so you can diagnose delivery issues, measure engagement, identify unsubscribes tied to a specific message, and segment audiences for retargeting or export.

<Frame caption="Audience activity tabs and table">
  <img src="https://mintcdn.com/onesignal/DAcDCtZEGr7EAIA1/images/push/push-reports-audience-activity.png?fit=max&auto=format&n=DAcDCtZEGr7EAIA1&q=85&s=6ca39ae71008717bc4606b0633369949" alt="Audience activity screenshot" width="2048" height="706" data-path="images/push/push-reports-audience-activity.png" />
</Frame>

<Tabs>
  <Tab title="Categories">
    | Category                     | Description                                                |
    | ---------------------------- | ---------------------------------------------------------- |
    | **Sent**                     | Message was sent to the device.                            |
    | **Confirmed Delivery**       | Delivery was confirmed by the device.                      |
    | **Did Not Confirm Delivery** | Delivery confirmation was not received.                    |
    | **Clicked**                  | User clicked the notification.                             |
    | **Did Not Click**            | User did not click the notification.                       |
    | **Failed**                   | Delivery failed.                                           |
    | **Unsubscribed**             | The subscription unsubscribed after receiving the message. |

    Each tab displays the number of recipients in that category and lets you drill into the individual subscription records.
  </Tab>

  <Tab title="Table columns">
    | Column                  | Description                                                       |
    | ----------------------- | ----------------------------------------------------------------- |
    | **External ID**         | Your system identifier (if set).                                  |
    | **OneSignal ID**        | Unique OneSignal user ID.                                         |
    | **Subscription ID**     | Unique subscription instance (device + app/browser).              |
    | **Device**              | Browser or OS type. If you see `()`, the device has been deleted. |
    | **Subscription Status** | Current status (for example, Subscribed, Unsubscribed).           |
    | **Sent**                | Time the message was sent.                                        |
    | **Confirmed Delivery**  | Time delivery was confirmed by the device, or `-` if not.         |
    | **Clicked**             | Timestamp if the user clicked, or `-` if not.                     |
    | **Failed**              | Indicates if delivery failed.                                     |
    | **Unsubscribed**        | Indicates if the user unsubscribed after receiving the message.   |
    | **Failure message**     | Error message if delivery failed (for example, "Invalid token").  |
  </Tab>
</Tabs>

<Warning>
  Audience activity data is only available for **30 days** from the time the message is sent. Export results if you need to retain them longer.
</Warning>

### Retargeting audiences

From the **Audience activity** view, you can send a **Retargeted Message** directly to any category (for example, all users who did not click).

This makes it easy to follow up with users who didn't engage, re-engage those who churned, or reinforce success with users who confirmed delivery.

***

### Exporting results

You can download audience data with the **Export** menu:

* **Selected activity** – exports only the currently viewed tab (for example, all users who failed delivery).
* **All activities** – exports the full report across every category.

Exports let you analyze results offline, share with other teams, or merge with your CRM and analytics tools.

<Card title="Exporting data" icon="file-export" href="./exporting-data"> Export message and user data to CSV for offline analysis. </Card>

***

## Message settings

This section shows the message configuration details and a visual summary of how the message was set up before delivery.

* **Audience** - Details of the audience including:
  * Total number of recipients - How many Subscriptions were sent the message
  * How the message was sent: Targeting filters or segments used
* **Schedule** - When the message started sending and per-user delivery options selected, if any.
* **Throttling** - Any throttling, frequency caps, or channel overrides
* **Message** - The message content.
  * Platforms targeted (Android, iOS, specific browsers)
* **Advanced Settings** - Like Priority, Time to live, and Collapse ID.
* **Additional Data** - Any custom data added to the message.

***

## FAQ

### When do push subscription statuses update?

Push subscription statuses update through two mechanisms:

**1. When the user opens your app or site**

The OneSignal SDK checks whether the push token is valid and whether notification permissions are still granted, then updates the subscription status immediately.

For example, if a user disables push notifications in their device settings and then reopens your app, the SDK detects the change and marks the subscription as **Unsubscribed** right away.

You can capture these changes with the SDK's Subscription Observer ([mobile](./mobile-sdk-reference#addobserver-push-subscription-changes) | [web](./web-sdk-reference#addeventlistener-push-subscription-changes)) to sync status to your own database.

**2. When you send push notifications**

If a user uninstalls your app, clears browser data, or disables push **and never returns**, OneSignal cannot detect the change until you send a notification. The push service (FCM, APNs, HMS) reports the token as invalid, and OneSignal marks the subscription as **Unsubscribed**.

This detection typically takes 2 or more messages because the push service does not immediately reject an invalid token:

| Send       | What happens                                                                                                                                                |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Message 1  | Delivered to device. User then unsubscribes in device settings or uninstalls the app.                                                                       |
| Message 2  | Push service accepts the message but the device does not receive it. OneSignal reports "Delivered" because the push service has not rejected the token yet. |
| Message 3  | Push service rejects the token. OneSignal marks the subscription as **Unsubscribed**.                                                                       |
| Message 4+ | OneSignal does not attempt delivery to this subscription.                                                                                                   |

Use [Event Streams](./event-streams) to detect unsubscribes in real time when sending messages.

<Note>
  If you go long periods without sending to all users, unsubscribes accumulate silently and appear as a large spike when you resume sending. Send to all users at least once or twice a month to detect unsubscribes gradually. See [FCM expired token FAQ](./fcm-expired-token-faq) for more on unsubscribe spikes.
</Note>

<Warning>
  Apple delays unsubscribe reporting by 14+ days. To protect user privacy, Apple does not immediately report uninstalls or permission revocations. If a user opens your app after disabling push, OneSignal detects the change instantly via the SDK. If the user never opens the app again, it may take several weeks for Apple to report the invalid token after you send notifications.

  See [Apple Forum](https://developer.apple.com/forums/thread/670868) and [Technical Note](https://developer.apple.com/library/archive/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG34) for details. Use the dashboard or API to [delete old subscriptions](./delete-users) to keep your audience clean.
</Warning>

Built with [Mintlify](https://mintlify.com).

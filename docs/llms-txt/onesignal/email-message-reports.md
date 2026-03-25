# Source: https://documentation.onesignal.com/docs/en/email-message-reports.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email message reports

> Understand OneSignal Email delivery metrics and message performance analytics including opens, clicks, bounces, suppressions, and spam reports.

Email message reports help you track the performance of each email, including delivery stats, open rate, click rate, and error diagnostics. When viewing an email report in OneSignal, you’ll see real-time statistics showing how your message is performing.

<Note>
  If the email is sent via a Journey or using Templates, see [Journey Analytics](./journeys-analytics) or [Template Analytics](./template-analytics) for additional details.
</Note>

<Frame caption="Snapshot view of real-time email message data">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c4f0241-Frame_16310.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=d811b41ef15ec7fc17978750e6d2be86" width="1201" height="531" data-path="images/docs/c4f0241-Frame_16310.png" />
</Frame>

## Delivery statistics

Audience Activity and data for messages sent via the API are retained for \~30 days. To retain historical performance, export data using the Dashboard or API. See [Exporting Data](./exporting-data).

### Delivered

Understand how many recipients received your message, and why others didn't.

| Metric               | Definition                                                                                                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sent**             | The number of emails successfully sent to the provider.                                                                                                                                                                               |
| **Audience**         | The number of subscriptions in the targeted segment(s).                                                                                                                                                                               |
| **Delivered**        | The number of emails confirmed as delivered to subscriptions' email server.                                                                                                                                                           |
| **Failed**           | The number of emails unable to be delivered to the inbox, excluding bounces. This may include failures reported by the ESP or OneSignal delivery failures.                                                                            |
| **Suppressed**       | The number of emails blocked due to prior bounces or spam reports to protect sender reputation. This metric is only recorded for apps configured to use OneSignal email.                                                              |
| **Bounced**          | The number of emails rejected due to invalid addresses, full inboxes, sender reputation, or DMARC issues. These addresses are added to a [Suppression List](/docs/en/suppressions), either managed by OneSignal or a third party ESP. |
| **Reported as Spam** | The number of recipients who marked the email as spam. These addresses are added to a [Suppression List](/docs/en/suppressions), either managed by OneSignal or a third party ESP.                                                    |
| **Unsubscribed**     | The number of recipients who opted out of receiving emails.                                                                                                                                                                           |
| **Total Opens**      | Total number of times the email was opened, including repeats.                                                                                                                                                                        |
| **Total Clicks**     | Total number of times links were clicked in an email, including repeats.                                                                                                                                                              |
| **Unique Opens**     | Count of individual recipients who opened the email. This metric is used with confirmed deliveries to determine open rate.                                                                                                            |
| **Unique Clicks**    | Count of individual recipients who clicked the email. This metric is used with confirmed deliveries to determine click rate.                                                                                                          |

**Why do we differentiate between total and unique clicks or opens?**

Unique clicks and opens are only counted once per subscriber, regardless of how many times that subscriber opens or clicks the same email. Total clicks and opens are not unique per subscriber and count every time an email is clicked or opened.

The following metrics are specific to email message reports:

| Name          | Description                                                                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Remaining** | Emails still queued for sending. May take up to 8 hours depending on your [Reputation](./email-deliverability) and the Inbox provider's policies (Gmail, Yahoo, Outlook, etc.). |

For detailed metric definitions across all channels, see the [Metrics Glossary](./analytics-metrics-glossary).

### Open rate

Open events are counted when the email is viewed, though privacy settings and inbox behavior may affect accuracy. See [Why are open events low?](#why-are-open-events-low%3F).

| Name             | Description                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| **Unique Opens** | Count of individual recipients who opened the email.                                               |
| **Total Opens**  | Total number of times the email was opened, including repeats.                                     |
| **Open Rate**    | `(Unique Opens / Delivered) * 100%`. Measures how many delivered emails were opened at least once. |

<Info>
  **Unique vs. Total Opens**

* **Open Rate** is always based on unique opens.
* Use **Total Opens** to see repeat engagement from the same recipients.
</Info>

<Warning>
  Open rate accuracy can be affected by inbox privacy features (e.g., Apple Mail Privacy Protection), ad blockers, and image tracking being disabled. These factors may cause opens to be **over-reported** (due to automatic image prefetching) or **under-reported** (when tracking pixels are blocked).

  For more reliable engagement insights, compare Open Rate with **CTR** and **CTOR**.
</Warning>

### Click-through rate

Measure engagement through link clicks in your email. Click tracking can be enabled or disabled in individual email sends. More details on links can be found in:

* [URLs, Links & Deep Links](./links)
* [Email unsubscribe links & headers](./unsubscribe-links-email-subscriptions)

| Name                          | Description                                                                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Click-Through Rate (CTR)**  | `(Unique Clicks / Delivered) * 100%`. Measures how many delivered emails resulted in a click. Requires [Click Tracking to be enabled](./unsubscribe-links-email-subscriptions). |
| **Total Clicks**              | All link clicks, including repeat clicks from the same user. See [URLs, Links and Deep Links](./links).                                                                         |
| **Click to Open Rate (CTOR)** | `(Unique Clicks / Unique Opens) * 100%`. Measures how engaging the email was after being opened.                                                                                |

<Info>
  **CTR vs CTOR**

* **CTR**: Clicks as a % of deliveries
* **CTOR**: Clicks as a % of opens
* Use both to evaluate message quality and engagement.

  *Tip: Use UTM parameters for tracking in tools like Google Analytics.*
</Info>

<Warning>
  If Click Tracking is enabled but click events are low, check for browser-level blocking (e.g., Brave or Firefox). Contact `support@onesignal.com` if the issue persists.
</Warning>

### Unsubscribed and reported as spam

Understand opt-outs and spam complaints so you can improve targeting and deliverability.

| Name                 | Description                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Unsubscribes**     | Number of recipients who opted out of receiving emails. Status is updated immediately.                                         |
| **Reported as Spam** | Recipients who marked your message as spam. These addresses are automatically added to the [Suppression List](./suppressions). |

<Note>
  Use segmentation and send-time optimization to lower unsubscribe and spam rates.
</Note>

<Warning>
  Keep an eye on your unsubscribe and spam rates. If they're too high, your app may get disabled until the issue is addressed.
  See:

* [Email Deliverability](./email-deliverability)
* [Email reputation best practices](./email-reputation-best-practices)
</Warning>

***

## Conversions

<Info>
  **Coming soon** — [Conversion metrics](/docs/en/conversion-metrics) will be available on message reports. Once available, you will see attributed and influenced conversions for each message directly in its report. See [Conversion metrics](/docs/en/conversion-metrics) for details on the attribution model and setup instructions.
</Info>

***

## Message statistics

Analyze performance trends over time, including engagement and delivery issues.

<Frame caption="Message Statistics over 24-hour view">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b515604ef097dd62b783a810d8d491d2e2fce84b69bddfa8877b6fb0ce65d0e6-Screenshot_2025-05-13_at_15.51.04.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=6e1c62efd8a9a62016c8f01f5a589de0" width="1633" height="582" data-path="images/docs/b515604ef097dd62b783a810d8d491d2e2fce84b69bddfa8877b6fb0ce65d0e6-Screenshot_2025-05-13_at_15.51.04.png" />
</Frame>

View metrics by:

* 30 days (default)
* 24 hours
* 60 minutes

You can toggle additional metrics like Bounced, ESP Failed, Sent, Spam, Suppressed, Total Clicks, and Total Opens.

Use the export icon in the top-right of the graph to download the data.

***

## Audience activity

The **Audience activity** report shows how each subscription interacted with a specific message. Results are grouped into categories so you can quickly see how recipients engaged.

<Frame caption="Audience activity tabs and table">
  <img src="https://mintcdn.com/onesignal/uUnoewrrt1DvIru9/images/push/audience-activity.png?fit=max&auto=format&n=uUnoewrrt1DvIru9&q=85&s=1568714f2133e3e9ef98c36de476e28f" alt="Audience activity screenshot" width="2150" height="402" data-path="images/push/audience-activity.png" />
</Frame>

<Tabs>
  <Tab title="Categories">
    | Category                     | Description                                                |
    | ---------------------------- | ---------------------------------------------------------- |
    | **Sent**                     | Message was sent to the device.                            |
    | **Confirmed delivery**       | Delivery was confirmed by the device.                      |
    | **Did not confirm delivery** | Delivery confirmation was not received.                    |
    | **Clicked**                  | User clicked the notification.                             |
    | **Did not click**            | User did not click the notification.                       |
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
    | **Subscription status** | Current status (for example, Subscribed, Unsubscribed).           |
    | **Sent**                | Time the message was sent.                                        |
    | **Confirmed delivery**  | Time delivery was confirmed by the device.                        |
    | **Clicked**             | Timestamp if the user clicked, or `-` if not.                     |
    | **Failed**              | Indicates if delivery failed.                                     |
    | **Unsubscribed**        | Indicates if the user unsubscribed after receiving the message.   |
    | **Failure message**     | Error message if delivery failed (for example, “Invalid token”).  |
  </Tab>
</Tabs>

<Note>
  Audience activity data is only available for **30 days** from the time the message is sent. Export results if you need to retain them longer.
</Note>

***

### Why audience activity is helpful

Audience activity helps you go beyond delivery counts by showing which specific users fall into each outcome. Use it to:

* **Diagnose delivery issues** by reviewing failed or unconfirmed deliveries.
* **Measure engagement** by comparing clicks vs. non-clicks.
* **Track churn** by identifying unsubscribes tied to a message.
* **Segment audiences** for retargeting or export.

***

### Exporting results

You can download audience data with the **Export** menu:

* **Selected activity** – exports only the currently viewed tab (for example, all users who did not click).
* **All activities** – exports the full report across every category.

Exports let you analyze results offline, share with other teams, or merge with your CRM and analytics tools.

***

### Retargeting users

From any tab, click **Send a retargeted message** to act on that specific group.

You can send:

* **New push**
* **New SMS**

This allows you to follow up with only the users in the selected activity group.

#### Example use cases

* Send a retargeted push to users in **Did not click**.
* Send an SMS to users in **Did not confirm delivery** who may not be reachable via push.
* Follow up with **Confirmed delivery** users to encourage further engagement.

***

### Example workflow

<Steps>
  <Step title="Open the Did not click tab">
    Navigate to the **Did not click** tab in Audience activity.
  </Step>

  <Step title="Review the list of subscriptions">
    Check which subscriptions received the notification but did not engage.
  </Step>

  <Step title="Send a retargeted message">
    Click **Send a retargeted message → New push** to follow up with this segment.
  </Step>

  <Step title="Export for deeper analysis">
    If needed, export the audience activity for offline analysis or multi-channel targeting in a journey.
  </Step>
</Steps>

***

## Click activity

Track which links were clicked and how many times.

| Name                         | Description                                                                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Unique Clicks**            | Count of links clicked by recipients.                                                                                                                                           |
| **Total Clicks**             | All link clicks, including repeat clicks from the same user. See [URLs, Links and Deep Links](./links).                                                                         |
| **Click-Through Rate (CTR)** | `(Unique Clicks / Delivered) * 100%`. Measures how many delivered emails resulted in a click. Requires [Click Tracking to be enabled](./unsubscribe-links-email-subscriptions). |

***

## FAQ

### Why are my emails marked as failed?

Failure reasons are shown in the Audience Activity export. Common causes include:

* Misspelled or non-existent domains (e.g. `@gmial.com`)
* Email addresses already on your ESP’s suppression list
* Using [Custom Unsubscribe Links](./unsubscribe-links-email-subscriptions) without also unsubscribing via [Update User API](/reference/update-user) or [CSV Upload](./import#csv-upload)
* Previously bounced addresses
* Inboxes throttling un-warmed sender domains (see [Warm-up Guide](./email-warm-up))

### Why are open events low?

-Inbox privacy features, ad blockers, and image tracking settings can prevent open events from being recorded.

-See the [Open Rate section](#open-rate) for details on how privacy features affect accuracy.

-Open tracking is not always 100% reliable. Test on multiple devices and networks for comparison.

### Why do I see emails in Pending?

Two main reasons:

1. **Scheduled delivery:** Especially if auto warm-up is enabled, delivery is spread out.
2. **Pending confirmation:** Some inboxes delay event feedback up to 8 hours.

If the message stays in Pending, it's likely sent but not confirmed. Check **Sent at** in Audience Activity for clues.

***

Built with [Mintlify](https://mintlify.com).

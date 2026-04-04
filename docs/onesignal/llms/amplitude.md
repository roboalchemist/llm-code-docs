# Source: https://documentation.onesignal.com/docs/en/amplitude.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amplitude

> Learn how to integrate OneSignal with Amplitude to sync user cohorts and message events for smarter, behavior-based notifications across push, email, SMS, and in-app channels.

<Frame caption="OneSignal + Amplitude Integration Overview">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/8b34926-onesignal-amplitude-integration.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=86fc3b4f8e4c08467808e34277d61c0c" width="1280" height="720" data-path="images/docs/8b34926-onesignal-amplitude-integration.png" />
</Frame>

Integrate OneSignal with [Amplitude](https://amplitude.com) to send detailed message events, custom events, and import behavioral user cohorts. This enables real-time targeting based on user behavior to improve onboarding, re-engagement, and conversion.

## Key benefits

* **Send message events to Amplitude**: Track delivery, clicks, failures, and more across push, in-app, email, and SMS.
* **Send custom events to OneSignal**: Send your custom events from Amplitude to OneSignal.
* **Import cohorts from Amplitude**: Automatically sync behavior-based cohorts into OneSignal as filters for targeting.

This is an app-level integration, giving you granular control over which apps and events are linked.

***

## Requirements

* [Amplitude Account](https://amplitude.com/pricing)
* [OneSignal Paid Plan](https://onesignal.com/pricing)
* OneSignal app with [Users](./users) and External ID set.

<Warning>
  This integration does not create users. It maps the users in Amplitude to those in OneSignal.
</Warning>

***

## Setup

### Add Amplitude to OneSignal

This step configures OneSignal → Amplitude (Outbound) to send OneSignal message events (delivery, clicks, failures, etc.) into your Amplitude project.

#### In OneSignal

1. Navigate to **Data > Integrations > Catalog**.
2. Search for Amplitude (or find it in the list) and click it.
3. Click **Settings**.
4. In the Amplitude integration page, open the **Outbound** tab and enter your Amplitude token.
5. Select the message events you want to send to Amplitude, then click **Save**.

<Frame caption="Amplitude Outbound settings in OneSignal">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/96ef30b-Screenshot_2024-06-27_at_12.38.45_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=837ed63cbe0ad9e7904d6d41d32d8b70" alt="Amplitude Outbound settings in OneSignal" />
</Frame>

#### In Amplitude

1. Find your project API Key then copy-paste it into OneSignal.
2. If using Amplitude's EU servers, check **Send events exclusively to Amplitude's EU Residency Endpoint**. You can verify this by your Amplitude URL. If you see `eu.amplitude.com` then you are using Amplitude's EU servers.

### Add OneSignal to Amplitude

This step configures Amplitude → OneSignal (Inbound) to sync cohorts and/or send custom events into OneSignal.

In your Amplitude Destinations, search for OneSignal.

<Frame caption="Add OneSignal Destination in Amplitude">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/integrations/amplitude-destination.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=c93051a960c69f5ffbaea9b4f5e95e86" alt="Add OneSignal Destination in Amplitude" />
</Frame>

Amplitude provides two OneSignal destination types in the catalog:

* **Cohorts**: Sync cohorts from Amplitude to OneSignal.
* **Events User Properties**: Send custom events from Amplitude to OneSignal.

<Note>
  If you plan to use both cohort syncing and custom events, add both OneSignal destinations. Each destination is configured separately in Amplitude, so you will enter your OneSignal credentials for each one.
</Note>

#### USER ID mapping

<Warning>
  This step is essential for cohort syncing and event tracking to work properly.
</Warning>

To match users across both systems:

* Use a shared identifier: The **[External ID](./users)** in OneSignal must match an Amplitude User ID Property selected (like user\_id).
* Verify that the selected user property exists across your Amplitude and OneSignal User Profiles.

### Additional properties

You can send additional properties to OneSignal that will be included in the [custom events](./custom-events).

This is helpful for processing events in OneSignal *only if* they contain a specific property.

<Check>
  Click **Save** when finished.

  You should now be able to export cohorts and custom events from Amplitude to OneSignal and collect message events from OneSignal to Amplitude.
</Check>

***

## Testing custom events

1. In the Amplitude > OneSignal Events Destination, click the Test Connection button.

<Frame caption="Amplitude > OneSignal Events Destination">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/integrations/amplitude-test-connection.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=8202b1ee8513456d78777425db4a7753" width="1970" height="1160" data-path="images/integrations/amplitude-test-connection.png" />
</Frame>

1. Make sure the `"user_id"` in the payload is set to an existing User’s External ID in your OneSignal App.
2. Click the **Send Test Event** button
3. The Response box should remain empty and you should see a message that says `"OneSignal has successfully received test event."`

<Frame caption="Response example">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/integrations/amplitude-test-connection-response.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=14b5824d639a748252a36315bc491383" width="2438" height="1500" data-path="images/integrations/amplitude-test-connection-response.png" />
</Frame>

<Warning>
  If you get an error, make sure your OneSignal App ID and REST API key are added to Amplitude correctly and the app is configured for [custom events](./custom-events).
</Warning>

1. In OneSignal, navigate to **Data > Custom Events** and you should see the test event in the list.

<Frame caption="Custom Event in OneSignal">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/integrations/onesignal-custom-event.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=18c287884737e192fde2da0e28d65676" width="2736" height="1032" data-path="images/integrations/onesignal-custom-event.png" />
</Frame>

<Warning>
  If you do not see the event, make sure the `"user_id"` is set to an existing User’s External ID in your OneSignal App.
</Warning>

## Export Amplitude cohorts to OneSignal

You can sync the users within your Amplitude cohorts to the users within OneSignal as long as they have the matching User ID/External ID property discussed in the previous step.

Exporting user data from Amplitude **does not create the user in OneSignal**, the user must already exist and have the matching External ID.

To export users from Amplitude to OneSignal:

1. In Amplitude, create a cohort. See [Amplitude's docs on cohorts](https://amplitude.com/docs/analytics/behavioral-cohorts).
2. Click **Sync** and choose **OneSignal** as the destination.
3. Choose sync frequency.

<Frame caption="Image showing how you can set a sync for your cohorts with OneSignal">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/integrations/amplitude-sync-cadence.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=9ba4b69273f73ccdd1f095c2a3ede63c" width="602" height="499" data-path="images/integrations/amplitude-sync-cadence.png" />
</Frame>

### OneSignal Segment creation

* The synced cohort appears in OneSignal as an **Amplitude Segment filter**.
* A Segment for the cohort will automatically be created if the following conditions are met:
  * The users in the Amplitude Cohort also exist in OneSignal with matching External ID.
  * You must not exceed your Segment limit in OneSignal.

If both conditions are met, OneSignal will automatically generate a Segment using the Amplitude Cohort filter and name of the Cohort.

<Frame caption="How to create a Segment from an Amplitude Cohort">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/526a986-Screenshot_2023-09-22_at_7.01.09_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=e5de1d6896a542a980b9840a05200586" width="1622" height="878" data-path="images/docs/526a986-Screenshot_2023-09-22_at_7.01.09_PM.png" />
</Frame>

<Note>
  Common questions:

* [Why don't my cohort & segment counts match?](#why-don’t-my-cohort-%26-segment-counts-match%3F)
* [Do unsubscribed users sync from Amplitude?](#do-unsubscribed-users-sync-from-amplitude%3F)
</Note>

***

## Track message events in Amplitude

Once connected, OneSignal will send message events to Amplitude in real time.

### Message events

These are the message event kinds that OneSignal sends to Amplitude. You can select which of these events you want to send to your Amplitude project within the OneSignal Integrations Settings.

| Message Event Kind (OneSignal) | Message Event Name (Amplitude)                                | Event Description                                                                      |
| ------------------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Push Sent                      | \[Onesignal] Push Delivered                                   | Push notification successfully sent.                                                   |
| Push Received                  | \[Onesignal] Push Confirmed delivery                          | Push notification successfully received                                                |
| Push Clicked                   | \[Onesignal] Push Clicked                                     | Push notification touched on device                                                    |
| Push Failed                    | \[Onesignal] Push Failed                                      | Push failed to be sent. Check the failed message report in OneSignal.                  |
| Push Unsubscribed              | \[Onesignal] Push Unsubscribed                                | The [Subscription](./subscriptions) unsubscribed from push.                            |
|                                |                                                               |                                                                                        |
| In-App Impression              | \[Onesignal] IAM Displayed                                    | In-App Message successfully displayed on device                                        |
| In-App Clicked                 | \[Onesignal] IAM Clicked                                      | In-App Message clicked on device                                                       |
| In-App Page Displayed          | \[Onesignal] IAM Page Displayed                               | In-App Message page is displayed                                                       |
|                                |                                                               |                                                                                        |
| Email Sent                     | \[Onesignal] Email Delivered                                  | Email successfully sent                                                                |
| Email Received                 | \[Onesignal] Email Confirmed delivery                         | Email received by recipient                                                            |
| Email Opened                   | \[Onesignal] Email Opened                                     | Email opened by recipient                                                              |
| Email Link Clicked             | \[Onesignal] Email Clicked                                    | Email link clicked on                                                                  |
| Email Unsubscribed             | \[Onesignal] Email Unsubscribed                               | Email unsubscribed by recipient                                                        |
| Email Reported As Spam         | \[Onesignal] Email Reported as SPAM                           | Email reported as spam by recipient                                                    |
| Email Bounced                  | \[Onesignal] Email Hard bounced                               | Email returned to sender due to permanent error                                        |
| Email Failed                   | \[Onesignal] Email Failed delivery                            | Could not deliver the email to the recipient's inbox                                   |
| Email Suppressed               | \[Onesignal] Email Not delivering to suppressed email address | Email not delivered as the recipient had suppressed the email address it was sent from |
|                                |                                                               |                                                                                        |
| SMS Sent                       | \[Onesignal] SMS Delivered                                    | SMS sent to recipient                                                                  |
| SMS Failed                     | \[Onesignal] SMS Failed delivery                              | SMS failed to send                                                                     |
| SMS Delivered                  | \[Onesignal] SMS Confirmed delivery                           | SMS successfully delivered                                                             |
| SMS Undelivered                | \[Onesignal] SMS Failed delivery                              | The SMS could not be sent.                                                             |

### Event properties

These are the properties that are present on any events sent from OneSignal to Amplitude

| PROPERTY NAME        | DESCRIPTION                                             |
| -------------------- | ------------------------------------------------------- |
| **Distinct ID**      | The external\_id associated with the message            |
| **Message ID**       | The identifier of the discrete message                  |
| **Message Name**     | The message name                                        |
| **Message Title**    | The message title                                       |
| **Message Contents** | The message contents                                    |
| **message\_type**    | The type of message sent, push, in-app, email, SMS      |
| **template\_id**     | The message template used (API and Journey Messages)    |
| **subscription\_id** | The OneSignal set device/email/sms identifier           |
| **device\_type**     | The device type that received the message               |
| **language**         | The two-character language code of the device           |
| **source**           | `onesignal` (is indicated as the source for all events) |

<Warning>
  See [Why doesn't my delivery data match between Amplitude and
  OneSignal?](#why-doesnt-my-delivery-data-match-between-amplitude-and-onesignal)
</Warning>

***

## FAQ

### Why don't my cohort & segment counts match?

1. Missing or mismatched External IDs
   Only users with a matching OneSignal External ID and Amplitude User ID are included. This integration doesn’t create users or subscriptions.

2. Unsubscribed users
   OneSignal segments only display the count for subscribed [Subscriptions](./subscriptions). Unsubscribed Subscriptions are available for Journeys or In-App Messages.

For example, if an Amplitude cohort has 10 users but the OneSignal segment shows 8 Subscriptions, the 2 missing users may:

* Not exist in OneSignal or have an incorrect External ID.
* Have unsubscribed subscriptions.

To verify, check the **Audience > Users** tab in OneSignal to see if the users exist and have active subscriptions.

### Do unsubscribed users sync from Amplitude?

Yes, but they are excluded from the OneSignal segment counts at this time. You can still message them via Journeys or In-app messsages if they have other [Subscriptions](./subscriptions) or their Subscription type supports it.

### Why doesn't delivery data match?

A single user may have multiple [Subscriptions](./subscriptions) (push devices, email addresses, phone numbers). Each Subscription generates its own delivery event. For example:

* 1 user = 2 Android + 1 iOS + 2 Web = 5 push Subscriptions
* 1 push message = up to 5 sent/received/clicked events

Use the `subscription_id` in event properties to trace the exact source.

To troubleshoot missing events:

* Ensure `OneSignal.login` is called whenever a user is identified to set the External ID.
* Verify that `OneSignal.logout` isn't removing the External ID.
* Check API requests or CSV uploads that may alter the External ID.

### How can we send user/subscription events?

User and subscription-level events (e.g., permission granted, user login/logout) are not automatically sent.

The OneSignal SDK has event listeners that can be used to track these events for you to send to Amplitude:

* User State Observer: [Mobile SDK](./mobile-sdk-reference#addobserver-user-state) , [Web SDK](./web-sdk-reference#addeventlistener-user-state)
* Permission Observer: [Mobile SDK](./mobile-sdk-reference#addpermissionobserver-push) , [Web SDK](./web-sdk-reference#permissionchange)

### Why is the OneSignal Subscription ID added to Amplitude as a device\_id?

Amplitude expects a `device_id` for deduplication. OneSignal uses `subscription_id` for this, which maps into `device_id` automatically.

See [Amplitude's docs](https://amplitude.com/docs/apis/analytics/http-v2#event-deduplication) for more information.

***

Built with [Mintlify](https://mintlify.com).

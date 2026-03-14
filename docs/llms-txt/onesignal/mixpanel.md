# Source: https://documentation.onesignal.com/docs/en/mixpanel.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mixpanel

> Learn how to integrate OneSignal with Mixpanel to sync cohorts, trigger personalized messaging, and track real-time user engagement.

<Frame caption="OneSignal + Mixpanel integration overview">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/a2e26d4-onesignal-mixpanel-integration.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=a474dab0bb6d1b5761d9995c7e6989da" width="1280" height="720" data-path="images/docs/a2e26d4-onesignal-mixpanel-integration.png" />
</Frame>

Integrate OneSignal with [Mixpanel](https://mixpanel.com) to send detailed message engagement events and import behavioral user cohorts. This enables real-time targeting based on user behavior to improve onboarding, re-engagement, and conversion.

## Key benefits

* **Send message events to Mixpanel**: Track delivery, clicks, failures, and more across push, in-app, email, and SMS.
  * **Real-time insights** – Unify Mixpanel product analytics with OneSignal engagement metrics.
  * **Data-driven campaigns** – Run smarter re-engagement using Mixpanel's behavioral segmentation.
* **Import cohorts from Mixpanel**: Automatically sync behavior-based cohorts into OneSignal as filters for targeting.
  * **Personalized messaging** – Trigger contextual OneSignal messages when users enter or exit Mixpanel cohorts.

***

## Requirements

* [Mixpanel Account](https://mixpanel.com/)
* [OneSignal Paid Plan](https://onesignal.com/pricing)
* OneSignal app with [Users](./users) and External ID set.

<Warning>
  This integration does not create users. It maps the users in Mixpanel to those in OneSignal.
</Warning>

***

## Setup

### Add Mixpanel to OneSignal

In OneSignal, navigate to **Data > Integrations > Mixpanel** and click **Activate**.

<Frame caption="Enable Mixpanel integration in OneSignal">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f5dfbab5a6c41ae816e34401b7fa5a8624e15d43f90ad723c4c7b2166dbd66de-Screenshot_2025-03-18_at_8.15.13_AM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=4c5a9ba2e4e2a2c8b2e2b2b2376253f1" width="1150" height="458" data-path="images/docs/f5dfbab5a6c41ae816e34401b7fa5a8624e15d43f90ad723c4c7b2166dbd66de-Screenshot_2025-03-18_at_8.15.13_AM.png" />
</Frame>

In Mixpanel:

1. Find your [Project Token](https://docs.mixpanel.com/docs/orgs-and-projects/managing-projects#find-your-project-tokens) then copy-paste it into OneSignal.
2. Check your [Data Residency](https://docs.mixpanel.com/docs/orgs-and-projects/managing-projects#project-details). If using Mixpanel's EU servers, check the **Send events exclusively to Mixpanel's EU Residency Server** box.

#### Select message events

Select which OneSignal message events you want to send to Mixpanel. When finished, click **Activate**.

<Frame caption="Mixpanel settings in OneSignal">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/bc980ae-Screenshot_2024-06-04_at_10.18.59_AM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=b98514269a60a2144c1dc0334969e7d3" width="2216" height="1412" data-path="images/docs/bc980ae-Screenshot_2024-06-04_at_10.18.59_AM.png" />
</Frame>

### Add OneSignal to Mixpanel

In your Mixpanel **Integrations**, add OneSignal.

<Frame caption="Add OneSignal Integration in Mixpanel">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/mixpanel-integration.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=b4e6bc1f405b2087b455b2942ce5aecd" width="2986" height="1300" data-path="images/docs/mixpanel-integration.png" />
</Frame>

Set the **Connector Name** as something identifiable like `OneSignal - APP_NAME` where `APP_NAME` is the name of the app in OneSignal.

You will need the following data available in OneSignal **Settings > [Keys & IDs](./keys-and-ids)** :

1. App ID
2. API Key

#### USER ID mapping

<Warning>
  This step is essential for cohort syncing and event tracking to work properly.
</Warning>

To match users across both systems:

* Use a shared identifier: The **[External ID](./users)** in OneSignal must match an Mixpanel User ID Property selected (like user\_id).
* Verify that the selected user property exists across your Mixpanel and OneSignal User Profiles.

<Frame caption="Mixpanel's dashboard for setting the OneSignal properties.">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b5e818708efcc73ea8eb0cccb6542c205069b395978b8fa796af28d816b33356-Screenshot_2025-03-18_at_11.22.54_AM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=c161191d039f187a20df7201d9ca71db" width="864" height="900" data-path="images/docs/b5e818708efcc73ea8eb0cccb6542c205069b395978b8fa796af28d816b33356-Screenshot_2025-03-18_at_11.22.54_AM.png" />
</Frame>

Verify the **User ID Property** you selected is available in your Mixpanel user profile properties.

<Frame caption="Mixpanel > Users > User Profile Properties">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4416681-small-Screenshot_2023-05-15_at_9.54.14_AM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=e89ad019a61077ae376fc92e1a1eb87a" width="521" height="1024" data-path="images/docs/4416681-small-Screenshot_2023-05-15_at_9.54.14_AM.png" />
</Frame>

The same value in Mixpanel for the user profile property must match the External ID in OneSignal.

<Frame caption="OneSignal > Audience > Users > External ID">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e6853b59781b29ccbd264f97925830986605ec5514d02b5435c27ec896804a89-Screenshot_2025-03-18_at_10.22.25_AM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=9a0b4237233c0492901853d72a6b1b63" width="2764" height="686" data-path="images/docs/e6853b59781b29ccbd264f97925830986605ec5514d02b5435c27ec896804a89-Screenshot_2025-03-18_at_10.22.25_AM.png" />
</Frame>

<Warning>
  If you match users to OneSignal based on the Mixpanel `$distinct_id` then it will only match with the top value.

  In below example, only `890ea9b1-9024-4fb9-a92f-152ba67dd21a` will work. It cannot match `109768518080488203109` or `$device:1880c06821f1b3-052354675cde95-1d525634-1fa400-1880c06821f1b3`.
</Warning>

<Frame caption="Use caution when setting Distinct ID if used for the User ID Property mapping.">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/e7b80eb-small-Screenshot_2023-05-15_at_10.07.10_AM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=ef1999c6f01a48063d98e7e2ea330052" width="464" height="314" data-path="images/docs/e7b80eb-small-Screenshot_2023-05-15_at_10.07.10_AM.png" />
</Frame>

Click **Continue** when finished.

<Check>
  You should now be able to export cohorts from Mixpanel to OneSignal and collect message events from OneSignal to Mixpanel.
</Check>

***

## Export Mixpanel cohorts to OneSignal

You can sync the users within your Mixpanel cohorts to the users within OneSignal as long as they have the matching User ID/External ID property discussed in the previous step.

Exporting user data from Mixpanel **does not create the user in OneSignal**, the user must already exist and have the matching External ID.

To export users from Mixpanel to OneSignal:

1. In Mixpanel, create a cohort.
2. Click **Options > Export to... > *The OneSignal Connection name***.

<Frame caption="How to export a Mixpanel cohort to OneSignal.">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/187698db55979af5f5c94d672ada1e0c8d7329d600a650e3115b77077ef99237-Screenshot_2025-03-18_at_12.04.16_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=fce16e4cde30d69f3b24a947cf71c937" width="2432" height="1008" data-path="images/docs/187698db55979af5f5c94d672ada1e0c8d7329d600a650e3115b77077ef99237-Screenshot_2025-03-18_at_12.04.16_PM.png" />
</Frame>

1. Choose sync frequency and press **Begin Sync**.

<Frame caption="Mixpanel frequency options.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c6b36cedac01d722acaa4240225ea6d10519458682f4c2844d681b8ee34b236e-Screenshot_2025-03-18_at_12.12.06_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=5bb3a035bfb3bea7d78553e86ccb943b" width="860" height="896" data-path="images/docs/c6b36cedac01d722acaa4240225ea6d10519458682f4c2844d681b8ee34b236e-Screenshot_2025-03-18_at_12.12.06_PM.png" />
</Frame>

### OneSignal Segment creation

* The synced cohort appears in OneSignal as an **Mixpanel Segment filter**.
* A Segment for the cohort will automatically be created if the following conditions are met:
  * The users in the Mixpanel Cohort also exist in OneSignal with matching External ID.
  * You must not exceed your Segment limit in OneSignal.

If both conditions are met, OneSignal will automatically generate a Segment using the Mixpanel Cohort filter and name of the Cohort.

<Note>
  Mixpanel requires at least one matching user to create a Segment in OneSignal.\
  Once the Segment is created, it will remain in OneSignal even if the cohort later has no users. In that case, the Segment simply shows as empty until users are added again.
</Note>

<Frame caption="How to create a Segment from a Mixpanel Cohort">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7b01785ad5a5f85377bdb20e664e5d5c38280cff56373d70726621569668907d-Screenshot_2025-03-18_at_12.38.47_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=3ba94cf6588a4158a86e77c4a23c3e34" width="1444" height="818" data-path="images/docs/7b01785ad5a5f85377bdb20e664e5d5c38280cff56373d70726621569668907d-Screenshot_2025-03-18_at_12.38.47_PM.png" />
</Frame>

<Note>
  Common questions:

* [Why don't my cohort & segment counts match?](#why-don’t-my-cohort-%26-segment-counts-match%3F)
* [Do unsubscribed users sync from Mixpanel?](#do-unsubscribed-users-sync-from-mixpanel%3F)
</Note>

***

## Track message events in Mixpanel

Once connected, OneSignal will send message events to Mixpanel in real time.

To test this, send yourself a message from OneSignal, then navigate to your user profile page in Mixpanel.

Within the Activity Feed, you should see the events populate:

<Frame caption="Example of Mixpanel activity feed with OneSignal message events.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c344970fd85bda82f9b6bedf1700a9cbb91afd63afc9fe1e866c42e1b380770e-Screenshot_2025-03-18_at_1.59.23_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=9ca542f553f6c08a15ca99d52d68be2b" width="2420" height="1654" data-path="images/docs/c344970fd85bda82f9b6bedf1700a9cbb91afd63afc9fe1e866c42e1b380770e-Screenshot_2025-03-18_at_1.59.23_PM.png" />
</Frame>

### Message events

These are the message event kinds that OneSignal sends to Mixpanel. You can select which of these events you want to send to your Mixpanel project within the OneSignal Integrations Settings.

| Message Event Kind (OneSignal) | Message Event Name (Mixpanel) | Event Description                                                                               |
| ------------------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------- |
| Push Sent                      | Message Sent                  | Push notification successfully sent.                                                            |
| Push Received                  | Message Received              | Push notification successfully received.                                                        |
| Push Clicked                   | App Opened from Push          | Push notification touched on device.                                                            |
| Push Failed                    | Push Failed                   | Push failed to be sent. Check the failed message report in OneSignal.                           |
| Push Unsubscribed              | Push Unsubscribed             | The [Subscription](./subscriptions) unsubscribed from push.                                     |
|                                |                               |                                                                                                 |
| In-App Impression              | Message Sent                  | In-App Message successfully displayed on device.                                                |
| In-App Clicked                 | Message Opened                | In-App Message clicked on device.                                                               |
| In-App Page Displayed          | In-App Page Displayed         | In-App Message page is displayed.                                                               |
|                                |                               |                                                                                                 |
| Email Sent                     | Message Sent                  | Email successfully sent.                                                                        |
| Email Received                 | Message Received              | Email received by recipient.                                                                    |
| Email Opened                   | Message Opened                | Email opened by recipient.                                                                      |
| Email Link Clicked             | App Opened from Push          | Email link clicked on.                                                                          |
| Email Unsubscribed             | Email Unsubscribed            | Email unsubscribed by recipient.                                                                |
| Email Reported As Spam         | Email Reported as Spam        | Email reported as spam by recipient.                                                            |
| Email Bounced                  | Email Bounced                 | Email returned to sender due to permanent error.                                                |
| Email Failed                   | Email Failed                  | Could not deliver the email to the recipient's inbox.                                           |
| Email Suppressed               | Email Suppressed              | The email address is on your suppression list. Either it bounced or marked your emails as spam. |
|                                |                               |                                                                                                 |
| SMS Sent                       | Message Sent                  | SMS sent to recipient.                                                                          |
| SMS Failed                     | SMS Failed                    | SMS failed to send.                                                                             |
| SMS Delivered                  | Message Received              | SMS successfully delivered.                                                                     |
| SMS Undelivered                | SMS Undelivered               | The SMS could not be sent.                                                                      |

### Event properties

These are the properties that are present on any events sent from OneSignal to Mixpanel

| PROPERTY NAME        | DESCRIPTION                                             |
| -------------------- | ------------------------------------------------------- |
| **Distinct ID**      | The external\_id associated with the message.           |
| **Message ID**       | The identifier of the discrete message.                 |
| **Message Name**     | The message name.                                       |
| **Message Title**    | The message title.                                      |
| **Message Contents** | The message contents.                                   |
| **message\_type**    | The type of message sent, push, in-app, email, SMS.     |
| **template\_id**     | The message template used (API and Journey Messages).   |
| **subscription\_id** | The OneSignal set device/email/sms identifier.          |
| **device\_type**     | The device type that received the message.              |
| **language**         | The two character language code of the device.          |
| **source**           | `onesignal` (is indicated as the source for all events) |

<Warning>
  See [Why doesn't my delivery data match between Mixpanel and OneSignal?](#why-doesnt-my-delivery-data-match-between-mixpanel-and-onesignal)
</Warning>

***

## FAQ

### Why don't my cohort & segment counts match?

1. Missing or mismatched External IDs
   Only users with a matching OneSignal External ID and Mixpanel User ID are included. This integration doesn’t create users or subscriptions.

2. Unsubscribed users
   OneSignal segments only display the count for subscribed [Subscriptions](./subscriptions). Unsubscribed Subscriptions are available for Journeys or In-App Messages.

For example, if an Mixpanel cohort has 10 users but the OneSignal segment shows 8 Subscriptions, the 2 missing users may:

* Not exist in OneSignal or have an incorrect External ID.
* Have unsubscribed subscriptions.

To verify, check the **Audience > Users** tab in OneSignal to see if the users exist and have active subscriptions.

### Do unsubscribed users sync from Mixpanel?

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

The OneSignal SDK has event listeners that can be used to track these events for you to send to Mixpanel:

* User State Observer: [Mobile SDK](./mobile-sdk-reference#addobserver-user-state) , [Web SDK](./web-sdk-reference#addeventlistener-user-state)
* Permission Observer: [Mobile SDK](./mobile-sdk-reference#addpermissionobserver-push) , [Web SDK](./web-sdk-reference#permissionchange)

***

Built with [Mintlify](https://mintlify.com).

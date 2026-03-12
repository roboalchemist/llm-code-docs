# Source: https://documentation.onesignal.com/docs/en/frequency-capping.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Push frequency capping

> Limit how often push notifications are sent

OneSignal helps you reach your users effectively—without overwhelming them. Sending too many messages can lead to unsubscribes, disengagement, or a poor user experience. Frequency Capping allows you to control how often users receive push notifications from your app by setting limits on the number of messages sent per minute, hour, day, or week.

<Note>
  Frequency Capping is available on selected [Paid Plans](https://onesignal.com/pricing).
</Note>

***

## How frequency capping works

Example: Setting a frequency cap of **3 notifications per 24h period**

**Calendar Day 1:**

* 9:00 AM: Send Notification 1. User receives Notification 1. (Count: 1) ✅
* 1:00 PM: Send Notification 2. User receives Notification 2. (Count: 2) ✅
* 5:00 PM: Send Notification 3. User receives Notification 3. (Count: 3) ✅

The user has now reached the 3-notification limit for their rolling 24-hour window, which started at 9:00 AM on Day 1.

**Calendar Day 2:**

* 8:00 AM: Send Notification 4. User is capped and does not receive Notification 4 because the 24-hour window from 9:00 AM on Day 1 hasn't expired yet. The count is still at 3.
* 9:00 AM: The 24-hour window from Notification 1 (9:00 AM on Day 1) resets. The count drops to 2. The user can now receive another notification.
* 9:01 AM: Send Notification 5. User receives Notification 5. (Count: 3) ✅
* 10:00 AM: Send Notification 6. User is capped and does not receive Notification 6.
* 11:00 AM: Send Notification 7. User is capped and does not receive Notification 7.
* 1:00 PM: The 24-hour window from Notification 2 (1:00 PM on Day 1) resets. The count drops to 2.
* 2:00 PM: Send Notification 8. User receives Notification 8. (Count: 3) ✅

In this example, notifications 4, 6, and 7 would be capped and not delivered to the user, while 1, 2, 3, 5, and 8 would be delivered.

<Note> “Per Day” refers to a rolling 24-hour period, not a calendar day.
For example, if a user receives a message at 6:45 PM, their 24-hour window lasts until 6:45 PM the next day. Any additional messages sent before that time will count toward the cap and may be blocked. </Note>

***

## When to use frequency capping

Frequency Capping is particularly useful in scenarios where messaging volume may become excessive:

* **Complex Campaign Environments**: Large organizations with multiple teams or overlapping marketing campaigns.
* **High-Frequency Triggers**: Systems that send notifications based on frequent events (e.g., stock price updates or automated news alerts).

***

## How to enable frequency capping

You can configure frequency capping at the app level via the OneSignal Dashboard:

<Steps>
  <Step>
    Navigate to **Settings > Push & In-app > Frequency Capping**.
  </Step>

  <Step>
    Set the maximum number of messages a user can receive in a given time period.

    <Frame caption="Notifications can be capped at x notifications per any time frame.">
      <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/ca59ff47b3c7bd4fe834d818299d7365957de85d86b1b5577b111dcbbef4bfdd-Screenshot_2025-04-16_at_12.07.24_PM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=d2d6528f4b6cc767fca4c20eef01dfe1" width="2394" height="1520" data-path="images/docs/ca59ff47b3c7bd4fe834d818299d7365957de85d86b1b5577b111dcbbef4bfdd-Screenshot_2025-04-16_at_12.07.24_PM.png" />
    </Frame>
  </Step>
</Steps>

### Important notes

* Capping applies to all push messages, regardless of source (API, Journeys, or manual sends).
* Messages blocked due to capping are dropped, not queued for later.

For example, if the cap is set to 2/day and a user already received 2 API messages, a Journey message will be dropped unless capping is overridden.

***

## Override frequency capping

In some cases, you may want to send a message even if it exceeds the cap. You can override frequency capping on a per-message basis:

<Tabs>
  <Tab title="Dashboard">
    In the message’s **Delivery Schedule**, select **Override frequency capping settings**.

    <Frame>
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/81e1bd0-Screenshot_2022-11-16_at_3.14.52_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=876b3661b21dbdcb5ec1c00920b2912d" width="2102" height="642" data-path="images/docs/81e1bd0-Screenshot_2022-11-16_at_3.14.52_PM.png" />
    </Frame>
  </Tab>

  <Tab title="API">
    Using the [Create Push notification API](/reference/push-notification) you can override the frequency capping with the parameter:

    * `enable_frequency_cap` set to `false`
  </Tab>
</Tabs>

### Notes on overriding

* Frequency capping must be enabled in the OneSignal dashboard.
* Overridden messages still count toward the cap. This affects whether future messages are delivered.

***

## Reporting

When capping is enabled, you can monitor how it impacts your notifications via dashboard messages reports or view message API.

Each message with capping enabled will show a status of:

* **Capped**: Frequency capping is enabled for the app and how many were capped.
* **Overridden**: Frequency capping is enabled for the app, but was overridden for the notification.

***

Built with [Mintlify](https://mintlify.com).

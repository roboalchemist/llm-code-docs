# Source: https://documentation.onesignal.com/docs/en/throttling.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Push throttling

> Learn how to control push notification delivery rates using OneSignal's push throttling to manage server load, optimize user experience, and avoid delivery delays.

## Overview

Push throttling in OneSignal allows you to control the rate at which push notifications are delivered to users. This is particularly useful for managing server capacity and ensuring a smooth user experience during high-volume sends.

***

## Benefits

* **Manage server load** – Prevent overload by distributing message delivery over time.
* **Preserve performance** – Avoid performance degradation during mass sends.
* **Improve user experience** – Maintain consistency and responsiveness across devices.

***

## Configuration options

Throttling must be enabled at the global settings level to be available for use.

### Global throttling settings

Enable throttling for all push messages under **Settings > Push & In-App > Throttling**. Once enabled, this setting applies to all push notifications by default, but can be overridden for individual messages.

<Frame caption="Navigate to Push Throttling Settings">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8790df687f1783338ce3b61fe6be6c68dd878ff6998a4f5e2f2408adc8d57c68-Screenshot_2025-04-11_at_2.44.04_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=3f7368b4be0df94629d9664ac75e7503" width="2368" height="1316" data-path="images/docs/8790df687f1783338ce3b61fe6be6c68dd878ff6998a4f5e2f2408adc8d57c68-Screenshot_2025-04-11_at_2.44.04_PM.png" />
</Frame>

### Per-message throttling override

You can override global throttling settings on individual messages.

1. During notification creation, check the "Override throttling setting" box
2. Set your desired messages-per-minute rate
3. To disable throttling for a specific message, enter "0" in the messages-per-minute field

For API-sent notifications, use the `throttle_rate_per_minute` property.

<Info>
  Throttling must be enabled at the global settings level to be available for
  any use.
</Info>

***

## How throttling works

### Rate conversion process

OneSignal converts your per-minute setting to a per-second rate to optimize delivery:

1. The system divides your throttle rate by 60 (seconds per minute)
2. The result is rounded down to the nearest whole number (OneSignal can't send partial messages)
3. This per-second rate is then applied throughout the delivery process

<Card title="Throttling conversion example" icon="calculator">
  * You set 1019 messages per minute
  * Calculation 1019 ÷ 60 = 16.98 messages per second
  * Rounded down 16 messages per second
  * Actual delivery rate 16 × 60 = 960 messages per minute
  * Difference 59 fewer messages per minute than the set rate

  This conversion ensures more efficient processing by eliminating delays between batches.
</Card>

***

## Limitations and Considerations

### 24-Hour Delivery Window

All throttled notifications must complete delivery within 24 hours of being sent. If your throttling rate would cause delivery to exceed 24 hours, OneSignal automatically adjusts the rate to ensure completion within this timeframe.

<Card title="Automatic throttling adjustment example" icon="clock">
  If you set a throttle rate of 10 messages per minute for 20,000 users (which
  would take approximately 33 hours), OneSignal will automatically adjust the
  rate to around 14 messages per minute to ensure delivery completes within the
  required 24-hour window.
</Card>

## Compatibility with Other Features

### Timezone and Intelligent Delivery

Throttling takes precedence over Timezone and Intelligent Delivery options. When throttling is enabled, these features will be ignored for that notification.

**To use Timezone or Intelligent Delivery:**

* Disable throttling for that specific notification under Delivery Schedule
* Set "Override throttling setting" to "0"
* For API notifications, set `throttle_rate_per_minute: 0`

### Journeys and Automated Messages

Throttling is **not supported** for:

* **Journeys**
* **Automated Messages**

These features send notifications dynamically as users enter segments or trigger events, which naturally spreads out delivery over time.

<Tip>
  Notifications sent via Journeys or Automated Messages do not support
  throttling. These messages are paced automatically based on user behavior and
  do not require manual rate control.
</Tip>

***

## Availability

Throttling is only available for:

* Push notifications sent via the [Create notification](/reference/create-message) API
* Push notifications created through the **Messages > New Push** interface

***

Built with [Mintlify](https://mintlify.com).

# Source: https://documentation.onesignal.com/docs/en/live-activities.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Activities

> Learn how to use iOS Live Activities with OneSignal to deliver real-time updates directly to the lock screen and Dynamic Island. Enable seamless tracking for events like sports scores, deliveries, and more.

Live Activities allow your iOS and iPadOS apps to deliver real-time updates to the Lock Screen and Dynamic Island, keeping users informed without needing to open the app. Introduced in iOS 16.1 and expanded to iOS 17, Live Activities are perfect for time-sensitive information like delivery tracking, game scores, or transit updates.

<Note>
  Live Activities are an iOS feature, but you can achieve similar capabilities with [Android Live Notifications](./android-live-notifications).
</Note>

<Frame caption="Live Activities Examples">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/67688a22bb44b87b57a4bd27f114eea45298dfa4d1d48f1b64b2d449ea93c206-channel-setup-live-activities.jpg?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=dde03fd57c37604ed28894c0d49d1480" width="1280" height="720" data-path="images/docs/67688a22bb44b87b57a4bd27f114eea45298dfa4d1d48f1b64b2d449ea93c206-channel-setup-live-activities.jpg" />
</Frame>

***

## Why use Live Activities?

Live Activities are great for real-time, transactional, or time-bound updates.

* Visible for up to 8 hours
* Provisional — no permission is required to show the first Live Activity
* Highly engaging and visible on premium device surfaces like the Lock Screen and Dynamic Island

<Note>
  [Learn more about use cases in our blog →](https://onesignal.com/blog/new-live-activities-support-to-help-you-drive-loyalty-faster)
</Note>

***

## Why use OneSignal?

OneSignal simplifies Live Activities by handling:

* Temporary push token management
* Scaling to millions of devices with a single API call
* Real-time analytics and performance insights
* Cross-channel orchestration with Push, Email, SMS, and In-App Messages

<Note>
  Live Activities are available on all plans except Free plans with more than 10,000 opted-in subscribers. [See pricing](https://onesignal.com/pricing) or contact `support@onesignal.com` for assistance.
</Note>

***

## Getting started with Live Activities

### Requirements

* iOS 16.1+ or iPadOS 17+
* OneSignal [Mobile SDK integrated](./mobile-sdk-setup)
* Setup completed per our [Live Activities Developer Guide](./live-activities-developer-setup)
* Click tracking and Confirmed Delivery require iOS SDK version **5.2.15 or higher**

### How Live Activities work

* **Visible Duration**: Active for up to 8 hours (can be removed using the `dismissal_date` parameter in the [Update Live Activity API](/reference/update-live-activity-api)).
* **No Permission Needed**: First activity is provisional; future ones depend on user settings.
* **Limit**: Max 5 Live Activities per app simultaneously.
* **Remote Start**: Supported from iOS 17.2+ via push.
* **Non-promo Use**: Must provide user value—not designed for ads.

### Creating & Updating a Live Activity

<Steps>
  <Step title="Start a Live Activity">
    Live Activities can be started in 2 ways:

    1. Using our [Start Live Activity API](/reference/start-live-activity) aka "push-to-start".
    2. Triggering it in-app ([Live Activities Developer Setup](./live-activities-developer-setup)).
  </Step>

  <Step title="Update a Live Activity">
    Use the [Update Live Activity API](/reference/update-live-activity-api) and pass the `activity_id` to update all associated devices.
  </Step>

  <Step title="End a Live Activity">
    Live Activities can end in the following ways:

    <Tabs>
      <Tab title="OneSignal SDK (`exitLiveActivity`)">
        * Sends a request to OneSignal's server to stop sending updates for the given `activityId`.
        * **Does not** remove the Live Activity from the screen. It will be removed automatically after 4 hours or via user action.
      </Tab>

      <Tab title="Update Live Activity API">
        Use the `event: end` field to stop further updates and include a `dismissal_date` to remove the Live Activity from the screen:

        * The Live Activity will be removed from the screen automatically after 4 hours or via user action.
        * Set a **future** `dismissal_date` time within the next 4 hours to remove it sooner.
        * Set a **past** `dismissal_date` time to remove it immediately from the user's screen. User must have clicked "Allow" for the Live Activity to be removed programmatically.
      </Tab>

      <Tab title="User actions">
        * User manually dismisses the Live Activity, like swiping it away.
        * User revokes Live Activity permission in iOS Settings.
      </Tab>
    </Tabs>

    <Note>
      The SDK method does *not* dismiss the Live Activity visually.

      * Developers must use the API with `dismissal_date` or native iOS methods (e.g., `activity.end(dismissalPolicy: .immediate)`).
      * User must have clicked "Allow" for the Live Activity to be removed programmatically.
    </Note>
  </Step>
</Steps>

***

## Analytics & reporting

OneSignal provides comprehensive analytics to help you measure and optimize the performance of your Live Activities. Track key metrics like delivery rates, clicks, failures, and subscription changes.

**Key metrics available:**

* **Sent**: Live Activities sent from OneSignal to Apple Push Notification service (APNs)
* **Confirmed Delivery**: Live Activities confirmed delivered to devices (requires iOS SDK 5.2.15+)
* **Failed**: Live Activities that failed to deliver
* **Unsubscribed**: Subscriptions marked unsubscribed when users dismiss or disable Live Activities
* **Clicked**: Total clicks across all Live Activities

<Note>
  For detailed information on message reports, audience activity, exporting data, and performance analysis, see our [Live Activities Analytics guide](./live-activities-analytics).
</Note>

***

## Best practices & guidelines

### Functionality

* Use Live Activities for transactional or contextual updates (e.g., ETA, score, timer).
  * Instead of users constantly going into your app to check for statuses or changes, they can get updates at a glance of their phone.
  * Events or tasks with a defined beginning and an end. Do not use a Live Activity to display ads or serve purely promotional purposes. What value are you providing?
* Avoid excessive updates to preserve device battery.
* Ensure a Live Activity is for an event or task that is no longer than 8 hours, and that it is only showing for as long as it is useful to the user.

### UI/UX

* Support all Live Activity presentations: Compact, Minimal, Expanded, Lock Screen.
* Use branding, spacing, and dark/light themes correctly.
* Prioritize clarity and tap targets. Don't try to draw attention to the Dynamic Island.
* Avoid displaying sensitive information in a Live Activity.

<Note>
  Refer to Apple's [Live Activities Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/live-activities) for more information on best practices for Live Activities.
</Note>

### Targeting & sending at scale

Ensure that a Live Activity appears when expected, usually when a user takes an action (e.g. to follow an event) or opens the app to check for updates (e.g. updated delivery time).

* Target segments of users for events like sports games, concerts, or other live events.
* Target individual users for personal or transactional events.

<Note>
  Details on how to target users can be found in our [Sending messages with the OneSignal API docs](reference/create-message).
</Note>

When updating Live Activities, you have the option to set a "priority" which Apple uses to determine how urgent the update is. Apple has internal thresholds in which they will throttle requests that use the high priority flag too frequently. Due to this internal threshold, Apple recommends choosing a mix of normal and high priority to prevent throttling. Details on how to set priority can be found in our [Update Live Activity API reference](/reference/update-live-activity-api).

If your use case relies on more frequent high priority updates, you can add the key `NSSupportsLiveActivitiesFrequentUpdates` to your Info.plist as a Boolean type set to YES as directed in [Apple's Developer Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency). Users will be presented with a dialog when the Live Activity exceeds its push budget, and if they allow the Live Activity to continue, the budget will automatically be increased for a seamless user experience.

***

## FAQ

### Do I have access to Live Activities in my plan?

Live Activities are available on all plans except for Free plans with more than 10,000 opted-in subscribers. If you have more than 10,000 opted-in subscribers on a Free Plan, you can upgrade to use Live Activities. [See pricing](https://onesignal.com/pricing) or contact `support@onesignal.com` for assistance.

### What is the budget for high-priority updates?

Apple does not provide a fixed limit for high-priority (`priority: 10`) updates, but they do enforce a dynamic system-level budget. Sending too many high-priority updates in a short period may result in throttling, where updates are delayed or dropped.

To reduce the risk of throttling:

* Use a mix of priority levels: Apple recommends using both `priority: 5` (standard) and `priority: 10` (high) for balance.
* Reserve `priority: 10` for time-sensitive or critical updates only (e.g., order status changes, game scores).

If your use case requires frequent updates:

* Add the key `NSSupportsLiveActivitiesFrequentUpdates` to your app's `Info.plist` file, set as a Boolean `YES`.
* When this budget is exceeded, iOS may prompt the user to allow additional updates. If the user agrees, Apple will automatically expand the allowed update limit to maintain a seamless experience.

For more details, refer to [Apple's Developer Docs](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications#Determine-the-update-frequency).

### Where can I see Live Activities in the OneSignal Dashboard?

Live Activities can only be sent via our Live Activities APIs. However, you can view historically sent Live Activities (up to 30 days) in the dashboard in Sent Messages, after filtering for Live Activities. Here you will be able to see which Live Activities were sent, what updated information was sent, and the audience size that received the update.

### What devices work with Live Activities?

Apple keeps an updated compatibility guide with all devices that work with [iOS 16+](https://support.apple.com/guide/iphone/supported-models-iphe3fa5df43/16.0/ios/16.0) and [iPadOS 17+](https://support.apple.com/guide/ipad/ipad-models-compatible-with-ipados-17-ipad213a25b2/ipados).

***

<Check>
  You should now be equipped with everything you need to know about Live Activities.

  Start setting up your Live Activities by following our [Live Activities Developer Docs](./live-activities-developer-setup).
</Check>

***

Built with [Mintlify](https://mintlify.com).

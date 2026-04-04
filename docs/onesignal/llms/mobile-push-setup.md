# Source: https://documentation.onesignal.com/docs/en/mobile-push-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile push setup

> End-to-end checklist for setting up mobile push notifications with OneSignal across iOS, Android, Huawei, and Amazon.

Push notifications re-engage Users when they're not actively using your app. They can display text and rich content like images, buttons, and sounds.

<Frame caption="Push notification examples on iOS and Android.">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d6ba464616e546aaf62a5bda18adb4422d036815db4b2454e8a8b6a4dcf67706-channel-setup-mobile-push.jpg?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=63d1840679897262b47a004375a1bb33" alt="iOS and Android mobile push notification examples showing rich content" width="1280" height="720" data-path="images/docs/d6ba464616e546aaf62a5bda18adb4422d036815db4b2454e8a8b6a4dcf67706-channel-setup-mobile-push.jpg" />
</Frame>

For push to work on mobile:

* Users must have your mobile app installed
* You must configure the correct platform credentials (FCM for Android, APNs for iOS, HMS for Huawei, ADM for Amazon)
* Users must grant permission to receive notifications

This guide walks through every step from SDK setup to sending personalized push messages.

***

## SDK setup and migration

Integrate the OneSignal SDK into your app to register devices and enable push messaging. If you're migrating from another provider, OneSignal supports migration from Firebase, Airship, Braze, and others.

<Columns cols={2}>
  <Card title="Mobile SDK setup" icon="mobile" href="./mobile-sdk-setup">
    Integrate the OneSignal SDK into your app to register devices and enable push messaging.
  </Card>

  <Card title="Migration from another provider" icon="arrow-right-arrow-left" href="./migrating-to-onesignal">
    Migrate from Firebase, Airship, Braze, or other push providers.
  </Card>
</Columns>

***

## Push permission prompts

Mobile platforms require Users to opt in before they can receive push notifications. Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/notifications) recommend describing what types of information you want to send and giving Users a clear way to opt in or out.

You can build a pre-permission prompt using OneSignal's in-app messages to explain the value before triggering the system prompt.

<Frame caption="Custom pre-permission push prompt built with in-app messages.">
  <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/mobile-push-setup-ask-users-for-permission-to-send-push.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=aa31e67179d80c4b99c2d86102091d60" alt="OneSignal in-app message used as a pre-permission prompt for push notifications" width="2136" height="1338" data-path="images/push/mobile-push-setup-ask-users-for-permission-to-send-push.jpg" />
</Frame>

<Columns cols={2}>
  <Card title="Prompt for push permissions" icon="bell" href="./prompt-for-push-permissions">
    Build a custom pre-permission prompt using in-app messages.
  </Card>

  <Card title="Mobile SDK reference" icon="code" href="./mobile-sdk-reference">
    Programmatically trigger permission requests in the SDK.
  </Card>

  <Card title="iOS provisional push" icon="apple" href="./ios-provisional-push-notifications">
    Show silent notifications in the notification center before prompting.
  </Card>
</Columns>

***

## Users and Subscriptions

Once the SDK is active, OneSignal automatically creates User and Subscription records as people open your app.

Mobile Subscriptions are created when Users:

* Open the app for the first time on a device
* Uninstall and reinstall the app, then open it again

Each device creates a separate Subscription. Subscriptions remain anonymous until you assign them an [External ID](./users#external-id) via `OneSignal.login`.

<Frame caption="OneSignal dashboard: Audience > Users">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/users-page.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=8992ef97cf3c9f336078f9dbf8a6374e" alt="OneSignal dashboard Users page showing a list of Users with Subscription details" width="2316" height="858" data-path="images/dashboard/users-page.png" />
</Frame>

<Columns cols={2}>
  <Card title="Users" icon="users" href="./users">
    Manage Users, assign External IDs, and understand anonymous vs. identified Users.
  </Card>

  <Card title="Subscriptions" icon="address-book" href="./subscriptions">
    How Subscriptions are created and managed across devices and channels.
  </Card>

  <Card title="Segments" icon="chart-pie" href="./segmentation">
    Group Users into dynamic segments for targeted messaging.
  </Card>
</Columns>

***

## Design push notifications

Crafting effective push notifications involves more than text. Watch how to make every push notification count, then explore the design elements below.

<Frame caption="How to make every push notification count">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/mlXEsZA2qlM?si=tIstWJYNFOzrtMR5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

<Frame caption="Anatomy of a mobile push notification on iOS and Android.">
  <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/ios-and-android-mobile-push-expanded.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=5f0a3048b1b945ce1c960807992e4c74" alt="Annotated diagram showing the anatomy of iOS and Android push notifications" width="1467" height="726" data-path="images/push/ios-and-android-mobile-push-expanded.jpg" />
</Frame>

1. [Title](./push#title): Attention-grabbing headline (recommended: under 50 characters)
2. [Message](./push#message): Main notification content (recommended: under 120 characters)
3. [Icons](./notification-icons): Your brand icon or notification-specific image
4. [Large image](./push#image): Eye-catching visual content
5. [Action buttons](./action-buttons): Call-to-action buttons
6. Timestamp when push was received
7. [App name](./push#app-name): The name of your app

<Columns cols={2}>
  <Card title="Push overview" icon="bell" href="./push">
    Full overview of push notification creation, options, and delivery behavior.
  </Card>

  <Card title="Templates" icon="clone" href="./templates">
    Save time with reusable templates for consistent messaging.
  </Card>
</Columns>

### Personalization and localization

Watch how to turn generic push notifications into high-performing messages, then explore the personalization options below.

<Frame caption="How to turn generic push notifications into high-performing messages">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Rf6N_rezxuk?si=8t2pd1bxKeN5ofq-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

<Columns cols={2}>
  <Card title="Message personalization" icon="wand-magic-sparkles" href="./message-personalization">
    Insert dynamic variables like name or preferences to tailor messages.
  </Card>

  <Card title="Multi-language messaging" icon="language" href="./multi-language-messaging">
    Automatically deliver messages in each User's preferred language.
  </Card>
</Columns>

***

## Configure push behavior

Control how notifications behave after delivery, including timing, display settings, and User interactions.

### Delivery, display, and dismiss settings

<Columns cols={2}>
  <Card title="Throttling" icon="gauge-high" href="./throttling">
    Control notification delivery speed for large audiences.
  </Card>

  <Card title="Frequency capping" icon="hand" href="./frequency-capping">
    Set limits to prevent over-sending notifications to the same User.
  </Card>

  <Card title="Time to live (TTL)" icon="clock" href="./push#time-to-live-ttl">
    Define how long push services retain messages when the device is offline.
  </Card>

  <Card title="Collapse ID" icon="layer-group" href="./push#collapse-id-mobile-push">
    Replace previous messages with newer ones to reduce notification clutter.
  </Card>

  <Card title="Android notification categories" icon="android" href="./android-notification-categories">
    Control importance level (banner, silent) and other display aspects.
  </Card>

  <Card title="iOS focus modes and interruption levels" icon="apple" href="./ios-focus-modes-and-interruption-levels">
    Control priority level (passive, time-sensitive) for iOS.
  </Card>

  <Card title="Notification sounds" icon="volume-high" href="./notification-sounds">
    Configure notification audio for each platform.
  </Card>

  <Card title="Badges" icon="circle-1" href="./badges">
    Manage app icon badge count behavior on iOS.
  </Card>
</Columns>

### Data and background notifications

Include custom data in push payloads that your app can handle without displaying a visible notification.

<Columns cols={2}>
  <Card title="Data and background notifications" icon="database" href="./data-notifications">
    Send custom payloads without a visual notification.
  </Card>

  <Card title="Additional data" icon="brackets-curly" href="./push#additional-data">
    Attach key-value data to push payloads for in-app handling.
  </Card>
</Columns>

### Click behavior and deep linking

Control what happens when a User taps a notification.

<Columns cols={2}>
  <Card title="URLs, links, and deep linking" icon="link" href="./links">
    Route Users to relevant content or pages using deep links and tracking URLs.
  </Card>

  <Card title="Deep linking" icon="arrow-up-right-from-square" href="./deep-linking">
    Platform-specific deep linking implementation details.
  </Card>

  <Card title="Action buttons" icon="hand-pointer" href="./action-buttons">
    Let Users take immediate actions from your notification.
  </Card>

  <Card title="Notification event observers" icon="code" href="./mobile-sdk-reference#push-notification-events">
    Listen for click events and trigger in-app behavior with custom code.
  </Card>
</Columns>

***

## Analytics and troubleshooting

Measure notification performance and resolve common delivery issues.

<Columns cols={2}>
  <Card title="Push message reports" icon="chart-line" href="./push-notification-message-reports">
    View delivery, open rate, and click-through metrics for each message.
  </Card>

  <Card title="Analytics overview" icon="chart-bar" href="./analytics-overview">
    Explore engagement and User behavior metrics across channels.
  </Card>

  <Card title="Notifications not shown or delayed" icon="circle-exclamation" href="./notifications-show-successful-but-are-not-being-shown">
    Troubleshooting checklist if messages aren't appearing on devices.
  </Card>

  <Card title="Notification images not showing" icon="image" href="./notification-images-not-showing">
    Fix image rendering issues across platforms.
  </Card>

  <Card title="Duplicate notifications" icon="copy" href="./duplicated-notifications">
    Troubleshoot why duplicate notifications are being displayed.
  </Card>
</Columns>

***

## Next steps

<Columns cols={2}>
  <Card title="A/B testing" icon="flask" href="./ab-testing">
    Optimize messages with experiments to find what drives engagement.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated, multi-step messaging flows triggered by User behavior.
  </Card>

  <Card title="Tags" icon="tags" href="./add-user-data-tags">
    Add User-level data for personalization and targeting.
  </Card>

  <Card title="In-app messages" icon="window-maximize" href="./in-app-messages-setup">
    Reach Users with rich, interactive messages inside your app.
  </Card>
</Columns>

***

## FAQ

### Do Users need to opt in for push notifications?

Yes. Both iOS and Android require Users to grant permission before they can receive push notifications. On iOS, you must show the system prompt. On Android 13+, the `POST_NOTIFICATIONS` permission is required. Use a [pre-permission prompt](./prompt-for-push-permissions) to explain the value before triggering the system dialog.

### What are FCM, APNs, HMS, and ADM?

These are platform-specific push delivery services. **FCM** (Firebase Cloud Messaging) delivers to Android and web. **APNs** (Apple Push Notification service) delivers to iOS and macOS. **HMS** (Huawei Mobile Services) delivers to Huawei devices. **ADM** (Amazon Device Messaging) delivers to Amazon Fire devices. You configure credentials for each in the OneSignal dashboard during [SDK setup](./mobile-sdk-setup).

### Why aren't my push notifications showing?

Common causes include missing or expired platform credentials, Users not granting permission, or device-level settings like Do Not Disturb or Focus modes. See [Notifications not shown or delayed](./notifications-show-successful-but-are-not-being-shown) for a full troubleshooting checklist.

### Can I send push notifications without a visible notification?

Yes. Use [data and background notifications](./data-notifications) to send custom payloads that your app handles silently. These are useful for triggering background syncs, updating local data, or refreshing content without interrupting the User.

Built with [Mintlify](https://mintlify.com).

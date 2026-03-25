# Source: https://documentation.onesignal.com/docs/en/push.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Push overview

> Send and manage mobile and web push notifications with OneSignal using the dashboard or API, with targeting, personalization, and scheduling.

Push notifications re-engage Users with timely, personalized content across devices — even when they're not actively using your app or website.

Watch how push notifications drive the highest engagement, or skip ahead to get started.

<Frame caption="Why push notifications drive the highest engagement">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/atjjj4BQqfc?si=PP-XrMF8ttXkXkuQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

OneSignal provides a complete platform to manage push notifications across mobile, web, and desktop:

* **Send campaigns and transactional messages** from the [dashboard](#send-push-notifications) or [API](/reference/create-message)
* **Automate multi-channel flows** with [Journeys](./journeys-overview)
* **Target Users precisely** using [Segments](./segmentation), filters, or User data
* **[A/B test](./ab-testing) and optimize** message performance
* **Personalize content** with User attributes and [dynamic content](./message-personalization)
* **Integrate with your stack** — HubSpot, Mixpanel, Amplitude, Zapier, and [more](./integrations)

***

## Push setup

Before sending push notifications, complete the platform setup, configure permission prompts, and enable the features you need.

### Platform setup guides

<Columns cols={2}>
  <Card title="Mobile push setup" icon="mobile" href="./mobile-push-setup">
    End-to-end setup for iOS, Android, Huawei, and Amazon push notifications.
  </Card>

  <Card title="Web push setup" icon="globe" href="./web-push-setup">
    Enable push for Chrome, Firefox, Safari, and Edge.
  </Card>

  <Card title="Mobile SDK setup" icon="code" href="./mobile-sdk-setup">
    Integrate the OneSignal SDK into your mobile app.
  </Card>

  <Card title="Web SDK setup" icon="browsers" href="./web-sdk-setup">
    Integrate the OneSignal SDK into your website.
  </Card>

  <Card title="Migrating to OneSignal" icon="arrow-right-arrow-left" href="./migrating-to-onesignal">
    Migration steps from Firebase, Airship, Braze, and other providers.
  </Card>

  <Card title="macOS app support" icon="desktop" href="./macos-app-setup">
    Configure OneSignal for macOS apps.
  </Card>

  <Card title="Windows app support" icon="desktop" href="./windows-app-setup">
    Configure OneSignal for Windows desktop apps.
  </Card>

  <Card title="watchOS and Wear OS support" icon="clock" href="./watchos-and-wear-os-support">
    Add OneSignal to Apple Watch and Wear OS devices.
  </Card>
</Columns>

### Permissions

A well-designed opt-in experience maximizes your push audience.

<Columns cols={2}>
  <Card title="Mobile push prompts" icon="bell" href="./prompt-for-push-permissions">
    Build pre-permission prompts and best practices for mobile apps.
  </Card>

  <Card title="Web push prompts" icon="bell-on" href="./permission-requests">
    Customize prompt timing and messaging for web push.
  </Card>

  <Card title="iOS provisional push" icon="apple" href="./ios-provisional-push-notifications">
    Deliver silent notifications to the notification center before prompting for full permission.
  </Card>

  <Card title="Android notification categories" icon="android" href="./android-notification-categories">
    Let Android Users customize how they receive notifications from your app.
  </Card>
</Columns>

### Features and advanced use cases

<Columns cols={2}>
  <Card title="Message personalization" icon="wand-magic-sparkles" href="./message-personalization">
    Add dynamic content to personalize messages for each User.
  </Card>

  <Card title="Multi-language messaging" icon="language" href="./multi-language-messaging">
    Send push notifications in each User's preferred language.
  </Card>

  <Card title="Throttling" icon="gauge-high" href="./throttling">
    Control notification delivery speed for large audiences.
  </Card>

  <Card title="Frequency capping" icon="hand" href="./frequency-capping">
    Limit the number of push notifications per User.
  </Card>

  <Card title="Data and background notifications" icon="database" href="./data-notifications">
    Send data-only notifications for background tasks.
  </Card>

  <Card title="VoIP notifications" icon="phone" href="./voip-notifications">
    Send VoIP-specific push notifications for calling apps.
  </Card>
</Columns>

***

## Send push notifications

You can send messages in several ways. The best option depends on your use cases.

<Columns cols={2}>
  <Card title="Dashboard" icon="window-maximize" href="#send-from-the-dashboard">
    Compose a message quickly within the dashboard.
  </Card>

  <Card title="Send via API" icon="code" href="/reference/create-message">
    Send messages programmatically using the REST API.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated, multi-step, and multi-channel flows.
  </Card>

  <Card title="A/B testing" icon="flask" href="./ab-testing">
    Test up to 10 message variants to optimize performance.
  </Card>
</Columns>

### Send from the dashboard

<Steps>
  <Step title="Select the message channel" icon="window-maximize">
    Select **Create...** then choose your message channel. You can also navigate to **Messages** or **Templates** to view previous messages.

    <Frame caption="Create a new message in the OneSignal dashboard.">
      <img src="https://mintcdn.com/onesignal/UDk6E5NjA3sdGdRN/images/dashboard/create-message.png?fit=max&auto=format&n=UDk6E5NjA3sdGdRN&q=85&s=97504cf71555ac4aeb263a36ad2d28b3" alt="OneSignal dashboard showing create message options" width="2128" height="1374" data-path="images/dashboard/create-message.png" />
    </Frame>
  </Step>

  <Step title="Choose a composition method" icon="pencil">
    * Start from scratch or use the [AI message composer](./ai-message-composer).
    * Use a pre-built [template](./templates)
  </Step>

  <Step title="Set a name and label" icon="tag">
    Add internal metadata for tracking and reporting. API equivalent: `name`
  </Step>

  <Step title="Select your audience" icon="users">
    Choose which users receive the message. You can include and exclude [segments](./segmentation) to target specific groups. Defaults to all "Subscribed Users" if no segment is set.

    <Frame caption="Name, label, and audience segment selection in the dashboard.">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/message-name-label-audience.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=1f41b0e42d31211b1c1badf87ba84056" alt="Dashboard fields for message name, label, and audience segment selection" width="1650" height="518" data-path="images/dashboard/message-name-label-audience.png" />
    </Frame>

    | Targeting method                                    | Dashboard | API |
    | --------------------------------------------------- | :-------: | :-: |
    | [**Segments**](./segmentation)                      |    Yes    | Yes |
    | **Filters** ([API only](/reference/create-message)) |     No    | Yes |
    | **Aliases** ([API only](/reference/create-message)) |     No    | Yes |
  </Step>
</Steps>

### Delivery schedule and optimization

See how timing impacts push notification performance.

<Frame caption="Timing is everything: How to send push notifications that drive action">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/pRTbUuvYsWY?si=uqL5wSK_vXH6VwMJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Choose when the message should start sending.

| Option               | Description                                        | API field    |
| -------------------- | -------------------------------------------------- | ------------ |
| **Send immediately** | Deliver to all recipients now.                     | —            |
| **Scheduled**        | Send at a specific time, up to 30 days in advance. | `send_after` |

**Per-user optimization:**

Set when users should receive the message.

| Option                                                | Description                                                              | API field                                          |
| ----------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------- |
| **Everyone at the same time**                         | All recipients receive the email at once. Best for urgent messages.      | —                                                  |
| **Intelligent Delivery**                              | Sends at the optimal time for each user based on their session activity. | `delayed_option: last-active`                      |
| **Custom time per timezone**                          | Sends at a set local time in each user's timezone.                       | `delayed_option: timezone`, `delivery_time_of_day` |
| **Override [Throttling](./throttling)**               | Change the throttle rate.                                                | `throttle_rate_per_minute`                         |
| **Override [Frequency capping](./frequency-capping)** | Disable frequency capping for this message.                              | `enable_frequency_cap`                             |

### Design properties

Push messages can either display User-facing content or perform background operations.

* **Display notifications**: Require a [message](#message) and may include a title, image, action buttons, and other visual elements.
* **Background/data-only notifications**: Omit the message, include [content\_available](./data-notifications), and optionally [additional data](#additional-data).

<Frame caption="1: Title, 2: Message, 3: Icon, 4: Image, 5: Action buttons, 6: App name or browser, 7: Timestamp received">
  <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/web-and-mobile-push-notifications-anatomy.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=abd46b4656559360cc713cfa98f138fe" alt="Annotated diagram showing the anatomy of web and mobile push notifications" width="1468" height="2302" data-path="images/push/web-and-mobile-push-notifications-anatomy.jpg" />
</Frame>

<Tip>
  Use the [AI message composer](./ai-message-composer) to quickly generate notification titles and body text. Adjust tone and content to match your brand in a few clicks.
</Tip>

#### Title

Top-most customizable text of the notification. Text appearance is controlled by the operating system.

* Required for **web push** and **Huawei**
* Defaults to site name on web if not set
* Recommended limit: 25–50 characters (mobile), 60–80 (web)
* Supports: [AI message composer](./ai-message-composer), emojis, [message personalization](./message-personalization), [multi-language messaging](./multi-language-messaging)
* API: `headings`

#### Subtitle

Secondary text supported on iOS and macOS only (via APNs). Not available on Android or web.

* Recommended limit: 25–50 characters
* Supports: emojis, [message personalization](./message-personalization), [multi-language messaging](./multi-language-messaging)
* API: `subtitle`

#### Message

Main content of the notification. Does not support custom fonts or styling. Style is set by the operating system.

* Required unless sending a background notification
* Supports: [AI message composer](./ai-message-composer), emojis, [message personalization](./message-personalization), [multi-language messaging](./multi-language-messaging)
* Recommended limit: \~150 characters
* API: `contents`

#### Icons

Customize small and large icons on Android and web. iOS always uses the app icon.

* See [Notification icons](./notification-icons)

#### Image

Add a large image to notifications on Android, iOS, and Chrome for Windows/Android.

* Recommended size: `1024×512px` (2:1 aspect ratio)
* Max size: 1 MB, max width: 2000 px
* Not supported on Safari (macOS/iOS) or macOS Notification Center
* Must be tapped or expanded on mobile to view
* Supported formats: `PNG`, `JPG`, `GIF` (animated only on iOS)
* API: `ios_attachments` (iOS), `big_picture` (Android), `chrome_web_image` (Chrome web)
* See [Images and rich media](./rich-media)

#### App name

The name of the app displaying the notification.

* **iOS**: Set in Xcode under *Display Name*; requires device restart to update
* **Android/Amazon/Huawei**: Set in `AndroidManifest.xml` under `<application android:label="YOUR APP NAME">`
* **Web**: Shows the site name and/or browser

### Feature properties

#### Action buttons

Add interactive buttons to the push notification.

* Supported on Android 4.1+ and iOS 8.0+
* See [Action buttons](./action-buttons)

#### Launch URL

Control where Users go when tapping the notification.

* API: `url` (single universal URL), `app_url` (deep link, e.g. `your-app://screen`), `web_url` (http/https web link)
* See [URLs, links, and deep links](./links)

#### Badges

Show dots or badge numbers on app icons.

* **iOS**: Red numeric badge; can set, increment, or clear. API: `ios_badgeType`, `ios_badgeCount`
* **Android**: Requires [notification categories](./android-notification-categories)
* **Huawei**: Badge displayed as a number or dot. API: `huawei_badge_class`, `huawei_badge_set_num`, `huawei_badge_add_num`
* **Web (Chrome/Android)**: Icon shown in Android status bar; must be a 72×72 alpha PNG. API: `chrome_web_badge`
* See [Badges](./badges)

#### Sound

Play a sound when the push is delivered.

* **iOS**: Set with `sound`
* **Android**: Set via [notification categories](./android-notification-categories)
* **Web**: Not available

#### Additional data

Add custom key-value pairs to the payload for SDK handling.

* Used by [mobile service extensions](./service-extensions) and click listeners in the [mobile SDK](./mobile-sdk-reference) and [web SDK](./web-sdk-reference)
* Dashboard supports only simple key-value data; use the API with `data` to send nested JSON
* Max total payload: \~4 KB; `data` field: up to 2048 bytes
* See [Notification payload reference](./osnotification-payload)

#### Collapse ID (mobile push)

Replace earlier notifications with a newer one if they share the same `collapse_id`. Max length: 64 characters. API: `collapse_id`

For example, a weather app sends three alerts. If the User opens their device after all three, only the last message displays.

#### Web push topic (web push)

Avoid replacing older web notifications by using unique `web_push_topic` values. Notifications with different topics remain visible independently. Max length: 64 characters. API: `web_push_topic`

#### Priority

Set the urgency of the push, especially in battery-saving modes.

* **High** (recommended): Immediate, alert-based messages
* **Normal**: Used for background/data notifications
* API: `priority`
* Platform docs: [APNs priority](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns), [FCM priority](https://firebase.google.com/docs/cloud-messaging/android/message-priority)

#### Time to live (TTL)

How long to keep a message if the device is offline. Default: 3 days. Range: 0–2,419,200 seconds (28 days). API: `ttl`

If a User is offline and the TTL expires, the message is discarded. Set `ttl: 0` for messages that should never be delivered late.

<Note>
  **iOS limitation**: APNs stores only the most recent notification while the device is offline. Earlier notifications are dropped. [Learn more](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW5).
</Note>

#### Notification grouping

Android and iOS automatically group notifications after a device receives 4 or more from your app.

* **iOS**: Use `thread_id` in the API to group messages together.
* **Android**: Use `android_group` in the API, or set the "Group Key" in the dashboard. For advanced customization, see [Android NotificationExtenderService](./service-extensions#android-notification-extender-service) and [Android's group notify guide](https://developer.android.com/training/notify-user/group).

<Frame caption="Grouped notifications on Android.">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/GnEw4PmmSVWWfgX5Uc3W_stacked_notification.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=cee04b5675b291562d92add259bc2224" alt="Android device showing grouped push notifications from the same app" width="900" height="460" data-path="images/docs/GnEw4PmmSVWWfgX5Uc3W_stacked_notification.png" />
</Frame>

***

## Cancel push notifications

Cancel a message if it has not been **Delivered** yet. OneSignal stops sending the message to all Subscriptions not already in the queue. This does not remove the message from devices that already received it.

In the [Message Report](./push-notification-message-reports), select **Actions > Cancel**, or use the [Cancel Message API](/reference/cancel-message).

### Remove a push notification from a device

Once delivered, you can only replace a push notification if you set a [Collapse ID](#collapse-id-mobile-push) or [Web push topic](#web-push-topic-web-push). Without one of these, the notification cannot be replaced or removed.

***

## Analytics

Track message performance and engagement.

<Columns cols={2}>
  <Card title="Push message reports" icon="chart-line" href="./push-notification-message-reports">
    Message-level delivery, open rate, and click-through reporting.
  </Card>

  <Card title="Analytics overview" icon="chart-bar" href="./analytics-overview">
    All analytics options available in OneSignal.
  </Card>

  <Card title="Event Streams" icon="signal-stream" href="./event-streams">
    Stream push events to your data warehouse or BI tools in real time.
  </Card>

  <Card title="View messages API" icon="code" href="/reference/view-messages">
    Pull message analytics programmatically via the REST API.
  </Card>
</Columns>

***

## FAQ

### What platforms does OneSignal push support?

OneSignal supports push on iOS (APNs), Android (FCM), Huawei (HMS), Amazon (ADM), web browsers (Chrome, Firefox, Safari, Edge), macOS, and Windows. See the [platform setup guides](#platform-setup-guides) above.

### How do I test push notifications before sending to Users?

Set up [test Subscriptions](./find-set-test-subscriptions) to verify delivery, rendering, and deep links without affecting real Users. You can also send to a single-user segment for quick testing.

### Why are my push notifications not showing?

Common causes include missing or expired platform credentials, Users not granting permission, or device-level settings like Do Not Disturb. See [Notifications not shown or delayed](./notifications-show-successful-but-are-not-being-shown) for a full troubleshooting checklist.

### What is the maximum push notification payload size?

The total payload size is approximately 4 KB across all platforms. The `data` field supports up to 2048 bytes. Exceeding these limits may cause notifications to be truncated or rejected.

Built with [Mintlify](https://mintlify.com).

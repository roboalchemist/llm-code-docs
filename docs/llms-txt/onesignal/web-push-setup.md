# Source: https://documentation.onesignal.com/docs/en/web-push-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web push setup

> Set up web push notifications with OneSignal to re-engage Users across Chrome, Firefox, Safari, and Edge.

Web push notifications re-engage Users with timely content — even when they're not actively browsing your website. They support rich content including text, images, action buttons, and sounds.

<Frame caption="Web push notifications reach Users even when they're not on your site">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/ac9092f6fd99acc866af2598470d3b4b6e8233d947e45d8aade0b8bfcea71c8f-channel-setup-web-push.jpg?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=e73d6a84ca1e7ea2402ca3dc73d33f02" alt="Web push notification examples across different browsers and devices" width="1280" height="720" data-path="images/docs/ac9092f6fd99acc866af2598470d3b4b6e8233d947e45d8aade0b8bfcea71c8f-channel-setup-web-push.jpg" />
</Frame>

For web push to work:

* **HTTPS website**: Web push only works on secure sites with a valid SSL certificate
* **Service worker**: You must be able to add the [OneSignal service worker](./onesignal-service-worker) to your website
* **Single domain origin**: Must follow the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
* **User permission**: Users must explicitly grant permission to receive notifications
* **Supported browsers**: Works across most modern browsers (Chrome, Firefox, Safari, Edge)

<Warning>
  Users cannot subscribe while in incognito or private browsing mode. iOS devices require additional setup (see [Web push for iOS](./web-push-for-ios)). Some browsers may have notification limits or require user interaction — see [Web push FAQ](./web-push-setup-faq).
</Warning>

This guide walks through every step from SDK setup to sending personalized push messages.

***

## Web push developer guides

Before sending web push notifications, complete the following setup steps.

<Note>
  Not a developer? See [Manage team members](./manage-team-members) to invite a teammate with developer access to your OneSignal project.
</Note>

<Columns cols={2}>
  <Card title="Web SDK setup" icon="browsers" href="./web-sdk-setup">
    Install and configure the OneSignal Web SDK, including localhost testing and permission prompts.
  </Card>

  <Card title="WordPress plugin" icon="plug" href="./wordpress">
    Integrate push notifications on WordPress using the official plugin — no coding required.
  </Card>

  <Card title="iOS web push setup" icon="apple" href="./web-push-for-ios">
    Follow Apple-specific steps to enable web push on iPhones and iPads running iOS 16.4+.
  </Card>

  <Card title="Migration from another provider" icon="arrow-right-arrow-left" href="./migrating-to-onesignal">
    Transition from another web push provider and retain your Subscriptions.
  </Card>
</Columns>

***

## Configuration options

Set up your website for web push in the OneSignal dashboard under **Settings > Push & In-App > Web**.

<Frame caption="Activate the web platform in your OneSignal settings">
  <img src="https://mintcdn.com/onesignal/KPVdijCt4_xCbkO8/images/dashboard/web-push-platform-activation.png?fit=max&auto=format&n=KPVdijCt4_xCbkO8&q=85&s=beba7df5d3a4ad5545311951da0f03d2" alt="OneSignal dashboard showing web push platform activation in settings" width="1188" height="597" data-path="images/dashboard/web-push-platform-activation.png" />
</Frame>

Select the integration type that matches your site:

<Frame caption="Choose your integration type based on your website setup">
  <img src="https://mintcdn.com/onesignal/BK2J-grzBpDdh8NC/images/dashboard/web-push-integration-type-options.png?fit=max&auto=format&n=BK2J-grzBpDdh8NC&q=85&s=f74c4245d969d80db72268a865bcf899" alt="OneSignal dashboard showing integration type options: Typical Site, WordPress, and Custom Code" width="2668" height="1454" data-path="images/dashboard/web-push-integration-type-options.png" />
</Frame>

<Columns cols={3}>
  <Card title="Typical site" icon="globe" href="./web-sdk-setup">
    **Recommended** — Configure prompts, welcome notification, and service worker setup directly in the dashboard.
  </Card>

  <Card title="WordPress" icon="plug" href="./wordpress">
    Use the official OneSignal WordPress plugin and configure prompts and welcome notification directly in the dashboard.
  </Card>

  <Card title="Custom code" icon="code" href="./web-push-custom-code-setup">
    Full control for developers who want to customize everything via code.
  </Card>
</Columns>

Site details:

* **Site Name**: Used in default notification titles
* **Site URL**: Must exactly match your domain origin (no paths or `www` mismatch)
* **Auto Resubscribe**: Recommended — Automatically re-subscribes returning Users who cleared browser data
* **Default Icon URL**: `256x256px` image shown in notifications (if unset, a default bell icon is used)

### Auto resubscribe

If Users clear their browser data, they stop receiving push notifications. Enable this option to automatically re-subscribe Users when they return to your site. See [Subscriptions](./subscriptions) for more details.

<Frame caption="Web settings in the OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1c14649d87698eba5cb74297a64064c9754ccb64e6335466e5a160edf9f4c009-Screenshot_2024-10-25_at_1.35.23_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=b34a1a59e462eba01c13fbf24327b4da" alt="OneSignal dashboard web push configuration settings showing site details and auto resubscribe option" width="2072" height="712" data-path="images/docs/1c14649d87698eba5cb74297a64064c9754ccb64e6335466e5a160edf9f4c009-Screenshot_2024-10-25_at_1.35.23_PM.png" />
</Frame>

***

### Web permission prompts

Prompting Users for notification permission is critical for opt-in. You can customize the behavior and appearance of permission requests based on your setup.

<Tip>
  Use clear messaging that explains the benefit, prompt Users at the right time (e.g., after engagement), and use a pre-prompt before triggering the native browser dialog.
</Tip>

<Columns cols={2}>
  <Card title="Web permission prompts" icon="bell" href="./permission-requests">
    Compare different prompt types (slidedown, category-based, native, subscription bell, and more).
  </Card>

  <Card title="Web SDK reference" icon="code" href="./web-sdk-reference">
    Programmatically control when and how prompts are shown using the SDK.
  </Card>
</Columns>

***

### Welcome notification

You can enable an optional confirmation push that's sent immediately after a User subscribes. Typical and WordPress integrations can set this in the dashboard.

<Frame caption="Welcome notifications confirm successful Subscription and demonstrate value">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f33b02284d74f534669e87edfc8cd23e6be06eb8e705f640fd96bd8b7292ff4d-Screenshot_2024-10-25_at_2.06.50_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=a70fc05fa5728334e75b95bbb276a923" alt="OneSignal dashboard showing welcome notification configuration with title, message, and URL fields" width="2072" height="728" data-path="images/docs/f33b02284d74f534669e87edfc8cd23e6be06eb8e705f640fd96bd8b7292ff4d-Screenshot_2024-10-25_at_2.06.50_PM.png" />
</Frame>

Custom Code integration uses the `welcomeNotification` object in the `OneSignal.init` function. See [Web SDK reference](./web-sdk-reference) for details.

**Why send welcome notifications?**

* Let Users know they've subscribed successfully
* Show what future notifications will look like
* Provide onboarding content or next steps

***

## Users and Subscriptions

When a User subscribes to push, OneSignal automatically creates a unique Subscription tied to their browser and device.

Web push Subscriptions are created when Users:

* Grant permission for push notifications on your website using a specific browser and device
* Return to your site after clearing browser data (if Auto Resubscribe is enabled)
* Subscribe from a new browser or device

<Note>
  Each browser/device combination creates a separate Subscription. Incognito/private browsing mode cannot create Subscriptions. Web push Subscriptions remain anonymous until you assign them an [External ID](./users#external-id).
</Note>

<Frame caption="OneSignal dashboard: Audience > Users">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/users-page.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=8992ef97cf3c9f336078f9dbf8a6374e" alt="OneSignal dashboard Users page showing a list of Users with Subscription details" width="2316" height="858" data-path="images/dashboard/users-page.png" />
</Frame>

<Columns cols={2}>
  <Card title="Users" icon="users" href="./users">
    Manage Users, assign External IDs, and track their activity.
  </Card>

  <Card title="Subscriptions" icon="address-book" href="./subscriptions">
    How Subscriptions work across browsers and devices.
  </Card>

  <Card title="Segments" icon="chart-pie" href="./segmentation">
    Group Users into Segments to target based on behavior, device, and more.
  </Card>
</Columns>

### iOS support

Apple added web push support for iPhones and iPads running iOS 16.4+ with stricter requirements:

* Users must add your site to their Home Screen
* Permission prompts are shown only after that step
* Notifications behave like native app alerts once enabled

<Columns cols={2}>
  <Card title="Web push for iOS" icon="apple" href="./web-push-for-ios">
    Step-by-step instructions to enable iOS support, including service worker and manifest setup.
  </Card>

  <Card title="Add to Home Screen guide" icon="mobile" href="./web-push-for-ios#step-4%3A-guide-users-to-%E2%80%9Cadd-to-home-screen%E2%80%9D">
    Tips for encouraging Users to install your site so they can receive iOS web push.
  </Card>
</Columns>

***

## Design web push notifications

Crafting effective push notifications involves more than text. Learn what elements are customizable and how to use them.

<Frame caption="Web push notification anatomy — customize elements 1–6, while 7–9 are controlled by the browser">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/dd4f79c-Web_Push_Examples.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=8d72d6952cd50f8c01a49ada61a15456" alt="Annotated diagram showing the anatomy of a web push notification with customizable and browser-controlled elements" width="1937" height="1359" data-path="images/docs/dd4f79c-Web_Push_Examples.png" />
</Frame>

1. [Title](./push#title): Attention-grabbing headline (recommended: under 50 characters)
2. [Message](./push#message): Main notification content (recommended: under 120 characters)
3. [Icon](./notification-icons): Your brand icon or notification-specific image (recommended: `256x256px` PNG or JPG)
4. [Large image](./push#image): Eye-catching visual content
5. [Action buttons](./action-buttons): Call-to-action buttons
6. Browser: The browser/app displaying the push
7. Domain: Your site origin automatically set by the browser
8. Timestamp and dismiss: Browser adds these controls
9. More options: Browser-specific additional controls

<Columns cols={2}>
  <Card title="Push overview" icon="bell" href="./push">
    Full overview of push notification creation, options, and delivery behavior.
  </Card>

  <Card title="Templates" icon="clone" href="./templates">
    Save time with reusable templates for consistent messaging.
  </Card>
</Columns>

### Personalization and localization

Customize push messages to match each User's preferences and language.

<Columns cols={2}>
  <Card title="Message personalization" icon="wand-magic-sparkles" href="./message-personalization">
    Insert dynamic variables like name or preferences to tailor messages.
  </Card>

  <Card title="Multi-language messaging" icon="language" href="./multi-language-messaging">
    Deliver messages in each User's preferred language.
  </Card>
</Columns>

***

## Configure web push behavior

Control how your push messages behave after sending — when they appear, how long they're stored, and how Users interact.

### Delivery, display, and dismiss settings

<Columns cols={2}>
  <Card title="Throttling" icon="gauge-high" href="./throttling">
    Control notification delivery speed.
  </Card>

  <Card title="Frequency capping" icon="hand" href="./frequency-capping">
    Set limits to prevent over-sending notifications to the same User.
  </Card>

  <Card title="Time to live (TTL)" icon="clock" href="./push#time-to-live-ttl">
    Define how long push services retain messages when the device is offline.
  </Card>

  <Card title="Web push topic" icon="layer-group" href="./push#web-push-topic-web-push">
    Use topics to group, replace, or suppress duplicate notifications.
  </Card>
</Columns>

### Click behavior

Control what happens when a User clicks a notification.

**By default:** Clicking opens your homepage.

**Customize it:**

* Direct Users to a specific URL
* Use UTM tracking
* Suppress default behavior with `?_osp=do_not_open`

<Columns cols={2}>
  <Card title="URLs, links, and deep linking" icon="link" href="./links">
    Route Users to relevant content or pages using deep links and tracking.
  </Card>

  <Card title="Action buttons" icon="hand-pointer" href="./action-buttons">
    Let Users take immediate actions from your notification.
  </Card>

  <Card title="Web SDK push event listeners" icon="code" href="./web-sdk-reference#push-notifications">
    Listen for click events and trigger in-app behavior with custom code.
  </Card>
</Columns>

***

## Test your setup

Before launching, thoroughly test your web push implementation across devices and browsers.

### Pre-launch checklist

* SDK is correctly loaded with no console errors
* Permission prompt appears and functions correctly
* Test notification is sent and received
* Icons and images render correctly
* Service worker is registered and up to date
* HTTPS certificate is valid

### Analytics and troubleshooting

Measure notification performance and resolve common delivery issues.

<Columns cols={2}>
  <Card title="Push message reports" icon="chart-line" href="./push-notification-message-reports">
    View delivery, open rate, and click-through metrics for each message.
  </Card>

  <Card title="Analytics overview" icon="chart-bar" href="./analytics-overview">
    Explore engagement and User behavior metrics across channels.
  </Card>

  <Card title="Notifications not shown or delayed" icon="circle-exclamation" href="./notifications-not-shown-web-push">
    Troubleshooting checklist if messages aren't appearing.
  </Card>

  <Card title="Notification images not showing" icon="image" href="./notification-images-not-showing">
    Fix image rendering issues across different browsers.
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

  <Card title="Analytics" icon="chart-bar" href="./analytics-overview">
    Track engagement and conversion metrics across channels.
  </Card>
</Columns>

***

## FAQ

### Can Users subscribe to web push on iOS?

Yes, starting with iOS 16.4+. Users must first add your website to their Home Screen, then grant notification permission. See [Web push for iOS](./web-push-for-ios) for the full setup steps.

### Why did a User stop receiving web push notifications?

The most common cause is that the User cleared their browser data, which removes the push Subscription. Enable **Auto Resubscribe** in your web push settings to automatically re-subscribe returning Users. See [Subscriptions](./subscriptions) for details.

### Do web push notifications work in incognito or private browsing mode?

No. Users cannot subscribe to web push while in incognito or private browsing mode. Subscriptions created in a normal session are not accessible in private mode.

### What browsers support web push notifications?

Chrome, Firefox, Safari (macOS and iOS 16.4+), and Edge all support web push. Each browser may have different prompt behavior and notification display. See [Web push FAQ](./web-push-setup-faq) for browser-specific details.

### Why is my web push prompt not showing?

Common causes include: the site is not served over HTTPS, the service worker is not registered correctly, the User already granted or denied permission, or the User is in incognito mode. Check the browser console for errors and see [Notifications not shown](./notifications-not-shown-web-push) for a full checklist.

Built with [Mintlify](https://mintlify.com).

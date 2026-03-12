# Source: https://documentation.onesignal.com/docs/en/prompt-for-push-permissions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt for push permissions

> Ask users for push notification permission at the right moment using in-app soft prompts and the native system prompt on iOS and Android.

## Why use a push permission prompt?

To send push notifications that appear as banners, show on the lock screen, and play sounds, your app must first request permission from the user. On iOS, Android, Huawei, Amazon, and Web, this involves displaying a system-level permission prompt.

<Frame caption="An iOS and Android device displaying the system-level permission prompt.">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7ace2bd5abf90a044c363ec9acb227467b62a7f49fdf0dd2922280dc188f4973-a90c2cc443f5fe9e7c80368c680a16cf1ca6203f7b28a0a6eec212add8510f80-Untitled_design_11.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=381c6c0ecf9c24cda0e9153fc582e319" alt="iOS and Android system-level push permission prompts side by side" width="1920" height="1080" data-path="images/docs/7ace2bd5abf90a044c363ec9acb227467b62a7f49fdf0dd2922280dc188f4973-a90c2cc443f5fe9e7c80368c680a16cf1ca6203f7b28a0a6eec212add8510f80-Untitled_design_11.png" />
</Frame>

This guide is for mobile app push subscribers. For web push, see [Web push permission prompts](./permission-requests).

**Prerequisites:** A [OneSignal account](https://dashboard.onesignal.com), a mobile app with the [OneSignal SDK installed](./mobile-sdk-setup), and [in-app messages enabled](./in-app-messages-setup).

<Warning>
  iOS allows the system permission prompt only once. Android allows it twice. If the user declines, they must manually enable notifications in system settings. A poorly timed prompt can permanently cost you a subscriber.
</Warning>

<Tip>
  On iOS, you can also use [provisional notifications](./ios-provisional-push-notifications), which deliver quietly to the Notification Center without prompting the user — ideal for testing or low-friction onboarding.
</Tip>

Because the system prompt is limited, both [Apple](https://developer.apple.com/design/human-interface-guidelines/managing-notifications) and [Google](https://developer.android.com/training/permissions/requesting) strongly recommend explaining the value of your notifications before showing it. You can trigger the prompt at any time using the `requestPermission()` [SDK method](./mobile-sdk-reference#requestpermission-fallbacktosettings-push-push), but without proper context, users are more likely to decline — and on iOS, a declined prompt cannot be shown again.

The recommended approach is a "soft prompt" — a custom in-app message that introduces the request before the system prompt. If the user accepts, the system prompt appears. If they decline, nothing happens and you can ask again later.

<Frame caption="An in-app soft prompt followed by the system-level push permission prompt.">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a6d382ca2711ba0e9f013bebe5c420d129fbfbc5ef0b2fbd9cb4bef78c7e9480-mobile-push-optimize-reach.webp?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=bfbc66b313bd85f944476e8363f1d093" alt="In-app message leading to system push permission prompt" width="1600" height="1058" data-path="images/docs/a6d382ca2711ba0e9f013bebe5c420d129fbfbc5ef0b2fbd9cb4bef78c7e9480-mobile-push-optimize-reach.webp" />
</Frame>

***

## Set up an in-app push permission prompt

<Steps>
  <Step title="Remove any automatic permission prompts">
    Before you begin, make sure your app isn't already triggering the native push prompt automatically:

    * Remove `requestPermission()` or `optIn()` methods if you're calling them on app start.
    * Remove native iOS calls to `requestAuthorizationWithOptions` and any methods generating push tokens.
    * Remove Android calls to `requestPermissions` and any methods generating push tokens.

    Also, make sure you're using the [latest version of the OneSignal SDK](https://github.com/OneSignal/sdks) in your app.
  </Step>

  <Step title="Create or edit the in-app message">
    Go to **Messages > In-App**, then either:

    * Edit the default Push Permission Prompt template, or
    * Click New Message to create your own.

    <Frame caption="Edit the default Push Permission Prompt template or create your own.">
      <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/prompt-for-push-set-up-an-in-app-push-permission-prompt.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=80dd758e2587507b2052b2e20df0409e" alt="OneSignal in-app messages list showing the Push Permission Prompt template" width="2616" height="1356" data-path="images/push/prompt-for-push-set-up-an-in-app-push-permission-prompt.jpg" />
    </Frame>

    Set the audience to **Show to all users**. OneSignal automatically filters this message to only show to users who haven't subscribed to push, based on the Push Permission Prompt click action.

    <Frame caption="Set the audience to 'Show to all users' because the Push Permission Prompt click action filters to unsubscribed users.">
      <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/prompt-for-push-set-up-an-in-app-push-permission-prompt-show-to-all-users.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=e9b2b23e4e7663ee7799fd4a92dbe473" alt="Audience setting configured to show to all users" width="1766" height="678" data-path="images/push/prompt-for-push-set-up-an-in-app-push-permission-prompt-show-to-all-users.jpg" />
    </Frame>
  </Step>

  <Step title="Customize the message design">
    Personalize the look, feel, and wording to fit your app. Let users know what kind of notifications they'll get and why they're valuable.

    See [Design in-app messages with drag and drop](./design-your-in-app-message) or [Design in-app messages with HTML](./design-your-in-app-message-with-html) for details.

    <Frame caption="The in-app message block editor for creating push opt-in messages.">
      <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/push-customize-the-message-design.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=df030196ba721eedfd4c1ad5af0fa3cd" alt="In-app message block editor with a push opt-in prompt" width="2604" height="1770" data-path="images/push/push-customize-the-message-design.jpg" />
    </Frame>
  </Step>

  <Step title="Add the push permission prompt click action">
    Add a **Push Permission Prompt** click action to any button or image in your message. When tapped, the system prompt appears.

    <Frame caption="Adding a Push Permission Prompt click action to a button.">
      <img src="https://mintcdn.com/onesignal/l4Z9oMlZl9nJOS_T/images/push/push-add-the-push-permission-prompt-click-action.jpg?fit=max&auto=format&n=l4Z9oMlZl9nJOS_T&q=85&s=8ed4971452754851f4ff064121bcb900" alt="Click action dropdown with Push Permission Prompt selected" width="2604" height="1770" data-path="images/push/push-add-the-push-permission-prompt-click-action.jpg" />
    </Frame>

    <Frame caption="The native iOS permission prompt triggered by the click action.">
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e18f7f87a5efaaa5284cf19be8de863c3833379d37b095aef9d015835a694485-prompt-2.webp?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=a484b1c75320beefb83bde20c443f789" alt="iOS native push notification permission prompt" width="1560" height="804" data-path="images/docs/e18f7f87a5efaaa5284cf19be8de863c3833379d37b095aef9d015835a694485-prompt-2.webp" />
    </Frame>

    If a user has already denied permission, the button directs them to your app's notification settings instead.

    <Info>
      In-app messages with a Push Permission Prompt action are not shown to users who have already allowed notifications.
    </Info>
  </Step>

  <Step title="Choose a trigger">
    The audience controls who is eligible to see the message. Triggers control when it appears.

    <Frame caption="Trigger options to control when the message is shown.">
      <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/52f0d8bef7cac18c1d791ec229d2bd86e995a8e01401c7559e2476fcfecddc6d-Screenshot_2024-10-29_at_2.18.33_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=1b55a4815213ddf3f77db8041e143aa2" alt="In-app message trigger configuration panel" width="1792" height="514" data-path="images/docs/52f0d8bef7cac18c1d791ec229d2bd86e995a8e01401c7559e2476fcfecddc6d-Screenshot_2024-10-29_at_2.18.33_PM.png" />
    </Frame>

    You can trigger the message:

    * On app open
    * After a set amount of session time
    * On a specific user event
    * Programmatically, using the [in-app message SDK methods](./mobile-sdk-reference) for full control over timing and context

    For example, to wait until the user has spent at least 5 minutes in the app:

    <Frame caption="Trigger configured to show the message after 5 minutes of session time.">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/81f8cca652667ae5920dbc8b73cca1b297d9e5f35d5ed4dc23d05640a4c838ae-Screenshot_2024-10-29_at_2.25.25_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=311ed96b93b789bb652cc365b5708d7a" alt="Session duration trigger set to 5 minutes" width="1792" height="624" data-path="images/docs/81f8cca652667ae5920dbc8b73cca1b297d9e5f35d5ed4dc23d05640a4c838ae-Screenshot_2024-10-29_at_2.25.25_PM.png" />
    </Frame>
  </Step>

  <Step title="Schedule and frequency">
    Control how often the message appears:

    * **Only once** — Low chance of converting users who weren't ready the first time.
    * **Every time conditions are met** — Too aggressive and may annoy users.
    * **Multiple times (recommended)** — Set a high max (e.g., 9999) with a gap between views (e.g., 2 weeks). This re-prompts unsubscribed users periodically without being intrusive. Adjust the gap based on your use case.

    <Frame caption="Schedule and frequency settings for the in-app message.">
      <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/eb61a38c8908fbeba60833eecc357d720e747c37abacffdfe246dbd7758bbaf4-Screenshot_2024-10-29_at_2.28.20_PM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=7a49b641bdeb959dde6edad5ef7de9dc" alt="Schedule configuration showing max displays and gap between views" width="1792" height="910" data-path="images/docs/eb61a38c8908fbeba60833eecc357d720e747c37abacffdfe246dbd7758bbaf4-Screenshot_2024-10-29_at_2.28.20_PM.png" />
    </Frame>

    <Check>
      Update your message and set it live. Monitor your stats and adjust the gap between displays as needed.
    </Check>
  </Step>
</Steps>

***

## Programmatically show the permission prompt

You can trigger the push permission prompt manually using the `requestPermission()` or `optIn()` [SDK methods](./mobile-sdk-reference). This is useful for custom flows such as:

* A [preference center](./preference-center)
* A user profile screen
* Specific in-app events

***

## Track push permissions and prompt results

When using in-app messages to prompt for push, you can track click actions with the [in-app message click listener](./mobile-sdk-reference#addclicklistener-in-app).

If the in-app message displays but the user doesn't tap the button, use the [in-app message lifecycle events](./mobile-sdk-reference#addlifecyclelistener) to track impressions and dismissals.

To track the result of the system-level permission prompt itself, use the [push permission listener](./mobile-sdk-reference#addpermissionobserver-push).

<Info>
  You can send these SDK events to your backend or analytics tool of choice.
</Info>

***

## FAQ

### What happens if a user denies the push permission prompt?

On iOS, denying the system prompt permanently disables push notifications for your app — the prompt cannot be shown again. On Android, the user gets one more chance (two total). After all attempts are used, the user must re-enable notifications manually in **Settings > Notifications** on their device. The OneSignal SDK's `requestPermission(fallbackToSettings: true)` method can redirect users to their notification settings if permission was previously denied.

### Can I customize the native system permission prompt?

No. The native iOS and Android permission dialogs are controlled by the operating system and cannot be customized. You can only control the soft prompt (the in-app message shown before the system prompt). Use the soft prompt to explain the value of your notifications, set expectations, and increase the chance of an "Allow" on the system prompt.

### Can I still prompt users who have provisional notifications?

Yes. If you use [iOS provisional push notifications](./ios-provisional-push-notifications), you can still show a soft prompt to convert those users to full push subscribers. Time the prompt strategically — after the user has seen value from your provisional notifications.

### How do I re-prompt users who previously denied push?

You cannot show the system permission prompt again once the user has declined on iOS (or twice on Android). Instead, use the `requestPermission(fallbackToSettings: true)` SDK method, which opens the app's notification settings page so the user can enable notifications manually. Pair this with an in-app message explaining why notifications are valuable.

### When did Android start requiring permission prompts?

Android 13 (API level 33) introduced the runtime notification permission, requiring explicit user consent for push notifications.

* **Released:** August 2022 (Pixel devices)
* **Required for target SDK:** As of August 31, 2023, all new apps and updates on Google Play must target API level 33 or higher.
* **Source:** [Google's developer guide on notification permissions](https://developer.android.com/develop/ui/views/notifications/notification-permission)

***

<Card title="iOS provisional push notifications" icon="apple" href="./ios-provisional-push-notifications">
  Send notifications to the Notification Center without an upfront permission prompt on iOS 12+.
</Card>

Built with [Mintlify](https://mintlify.com).

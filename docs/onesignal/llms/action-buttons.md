# Source: https://documentation.onesignal.com/docs/en/action-buttons.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Action buttons for push notifications

> Add interactive action buttons to your push notifications on iOS, Android, and the web. Learn setup via Dashboard & API, supported platforms, click handling, icons, and event tracking.

<Frame caption="Image showing action buttons in iOS">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c40c0d1-ios15-action-icons--1.jpeg?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=51965abdd020931ca08de3f44dd96370" width="1000" height="580" data-path="images/docs/c40c0d1-ios15-action-icons--1.jpeg" />
</Frame>

<Info>
  This guide applies only to push notifications. For in-app messages, see [In-App Messages: How to add Click Actions](./iam-click-actions).
</Info>

Action Buttons let you add multiple, labeled actions to a single push notification, so users can respond without opening your app or site first. Depending on the operating system and device, users reveal buttons by expanding the notification (long press, swipe + View, or an expand affordance).

***

## Add action buttons

You can configure Action Buttons in [Templates](./templates), directly when composing a message in the dashboard, or via the [API](/reference/push-notification).

### Dashboard & template setup

When creating a push, open **Advanced Options > Action Buttons**.

<Frame caption="Image showing action buttons to be added for iOS and Android">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/64712e6-Screenshot_2023-06-02_at_1.53.48_PM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=b2bb426793efd74cf713471e75894fc3" width="1614" height="1588" data-path="images/docs/64712e6-Screenshot_2023-06-02_at_1.53.48_PM.png" />
</Frame>

### API setup

* **Mobile Apps**: Use the `buttons` parameter. Pass an array of up to 3 objects with `id`, `text`, and `icon`.
* **Web (Chrome)**: Use `web_buttons`, passing up to 2 objects with `id`, `text`, `icon`, and `url`.

***

## Action button properties

* **Action ID**: A unique identifier for the specific button action. The ID of the clicked button is passed to you so you can identify which button was clicked. (e.g. 'accept-button')

  * Must be unique per button.
  * Available in the OSNotification Payload and can be accessed within the SDK Notification Opened Event Handler.
  * API: `id` property

* **Label**: The text the button should display to your users. (e.g. 'Accept')

  * API: `text` property

* **Icon**: Optional icon displayed with the button label. Not available on all platforms and operating systems. See FAQ below for details.

  * Mobile apps must include the button within its image resources. See Action Button Icons below for details.
  * Websites can use a valid publicly reachable URL to an icon. Keep this small because it's downloaded on every notification display. (e.g. `http://site.com/icon.png`)
  * API: `icon` property

* **Launch URL 1**: The URL to open when the action button of the first button is clicked. Pass `'do_not_open'` to prevent opening any URL. (e.g. 'do\_not\_open')

  * Web only
  * Max 2 web buttons
  * API: `web_buttons.url` property

### Action button icons

* iOS supports action button icons for iOS 15+
* Android stopped supporting action button icons for [Android N (AKA 7)](https://android-developers.googleblog.com/2016/06/notifications-in-android-n.html)

***

## Handle action button clicks

When a user taps a button, OneSignal delivers the Action ID to your app/site. You can either use the default behavior (open your app/site) or override it.

### Default behavior (Open App/Site, Then Handle)

1. The app/site opens (or is focused on web).
2. Your click/open listener receives the event with the Action ID. (See [mobile SDK reference](./mobile-sdk-reference#addclicklistener-push) or [web SDK reference](./web-sdk-reference#addeventlistener-notifications) for click listener details.)
3. Use the Action ID to track which button was clicked and handle the click event accordingly. This could mean deep linking to a specific screen in your app or triggering a custom event.

#### Prevent app launch from action button clicks

* **Android:** Follow [Android SDK setup > Disable default open behavior](./android-sdk-setup#disable-default-open-behavior). This lets you intercept clicks in a [Service Extensions](./service-extensions) and run custom logic (e.g. call an API) without opening the app.
* **iOS:** Include an `ios_category` on the notification to associate actions via the [UNNotificationCategory Object](https://developer.apple.com/documentation/usernotifications/unnotificationcategory). See Apple's [Declaring Your Actionable Notification Types](https://developer.apple.com/documentation/usernotifications/declaring_your_actionable_notification_types) for more details.
* **Web (Chrome):** Use the `_osp=do_not_open` magic string to prevent opening any URL. This is supported on Chrome and Firefox, but not supported for the Safari web browser.

***

## Supported platforms & limits

| Platform                  | Buttons Supported | Notes                                                          |
| ------------------------- | ----------------- | -------------------------------------------------------------- |
| iOS                       | Up to 4           | Icons on iOS 15+. Requires categories for background handling. |
| Android / Amazon / Huawei | Up to 3           | No button icons from Android 7+.                               |
| Web – Chrome              | Up to 2           | Buttons and icons supported. `_osp=do_not_open` supported.     |
| Web – Firefox             | No buttons        | `_osp=do_not_open` works for the launch URL only.              |
| Web – Safari              | No buttons        | `_osp=do_not_open` not supported. Provide a real URL.          |

<Note>Users often need to **expand** the notification to see buttons (e.g., long press on iOS, swipe + **View** on some Android OEMs).</Note>

***

## Troubleshooting

### Buttons don’t show up

* Expand the notification (long press, swipe + View, or expand).
* Verify you added Action ID and Label for each button.
* Check platform limits (e.g., only 2 buttons on Chrome).

### Clicking a button doesn’t open the browser on mobile web

If the browser is in the background or fully closed, most mobile browsers (including Chrome) will not come to the foreground or open the URL, even though click events still trigger in the service worker. This is intentional browser behavior to prevent background apps from interrupting the user.

* Most mobile browsers won’t foreground themselves from a background service worker. Clicks still fire in the worker, but the tab doesn’t open. This is intentional.
* Ensure the launch URL and the button URL are exactly identical (including trailing slashes) if you expect the tab to be focused instead of opening a new one.

### Icons don’t appear

* iOS must be 15+ for button icons.
* Android 7+ does not render action button icons.
* On web, confirm the icon URL is publicly accessible and small (fast to download).

### Why is there a close action button?

By default web push notifications on Windows 10 include the Close button. However, if you add your own action button, then this close button is removed. So, in either case the notification will remain on-screen till the user interacts with it. This is designed by Google to give the users the chance to interact with the notification.

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).

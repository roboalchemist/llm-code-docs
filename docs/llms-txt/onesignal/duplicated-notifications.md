# Source: https://documentation.onesignal.com/docs/en/duplicated-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Duplicated Notifications

> Learn how to troubleshoot and fix issues with receiving duplicate push or in-app notifications in your app, including causes related to SDK versions, server-side logic, and multi-app environments.

This guide helps you troubleshoot issues related to receiving **duplicate push notifications**. If you're seeing **duplicate in-app messages**, refer to our [Duplicated In-App Messages](./in-app-message-troubleshooting#duplicated-in-app-messages) guide.

<Info>
  • Apple acknowledged a bug in iOS 17 that caused duplicates. This was fixed in iOS 17.3. [Read more](https://forums.developer.apple.com/forums/thread/747044).
  • If you're using OneSignal Android SDK versions **4.4.1 – 4.6.2**, update to the latest version to avoid known issues.
</Info>

## Same message sent multiple times

The most common cause of duplicate notifications is **sending the same notification payload more than once** through the OneSignal API.

### Common reasons

* Your server retries requests without checking if the first succeeded.
* Accidental logic duplication in your backend notification pipeline.
* You're migrating to OneSignal but **still sending notifications from a previous provider**. Avoid sending from both systems simultaneously.

## Multiple push notification SDKs

Check if your app includes **another push notification SDK** (e.g., Firebase, Urban Airship). These may **also process and display** OneSignal notifications.

* OneSignal includes logic to avoid duplication when it is the only SDK.
* Other SDKs may not recognize and filter out OneSignal's payloads, leading to multiple displays.

See FAQ below for more on SDK interoperability.

## Multiple app instances

<Tabs>
  <Tab title="Android">
    ### Android

    Duplicate notifications may occur when:

    * You have both **production** and **development** versions of your app installed.
    * Each app has a unique package name and receives its own push token.

    Long press on a notification to confirm which app instance it came from.
  </Tab>

  <Tab title="IOS">
    ### iOS

    If two device records in OneSignal share the **same push token**, the device may receive **two notifications**.

    * This can happen when importing or registering the same token multiple times.
    * OneSignal includes checks to prevent this, but edge cases may bypass them.
  </Tab>

  <Tab title="Web Push">
    ### Web Push

    Web push duplicates are caused by **subscribing to multiple origins** using the same OneSignal App ID.

    > [What is an origin?](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

    Examples:

    * A user subscribes to `https://example.com` and `https://sub.example.com`—each counts as a different origin.
    * If you send a push using the same App ID, the user will receive a notification for **each subscribed origin**.

    #### How to fix:

    1. [Reset browser data and push permissions](./troubleshooting-web-push#section-clearing-your-cache-and-resetting-push-permissions) per origin.
    2. If this is affecting many users, **create a new OneSignal App** and use a new App ID in your site’s init code.
    3. Have users revisit the site and resubscribe.

    Additional cause:

    * Subscribing on **multiple browsers or browser profiles** will also lead to multiple notifications.
  </Tab>
</Tabs>

## Diagnostic tips

<Info>
  To help us debug duplicate issues faster, collect and send:

* OneSignal SDK version
* Device OS version
* Build environment (Mac/Windows)
* Xcode logs or logcat outputs
* List of other libraries/plugins in your app
* Detailed reproduction steps
</Info>

***

## FAQ

<AccordionGroup>
  <Accordion title="What happens if I have 2 different notification SDKs in my app?">
    * **Android**: OneSignal will only handle notifications containing a `"custom"` key with an `"i"` field. If your previous SDK does not check for this key, it may also handle and show the same notification.
    * **iOS**: All notifications appear in the system tray. If both SDKs send the same message, the user will see it twice.
      **Recommendation**: For iOS click handling, check for the `"custom"` payload before processing or use your own payload keys to avoid duplicate handling.
  </Accordion>

  <Accordion title="How to send push from a previous provider and OneSignal?">
    * **Android**: Remove old SDK notification handling code when integrating OneSignal and releasing the app. As users update, they'll stop receiving push from the old provider.
    * **iOS**: You can continue sending from the old provider temporarily while users update. Once fully transitioned, send from OneSignal only to avoid duplicates.
  </Accordion>
</AccordionGroup>

***

Built with [Mintlify](https://mintlify.com).

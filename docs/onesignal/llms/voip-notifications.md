# Source: https://documentation.onesignal.com/docs/en/voip-notifications.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# VoIP push notifications

> Send VoIP push notifications with OneSignal on iOS and understand Android alternatives. Learn required setup, Apple limitations, and how to manually register and send VoIP pushes using the OneSignal API.

## Overview

VoIP push notifications are handled differently by Apple than standard push notifications. Because of these platform constraints, OneSignal supports sending VoIP notifications—but does not manage VoIP token registration for you.

You must:

* Register VoIP tokens yourself using Apple PushKit
* Upload a VoIP-specific APNs certificate
* Use OneSignal’s API to register tokens and send notifications

<Warning> OneSignal **does not automatically register or refresh VoIP (PushKit) tokens**. You must manually register VoIP tokens with OneSignal using the API. </Warning>

### Platform differences at a glance

| Platform    | VoIP push supported? | How it works                                          |
| ----------- | -------------------- | ----------------------------------------------------- |
| **iOS**     | ✅ Yes                | Uses Apple PushKit and a VoIP APNs certificate        |
| **Android** | ❌ No                 | Uses data-only pushes to simulate call-style behavior |

## If you are building a cross-platform calling app, you will use different approaches per platform

## Android: simulate VoIP-style behavior (not true VoIP)

Android does not support VoIP push notifications. There is no equivalent to Apple PushKit.

Instead, Android calling apps simulate VoIP behavior using:

* Data-only push notifications
* Foreground services
* Custom call-style UI

You can use OneSignal’s normal Android push support combined with native Android APIs to achieve this.

**Recommended approach:**

* Send data-only notifications
* Handle them in your app to:
  * Start a foreground service
  * Launch a call UI activity
  * Display a custom incoming call notification

**If you want to intercept and fully control notification rendering, use Android’s [Notification Service Extension](./service-extensions#notification-service-extension).**

**Helpful resources:**

* [Android calling app guide](https://developer.android.com/guide/topics/connectivity/telecom/selfManaged)
* [Incoming call UI example](https://medium.com/@dcostalloyd90/show-incoming-voip-call-notification-and-open-activity-for-android-os-10-5aada2d4c1e4)

<Info> Android setup is **not specific to OneSignal**. OneSignal only delivers the push payload; your app handles call behavior. </Info>

***

## iOS: send true VoIP push notifications

On iOS, VoIP notifications use Apple PushKit and have special delivery rules that differ from standard push notifications.

**How iOS VoIP works with OneSignal:**

For iOS VoIP notifications:

1. Your app registers a VoIP token using PushKit
2. You upload a VoIP Services APNs certificate to OneSignal
3. You register the VoIP token with OneSignal using the API
4. You send VoIP pushes using apns\_push\_type\_override: "voip"

Because Apple treats VoIP pushes differently, OneSignal must also treat them as a separate app configuration.

### 1. Register a VoIP token using PushKit

Use Apple’s PushKit framework to register for VoIP notifications and receive a VoIP token.

* Implement PushKit in your app
* Store and refresh the VoIP token as Apple rotates it
* Follow Apple’s VoIP policies closely

Apple resources:

* [PushKit documentation](https://developer.apple.com/documentation/pushkit)
* [Responding to VoIP pushes](https://developer.apple.com/documentation/pushkit/responding_to_voip_notifications_from_pushkit)
* [Apple’s VoIP Best Practices](https://developer.apple.com/library/content/documentation/Performance/Conceptual/EnergyGuide-iOS/OptimizeVoIP.html)

### 2. Create a new OneSignal app for VoIP users

You must maintain **two separate OneSignal apps**:

* **Main Push App**: For standard push notifications
* **VoIP App**: For VoIP-only notifications

Both apps must:

* Use the same iOS bundle ID
* Be associated with the same native iOS app

### 3. Upload a VoIP Services Certificate

In your VoIP OneSignal app:

* Upload a VoIP Services Certificate (.p12)
* Do not reuse your standard APNs certificate

<Warning>
  You must upload a **VoIP Services Certificate (.p12)** for the VoIP app, using the same bundle ID as your main app.
</Warning>

<Frame caption="VoIP certificate in Keychain Access">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/6101554-Screen_Shot_2020-04-26_at_1.07.52_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=5d19f1262fdf67d5185ed8d8b4743493" width="1868" height="1624" data-path="images/docs/6101554-Screen_Shot_2020-04-26_at_1.07.52_PM.png" />
</Frame>

<Frame caption="VoIP certificate uploaded in OneSignal dashboard">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/81a2fea-a2a2e71-Screenshot_2024-02-23_at_1.32.08_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=6ee92a10fc3473c644880fa7517eb46b" width="466" height="130" data-path="images/docs/81a2fea-a2a2e71-Screenshot_2024-02-23_at_1.32.08_PM.png" />
</Frame>

### 4. Register the VoIP token with OneSignal

Use the [Create User](/reference/create-user) API to register the VoIP token with your VoIP OneSignal app.

<Warning>
  If the VoIP token comes from a **development or sandbox build**, you must include `"test_type": 1` property.

  If you omit this:

* The API call may succeed
* The push will silently fail
</Warning>

```curl  theme={null}
curl --request POST \
     --url https://api.onesignal.com/apps/YOUR_VOIP_APP_ID/users \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "subscriptions": [
    {
      "type": "iOSPush",
      "token": "your-voip-token",
      "test_type": 1 // omit in production
    }
  ]
}
'
```

To update the token later, use the [Update Subscription](/reference/update-subscription) API.

### 5. Send VoIP notifications

Use the [Create Notification](/reference/create-message) API and include the following parameters:

* `"apns_push_type_override": "voip"`
* The `app_id` of your VoIP app
* The `subscription_id` of the VoIP token you registered
* You can use `contents` or `content_available` one is required

```curl  theme={null}
curl --include \
     --request POST \
     --header "Content-Type: application/json; charset=utf-8" \
     --header "Authorization: key YOUR_REST_API_KEY" \
     --data-binary '{
  "app_id": "YOUR_VOIP_APP_ID",
  "content_available": true,
  "data": {
    "your_custom_data": "your_custom_value"
  },
  "apns_push_type_override": "voip",
  "include_subscription_ids": ["YOUR_VOIP_SUBSCRIPTION_ID"]
}' \
https://api.onesignal.com/notifications
```

### 6. Verify your VoIP setup

Your iOS VoIP integration is working if:

1. The VoIP token appears as an iOS push subscription in your **VoIP app**
2. A VoIP push triggers `pushRegistry(_:didReceiveIncomingPushWith:for:completion:)`
3. The app wakes even when terminated or backgrounded

***

## FAQ

### Do confirmed deliveries work with VoIP?

No, [Confirmed Deliveries](./confirmed-delivery) are **not tracked** for VoIP pushes. They rely on the Notification Service Extension, which does **not** trigger for VoIP notifications.

Instead, track receipt via the native iOS PushKit event:

```swift  theme={null}
pushRegistry(_:didReceiveIncomingPushWith:for:completion:)
```

This event is part of your main app target and doesn't require a separate extension. Learn more in [Apple’s VoIP documentation](https://developer.apple.com/documentation/pushkit/responding_to_voip_notifications_from_pushkit#3377587).

***

Built with [Mintlify](https://mintlify.com).

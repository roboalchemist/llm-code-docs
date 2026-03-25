# Source: https://documentation.onesignal.com/docs/en/app-clip-support.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS: App Clip Support

> Learn how to enable and configure OneSignal push notifications in iOS App Clips. Covers setup steps, limitations, and support for advanced experiences like Target-Content-ID.

## OneSignal support for App Clips

OneSignal supports sending push notifications to iOS App Clips. Since App Clips have a separate bundle identifier, they require their own push configuration. Follow the steps below to properly configure your App Clip with OneSignal and understand current limitations.

***

## Setup

### 1. Create a new app for your App Clip

You must create a separate app in the OneSignal Dashboard for your App Clip. This is because:

* App Clips use a different bundle identifier from the main app.
* Apple requires a distinct APNs certificate or Key for each unique bundle ID.

<Info>
  Make sure your App Clip bundle ID has its own APNs authentication configured
  in Apple Developer Console and linked in OneSignal.
</Info>

### 2. Set up OneSignal in your App Clip

Follow the standard OneSignal [iOS SDK setup guide](./ios-sdk-setup), but skip the Notification Service Extension step:

* ✅ Do: Add the OneSignal SDK to your App Clip target.
* ❌ Skip: Notification Service Extension — App Clips do not support this capability.

### 3. Enable ephemeral push permission

Add the following to your App Clip’s `Info.plist` to automatically enable 8-hour push notification permissions when the App Clip is opened:

```xml  theme={null}
<key>NSAppClip</key>
<dict>
  <key>NSAppClipRequestEphemeralUserNotification</key>
  <true/>
</dict>
```

<Frame caption="Ephemeral push notification Info.plist setting">
  {" "}

  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1d22192-Screen_Shot_2020-07-23_at_3.05.41_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=a6886e9a289c656e0179ad3802712cbe" width="553" height="40" data-path="images/docs/1d22192-Screen_Shot_2020-07-23_at_3.05.41_PM.png" />

  {" "}
</Frame>

This ephemeral permission expires after 8 hours unless the user disables it earlier.

You can also request indefinite push permission upon launch, similar to full apps.

Refer to [Apple’s documentation](https://developer.apple.com/documentation/appclip/enabling-notifications-in-app-clips) for full guidance.

### 4. Support advanced App Clip experiences

To target specific App Clip experiences with notifications:

1. In the OneSignal Dashboard, open **Settings > iOS platform configuration**.
2. Add a value to the **Target-Content-ID** field. This should be the experience URL you configured in App Store Connect.

<Frame caption="Targeting a specific App Clip experience via Target-Content-ID">
  {" "}

  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/target_content_id.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=0f54fa170c22021768221202f142567d" width="801" height="732" data-path="images/docs/target_content_id.png" />

  {" "}
</Frame>

Learn more in Apple’s guide to [Creating an App Clip](https://developer.apple.com/documentation/app_clips/creating_an_app_clip), which covers Associated Domains and Target-Content-ID usage.

***

## App Clip limitations

Due to iOS platform restrictions, the following limitations apply to App Clips:

* Ephemeral permission duration: Only lasts 8 hours. To send notifications beyond this, request full push permission.
* No Notification Service Extension support:
  * ❌ No rich media (images, videos, etc.)
  * ❌ No custom action buttons (only predefined categories allowed)
* Location access is limited:
  * App Clips cannot request Always location access.
  * They can request When In Use, which expires at 4:00 a.m. the next day.

***

Built with [Mintlify](https://mintlify.com).

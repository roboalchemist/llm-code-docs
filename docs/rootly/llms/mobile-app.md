# Source: https://docs.rootly.com/on-call/mobile-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile App

> Download and use the Rootly mobile app for iOS and Android to receive, acknowledge, and escalate alerts while on-call.

<Frame><img src="https://mintcdn.com/rootly/n-fKYpx5M7fU1qc2/images/mobile/mobile-app.webp?fit=max&auto=format&n=n-fKYpx5M7fU1qc2&q=85&s=659bfb6359ec65ad5389185fb070520c" alt="" width="925" height="749" data-path="images/mobile/mobile-app.webp" /></Frame>

<Note>
  Required User Seats and User Permissions

  Users will need an on-call seat to log in and access the app.
</Note>

The Rootly mobile app lets you receive and acknowledge alerts, escalate alerts to incidents, and see all the information you need while you are on-call.

## Download the mobile app

Rootly's mobile app supports both iOS and Android devices.

<CardGroup cols={2}>
  <Card title="Download on iOS" icon="apple" href="https://apps.apple.com/us/app/rootly/id6478240412" horizontal>
    Download from the App Store
  </Card>

  <Card title="Download on Android" icon="android" href="https://play.google.com/store/apps/details?id=com.rootly.app&hl=en_US" horizontal>
    Download from Google Play
  </Card>
</CardGroup>

After downloading:

1. Open the Rootly app on your device
2. Enter your Rootly credentials to log in

## Log in to Rootly

Log in to your Rootly account using any of the following methods:

* Email address and password
* Google SSO
* Slack SSO
* Third-party identity provider (SAML SSO)

Compatibility

For security purposes minimum software versions supported are:

* Android 11+ (SDK 30+)
* iOS 16+

## Push Notification

### IOS

* IOS used critical alert for high urgency alerts.

<Warning>
  Apple Watch Compatibility

  If you have an Apple Watch connected to your iPhone, critical alerts may not play sound on your iPhone. To fix this:

  1. Open the Watch app on your iPhone
  2. Go to Notifications
  3. Scroll down to "Mirror iPhone Alerts from"
  4. Unselect Rootly

  This allows the full Rootly sound to play on your iPhone while on-call.
</Warning>

### Android

#### Battery-Saving Mode

Users may experience delayed notifications when using battery-saving mode. To resolve this for Rootly, navigate to Settings > Battery > Battery usage > Rootly, and choose Unrestricted.

On some devices, this setting might appear as Don't wake for notifications. Disabling this option can help ensure notifications are received promptly.

#### Samsung

Battery Optimization and App Restrictions: Samsung devices are known to aggressively manage background processes to optimize battery life. When an app is in the background or killed, Samsung’s battery optimization settings can block notifications entirely, or modify their behavior (such as muting sound or vibration). You can check if battery optimization is affecting your app:

`Go to Settings > Apps > Your App > Battery > Optimize Battery Usage and turn off optimization for your app.`

Device-Specific Notification Handling: Some Samsung devices (especially recent ones with One UI) impose additional restrictions on background notifications. You might need to guide users to allow the app to run in the background or turn off restrictions. For this:

`Go to Settings > Device Care > Battery > App power management and disable "Put unused apps to sleep" for your app.`

<Warning>
  Android Work Profiles

  Due to a Work Profile limitation from Android, overriding System Volume and Do Not Disturb will not work when the Rootly app is under a Work Profile.

  For better behavior, it is recommended to also add **Google Chrome** to your Work Profile alongside the Rootly app. This ensures optimal functionality and performance.
</Warning>

## China Support

Rootly is available in china in the following stores.

| Store  |   Status  | Version |                             Link                             |
| :----- | :-------: | :-----: | :----------------------------------------------------------: |
| HONOR  | Published |  2.7.0  |                              N/A                             |
| OPPO   | Published |  2.7.0  |                              N/A                             |
| VIVO   | Published |  2.7.0  |                              N/A                             |
| XIAOMI | Published |  2.7.0  | [Open Link](https://app.mi.com/details?id=cn.net.rootly.app) |

Alternatively you can download the chinese version [here](https://rootly-heroku.s3.us-east-1.amazonaws.com/android/app-cnProduction-release-2.7.0.apk)

## Rootly vCard

Incoming pages from Rootly can come from various numbers depending on the country you're located in. To ensure that each page appears as Rootly calling, you can download the Rootly vCard through this link: [https://rootly.com/rootly-outgoing-numbers.vcf](https://rootly.com/rootly-outgoing-numbers.vcf).


Built with [Mintlify](https://mintlify.com).
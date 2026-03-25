# Source: https://documentation.onesignal.com/docs/en/amazon-sdk-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon SDK setup

> Step-by-step guide to integrate the OneSignal SDK into your Amazon Fire OS app for push notifications and in-app messaging capabilities.

## Overview

This guide explains how to integrate OneSignal push notifications into an Amazon Fire OS app. It covers everything from installation to configuration and service worker management.

***

## Requirements

* Your app must be distributed on the Amazon AppStore
* Android 7.0+ device or emulator
* Configured OneSignal app and platform

### Configure your OneSignal app and platform

Configure your OneSignal app with the platforms you support — Apple (APNs), Google (FCM), Huawei (HMS), and/or Amazon (ADM).

<Note>
  If your organization already has a OneSignal account, [ask to be invited](/docs/en/manage-team-members) to the Organization. Otherwise, [sign up for a free account](https://onesignal.com) to get started.
</Note>

<Accordion title="Step-by-step setup instructions" icon="circle-chevron-down">
  <Steps>
    <Step title="Create or select your app">
      Create a new app by clicking **New App/Website**, or add a platform to an existing app in **Settings > Push & In-App**. Select the platform(s) you want to configure and click **Next: Configure Your Platform**.

      <Frame caption="Setting up your first OneSignal app, Organization, and channel.">
        <img src="https://mintcdn.com/onesignal/BK2J-grzBpDdh8NC/images/dashboard/new-app-org-channel.png?fit=max&auto=format&n=BK2J-grzBpDdh8NC&q=85&s=ee0045484152ed15095f619344aa0564" alt="OneSignal dashboard showing the new app setup flow with Organization name, app name, and channel selection" width="2592" height="1904" data-path="images/dashboard/new-app-org-channel.png" />
      </Frame>
    </Step>

    <Step title="Configure platform credentials">
      Enter the credentials for your platform:

      * **Android**: [Set up Firebase credentials](/docs/en/android-firebase-credentials)
      * **iOS**: [p8 token (recommended)](/docs/en/ios-p8-token-based-connection-to-apns) or [p12 certificate](/docs/en/ios-p12-generate-certificates)
      * **Amazon**: [Generate API key](/docs/en/generate-an-amazon-api-key)
      * **Huawei**: [Authorize OneSignal](/docs/en/authorize-onesignal-to-send-huawei-push)

      Click **Save & Continue** after entering your credentials.
    </Step>

    <Step title="Save your App ID and install the SDK">
      Your **App ID** is displayed on the final screen. Copy and save it — you need it when initializing the SDK. Select your SDK platform, then follow the setup guide.

      <Frame caption="Save your App ID and invite additional team members.">
        <img src="https://mintcdn.com/onesignal/VypVshrFHTBZfEma/images/dashboard/app-id-and-team-invite.png?fit=max&auto=format&n=VypVshrFHTBZfEma&q=85&s=e1e2aab6cca7c4aa6b9a76eff362d5af" alt="OneSignal dashboard showing the App ID and team invite option after setup" width="2592" height="1904" data-path="images/dashboard/app-id-and-team-invite.png" />
      </Frame>
    </Step>
  </Steps>
</Accordion>

***

## Setup

### Update `AndroidManifest.xml`

Open your `AndroidManifest.xml` file and add `xmlns:amazon="http://schemas.amazon.com/apk/res/android"` in the manifest tag right after the `xmlns:android` property.

```xml xml theme={null}
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="com.onesignal.example"
    android:versionCode="1"
    android:versionName="1.0" >
```

Add the following permissions, replacing `COM.YOUR.PACKAGE_NAME` with your actual package name:

```xml xml theme={null}
<uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />
<permission
  android:name="COM.YOUR.PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
  android:protectionLevel="signature"
/>
<uses-permission android:name="COM.YOUR.PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
```

Configure ADM services and receivers in the `<application>` tag, replacing `COM.YOUR.PACKAGE_NAME` with your actual package name:

```xml xml theme={null}
<application ....>
  <amazon:enable-feature android:name="com.amazon.device.messaging"
                         android:required="false"/>
  <service android:name="com.onesignal.notifications.services.ADMMessageHandler"
           android:exported="false" />
  <service android:name="com.onesignal.notifications.services.ADMMessageHandlerJob"
           android:permission="android.permission.BIND_JOB_SERVICE"
           android:exported="false" />
  <receiver android:name="com.onesignal.notifications.receivers.ADMMessageReceiver"
           android:permission="com.amazon.device.messaging.permission.SEND"
            android:exported="true" >
    <intent-filter>
      <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
      <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
      <category android:name="COM.YOUR.PACKAGE_NAME" />
    </intent-filter>
  </receiver>

</application>
```

### Amazon API key file

Place your `api_key.txt` inside an `assets` folder in the root of your Android project.

<Frame caption="Amazon API Key">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/77ac1b6-AmazonAndroidStudio_api_key.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=eb15b9b097ed28f2b89fcdf3295c9115" width="506" height="292" data-path="images/docs/77ac1b6-AmazonAndroidStudio_api_key.png" />
</Frame>

To create an `api_key.txt` for your app, follow our [Generate an Amazon API Key](./generate-an-amazon-api-key) guide.

Make sure to use the same keystore when building your APK as you did in step 2.4 in the Amazon Configuration guide.

Ensure that you are not building a `debug` app when testing Amazon push notifications. It must be a `release` type.

Submit the signed APK to [Live App Testing](https://developer.amazon.com/docs/app-testing/live-app-testing-getting-started.html). Submitting a signed APK is a necessary requirement for ADM to work.

<Frame caption="Build Variant">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a8d01f9-AndroidStudioBuildVariant.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=00e265069869aad54ac796aa405af681" width="387" height="75" data-path="images/docs/a8d01f9-AndroidStudioBuildVariant.png" />
</Frame>

***

## Testing the OneSignal SDK integration

This guide helps you verify that your OneSignal SDK integration is working correctly by testing push notifications, subscription registration, and in-app messaging.

<Warning>
  If you are testing with an Android emulator, it should start with a cold boot.

  1. Go to **Device Manager** in Android Studio.
  2. Select your emulator device and click **Edit**.
  3. Go to **Additional Settings** or **More**.
  4. Set the **Boot option** to **Cold Boot**.
  5. Save changes and restart the emulator.
</Warning>

### Check mobile subscriptions

<Steps>
  <Step title="Launch your app on a test device.">
    The native push permission prompt should appear automatically if you added the `requestPermission` method during initialization.

    <Frame caption="iOS and Android push permission prompts">
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a90c2cc443f5fe9e7c80368c680a16cf1ca6203f7b28a0a6eec212add8510f80-Untitled_design_11.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=96dbf224b3ae93b3d814712cdc5416ba" width="1920" height="1080" data-path="images/docs/a90c2cc443f5fe9e7c80368c680a16cf1ca6203f7b28a0a6eec212add8510f80-Untitled_design_11.png" />
    </Frame>
  </Step>

  <Step title="Check your OneSignal dashboard">
    Before accepting the prompt, check the OneSignal dashboard:

    * Go to **Audience > Subscriptions**.
    * You should see a new entry with the status "Never Subscribed".

    <Frame caption="Dashboard showing subscription with 'Never Subscribed' status">
      <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f19fa5ada3572ce14447bb5639744e9da75cd7a3ab43ecc1a057f2ed92b38e6f-Screenshot_2025-03-16_at_14.55.39.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=b04ca3217e22155841b500a55c7f1511" width="1588" height="976" data-path="images/docs/f19fa5ada3572ce14447bb5639744e9da75cd7a3ab43ecc1a057f2ed92b38e6f-Screenshot_2025-03-16_at_14.55.39.png" />
    </Frame>
  </Step>

  <Step title="Return to the app and tap Allow on the prompt." />

  <Step title="Refresh the OneSignal dashboard Subscription's page.">
    The subscription's status should now show **Subscribed**.

    <Frame caption="Dashboard showing subscription with 'Subscribed' status">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/85b0376cdcc6f93fb7b3895b18cd1788d2342776d7995909881e5c64dd40fb62-Screenshot_2025-03-16_at_15.57.34.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=c6abec64d102b84e30f6c9c0327808ef" width="1588" height="976" data-path="images/docs/85b0376cdcc6f93fb7b3895b18cd1788d2342776d7995909881e5c64dd40fb62-Screenshot_2025-03-16_at_15.57.34.png" />
    </Frame>

    <Check>You have successfully created a [mobile subscription](/docs/en/subscriptions).
    Mobile subscriptions are created when users first open your app on a device or if they uninstall and reinstall your app on the same device.</Check>
  </Step>
</Steps>

### Set up test subscriptions

Test subscriptions are helpful for testing a push notification before sending a message.

<Steps>
  <Step title="Add to Test Subscriptions.">
    In the dashboard, next to the subscription, click the **Options (three dots)** button and select **Add to Test Subscriptions**.

    <Frame caption="Adding a device to Test Subscriptions">
      <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/add-to-test-subscriptions.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=2455d4cd74ea4ad686f76730cd95bbaa" width="1188" height="742" data-path="images/dashboard/add-to-test-subscriptions.png" />
    </Frame>
  </Step>

  <Step title="Name your subscription.">
    Name the subscription so you can easily identify your device later in the **Test Subscriptions tab**.
  </Step>

  <Step title="Create a test users segment.">
    Go to **Audience > Segments > New Segment**.
  </Step>

  <Step title="Name the segment.">
    Name the segment `Test Users` (the name is important because it will be used later).
  </Step>

  <Step title="Add the Test Users filter and click Create Segment.">
    <Frame caption="Creating a 'Test Users' segment with the Test Users filter">
      <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/create-test-users-segment.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=91b8a021be6e83662854e68ec3e1da04" width="1188" height="742" data-path="images/dashboard/create-test-users-segment.png" />
    </Frame>

    <Check>You have successfully created a segment of test users.
    We can now test sending messages to this individual device and groups of test users.</Check>
  </Step>
</Steps>

### Send test push via API

<Steps>
  <Step title="Get your App API Key and App ID.">
    In your OneSignal dashboard, go to **Settings > [Keys & IDs](/docs/en/keys-and-ids)**.
  </Step>

  <Step title="Update the provided code.">
    Replace `YOUR_APP_API_KEY` and `YOUR_APP_ID` in the code below with your actual keys. This code uses the `Test Users` segment we created earlier.

    ```curl  theme={null}
    curl -X \
    POST --url 'https://api.onesignal.com/notifications' \
     --header 'content-type: application/json; charset=utf-8' \
     --header 'authorization: Key YOUR_APP_API_KEY' \
     --data \
     '{
      "app_id": "YOUR_APP_ID",
      "target_channel": "push",
      "name": "Testing basic setup",
      "headings": {
       "en": "👋"
      },
      "contents": {
        "en": "Hello world!"
      },
      "included_segments": [
        "Test Users"
      ],
      "ios_attachments": {
        "onesignal_logo": "https://avatars.githubusercontent.com/u/11823027?s=200&v=4"
      },
      "big_picture": "https://avatars.githubusercontent.com/u/11823027?s=200&v=4"
    }'
    ```
  </Step>

  <Step title="Run the code.">
    Run the code in your terminal.
  </Step>

  <Step title="Check images and confirmed delivery.">
    If all setup steps were completed successfully, the test subscriptions should receive a notification with an image included:

    <Frame caption="Push notification with image on iOS and Android">
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e4e3e812eb6841ff11795a6ee0ea36eff483920ea9266733d6948ed34df3def3-Untitled_design_9.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=9bf6f4a73e38ec424b8cfec75a474a26" width="1200" height="800" data-path="images/docs/e4e3e812eb6841ff11795a6ee0ea36eff483920ea9266733d6948ed34df3def3-Untitled_design_9.png" />
    </Frame>

    <Info>Images will appear small in the collapsed notification view. Expand the notification to see the full image.</Info>
  </Step>

  <Step title="Check for confirmed delivery.">
    In your dashboard, go to **Delivery > Sent Messages**, then click the message to view stats.

    You should see the **confirmed** stat, meaning the device received the push.
    <Check>You have successfully sent a notification via our API to a segment.</Check>

    <Warning>
      * No image received? Your [Notification Service Extension](#ios-setup) might be missing.
      * No confirmed delivery? Review the troubleshooting guide [here](/docs/en/confirmed-delivery#troubleshooting-confirmed-delivery).
      * Having issues? Copy-paste the api request and a log from start to finish of app launch into a `.txt` file. Then share both with `support@onesignal.com`.
    </Warning>
  </Step>
</Steps>

### Send an in-app message

[In-app messages](/docs/en/in-app-messages-setup) let you communicate with users while they are using your app.

<Steps>
  <Step title="Close or background your app on the device.">
    This is because users must meet the in-app audience criteria *before* a new session starts. In OneSignal, a new session starts when the user opens your app after it has been in the background or closed for at least 30 seconds. For more details, see our guide on [how in-app messages are displayed](/docs/en/in-app-messages-setup#how-are-iams-displayed%3F).
  </Step>

  <Step title="Create an in-app message.">
    * In your OneSignal dashboard, navigate to **Messages > In-App > New In-App**.
    * Find and select the **Welcome** message.
    * Set your Audience as the **Test Users** segment we used previously.

    <Frame caption="Targeting the 'Test Users' segment with an in-app message">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2979dfb2c6e0711669ebe737d78d975dcfed9f8117bdd68846255b9fc91e4771-Screenshot_2025-03-17_at_14.56.23.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=f705ee679a9248dab378305e15fa24bf" width="1410" height="752" data-path="images/docs/2979dfb2c6e0711669ebe737d78d975dcfed9f8117bdd68846255b9fc91e4771-Screenshot_2025-03-17_at_14.56.23.png" />
    </Frame>
  </Step>

  <Step title="Customize the message content if desired.">
    <Frame caption="Example customization of in-app Welcome message">
      <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4c511ebdb04f33055556b9969bab8deee0d62154573cf0b41ffb25cc8431e7c0-Screenshot_2025-03-17_at_14.59.37.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=6134cc70e578d1055f770edcbad47efb" width="1646" height="1070" data-path="images/docs/4c511ebdb04f33055556b9969bab8deee0d62154573cf0b41ffb25cc8431e7c0-Screenshot_2025-03-17_at_14.59.37.png" />
    </Frame>
  </Step>

  <Step title="Set Trigger to 'On app open'." />

  <Step title="Schedule frequency.">
    Under **Schedule > How often do you want to show this message?** select **Every time trigger conditions are satisfied**.

    <Frame caption="In-app message scheduling options">
      <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c48ccaf33a74d5aa442c768a18b8e642024b89305aae665d613aee1d8bde43ec-Screenshot_2025-03-17_at_15.00.40.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=9a57431acffa267d22af4e19052fb5ee" width="1646" height="1070" data-path="images/docs/c48ccaf33a74d5aa442c768a18b8e642024b89305aae665d613aee1d8bde43ec-Screenshot_2025-03-17_at_15.00.40.png" />
    </Frame>
  </Step>

  <Step title="Make message live.">
    Click **Make Message Live** so it is available to your Test Users each time they open the app.
  </Step>

  <Step title="Open the app and see the message.">
    After the in-app message is live, open your app. You should see it display:

    <Frame caption="Welcome in-app message shown on devices">
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a7ed4bb02be56900a65d2519e3d69f9c9b2c2a1c65fe740f07789e4ffe79cd67-Untitled_design_10.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=6f692b569706ca39df0b4cc2b70f3de2" width="1920" height="1080" data-path="images/docs/a7ed4bb02be56900a65d2519e3d69f9c9b2c2a1c65fe740f07789e4ffe79cd67-Untitled_design_10.png" />
    </Frame>

    <Warning>
      Not seeing the message?

      * Start a new session
        * You must close or background the app for at least 30 seconds before reopening. This ensures a new session is started.
        * For more, see [how in-app messages are displayed](/docs/en/in-app-messages-setup#how-are-iams-displayed%3F).
      * Still in the `Test Users` segment?
        * If you reinstalled or switched devices, re-add the device to [Test Subscriptions](#set-up-test-subscriptions) and confirm it's part of the Test Users segment.
      * Having issues?
        * Follow [Getting a Debug Log](/docs/en/capturing-a-debug-log) while reproducing the steps above. This will generate additional logging that you can share with `support@onesignal.com` and we will help investigate what's going on.
    </Warning>
  </Step>
</Steps>

<Check>
  You have successfully setup the OneSignal SDK and learned important concepts like:

* Gathering [Subscriptions](/docs/en/subscriptions), setting [Test subscriptions](/docs/en/find-set-test-subscriptions), and creating [Segments](/docs/en/segmentation).
* Sending [Push](/docs/en/push) with images and [Confirmed Delivery](/docs/en/confirmed-delivery) using Segments and our [Create message](/reference/create-message) API.
* Sending [In-app messages](/docs/en/in-app-messages-setup).

  Continue with this guide to identify users in your app and setup additional features.
</Check>

***

## User identification

Previously, we demonstrated how to create mobile [Subscriptions](/docs/en/subscriptions). Now we'll expand to identifying [Users](/docs/en/users) across all their subscriptions (including push, email, and SMS) using the OneSignal SDK. We'll cover External IDs, tags, multi-channel subscriptions, privacy, and event tracking to help you unify and engage users across platforms.

### Assign External ID

Use an External ID to identify users consistently across devices, email addresses, and phone numbers using your backend's user identifier. This ensures your messaging stays unified across channels and 3rd party systems (especially important for [Integrations](/docs/en/integrations)).

Set the External ID with our SDK's [`login` method](/docs/en/mobile-sdk-reference#login-external-id) each time they are identified by your app.

<Note>
  OneSignal generates unique read-only IDs for subscriptions (Subscription ID) and users (OneSignal ID).

  As users download your app on different devices, subscribe to your website, and/or provide you email addresses and phone numbers outside of your app, new subscriptions will be created.

  Setting the External ID via our SDK is highly recommended to identify users across all their subscriptions, regardless of how they are created.
</Note>

### Add data tags

[Tags](/docs/en/add-user-data-tags) are key-value pairs of string data you can use to store user properties (like `username`, `role`, or preferences) and events (like `purchase_date`, `game_level`, or user interactions). Tags power advanced [Message Personalization](/docs/en/message-personalization) and [Segmentation](/docs/en/segmentation) allowing for more advanced use cases.

Set tags with our SDK [`addTag` and `addTags` methods](/docs/en/mobile-sdk-reference#data-tags) as events occur in your app.

In this example, the user reached level 6 identifiable by the tag called `current_level` set to a value of `6`.

<Frame caption="A user profile in OneSignal with a tag called &#x22;current_level&#x22; set to &#x22;6&#x22;">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d4674261847231079fecc176ba88065409c90943e3854b9df200457325a0aed4-Screenshot_2025-03-18_at_14.47.25.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=91083bf83a4c03ea40d485b23f072259" width="1380" height="941" data-path="images/docs/d4674261847231079fecc176ba88065409c90943e3854b9df200457325a0aed4-Screenshot_2025-03-18_at_14.47.25.png" />
</Frame>

We can create a segment of users that have a level of between 5 and 10, and use that to send targeted and personalized messages:

<Frame caption="Segment editor showing a segment targeting users with a current_level value of greater than 4 and less than 10">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/300d36b632a6f6d7017780457bbe2610b71767fd0db093c7611e59714dcbda5b-Screenshot_2025-03-18_at_14.49.56.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=b84ab0d2c6eedbd6d4e7a2bf15afe103" width="1380" height="941" data-path="images/docs/300d36b632a6f6d7017780457bbe2610b71767fd0db093c7611e59714dcbda5b-Screenshot_2025-03-18_at_14.49.56.png" />
</Frame>

<br />

<Frame caption="Screenshot showing a push notification targeting the Level 5-10 segment with a personalized message">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/97e09b42d25c6d3f4c7cb0a6fff4dfb8893cbb4b283f7ff1f77977c33113319c-Screenshot_2025-03-18_at_14.55.47.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=c7839b12057d65a12a4eaddce6e2c11f" width="2764" height="2286" data-path="images/docs/97e09b42d25c6d3f4c7cb0a6fff4dfb8893cbb4b283f7ff1f77977c33113319c-Screenshot_2025-03-18_at_14.55.47.png" />
</Frame>

<br />

<Frame caption="The push notification is received on an iOS and Android device with the personalized content">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3bf1810580f30984745017056383f151b874513b6bfb1445fb1016e5c9a79e82-Untitled_design_12.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=94b6e9eeeb5516285a256a72063a0906" width="1920" height="1080" data-path="images/docs/3bf1810580f30984745017056383f151b874513b6bfb1445fb1016e5c9a79e82-Untitled_design_12.png" />
</Frame>

### Add email and/or SMS subscriptions

Earlier we saw how our SDK creates mobile subscriptions to send push and in-app messages. You can also reach users through emails and SMS channels by creating the corresponding subscriptions.

* Use the [`addEmail` method](/docs/en/mobile-sdk-reference#addemail-%2C-removeemail) to create email subscriptions.
* Use the [`addSms` method](/docs/en/mobile-sdk-reference#addsms-%2C-removesms) to create SMS subscriptions.

If the email address and/or phone number already exist in the OneSignal app, the SDK will add it to the existing user, it will not create duplicates.

You can view unified users via **Audience > Users** in the dashboard or with the [View user API](/reference/view-user).

<Frame caption="A user profile with push, email, and SMS subscriptions unified by External ID">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b1cf9999d41da6e4ce333e1126612529b85eac47447bb0b434418d082f595acd-Screenshot_2025-03-18_at_14.43.46.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=7c3885b66e44e097fa0ed7c47f27c911" width="1506" height="848" data-path="images/docs/b1cf9999d41da6e4ce333e1126612529b85eac47447bb0b434418d082f595acd-Screenshot_2025-03-18_at_14.43.46.png" />
</Frame>

<Note>
  Best practices for multi-channel communication

* Obtain explicit consent before adding email or SMS subscriptions.
* Explain the benefits of each communication channel to users.
* Provide channel preferences so users can select which channels they prefer.
</Note>

***

### Privacy & user consent

To control when OneSignal collects user data, use the SDK's consent gating methods:

* [`setConsentRequired(true)`](/docs/en/mobile-sdk-reference#setconsentrequired): Prevents data collection until consent is given.
* [`setConsentGiven(true)`](/docs/en/mobile-sdk-reference#setconsentgiven): Enables data collection once consent is granted.

See our Privacy & security docs for more on:

* [Data collected by the SDK](/docs/en/data-collected-by-the-onesignal-sdk)
* [Handling personal data](/docs/en/handling-personal-data)

***

## Prompt for push permissions

Instead of calling `requestPermission()` immediately on app open, take a more strategic approach. Use an in-app message to explain the value of push notifications before requesting permission.

For best practices and implementation details, see our [Prompt for push permissions](/docs/en/prompt-for-push-permissions) guide.

***

## Listen to push, user, and in-app events

Use SDK listeners to react to user actions and state changes.

The SDK provides several event listeners for you to hook into. See our [SDK reference guide](/docs/en/mobile-sdk-reference) for more details.

### Push notification events

* [`addClickListener()`](/docs/en/mobile-sdk-reference#addclicklistener-push): Detect when a notification is tapped. Helpful for [Deep Linking](/docs/en/deep-linking).
* [`addForegroundLifecycleListener()`](/docs/en/mobile-sdk-reference#addforegroundlifecyclelistener-push): Control how notifications behave in foreground.

For full customization, see [Mobile Service Extensions](/docs/en/service-extensions).

### User state changes

* [`addObserver()` for user state](/docs/en/mobile-sdk-reference#addobserver-user-state): Detect when the External ID is set.
* [`addPermissionObserver()`](/docs/en/mobile-sdk-reference#addpermissionobserver-push): Track the user's specific interaction with the native push permission prompt.
* [`addObserver()` for push subscription](/docs/en/mobile-sdk-reference#addobserver-push-subscription-changes): Track when the push subscription status changes.

### In-app message events

* [`addClickListener()`](/docs/en/mobile-sdk-reference#addclicklistener-in-app): Handle in-app click actions. Ideal for deep linking or tracking events.
* [`addLifecycleListener()`](/docs/en/mobile-sdk-reference#addclicklistener-in-app): Track full lifecycle of in-app messages (shown, clicked, dismissed, etc.).

***

## Advanced setup & capabilities

Explore more capabilities to enhance your integration:

* [🔁 Migrating to OneSignal from another service](/docs/en/migrating-to-onesignal)
* [🌍 Location tracking](/docs/en/mobile-sdk-reference#location)
* [🔗 Deep Linking](/docs/en/deep-linking)
* [🔌 Integrations](/docs/en/integrations)
* [🧩 Mobile Service Extensions](/docs/en/service-extensions)
* [🛎️ Action buttons](/docs/en/action-buttons)
* [🌐 Multi-language messaging](/docs/en/multi-language-messaging)
* [🛡️ Identity Verification](/docs/en/identity-verification)
* [📊 Custom Outcomes](/docs/en/custom-outcomes)
* [📲 Live Activities](/docs/en/live-activities)

### Mobile SDK setup & reference

Make sure you've enabled all key features by reviewing the [Mobile push setup](/docs/en/mobile-push-setup) guide.

For full details on available methods and configuration options, visit the [Mobile SDK reference](/docs/en/mobile-sdk-reference).

<Check>Congratulations! You've successfully completed the Mobile SDK setup guide.</Check>

***

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

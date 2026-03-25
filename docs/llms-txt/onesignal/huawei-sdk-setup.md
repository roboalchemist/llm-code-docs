# Source: https://documentation.onesignal.com/docs/en/huawei-sdk-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Huawei SDK setup

> OneSignal Huawei SDK Setup Guide for Android Studio.

## Overview

This guide explains how to integrate OneSignal push notifications into a Huawei app distributed on the Huawei AppGallery.

These instructions are for native apps written in Java or Kotlin. For other supported SDKs see:

<Columns cols={2}>
  <Card title="Ionic/Cordova/Capacitor" href="./huawei-cordova-sdk-setup" arrow={true} />

  <Card title="Flutter" href="./huawei-flutter-sdk-setup" arrow={true} />

  <Card title="React Native" href="./huawei-react-native-sdk-setup" arrow={true} />

  <Card title="Unity" href="./huawei-unity-sdk-setup" arrow={true} />
</Columns>

***

## Requirements

* [Android Studio](https://developer.android.com/studio)
* A Huawei device with "Huawei App Gallery" installed
* Configured OneSignal App and Platform

***

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

### 1. Setup the OneSignal SDK

<Card title="OneSignal Android SDK setup" href="./android-sdk-setup" arrow={true}>
  Follow the OneSignal Android SDK setup guide to implement our SDK into your app.
  Note that Firebase/Google setup is not required for app builds released to the Huawei AppGallery.
</Card>

### 2. Huawei configuration (agconnect-services.json)

<Info>
  You can skip this step if you already have a Huawei `agconnect-services.json` in your Android Studio Project from setting up a different Huawei service.
</Info>

From the [AppGallery Connect Project List](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/myProject) select your app.

Click on the "agconnect-services.json" button to download this file.

<Frame>
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b4f866d-Huawei_AppGallery_Connect_ProjectSettings_Download_agconnect-services.json_file.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=0d2a452e3c007ce4a63fa3ed50204a32" width="1262" height="696" data-path="images/docs/b4f866d-Huawei_AppGallery_Connect_ProjectSettings_Download_agconnect-services.json_file.png" />
</Frame>

Place this file in your app directory in Android Studio.

<Frame>
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5a9ee3b-Huawei_AndroidStudio_agconnect-services.json_file.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=6c9e6eb15b63c4089b959e3652b9b695" width="362" height="326" data-path="images/docs/5a9ee3b-Huawei_AndroidStudio_agconnect-services.json_file.png" />
</Frame>

### 3. Generating a signing certificate fingerprint

<Info>
  You can skip this step if you already have added your SHA-256 certificate fingerprint to Huawei's dashboard for a different Huawei service.
</Info>

From your Android Studio go to **View > Tool Windows > Gradle**.

<Frame>
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/092273b-Huawei_AndroidStudio_Open_Gradle_Tasks_List.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=6a59f3f7060ee0d384c281e234c92f17" width="595" height="358" data-path="images/docs/092273b-Huawei_AndroidStudio_Open_Gradle_Tasks_List.png" />
</Frame>

From here select **app > Tasks > android > signingReport**.

<Frame>
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/db2ecdd-Huawei_AndroidStudio_Run_signingReport.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=d239877b38edbdf268dce6c999726fb0" width="294" height="216" data-path="images/docs/db2ecdd-Huawei_AndroidStudio_Run_signingReport.png" />
</Frame>

Copy your `SHA-256` for your `release` variant.

* Optional but recommended for quicker testing is the `SHA-256` for your `debug` variant too.
* You may have other custom variants in your project, if you need push support for them copy these as well.

<Frame>
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f6b08a6-Huawei_AndroidStudio_signingReport_output.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=05d59af3ed44175b67778fa8d0c4cf8f" width="798" height="346" data-path="images/docs/f6b08a6-Huawei_AndroidStudio_signingReport_output.png" />
</Frame>

From the [AppGallery Connect Project List](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/myProject) select your app.

Scroll to the bottom to find the "SHA-256 certificate fingerprint" field were you should enter your keys.

<Frame>
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9bf59ea-Huawei_AppGallery_Connect_SHA256_cert_fingerprint.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=e3b1c87ac0ec02d95e60fa115f8f51a2" width="1292" height="622" data-path="images/docs/9bf59ea-Huawei_AppGallery_Connect_SHA256_cert_fingerprint.png" />
</Frame>

### 4. Add Huawei gradle plugin and dependencies

<Tabs>
  <Tab title="Groovy + AGP 7.x">
    Open your root `build.gradle` (Project: ) in Android Studio and add ` maven {url 'https://developer.huawei.com/repo/'}` under `buildscript { repositories }` and `allprojects { repositories }`
  </Tab>

  <Tab title="Kotlin + AGP 8.x">
    Open your `settings.gradle.kts` file and add `maven {url 'https://developer.huawei.com/repo/'}` under `pluginManagement { repositories }` and `dependencyResolutionManagement { repositories }`
  </Tab>
</Tabs>

Under `buildscript { dependencies }` add `classpath 'com.huawei.agconnect:agcp:1.9.1.301'`

You should have in total 3 new lines in your root `build.gradle`, highlighted below.

<Frame>
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d1791d3-Huawei_AndroidStudio_root_build.gradle_file_2.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=b5e3b1016d53fb02c4c7eee1fee75c43" width="941" height="664" data-path="images/docs/d1791d3-Huawei_AndroidStudio_root_build.gradle_file_2.png" />
</Frame>

Open your `app/build.gradle` file and add `implementation 'com.huawei.hms:push:6.3.0.304'` under the `dependencies` section.

Also to the `app/build.gradle` file add `apply plugin: 'com.huawei.agconnect'` to the very bottom of the file.

You should have in total 2 new lines in your `app/build.gradle`, highlighted below.

<Tip>
  Make sure to press "Sync Now" on the banner that pops up after saving!
</Tip>

<Frame>
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0b441ec-Huawei_AndroidStudio_sync_now.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=ae87a2d2f8a1b7aaf9fe17208255be4c" width="1033" height="112" data-path="images/docs/0b441ec-Huawei_AndroidStudio_sync_now.png" />
</Frame>

***

## Additional configuration steps

### Compatibility with other HMS push libraries or your own `HmsMessageService` class

Required if:

* You have another HMS push SDK/Library in your app in-addition to OneSignal
* You have your own `HmsMessageService`

<Accordion title="More details...">
  Create a class that extends from `HmsMessageService`, if you don't have one already and add the following methods.

  <Warning>
    If you already had a class that extends `HmsMessageService` please add the two
    new `OneSignalHmsEventBridge` lines instead of creating another class.
  </Warning>

  ```java Java theme={null}
  public class YourHmsMessageService extends HmsMessageService {
    public void onNewToken(String token) {
        // ...
        // Forward event on to OneSignal SDK
        OneSignalHmsEventBridge.onNewToken(this, token);
    }

    @Override
    public void onMessageReceived(RemoteMessage message) {
        // ...
        // Forward event on to OneSignal SDK
        OneSignalHmsEventBridge.onMessageReceived(this, message);
    }
  }
  ```

  This is to forward `onNewToken` and `onMessageReceived` to OneSignal via the `OneSignalHmsEventBridge`.

  If you didn't have a class that extended `HmsMessageService` before make sure to add it to your `AndroidManifest.xml` under the `<application>` tag.

  ```xml AndroidManifest.xml theme={null}
  <application>
      ...

      <!--
        Ensure you only have one intent-filter for "com.huawei.push.action.MESSAGING_EVENT".
        HMS only supports one per app.
      -->
      <service
          android:name=".YourHmsMessageService"
          android:exported="false">
          <intent-filter>
              <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
          </intent-filter>
      </service>

      ...
  </application>
  ```

</Accordion>

### Omit Google libraries for Huawei AppGallery builds (optional)

<Accordion title="More details...">
  <Tabs>
    <Tab title="Option 1">
      If your app will only be available on the Huawei AppGallery and you want to omit any Google related dependencies that OneSignal includes you can use `exclude` with `implementation` in your `app/build.gradle`.

      <CodeGroup>
        ```groovy app/build.gradle theme={null}
        implementation('com.onesignal:OneSignal:[5.4.0, 5.99.99]') {
            exclude group: 'com.google.android.gms'
            exclude group: 'com.google.firebase'
        }
        ```
      </CodeGroup>
    </Tab>

    <Tab title="Option 2">
      If your app will be for both the Google Play Store and Huawei AppGallery and you want to be selective on which libraries you will include to make your APK smaller you can add dependencies based on buildTypes or variants. Example:

      <CodeGroup>
        ```groovy app/build.gradle theme={null}
        android {
          // ...
           buildTypes {
               debug {
               }
               release {
               }
               // **** Add your custom hauwei buildType here
               huawei {
               }
           }
        }

        dependencies {
        // \*\*\*\* Use the full OneSignal dependencies for Google Play Store builds
        debugImplementation 'com.onesignal:OneSignal:[5.0.0, 5.99.99]'
        releaseImplementation 'com.onesignal:OneSignal:[5.0.0, 5.99.99]'

            // **** Only include hms:push for your Huawei AppGallery builds.
            huaweiImplementation 'com.huawei.hms:push:6.3.0.304'
            // Omit Google / Firebase libraries for Huawei builds.
            huaweiImplementation('com.onesignal:OneSignal:[5.0.0, 5.99.99]') {
                exclude group: 'com.google.android.gms'
                exclude group: 'com.google.firebase'
            }

        }

        ```
      </CodeGroup>
    </Tab>
  </Tabs>
</Accordion>

### Prefer HMS over FCM (optional)

<Accordion title="More details...">
  ***If you have [omitted Google Libraries](./huawei-sdk-setup#omit-google-libraries-for-huawei-appgallery-builds-optional) for Huawei AppGallery build above, this step doesn't apply.***

  By default OneSignal prefers using FCM over HMS if both are included in your app. If you like to change this to prefer HMS instead you can add the following to your `AndroidManifest.xml`:

  <CodeGroup>
    ```xml xml theme={null}
    <application>
            ...
            <meta-data android:name="com.onesignal.preferHMS" android:value="true"/>
            ...
     </application>
    ```
  </CodeGroup>
</Accordion>

***

## Huawei troubleshooting

While testing, make sure to keep the [OneSignal setLogLevel method](./mobile-sdk-reference#setloglevel) set to VERBOSE.

Check the logs to see any errors being thrown and [Huawei Common Error Codes](https://developer.huawei.com/consumer/en/doc/development/HMS-2-References/hmssdk_huaweipush_api_reference_errorcode).

<Accordion title="6003 error">
  You may need to create a debug or release keystore signature (choose the correct app build path, `debug` or `release`) so that a `6003` error is avoided when registering for Huawei `pushToken` with the OneSignal SDK. See ["Configure a Signature" section](https://developer.huawei.com/consumer/en/doc/HMS-Guides/Preparations#h2-1584707362385)
</Accordion>

<Accordion title="notification_types: -25">
  `"notification_types":-25` means OneSignal timed out waiting for a response from Huawei's HMS to get a push token. This is most likely due to another 3rd-party HMS push SDK or your own HmsMessageService getting this event instead of OneSignal.

  Please review [step on how to check this and forward the event if this is the case](#compatibility-with-other-hms-push-libraries-or-your-own-hmsmessageservice-class).
</Accordion>

<Accordion title="notification_types: -28">
  This means there is a class HMS is missing from the app that is needed for push. Just having `com.huawei.hms:push` in the `build.gradle` will cause this specific error not to happen any more. However, if you have some aggressive Proguard or R8 settings, this might cause issues. We recommend turn off `minifyEnabled` temporary if you have it to see if that is the root of the issue.

  Also, you shouldn't mix and match major release versions of other HMS libraries. Start with either 4 or 5. Make sure not to have a mixture from 3 to 5 which is going to create other errors
</Accordion>

<Accordion title="Error getting Huawei push token">
  ```
  E/OneSignal: HMS ApiException getting Huawei push token!
      com.huawei.hms.common.ApiException: -5: Core error
  ```

  Check your Proguard or R8 rules to make sure they are setup properly. Possibly disable it temporarily to see if it is related. If it fixes the issue after disabling Proguard or R8 then you can follow this guide and turn it back on See ["Configure a Signature" section](https://developer.huawei.com/consumer/en/doc/HMS-Guides/Preparations#h2-1584707362385)
</Accordion>

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

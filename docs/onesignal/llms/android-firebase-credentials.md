# Source: https://documentation.onesignal.com/docs/en/android-firebase-credentials.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Android Firebase credentials

> Learn how to generate and configure Firebase Cloud Messaging (FCM) Service Account credentials for OneSignal to send Android push notifications to apps on the Google Play Store.

To send push notifications to Android devices through the Google Play Store, OneSignal requires Firebase Cloud Messaging (FCM) credentials. This guide walks you through generating the required Service Account JSON file and uploading it to your OneSignal app settings.

For technical background, see [Google’s Service Account documentation](https://cloud.google.com/iam/docs/service-account-overview).

<Note>
  This guide is for developers integrating OneSignal with an Android mobile app distributed via the Google Play Store.

* This guide should not be used for Web Push. See [Web push setup](./web-push-setup).
* For Huawei apps distributed via the Huawei App Gallery, see [Huawei: Authorizing OneSignal](./authorize-onesignal-to-send-huawei-push).
</Note>

***

## Requirements

* An Android app distributed via the Google Play Store
* A [Firebase account (free)](https://firebase.google.com)
* A [OneSignal account](https://onesignal.com)

***

## Setup

### 1. Create or open your Firebase Project

Go to the [Firebase console](https://console.firebase.google.com/).

* If you don’t have a project yet, click **Add project** and complete the setup.
* If you already have a project, **select it**.

<Frame caption="Page of Projects within Firebase">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/af78883-Screenshot_2024-06-27_at_9.56.53_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=70f753e043df7f26eb0cdcb9aa6e7dd6" width="2220" height="1268" data-path="images/docs/af78883-Screenshot_2024-06-27_at_9.56.53_AM.png" />
</Frame>

### 2. Enable Firebase Cloud Messaging API v1

<Steps>
  <Step title="Go to Project Settings">
    In Firebase, click the **gear icon** next to **Project Overview > Project settings**.

    <Frame caption="Firebase gear icon submenu, showing Project Settings">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/85fe0ac-Screenshot_2024-06-27_at_9.59.24_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=6365da65ac84db166637d06f74675a29" width="2170" height="758" data-path="images/docs/85fe0ac-Screenshot_2024-06-27_at_9.59.24_AM.png" />
    </Frame>
  </Step>

  <Step title="Go to Cloud Messaging">
    Go to the **Cloud Messaging** tab.

    If **Firebase Cloud Messaging API (V1)** is **disabled**, click the **3-dot menu > Open in Cloud Console**.

    <Frame caption="Firebase Cloud Messaging API (V1) is disabled in this image. Ensure it is enabled for your project.">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/04dd9fc-Screenshot_2024-06-27_at_10.01.20_AM.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=00a205057d79bdf4d7a274d759f8976c" width="1654" height="670" data-path="images/docs/04dd9fc-Screenshot_2024-06-27_at_10.01.20_AM.png" />
    </Frame>

    In the Google Cloud Console, click **Enable**. Wait a few minutes for the change to reflect in Firebase.

    <Frame caption="Enable Firebase Cloud Messaging API v1.">
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/386f283-Screenshot_2024-06-27_at_10.05.57_AM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=c68e7e50bbc83ec0f1fe7c006dbb717c" width="1612" height="844" data-path="images/docs/386f283-Screenshot_2024-06-27_at_10.05.57_AM.png" />
    </Frame>
  </Step>
</Steps>

### 3. Generate a Service Account JSON file

<Steps>
  <Step title="Return to Project Settings > Service Accounts">
    At the bottom, click **Generate new private key**.

    <Frame caption="Service Accounts section within Firebase">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/88fc0c0-Screenshot_2024-06-27_at_10.12.07_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=79080960dc590694c0782faaea44ea13" width="1788" height="1682" data-path="images/docs/88fc0c0-Screenshot_2024-06-27_at_10.12.07_AM.png" />
    </Frame>
  </Step>

  <Step title="Confirm and generate key">
    Confirm by clicking **Generate key** in the popup.

    <Frame caption="🔒 This file contains sensitive credentials. Do not share it or check it into version control.">
      <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f84ae62-Screenshot_2024-06-27_at_10.20.49_AM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=9ebbbdbc5a95aa9e88941391bdf99b5a" width="1248" height="564" data-path="images/docs/f84ae62-Screenshot_2024-06-27_at_10.20.49_AM.png" />
    </Frame>
  </Step>

  <Step title="Save the file">
    Save the `.json` file in a secure location. You will need it shortly.

    <Info>
      Required Service Account permissions:

      * `cloudmessaging.messages.create`
      * `firebase.projects.get`

      These are included by default. If you're using a custom Service Account, ensure it has:

      * `roles/firebasemessaging.admin`
      * `roles/firebase.viewer`
    </Info>
  </Step>
</Steps>

### 4. Upload your credentials to OneSignal

<Steps>
  <Step title="Go to Android platform settings">
    In your OneSignal dashboard, go to: **Settings > Push & In-App > Push Platforms > Google Android (FCM)**.

    Click **Activate**.

    <Frame caption="Platforms screen within OneSignal app settings">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/9003bdd135471cd7a0be2c66197968b4c1f802dc57e4ece68db668c1394633fa-Screenshot_2025-03-31_at_3.32.00_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=dc8843c67f9e4a0afb78911b8a6ce722" width="2324" height="1488" data-path="images/docs/9003bdd135471cd7a0be2c66197968b4c1f802dc57e4ece68db668c1394633fa-Screenshot_2025-03-31_at_3.32.00_PM.png" />
    </Frame>
  </Step>

  <Step title="Upload your credentials">
    Upload the `.json` file under **Service Account JSON** by clicking **Choose file**.

    <Frame caption="FCM configuration screen">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/30484ba18d6e18c5a2dbbd9238afcb1294e19e1d916f820dec9e1d86f3d3dc6b-Screenshot_2025-03-31_at_3.34.39_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=2d8ca81ec7056fbc91735f1041cb413f" width="2324" height="868" data-path="images/docs/30484ba18d6e18c5a2dbbd9238afcb1294e19e1d916f820dec9e1d86f3d3dc6b-Screenshot_2025-03-31_at_3.34.39_PM.png" />
    </Frame>

    <Warning>
      If prompted, select **Firebase Cloud Messaging API (V1)** from the dropdown.

      To verify you're using the correct Firebase project, match the **Sender ID** in Firebase (`Cloud Messaging > Sender ID`) with the one shown in your OneSignal settings.
    </Warning>
  </Step>

  <Step title="Save and continue" />

  <Step title="Choose your SDK">
    Select the SDK you are using and click **Save & Continue**.

    <Frame caption="SDK selection screen">
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d8507f6-Screenshot_2024-06-27_at_10.43.29_AM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=af1b3ef1edae8a63ef0989078879f984" width="2088" height="1036" data-path="images/docs/d8507f6-Screenshot_2024-06-27_at_10.43.29_AM.png" />
    </Frame>
  </Step>

  <Step title="Add the OneSignal App ID to your code">
    Continue following the [Mobile SDK setup](./mobile-sdk-setup) and add this OneSignal App ID to your code.

    <Frame caption="Android configuration installation and testing screen">
      <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/65b7f30-Screenshot_2024-06-27_at_10.47.45_AM.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=865cd44b7e9dedd301ac6ac75a69d17a" width="2088" height="768" data-path="images/docs/65b7f30-Screenshot_2024-06-27_at_10.47.45_AM.png" />
    </Frame>
  </Step>
</Steps>

<Check>
  You’ve successfully connected your OneSignal app to Firebase Cloud Messaging (V1).

  Next, complete [Mobile SDK setup](./mobile-sdk-setup) or go to [Mobile push setup](./mobile-push-setup) for platform-specific instructions.
</Check>

***

## FAQ

### Error: “This configuration is for a different Firebase Project...”

This error occurs when the uploaded JSON file belongs to a different Firebase project (i.e., different Sender ID).

**Solution**: Use the original Firebase project's JSON file. If unavailable, contact `support@onesignal.com` with your App ID. Switching projects resets push tokens—your users must reopen the app to get push again.

### Can I change my Sender ID?

No. The Sender ID is locked once your app surpasses 100 Android users to prevent accidental invalidation of push tokens.

If necessary, contact `support@onesignal.com` with your App ID for assistance.

### Do I need to update my code when switching to FCM V1?

No app or SDK changes are required—this is a dashboard-only update.

### What is the deadline for switching to FCM v1?

Google began deprecating legacy FCM APIs in **July 2024**. Migration is strongly recommended. See [Google's announcement](https://firebase.google.com/docs/cloud-messaging/migrate-v1).

### Why don’t I see a Sender ID in OneSignal?

If your Firebase server key looks like `AIz...`, you're likely using an outdated Google Cloud Messaging (GCM) setup. Create a new Firebase project and upload a Service Account JSON file.

### How can I check which apps are still using the Legacy API?

Use the [View apps](/reference/view-apps) API and check for:

* `"gcm_key"` → using Legacy, needs update
* `"fcm_v1_service_account_json"` → using V1 ✅
* Neither → app does not use Android push

***

Built with [Mintlify](https://mintlify.com).

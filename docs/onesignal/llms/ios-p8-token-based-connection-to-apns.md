# Source: https://documentation.onesignal.com/docs/en/ios-p8-token-based-connection-to-apns.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS p8 token-based connection to APNs

> Set up a .p8 authentication key to connect your iOS or macOS app to Apple Push Notification service (APNs) through OneSignal.

Sending push notifications to iOS apps requires an authenticated connection to Apple Push Notification service (APNs). You can authenticate using a **token-based (.p8 key)** or a **[certificate-based (.p12 file)](./ios-p12-generate-certificates)** method — only one is necessary.

This guide covers the **token-based .p8 key**, the recommended approach.

***

## Requirements

Make sure you have the following before starting:

* An iOS mobile app.
* A [**Paid Apple Developer Account**](https://developer.apple.com/) with [**Admin** access](https://appstoreconnect.apple.com/access/users).
* A [**OneSignal Account**](https://onesignal.com).
* A Mac with Xcode 14+.
* An Xcode project with **Push Notification capability enabled**.

***

## Set up APNs authentication

### Generate your .p8 key in Apple Developer Account

<Tip>
  For Apple's full instructions, see [Create a private key to access a service](https://developer.apple.com/help/account/keys/create-a-private-key/).
</Tip>

1. Log into your [Apple Developer Account](https://developer.apple.com/).
2. Go to **Certificates, Identifiers & Profiles > [Keys](https://developer.apple.com/account/resources/authkeys)**.
3. Click the **blue plus (+)** icon.
   * If you don’t see it, contact your Admin for access.

<Frame>
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1e2ff6e-Apple_Key_Page.jpg?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=695489e801fe6cb492ed826e0ea2c22b" alt="Apple Developer Keys page showing the blue plus icon to create a new key" width="2616" height="884" data-path="images/docs/1e2ff6e-Apple_Key_Page.jpg" />
</Frame>

1. Select **Apple Push Notifications service (APNs)**.
2. When configuring the key, ensure that **Sandbox & Production** is selected:

<Frame>
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/p8-sandboxandproductionkey.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=1f04581e46bd74cdbc27792b243b952b" alt="Apple Developer key configuration with Sandbox and Production selected" width="1232" height="495" data-path="images/docs/p8-sandboxandproductionkey.png" />
</Frame>

1. Enter a name for the key and click **Continue**, then **Register**.

<Frame>
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/312d551-Apple_Key_Page_-_Register.jpg?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=9b88f0e1cdb3fbdba05357ef988a1165" alt="Apple Developer key registration page with Continue and Register buttons" width="2622" height="922" data-path="images/docs/312d551-Apple_Key_Page_-_Register.jpg" />
</Frame>

1. **Download your .p8 key** and store it securely. You won’t be able to download it again.

<Warning>
  If you need to create a new .p8 and already have two, you **must first revoke one of the existing keys** — and it will no longer be usable.
</Warning>

***

### Upload the .p8 key to OneSignal

1. Navigate to **Settings > Push & In-App > Apple iOS (APNs) Settings** in your OneSignal dashboard.

<Frame caption="OneSignal dashboard push configuration page.">
  <img src="https://mintcdn.com/onesignal/KPVdijCt4_xCbkO8/images/dashboard/push-and-in-app-ios-settings.png?fit=max&auto=format&n=KPVdijCt4_xCbkO8&q=85&s=af9c2dedfc4c8f26f3aeee035cba5eb1" alt="OneSignal Settings page showing Push and In-App section with Apple iOS APNs settings" width="1188" height="654" data-path="images/dashboard/push-and-in-app-ios-settings.png" />
</Frame>

1. Choose **.p8 Auth Key (Recommended)** as the authentication method.

<Frame caption="If updating from a p12 or another p8, you'll have the option to 'update authentication'">
  <img src="https://mintcdn.com/onesignal/NCUI56Tiw7V-s0dT/images/dashboard/apns-authentication-method-selection.png?fit=max&auto=format&n=NCUI56Tiw7V-s0dT&q=85&s=bb08d987da33025d482b107fc1db1045" alt="OneSignal APNs authentication method selection showing p8 Auth Key recommended option" width="1188" height="844" data-path="images/dashboard/apns-authentication-method-selection.png" />
</Frame>

Provide the following:

* **`.p8 File`** – The private key file you downloaded from your Apple Developer account.
* **`Key ID`** – A 10-character alphanumeric string (e.g., `ABC123DEFG`) found next to your key name in the [Keys section](https://developer.apple.com/account/resources/authkeys) of your Apple Developer account. Make sure it matches the downloaded .p8 file.
* **`Team ID`** – A 10-character alphanumeric string (e.g., `9A1B2C3D4E`) shown next to your team name in the top-right corner of your [Apple Developer account](https://developer.apple.com/account/). This is **not** the same as the Key ID.
* **`App Bundle ID`** – A reverse-domain string (e.g., `com.example.app`) found in:
  * The [Identifiers section](https://developer.apple.com/account/resources/identifiers/list) of your Apple Developer account, or
  * **Xcode > Main App Target > Signing & Capabilities**

<Warning>
  **Key ID** and **Team ID** are both 10-character strings found in your Apple Developer account but in different locations. Double-check you haven't swapped them — this is the most common misconfiguration.
</Warning>

<Frame caption="Finding your .p8 key details">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c8d0207041e7c277f7e4ca49a3f6100280ddcbf970fce9b720fddfbda6683bb6-p8.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=fc9c689b0880bda69813428ee7fdbe5f" alt="Apple Developer account showing Key ID and Team ID locations" width="1445" height="506" data-path="images/docs/c8d0207041e7c277f7e4ca49a3f6100280ddcbf970fce9b720fddfbda6683bb6-p8.png" />
</Frame>

<Frame caption="Finding your Bundle ID on Xcode">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/35a1fd8940c4964156b9b0b83fbc41772189ae3d2eb29f80318137887344cf4c-ea1f341-Screenshot_2024-06-18_at_3.25.41_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=1ade7692a469b12376088ce5fac6c3c3" alt="Xcode Signing and Capabilities tab showing the Bundle Identifier field" width="2830" height="798" data-path="images/docs/35a1fd8940c4964156b9b0b83fbc41772189ae3d2eb29f80318137887344cf4c-ea1f341-Screenshot_2024-06-18_at_3.25.41_PM.png" />
</Frame>

Click **Save & Continue** when done.

<Check>
  You’ve successfully set up **APNs authentication using a .p8 key** in OneSignal.

  Your iOS app is now ready to send and receive push notifications! 🎉
</Check>

***

## .p8 troubleshooting

<Steps>
  <Step title="Check .p8 file format">
    * Open the `.p8` file in a text editor.

    * It should look like this:

      ```text  theme={null}
      -----BEGIN PRIVATE KEY-----
      64 character line
      64 character line
      64 character line
      8 character line
      -----END PRIVATE KEY-----
      ```
  </Step>

  <Step title="Ensure you didn’t upload a .p12 by mistake">
    * `.p8` keys come from the **Keys** section of your Apple Developer account.
    * `.p12` certificates are from the **Certificates** section. These are not compatible with .p8 authentication.
  </Step>

  <Step title="Confirm you have the correct Key ID">
    * Go to your [Apple Developer > Keys section](https://developer.apple.com/account/resources/authkeys).
    * The Key ID is the 10-character string shown next to your key name (e.g., `ABC123DEFG`).
    * Match the Key ID you entered in OneSignal with the one listed for the downloaded `.p8` key.
    * **Do not confuse this with your Team ID** — both are 10-character strings but found in different places.
  </Step>

  <Step title="Verify the Team ID">
    * Your **Team ID** is the 10-character string shown next to your team name in the top-right corner of your [Apple Developer account](https://developer.apple.com/account/).
    * Make sure it is copied exactly and matches the account where the key was generated.
    * **Do not confuse this with your Key ID** — the Team ID identifies your developer account, not a specific key.
  </Step>

  <Step title="Ensure the key has apns capability">
    * When viewing your key in Apple Developer, the **Apple Push Notifications service (APNs)** capability should be listed.
    * If not, revoke the key and create a new one.
  </Step>

  <Step title="Wait a few minutes">
    * Newly created keys may take **10–15 minutes** to propagate before Apple allows external authentication.
    * If you get validation errors immediately after creation, wait and try again.
  </Step>
</Steps>

### Need help?

* Revoke the current `.p8` key and create a new one from scratch.
* Double-check you’re using a **valid Bundle ID** from the same account the key was created under.
* Reach out to `support@onesignal.com` with a screenshot of your Apple Developer Key configuration and the Key ID, Team ID, and Bundle ID.

***

## Next steps

<Columns cols={2}>
  <Card title="iOS SDK setup" icon="apple" href="./ios-sdk-setup">
    Install the OneSignal SDK, initialize it in your app, and send a test notification.
  </Card>

  <Card title="Mobile SDK setup" icon="mobile" href="./mobile-sdk-setup">
    Choose your platform and follow the full SDK integration guide for Android, iOS, or cross-platform frameworks.
  </Card>
</Columns>

***

## FAQ

### What's the difference between .p8 and .p12?

A **.p8 key** is a token-based authentication key that does not expire and works across all apps under your Apple Developer account. A **.p12 certificate** is app-specific and expires after one year, requiring annual renewal. OneSignal recommends .p8 for its simplicity and lower maintenance. See the [.p12 certificate guide](./ios-p12-generate-certificates) for the alternative method.

### Does my .p8 key expire?

No. Unlike .p12 certificates, .p8 keys do not expire. Once created, a .p8 key remains valid until you revoke it in your Apple Developer account.

### Can I use one .p8 key for multiple apps?

Yes. A single .p8 key works for all apps under the same Apple Developer account. You can upload the same .p8 file to multiple OneSignal apps — each app only needs its own unique Bundle ID.

### Do I need a provisioning profile, and how do I create one?

Yes, Apple requires different types of profiles for development, testing (Ad Hoc), and distribution to the App Store.

In Xcode, select **Automatically manage signing** to create one automatically.

<Frame>
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/63400c422a45ceb7bd54a647c73252bc4221e3d9c62e7a595b4d58f8ae1a8c3e-Screenshot_2025-04-21_at_4.48.21_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=1f8f70d1078a89beb067d442690d6594" alt="Xcode Signing and Capabilities tab with Automatically manage signing enabled" width="2058" height="632" data-path="images/docs/63400c422a45ceb7bd54a647c73252bc4221e3d9c62e7a595b4d58f8ae1a8c3e-Screenshot_2025-04-21_at_4.48.21_PM.png" />
</Frame>

Otherwise, see [Apple's docs on provisioning profiles](https://developer.apple.com/help/account/provisioning-profiles/provisioning-profile-updates) for details.

***

Built with [Mintlify](https://mintlify.com).

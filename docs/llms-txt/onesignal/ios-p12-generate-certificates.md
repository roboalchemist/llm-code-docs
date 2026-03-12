# Source: https://documentation.onesignal.com/docs/en/ios-p12-generate-certificates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS p12 certificate generation

> Generate and upload a .p12 push certificate to connect your iOS or macOS app to Apple Push Notification service (APNs) through OneSignal.

Sending push notifications to iOS apps requires an authenticated connection to Apple Push Notification service (APNs). You can authenticate using a **[token-based (.p8 key)](./ios-p8-token-based-connection-to-apns)** or a **certificate-based (.p12 file)** method — only one is necessary.

<Warning>
  .p12 certificates expire after one year. If you don't want to manage annual renewal, [create a .p8 key](./ios-p8-token-based-connection-to-apns) instead — .p8 keys do not expire.
</Warning>

This guide covers the **certificate-based (.p12 file)** method. This is not recommended because you must renew it annually, which requires generating a new certificate in your Apple Developer Account and re-uploading it to your OneSignal dashboard.

***

## Requirements

Make sure you have the following before starting:

* An iOS or macOS app.
* A [**Paid Apple Developer Account**](https://developer.apple.com/) with [**Admin** access](https://appstoreconnect.apple.com/access/users).
* A [**OneSignal Account**](https://onesignal.com).
* A Mac with Xcode 14+.
* The **Bundle ID** for your app target as set in Xcode.
* An Xcode project with **Push Notification capability enabled**.

***

## Create a Certificate Signing Request (CSR)

You first need to create a `.certSigningRequest` file on macOS.

1. Open **Applications > Utilities > Keychain Access**.
2. From the menu bar, click **Keychain Access > Certificate Assistant > Request a Certificate From a Certificate Authority...**

<Frame caption="Mac keychain access">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4792ecd2f2859197d192d41e953c7cb461b62a08955e36de8674d13ebe3245d9-image.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=0d53d2a7d0a7992bb646cda2c10b2e3f" alt="Keychain Access menu showing Certificate Assistant option" width="709" height="314" data-path="images/docs/4792ecd2f2859197d192d41e953c7cb461b62a08955e36de8674d13ebe3245d9-image.png" />
</Frame>

1. Fill in the required fields:
   * **User Email Address**: `[email protected]`
   * **Common Name**: Your name or the name for the certificate
   * **CA Email Address**: Leave this blank
   * **Request is**: Select **Saved to disk**

<Frame caption="Certificate Assistant window">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/edfa46c8fa6d2a2743ec85d049cbed85d67eb4163388f44c7cbb602740ec1430-image.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=d78feadfda1f4a2c71806f8ab10edd04" alt="Certificate Assistant window with email, common name, and Saved to disk fields" width="728" height="554" data-path="images/docs/edfa46c8fa6d2a2743ec85d049cbed85d67eb4163388f44c7cbb602740ec1430-image.png" />
</Frame>

1. Click **Continue**, choose a location to save the `.certSigningRequest` file, and click **Save**.

***

## Enable push capabilities for the app

<Note>
  Skip this section if you use **Automatically manage signing** in Xcode.
</Note>

1. Go to the [Identifiers](https://developer.apple.com/account/ios/identifier/bundle) section of the Apple Developer portal, locate and select your app's **App ID** from the list.

<Frame>
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0f111cc6bc3d596c4f8ede9a8f62f8fafc526358cfc0f2f8b1e1a4f7fc8248fc-image.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=05b2003fb8c2fcd9131c44a793a0aba3" alt="Apple Developer Identifiers section showing list of App IDs" width="894" height="319" data-path="images/docs/0f111cc6bc3d596c4f8ede9a8f62f8fafc526358cfc0f2f8b1e1a4f7fc8248fc-image.png" />
</Frame>

1. Enable the **Push Notifications** capability by checking the box.

<Warning>
  **Do not** click **"Configure"** — just enable the toggle.
</Warning>

<Frame>
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3a420360bc845131ad00179d9542b9cc0dae47448ee0eef5068e609b7340f5d3-image.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=ba0781029d19036ddad3db3e45037d2b" alt="App ID capabilities list with Push Notifications checkbox enabled" width="2008" height="142" data-path="images/docs/3a420360bc845131ad00179d9542b9cc0dae47448ee0eef5068e609b7340f5d3-image.png" />
</Frame>

***

## Create a push certificate

Follow these steps to generate the Apple Push Notification service (APNs) SSL certificate:

1. Visit the [Apple Certificates page](https://developer.apple.com/account/resources/certificates/add).

2. Click the **plus (+)** button to create a new certificate.

3. Under **Services**, select:

   * **Apple Push Notification service SSL (Sandbox & Production)**
   * Then click **Continue**

   <Frame>
     <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6a48d1c410b80812f2893209eec0ae3d761ec86e40229b03ac780f1ae7124e48-image.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=6e0d0bb4d73dab95c32a0dc96d740723" alt="Apple Certificates page showing Apple Push Notification service SSL Sandbox and Production option" width="896" height="865" data-path="images/docs/6a48d1c410b80812f2893209eec0ae3d761ec86e40229b03ac780f1ae7124e48-image.png" />
   </Frame>

4. Select your **App ID** from the list and click **Continue**.

<Frame>
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/35daef0614fe669cadeb12adb900f0da6deab8b4283e29e1ba2712ce3d23e634-image.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=af9f0fb1fefed645b5ebefc6964d0d2d" alt="App ID selection dropdown for the push certificate" width="897" height="366" data-path="images/docs/35daef0614fe669cadeb12adb900f0da6deab8b4283e29e1ba2712ce3d23e634-image.png" />
</Frame>

1. Upload your previously generated `.certSigningRequest` file.

<Frame>
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6bb85bd5c6f420f73f1325ca5ccceea1c9cb22c618ccae8e7b34b5ead7fe28aa-image.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=1ca586cee9190e53ea681b411e36a786" alt="Upload Certificate Signing Request file dialog" width="662" height="626" data-path="images/docs/6bb85bd5c6f420f73f1325ca5ccceea1c9cb22c618ccae8e7b34b5ead7fe28aa-image.png" />
</Frame>

1. Click **Continue**, then click **Download** to save the resulting `.cer` file to your computer.

<Frame>
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/ca14b193b3ac73e0e4dfbc1697a3e24454341ebd880d2391d369fe20868f9434-image.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=e81079a2a25e6e82ed0eb9f1204ab774" alt="Download button for the generated .cer certificate file" width="924" height="368" data-path="images/docs/ca14b193b3ac73e0e4dfbc1697a3e24454341ebd880d2391d369fe20868f9434-image.png" />
</Frame>

You’ll use this `.cer` file in the next section to create your `.p12` certificate.

***

## Create a private key and export the .p12 certificate

1. **Double-click** the downloaded `.cer` file to import it into **Keychain Access**.

2. In Keychain Access, navigate to:

   * **Keychains > Login**
   * **Category > My Certificates**

3. Locate the certificate named **Apple Push Services**.

4. **Right-click** the certificate and select **Export**.

<Frame caption="Export will generate a .p12 file at your desired file location">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a8aae38ea4755020f4695ddd6fd2ccfc0e0bd8d262414665467f973d3ed90912-image.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=ce1453c325f0ad6790754f25a7a1a506" alt="Keychain Access right-click menu showing Export option for Apple Push Services certificate" width="960" height="720" data-path="images/docs/a8aae38ea4755020f4695ddd6fd2ccfc0e0bd8d262414665467f973d3ed90912-image.png" />
</Frame>

1. Choose a location to save the file, and select the file format as **`.p12`**.

2. When prompted, set a **password** for the `.p12` file. You will need this password when uploading to OneSignal.

<Frame>
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/070cbc6d0197377e3805cf23e92bf9d876efdb1754e9c233db8bde453cc7dcd4-Screenshot_2025-04-16_at_2.10.17_PM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=58e96cbb675ff90014c37e7fd1852975" alt="Save dialog showing .p12 file format selection and password prompt" width="918" height="558" data-path="images/docs/070cbc6d0197377e3805cf23e92bf9d876efdb1754e9c233db8bde453cc7dcd4-Screenshot_2025-04-16_at_2.10.17_PM.png" />
</Frame>

***

## Upload the .p12 to OneSignal

1. In your [OneSignal dashboard](https://onesignal.com), go to your app > **Settings > Push & In-App > Apple iOS**.
2. Upload the `.p12` file (and enter the password if you set one). Click **Save**.

<Check>
  You’ve successfully set up **APNs authentication using a .p12 certificate** in OneSignal.

  Your iOS app is now ready to send and receive push notifications! 🎉
</Check>

***

## .p12 troubleshooting

### Invalid certificate format error

**Cause:** The uploaded file is not in `.p12` format.

**Fix:** Ensure you export the certificate from Keychain Access **as `.p12`** (not `.cer` or `.pem`).

### "Incorrect password" when uploading to OneSignal

**Cause:** Password was entered incorrectly or not set.

**Fix:**

* Try exporting again and set a **new password**.
* Ensure no extra spaces are added when pasting.
* If using Provisionator, the password is shown in the UI.

### Missing private key in exported file

**Cause:** Certificate was imported but not paired with a private key.

**Fix:**

* Make sure you **generate the CSR** from Keychain Access on the same machine.
* After downloading the `.cer` file, double-click to install and check if the key appears under **My Certificates**.

### Push notifications not working after upload

**Cause:** Incorrect App ID, or Provisioning Profile missing capabilities.

**Fix:**

* Confirm the `.p12` matches the **App ID** used in the app.
* In Apple Developer Portal, ensure the App ID has **Push Notifications enabled**.
* Make sure the Provisioning Profile includes **Push**.

### Expired certificate

**Cause:** `.p12` certificate is no longer valid.

**Fix:**

* Go to Apple Developer > Certificates and check expiry.
* Revoke the old certificate and create a new one.

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

### When does my .p12 certificate expire, and how do I renew it?

.p12 certificates expire **one year** after creation. To renew, generate a new CSR, create a new push certificate in Apple Developer, export it as .p12, and re-upload it to your OneSignal dashboard. Set a calendar reminder to avoid disruption. Alternatively, switch to a [.p8 key](./ios-p8-token-based-connection-to-apns), which does not expire.

### Should I use .p8 or .p12?

OneSignal recommends **.p8 keys** for most apps. A .p8 key does not expire, works across all apps under your Apple Developer account, and is simpler to manage. A .p12 certificate is app-specific and must be renewed annually. See the [.p8 key guide](./ios-p8-token-based-connection-to-apns) for setup instructions.

### Do I need a provisioning profile, and how do I create one?

Yes, Apple requires different types of profiles for development, testing (Ad Hoc), and distribution to the App Store.

In Xcode, select **Automatically manage signing** to create one automatically.

<Frame>
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/73993224529058ffe5797afc5998c49bd54a64d5dd97cce26479b5f69c0bf46d-Screenshot_2025-04-21_at_4.48.21_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=794544ccd6d05744f053386b2a961c74" alt="Xcode Signing and Capabilities tab with Automatically manage signing enabled" width="2058" height="632" data-path="images/docs/73993224529058ffe5797afc5998c49bd54a64d5dd97cce26479b5f69c0bf46d-Screenshot_2025-04-21_at_4.48.21_PM.png" />
</Frame>

Otherwise, see [Apple's docs on provisioning profiles](https://developer.apple.com/help/account/provisioning-profiles/provisioning-profile-updates) for details.

***

Built with [Mintlify](https://mintlify.com).

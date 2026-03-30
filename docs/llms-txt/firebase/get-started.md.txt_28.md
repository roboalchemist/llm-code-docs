# Source: https://firebase.google.com/docs/in-app-messaging/get-started.md.txt

This quickstart shows you how to set up Firebase In-App Messaging and send your first message.
<button value="ios" default="">iOS+</button> <button value="android">Android</button> <button value="flutter">Flutter</button>

<br />

## Before you begin


Before starting, make sure to [add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).

## Add the Firebase In-App Messaging SDK to your project


Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```

> [!NOTE]
> **Note:** New projects should use the default (latest) SDK version, but you can choose an older version if needed.

3. Choose the In-App Messaging library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. To use In-App Messaging, you must [enable Google Analytics](https://support.google.com/firebase/answer/9289399#linkga) in your Firebase project and add the Firebase SDK for Google Analytics to your app. You can select either the library without IDFA collection or with IDFA collection. See our FAQ on the [latest organization of modules in the Google Analytics for Firebase SDK](https://firebase.google.com/support/faq#analytics-odm2-sdk-refactor-ios).
6. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.

Now, initialize the SDK in your app:

1. Import the Firebase module in your `App` struct or `UIApplicationDelegate`, if you haven't yet:

   ##### Swift

   ```swift
   import Firebase
   ```

   ##### Objective-C

   ```objective-c
   @import Firebase;
   ```
2. Also configure a [`FirebaseApp`](https://firebase.google.com/docs/reference/ios/firebasecore/api/reference/Classes/FIRApp) shared instance, typically in your `App`'s initializer or your app delegate's `application(_:didFinishLaunchingWithOptions:)` method, if you haven't yet:

   ##### Swift

   ```swift
   FirebaseApp.configure()
   ```

   ##### Objective-C

   ```objective-c
   [FIRApp configure];
   ```
3. Compile and run your app.

> [!NOTE]
> **Note:** Firebase In-App Messaging requires Firebase version 5.6.0 or higher. If you're having trouble compiling your app, try running `pod update` in your app's project directory. Keep in mind, though, that the command updates all of your app's dependencies, not just Firebase ones.

<br />

## Send a test message

### Get your app's installation ID

To conserve power, Firebase In-App Messaging only retrieves messages from the
server once per day. That can make testing difficult, so the
Firebase console allows you to specify a test device that displays messages
on demand.


That testing device is determined by a Firebase installation ID provided by the
Firebase installations service. To find your testing app's installation ID, run the app with the
runtime command argument `-FIRDebugEnabled`:

1. With your Xcode project open, select **Product \> Scheme \> Edit scheme...** from the top menu bar.
2. Open the **Arguments** tab of the dialog that pops up.
3. Click **+ Add items** under **Arguments Passed On Launch**.
4. Enter "-FIRDebugEnabled" in the newly-created field.
5. Click **Close**, then run your app.

Once your app starts running, look for the following line in the Xcode console's logs:

```
[Firebase/InAppMessaging][I-IAM180017] Starting InAppMessaging runtime with Firebase Installation ID YOUR_INSTALLATION_ID
```

<br />

### Send a message to your testing device

Once you've launched your app on the testing device and you have its
Firebase installation ID (FID), you can try out your Firebase In-App Messaging
setup by sending a test message:

1. In the Firebase console, open the [Messaging page](https://console.firebase.google.com/project/_/messaging/).
2. If this is your first campaign, click **Create your first campaign** .
   1. Select **Firebase In-App messages** and click **Create**.
3. Otherwise, on the **Campaigns** tab, click **New campaign** .
   1. Select **In-App Messaging**.
4. Enter a **Title** for your first message.
5. Click **Test on Device**
6. Enter your app's Firebase installation ID in the **Add an installation ID** field.
7. Click **Test** to send the message.

Firebase In-App Messaging sends your test message as soon as you click **Test**. To see the
message, you need to close, then reopen the app on your testing device.

To confirm whether your device is a test device, look for the following
log message:

```
[Firebase/InAppMessaging][I-IAM180017] Seeing test message in fetch response. Turn the current instance into a testing instance.
```
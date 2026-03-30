# Source: https://documentation.onesignal.com/docs/en/flutter-sdk-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flutter SDK setup

> Instructions for adding the OneSignal Flutter SDK to your Flutter app for iOS and Android

export const SdkReleasesIframe = ({sdkFilter = undefined, viewMode = undefined, height, ...frameProps}) => {
  const baseUrl = 'https://onesignal.github.io/sdk-releases';
  const buildUrl = (theme, sdkFilter, viewMode) => {
    const url = new URL(baseUrl);
    const params = new URLSearchParams();
    if (theme) {
      params.set('theme', theme);
    }
    if (sdkFilter) {
      params.set('sdk', sdkFilter);
    }
    if (viewMode) {
      params.set('viewMode', viewMode);
    }
    if (params.toString()) {
      url.search = params.toString();
    }
    return url.toString();
  };
  const detectTheme = () => {
    if (document.documentElement.classList.contains('dark')) {
      return 'dark';
    }
    return 'light';
  };
  const [theme, setTheme] = useState('light');
  const [iframeSrc, setIframeSrc] = useState(() => {
    const initialTheme = detectTheme();
    return buildUrl(initialTheme, sdkFilter, viewMode);
  });
  useEffect(() => {
    const currentTheme = detectTheme();
    setTheme(currentTheme);
    setIframeSrc(buildUrl(currentTheme, sdkFilter, viewMode));
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const handleThemeChange = () => {
      const newTheme = detectTheme();
      setTheme(newTheme);
      setIframeSrc(buildUrl(newTheme, sdkFilter, viewMode));
    };
    if (mediaQuery.addEventListener) {
      mediaQuery.addEventListener('change', handleThemeChange);
    } else {
      mediaQuery.addListener(handleThemeChange);
    }
    window.addEventListener('storage', handleThemeChange);
    const observer = new MutationObserver(handleThemeChange);
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class', 'data-theme']
    });
    return () => {
      if (mediaQuery.removeEventListener) {
        mediaQuery.removeEventListener('change', handleThemeChange);
      } else {
        mediaQuery.removeListener(handleThemeChange);
      }
      window.removeEventListener('storage', handleThemeChange);
      observer.disconnect();
    };
  }, [sdkFilter, viewMode]);
  const getIframeHeight = () => {
    if (viewMode === 'table') {
      return '450';
    }
    if (viewMode === 'mini') {
      return '170';
    }
    return '800';
  };
  const iframeHeight = height || getIframeHeight();
  return <Frame {...frameProps}>
      <iframe src={iframeSrc} width="100%" height={iframeHeight} frameBorder="0" style={{
    border: "none"
  }} title="SDK Releases" key={iframeSrc} />
    </Frame>;
};

<SdkReleasesIframe sdkFilter="flutter" viewMode="mini" />

## Overview

This guide explains how to integrate OneSignal push notifications into a Flutter application. It covers everything from installation to configuration and service worker management.

### Requirements

* Flutter 3.29.0+
* Configured OneSignal app and platform

**iOS Requirements**

* macOS with Xcode 14+ (setup instructions use Xcode 16.2)
* Device with iOS 12+, iPadOS 12+, or Xcode simulator running iOS 16.2+
* CocoaPods 1.16.2+

**Android Requirements**

* Android 7.0+ device or emulator with Google Play Store (Services) installed

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

## SDK setup

### 1. Add SDK

Add the `onesignal_flutter` package to your `pubspec.yaml` file under `dependencies`:

```yaml pubspec.yaml theme={null}
  dependencies:
   onesignal_flutter: ^5.1.2
```

Run `flutter pub get` to install the SDK.

### 2. Initialize SDK

In your `main.dart` file initialize OneSignal in your App's root component with the provided methods.

Replace `YOUR_APP_ID` with your OneSignal App ID found in your OneSignal dashboard **Settings > [Keys & IDs](./keys-and-ids)**.

<Note>
  If you don't have access to the OneSignal app, ask your [Team Members](./manage-team-members) to invite you.
</Note>

```javascript main.dart theme={null}
// Include the OneSignal package
import 'package:onesignal_flutter/onesignal_flutter.dart';

void main() {
  runApp(const MyApp());

  // Enable verbose logging for debugging (remove in production)
  OneSignal.Debug.setLogLevel(OSLogLevel.verbose);
  // Initialize with your OneSignal App ID
  OneSignal.initialize("YOUR_APP_ID");
  // Use this method to prompt for push notifications.
  // We recommend removing this method after testing and instead use In-App Messages to prompt for notification permission.
  OneSignal.Notifications.requestPermission(false);

}
```

<Warning>
  When implementing the [Push Notification Click Listener](./mobile-sdk-reference#push-notification-events), if the app is force-closed and you click a notification, the app will not open and the Click Listener will not register in `Debug` mode. To fix this, you can either:

* Use a release build via flutter e.g. `flutter run --release` (requires a physical device)
* Update the Xcode scheme to be `Release` not `Debug`
</Warning>

***

## Android setup

Make sure your OneSignal app is configured for the Android platform using your [Firebase credentials](/docs/en/android-firebase-credentials).

Set up your [notification icons](/docs/en/notification-icons) to match your app’s branding. If this step is skipped, a default bell icon will display for your push notifications.

**Build for Android**

At this point, you should be able to build and run your app on a physical Android device or emulator without issues.

<Check>
  After confirming that your Android build works:

* Continue with the [iOS setup](#ios-setup), if applicable.
* Or jump ahead to [Testing the OneSignal SDK integration](#testing-the-onesignal-sdk-integration).
</Check>

***

## iOS setup

Make sure your OneSignal app is configured for the iOS platform using either the [p8 Token (Recommended)](/docs/en/ios-p8-token-based-connection-to-apns) or [p12 Certificate](/docs/en/ios-p12-generate-certificates).

Follow these steps to add push notifications to your iOS app, including support for [Badges](/docs/en/badges), [Confirmed Delivery](/docs/en/confirmed-delivery), and images.

### 1. Add Push Notifications capability to app target

The [Push Notifications capability](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns#Enable-the-push-notifications-capability) allows your app to register a push token and receive notifications.

1. Open your app’s `.xcworkspace` file in Xcode.
2. Select **your app target > Signing & Capabilities**
3. Click **+ Capability** and add **Push Notifications** capability

<Frame caption="The app target is given Push Notifications capability.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c44118529490f1a7a1245a4c1e8b525d9eb23ab430f035b26b426889fc0486b6-382d57ff7ce1023a863da9f18a97b9a643b1e4b172ec02f1b6661160c362d827-Screenshot_2025-03-10_at_11.19.03_AM.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=e4475a29ab479ec1bd151c809bebd26a" width="2436" height="1324" data-path="images/docs/c44118529490f1a7a1245a4c1e8b525d9eb23ab430f035b26b426889fc0486b6-382d57ff7ce1023a863da9f18a97b9a643b1e4b172ec02f1b6661160c362d827-Screenshot_2025-03-10_at_11.19.03_AM.png" />
</Frame>

### 2. Add Background Modes capability to app target

This enables your app to wake in the background when push notifications arrive.

1. Add [Background Modes](https://developer.apple.com/documentation/usernotifications/pushing-background-updates-to-your-app) capability
2. Enable **Remote notifications**

<Frame caption="The app target is given Remote Notifications background execution mode.">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/498bd555602023bd8f3ba8e7ee58c8f58eb260accd2f941f64e3e5de07ad99d8-Screenshot_2025-03-10_at_11.20.58_AM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=79995d23ebbcb67d6a2bd0412259f8c0" width="2436" height="1324" data-path="images/docs/498bd555602023bd8f3ba8e7ee58c8f58eb260accd2f941f64e3e5de07ad99d8-Screenshot_2025-03-10_at_11.20.58_AM.png" />
</Frame>

### 3. Add app target to App Group

[App Groups](https://developer.apple.com/documentation/xcode/configuring-app-groups/#Create-App-Groups-for-all-other-platforms) allow data sharing between your app and the Notification Service Extension. Required for Confirmed Delivery and Badges.

<Tabs>
  <Tab title="If you do NOT have an App Group configured">
    1. Add **App Groups** capability
    2. In the App Groups capability click **+**
    3. Add a new container ID in format: `group.your_bundle_id.onesignal`

    * Keep **group.** and **.onesignal** prefix and suffix. Replace **`your_bundle_id`** with your app's bundle identifier.
    * For example, bundle identifier `com.onesignal.MyApp`, will have the container name `group.com.onesignal.MyApp.onesignal`.

    <Frame caption="The app target is part of the App Group.">
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/34e545ae24b0fbdf043fd587102f7039cd1daf65777e84690946f4fb20f739aa-Screenshot_2025-03-10_at_11.22.52_AM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=5904f8a6dd4030f5ee7cfa82b3c3eeb8" width="2436" height="1324" data-path="images/docs/34e545ae24b0fbdf043fd587102f7039cd1daf65777e84690946f4fb20f739aa-Screenshot_2025-03-10_at_11.22.52_AM.png" />
    </Frame>

    <Warning> Your App Group name must exactly match your bundle ID’s spelling and capitalization across all targets. </Warning>
  </Tab>

  <Tab title="If you DO have an App Group">
    1. Open your **App Target** and **OneSignalNotificationServiceExtension Target's** `Info.plist`
    2. Add a new property to the `Info.plist` for both targets:

    * **Key:** `OneSignal_app_groups_key`
    * **Value:** Your existing App Group name (e.g., `group.your-custom-group-id`)

    ```xml XML theme={null}
    <key>OneSignal_app_groups_key</key>
    <string>group.your-custom-group-id</string>
    ```

    <Frame caption="Custom app group set inside the app target.">
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/aa3a061cbf89856a5ee75737e24a3dc7b36e96a866d277e68a170f136cbeae48-Screenshot_2025-03-10_at_11.24.56_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=84e93061a8c82c1ca44cc14b81995d46" width="2788" height="1400" data-path="images/docs/aa3a061cbf89856a5ee75737e24a3dc7b36e96a866d277e68a170f136cbeae48-Screenshot_2025-03-10_at_11.24.56_AM.png" />
    </Frame>

    <Warning>
      Make sure to update the `OneSignal_app_groups_key` in **both** the App Target **and** OneSignalNotificationServiceExtension Target's `Info.plist`!
    </Warning>
  </Tab>
</Tabs>

### 4. Add Notification Service Extension

The [Notification Service Extension (NSE)](https://developer.apple.com/documentation/usernotifications/modifying-content-in-newly-delivered-notifications) enables rich notifications and Confirmed Delivery analytics.

1. In Xcode: **File > New > Target...**
2. Select **Notification Service Extension**, then **Next**.
3. Set the product name to `OneSignalNotificationServiceExtension` and press **Finish**.
4. Press **Don't Activate** on the Activate scheme prompt.

<Frame caption="Select the Notification Service Extension target.">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3ba0018a789c52c5c8d2f485d31e0ba0e07398d7abf5980215e4d4d2a2e0e948-Screenshot_2025-03-10_at_11.27.24_AM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=c5c5399c449ec5201dfb3342f9eeb538" width="2788" height="1400" data-path="images/docs/3ba0018a789c52c5c8d2f485d31e0ba0e07398d7abf5980215e4d4d2a2e0e948-Screenshot_2025-03-10_at_11.27.24_AM.png" />
</Frame>

<Frame caption="Name the Notification Service Extension .">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/afb3452c5ef95511c7ca4ef50c36ea2e5c205030c35d7ea066270a40f9ec3234-Screenshot_2025-03-10_at_11.27.47_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=ed78140e080cf8aad1e727d819bac8ad" width="2788" height="1400" data-path="images/docs/afb3452c5ef95511c7ca4ef50c36ea2e5c205030c35d7ea066270a40f9ec3234-Screenshot_2025-03-10_at_11.27.47_AM.png" />
</Frame>

<Frame caption="Cancel activation to continue debugging your app target.">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/cfc756b0273e5973af42a4a2933f3efcb5c4aeaf7ca5cec6bd196e8c01250f62-Screenshot_2025-03-10_at_11.28.01_AM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=03f43bf27f643419eba14e438f3f07a1" width="2788" height="1400" data-path="images/docs/cfc756b0273e5973af42a4a2933f3efcb5c4aeaf7ca5cec6bd196e8c01250f62-Screenshot_2025-03-10_at_11.28.01_AM.png" />
</Frame>

Set the OneSignalNotificationServiceExtension **Minimum Deployment Target** to match your main app (iOS 15+ recommended).

<Info> If you're using CocoaPods, set the deployment version in your Podfile as well. </Info>

<Frame caption="Set the same deployment target as the main app.">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/17cc605c99d890e50e83e45bfbe89ce5c7b226b6b000b9aa739d70a1bf41c231-Screenshot_2025-03-10_at_11.29.35_AM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=48f72f24a321d60e6623b440b591987a" width="2788" height="1400" data-path="images/docs/17cc605c99d890e50e83e45bfbe89ce5c7b226b6b000b9aa739d70a1bf41c231-Screenshot_2025-03-10_at_11.29.35_AM.png" />
</Frame>

### 5. Add NSE target to app group

Use the same App Group ID you added in step 3.

1. Go to **OneSignalNotificationServiceExtension > Signing & Capabilities**
2. Add **App Groups**
3. Add the exact same group ID

<Warning>
  If you are using a custom App Group name and not `group.your_bundle_id.onesignal` then make sure to add your App Group ID to both the App Target and OneSignalNotificationServiceExtension Target's `Info.plist`! See [step 3](#3-add-app-target-to-app-group) for more information.
</Warning>

<Frame caption="The NSE now belongs to the same app group as your app target.">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/e763a62e9ab8457d16fbb9a2c1f9344bb73a5a5d40fa920bbba18e040128a229-Screenshot_2025-03-10_at_11.30.24_AM.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=096adcb29f4d4d61bf51a0b9caed695d" width="2788" height="1400" data-path="images/docs/e763a62e9ab8457d16fbb9a2c1f9344bb73a5a5d40fa920bbba18e040128a229-Screenshot_2025-03-10_at_11.30.24_AM.png" />
</Frame>

### 6. Update NSE code

1. Navigate to the **OneSignalNotificationServiceExtension** folder
2. Replace the contents of the `NotificationService.swift` or `NotificationService.m` file with the following:

<Frame caption="Navigate to your NotificationService file.">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/ab43a237c660116a9547fe9b53ab2594181f6c04297b5a7236d21764122d26b3-Screenshot_2025-03-10_at_11.31.52_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=917ea1a94b0485f5f14d3fe8d28886d4" width="2788" height="1400" data-path="images/docs/ab43a237c660116a9547fe9b53ab2594181f6c04297b5a7236d21764122d26b3-Screenshot_2025-03-10_at_11.31.52_AM.png" />
</Frame>

<CodeGroup>
  ```swift Swift theme={null}
  import UserNotifications
  import OneSignalExtension

  class NotificationService: UNNotificationServiceExtension {
      var contentHandler: ((UNNotificationContent) -> Void)?
      var receivedRequest: UNNotificationRequest!
      var bestAttemptContent: UNMutableNotificationContent?

      // Note this extension only runs when `mutable_content` is set
      // Setting an attachment or action buttons automatically sets the property to true
      override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
          self.receivedRequest = request
          self.contentHandler = contentHandler
          self.bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)

          if let bestAttemptContent = bestAttemptContent {
              // DEBUGGING: Uncomment the 2 lines below to check this extension is executing
  //            print("Running NotificationServiceExtension")
  //            bestAttemptContent.body = "[Modified] " + bestAttemptContent.body

              OneSignalExtension.didReceiveNotificationExtensionRequest(self.receivedRequest, with: bestAttemptContent, withContentHandler: self.contentHandler)
          }
      }

      override func serviceExtensionTimeWillExpire() {
          // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.
          if let contentHandler = contentHandler, let bestAttemptContent =  bestAttemptContent {
              OneSignalExtension.serviceExtensionTimeWillExpireRequest(self.receivedRequest, with: self.bestAttemptContent)
              contentHandler(bestAttemptContent)
          }
      }
  }

  ```

  ```objectivec Objective-C theme={null}
  #import <OneSignalExtension/OneSignalExtension.h>
  #import "NotificationService.h"

  @interface NotificationService ()

  @property (nonatomic, strong) void (^contentHandler)(UNNotificationContent *contentToDeliver);
  @property (nonatomic, strong) UNNotificationRequest *receivedRequest;
  @property (nonatomic, strong) UNMutableNotificationContent *bestAttemptContent;

  @end

  @implementation NotificationService

  // Note, this extension only runs when mutable-content is set
  // Setting an attachment or action buttons automatically adds this
  - (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {
      self.receivedRequest = request;
      self.contentHandler = contentHandler;
      self.bestAttemptContent = [request.content mutableCopy];

      // DEBUGGING: Uncomment the 2 lines below and comment out the one above to ensure this extension is executing
  //     NSLog(@"Running NotificationServiceExtension");
  //     self.bestAttemptContent.body = [@"[Modified] " stringByAppendingString:self.bestAttemptContent.body];

      [OneSignalExtension didReceiveNotificationExtensionRequest:self.receivedRequest
                         withMutableNotificationContent:self.bestAttemptContent
                                     withContentHandler:self.contentHandler];
  }

  - (void)serviceExtensionTimeWillExpire {
      // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.

      [OneSignalExtension serviceExtensionTimeWillExpireRequest:self.receivedRequest withMutableNotificationContent:self.bestAttemptContent];

      self.contentHandler(self.bestAttemptContent);
  }

  @end
  ```

</CodeGroup>

You should see an error because the OneSignal package is not installed. This will be resolved in the next step.

<Frame caption="This file shows an error until you install the package in the next step.">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d3d8900d922b3bcaa44c0012e152ca233404d4c80d8bd427792c456aab798d06-Screenshot_2025-03-10_at_11.32.12_AM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=11c4114e117cb74099d9a063d6d11ebc" width="2788" height="1400" data-path="images/docs/d3d8900d922b3bcaa44c0012e152ca233404d4c80d8bd427792c456aab798d06-Screenshot_2025-03-10_at_11.32.12_AM.png" />
</Frame>

### 7. Add OneSignal to the NSE target

Update your `ios/Podfile` to include:

<CodeGroup>
  ```ruby Podfile theme={null}
  target 'OneSignalNotificationServiceExtension' do
    pod 'OneSignalXCFramework', '>= 5.0.0', '< 6.0'
  end
  ```

  ```ruby Example theme={null}
  target 'MyApp' do
    config = use_native_modules!

    use_react_native!(
      :path => config[:reactNativePath],
      # An absolute path to your application root.
      :app_path => "#{Pod::Config.instance.installation_root}/.."
    )

    post_install do |installer|
      # https://github.com/facebook/react-native/blob/main/packages/react-native/scripts/react_native_pods.rb#L197-L202
      react_native_post_install(
        installer,
        config[:reactNativePath],
        :mac_catalyst_enabled => false,
        # :ccache_enabled => true
      )
    end
  end

  target 'OneSignalNotificationServiceExtension' do
    pod 'OneSignalXCFramework', '>= 5.0.0', '< 6.0'
  end
  ```

</CodeGroup>

Open your project in the terminal and run:

```shell shell  theme={null}
cd ios pod install cd .. 
```

#### Common pod install errors

You may run into the following errors, here is how you can resolve them.

<Accordion
  title="ArgumentError - \[Xcodeproj] Unable to find compatibility version string for
object version `70`."
>
  CocoaPods relies on the `xcodeproj` Ruby gem to read your Xcode project files. As of now, the latest `xcodeproj` release does not recognize object version 70, which was introduced by Xcode 16. So when CocoaPods tries to open your `.xcodeproj` file, it crashes with this error.

  1. Close Xcode.
  2. Navigate to your project's `ios/<your-app>.xcodeproj/project.pbxproj` file.
  3. Change this line: `objectVersion = 70;`
  4. Replace it with: `objectVersion = 55;`
  5. Save, close, and rerun `cd ios pod install cd ..`
</Accordion>

### Build for iOS

You should now be able to build and run your app on a real iOS device or iOS simulator (16.2+).

#### Common iOS build errors

<Accordion title="commandPhaseScript Execution exited with a non-zero code">
  1. Delete your Podfile.lock
  2. Delete your Pods folder
  3. Delete your .xcworkspace
  4. Pod install
  5. Cmd + Shift + K to Clean the build and then retry building

  If these steps do not resolve the error, build directly from the Xcode, then find the build error in the report navigator pictured below.

  <img src="https://mintcdn.com/onesignal/OghcODXOQUjR-yOB/images/mobile/report_navigator.png?fit=max&auto=format&n=OghcODXOQUjR-yOB&q=85&s=8338a61a067603962102e3de0987e415" width="2460" height="488" data-path="images/mobile/report_navigator.png" />
</Accordion>

<Accordion title="Cycle Inside... building could produce unreliable results.">
  You may see this error when building with Xcode 15+, due to a default configuration change affecting cross platform systems.

  1. Open your `.xcworkspace` folder in Xcode and navigate to **your app target > Build Phases**.
  2. You should have a phase called **"Embed Foundation Extensions"** or **"Embed App Extensions"**.
  3. Drag and move this build phase to *above* **"Run Script"**.
  4. Build and run your app. The error should be resolved.

  <Frame caption="Correct order of Build Phases in Xcode.">
    <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/347d494eab3ea84c977d5785d16c1602d25204c9333b1ec1166c520d004a87d6-Screenshot_2025-03-06_at_4.23.01_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=279facba4338900c1d123934bf2eb2e6" width="2708" height="1486" data-path="images/docs/347d494eab3ea84c977d5785d16c1602d25204c9333b1ec1166c520d004a87d6-Screenshot_2025-03-06_at_4.23.01_PM.png" />
  </Frame>

  <Frame caption="Uncheck Copy only when installing.">
    <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/f7ef57730ef4aba1d669c8c6efac6be2a18c3035564c658967e7cf2e50708933-Screenshot_2025-03-06_at_4.29.29_PM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=7175d9f2c5819343c58b60045e40358d" width="2620" height="1398" data-path="images/docs/f7ef57730ef4aba1d669c8c6efac6be2a18c3035564c658967e7cf2e50708933-Screenshot_2025-03-06_at_4.29.29_PM.png" />
  </Frame>
</Accordion>

<Accordion title="PBXGroup Error">
  <Info>
    RuntimeError - `PBXGroup` attempted to initialize an object with unknown ISA `PBXFileSystemSynchronizedRootGroup` from attributes: `{"isa"=>"...", "exceptions"=>["//", "..."], "explicitFileTypes"=>{}, "explicitFolders"=>[], "path"=>"OneSignalNotificationServiceExtension", "sourceTree"=>"<group>"}`
  </Info>

  Fix:

  1. Find the folder listed under "path" in the error
  2. In Xcode project sidebar, right-click the folder
  3. Select **Convert to Group**

  <Frame caption="Path error for PBXGroup.">
    <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/92100ba09cde1f8de53dae773dca16847c7e1c6329bc9f4172331f2bc2191592-16c6fb188242f0e43237a0da47c6a2a9.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=6fea922df9bca81d0ca5d3d7b346f07a" width="659" height="216" data-path="images/docs/92100ba09cde1f8de53dae773dca16847c7e1c6329bc9f4172331f2bc2191592-16c6fb188242f0e43237a0da47c6a2a9.png" />
  </Frame>

  <br />

  <Frame caption="Convert folder to group.">
    <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b90d34ba26c94f437fd553514647fc4024ec42301ad2798eba7faec695974720-d46625820efed3f9dbca1e223ac0797f.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=5034133ed9e06897abe672a62ff94913" width="483" height="364" data-path="images/docs/b90d34ba26c94f437fd553514647fc4024ec42301ad2798eba7faec695974720-d46625820efed3f9dbca1e223ac0797f.png" />
  </Frame>
</Accordion>

<Check>
  After confirming that your iOS build works, continue with [Testing the OneSignal SDK integration](#testing-the-onesignal-sdk-integration).
</Check>

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

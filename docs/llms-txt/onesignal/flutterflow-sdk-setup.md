# Source: https://documentation.onesignal.com/docs/en/flutterflow-sdk-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flutterflow SDK setup

> Instructions for adding the OneSignal Flutter SDK to your Flutterflow app for iOS and Android

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

This guide is for Flutterflow mobile app setup. If you have a Flutterflow site, please see our [Web SDK setup](./web-sdk-setup) guide.

## Requirements

* Flutterflow plan: Standard or higher
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

## Setup

### 1. Create a new custom action

In your Flutterflow project, navigate to Custom Code, then click the +Add button and select Action.

<Frame>
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f6a30014959335e895c0b3ce51eb78ea3dbae10a092461df7b390fe9862e43d3-Screenshot_2024-09-09_at_16.30.54.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=449ba1ba0cc5255a75876ed041baf6ab" width="440" height="654" data-path="images/docs/f6a30014959335e895c0b3ce51eb78ea3dbae10a092461df7b390fe9862e43d3-Screenshot_2024-09-09_at_16.30.54.png" />
</Frame>

Under Action settings on the right-hand toolbar, click Add Dependency and enter the following dependency and click refresh to add it to the action:

```yaml dependency theme={null}
  dependencies:
   onesignal_flutter: ^5.1.2
```

<Frame>
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/cc2adb5fd282176c331cd6684ccc4afcec48c9e6d1d5c172f79196b19beb2c05-Screenshot_2024-09-09_at_16.30.18.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=a16a21ea7f62669dc8498b246b53dfde" width="341" height="200" data-path="images/docs/cc2adb5fd282176c331cd6684ccc4afcec48c9e6d1d5c172f79196b19beb2c05-Screenshot_2024-09-09_at_16.30.18.png" />
</Frame>

In the Action Code, under the pre-loaded code add the following, then save and compile your action.

Replace `YOUR_APP_ID` with your OneSignal App ID found in your OneSignal dashboard **Settings > [Keys & IDs](./keys-and-ids)**.

<Note>
  If you don't have access to the OneSignal app, ask your [Team Members](./manage-team-members) to invite you.
</Note>

```javascript Flutter theme={null}
  import 'package:onesignal_flutter/onesignal_flutter.dart';

  Future onesignal() async {
    //Remove this method to stop OneSignal Debugging
    OneSignal.Debug.setLogLevel(OSLogLevel.verbose);

    OneSignal.initialize("YOUR_APP_ID");

    // The promptForPushNotificationsWithUserResponse function will show the iOS or Android push notification prompt. We recommend removing the following code and instead using an In-App Message to prompt for notification permission
    OneSignal.Notifications.requestPermission(true);
  }
```

Next, click on the main.dart file in the left-hand tool bar and click the + icon next to Initial Actions in the right-hand bar and click on the `onesignal` action that has just been created.

<Frame>
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/61ef594d0a96baa53c5d0eebb714b1c823dfe2bd31233fa8be75f6a98d1dc79e-Screenshot_2024-09-09_at_16.34.14.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=b98847b383abbaaa876f4f30f372a9bc" width="330" height="106" data-path="images/docs/61ef594d0a96baa53c5d0eebb714b1c823dfe2bd31233fa8be75f6a98d1dc79e-Screenshot_2024-09-09_at_16.34.14.png" />
</Frame>

This will add the action to you app and cause the OneSignal SDK to be initialised when the app runs:

<Frame>
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/88c1ee61db6558d018470de2af99705b96b0fc65fe712bcca4e5de552db10aa7-Screenshot_2024-09-09_at_16.34.59.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=4b15b27f21ca97473009b36b8988824b" width="391" height="63" data-path="images/docs/88c1ee61db6558d018470de2af99705b96b0fc65fe712bcca4e5de552db10aa7-Screenshot_2024-09-09_at_16.34.59.png" />
</Frame>

### 2. Exporting the project

<Tabs>
  <Tab title="APK download (Android only)">
    Open the Developer Menu and download the APK:

    <Frame>
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3df0cad35728b0e828b3465cd3e46556336e35af2afaf646ed2718c33cb10eff-Screenshot_2024-09-16_at_10.38.32.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=555bc4c195596f26147ed6eb23caedb3" width="910" height="810" data-path="images/docs/3df0cad35728b0e828b3465cd3e46556336e35af2afaf646ed2718c33cb10eff-Screenshot_2024-09-16_at_10.38.32.png" />
    </Frame>

    Once the APK has downloaded, you can test the app by dragging the APK into an Android emulator to install it. Push capabilities should work immediately and you can send push notifications to the device as soon as you provide push permissions through the native prompt.
  </Tab>

  <Tab title="Full project download (iOS and Android)">
    Open the Developer Menu and download the project code:

    <Frame>
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3a262e0407e7a9d37b5ee7fafeb4eef52432b4152973ac4964493d2f1be0c472-Screenshot_2024-09-16_at_10.47.18.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=6145a1a5780183a4e8a96ba9f194d269" width="856" height="798" data-path="images/docs/3a262e0407e7a9d37b5ee7fafeb4eef52432b4152973ac4964493d2f1be0c472-Screenshot_2024-09-16_at_10.47.18.png" />
    </Frame>
  </Tab>
</Tabs>

### 3. iOS Setup

The downloaded project will likely not be ready to launch in iOS. Before setting up the OneSignal specific additions, you will need to make sure that the project is fully built. To do so:

* Open up a Terminal window, cd (change directory) to the `ios` folder of your downloaded project.
* In Terminal type `flutter build ios`and press enter. Wait for the build to complete, this may take some time depending on the size of your project.
* Still in Terminal type `pod install` and press enter. Wait for the pod install to complete.

Open the `.xcworkspace` file in Xcode located your project's ios folder.

Select the **root project > your main app target > Signing & Capabilities**.

If you do not see Push Notifications enabled, click **+ Capability** and add **Push Notifications**. Ensure that you enter the correct details for your Team and Bundle Identifier.

<Frame>
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/82b4cec-1.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=d21289daf4e3311536bfc364d7527f7d" width="2284" height="1120" data-path="images/docs/82b4cec-1.png" />
</Frame>

Click **+ Capability** again and add **Background Modes**. Then check **Remote notifications**.

<Frame>
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2269f7e-2.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=976c5bc914e9a89da5cd8bbc49bf6cca" width="2300" height="1306" data-path="images/docs/2269f7e-2.png" />
</Frame>

#### Add Notification Service Extension

The OneSignalNotificationServiceExtension allows your iOS application to receive rich notifications with images, buttons, and badges. It's also required for OneSignal's Confirmed Delivery analytics features.

In Xcode Select **File > New > Target...**

Select **Notification Service Extension** then **Next**.

<Frame>
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6eb36bd-73ca2a9-1.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=e00c22fe2866135fdfd3267b63e2b580" width="1470" height="1052" data-path="images/docs/6eb36bd-73ca2a9-1.png" />
</Frame>

Enter the product name as `OneSignalNotificationServiceExtension` and press **Finish**.

<Frame>
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/854f36b-Screenshot_2023-12-26_at_9.19.02_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=b622e02e68381234bed7a87668a17b81" width="1314" height="937" data-path="images/docs/854f36b-Screenshot_2023-12-26_at_9.19.02_PM.png" />
</Frame>

Do not activate the scheme on the dialog that is shown after selecting **Finish**.

Press **Cancel** on the "Activate scheme" prompt.

<Frame caption="By canceling, you keep debugging your app instead of the extension you just created. If you activated by accident, you can switch back to debug your app target near the middle-top next to the device selector.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c59226d-d8186b6-300.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=26f4fd19ea850cbb252cb5bbbbc70b06" width="300" height="420" data-path="images/docs/c59226d-d8186b6-300.png" />
</Frame>

Select the **OneSignalNotificationServiceExtension** target and **General** settings.

Set **Minimum Deployments** to be the **same value as your Main Application Target**. This should be iOS 11 or higher.

<Frame caption="This should be the same value as your Main Application Target.">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b9ac509-flutter-mindeployment.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=923c5bf3f264ad5e3847558ece7c9a13" width="2290" height="1058" data-path="images/docs/b9ac509-flutter-mindeployment.png" />
</Frame>

#### Add App Groups

App Groups allow your app and the OneSignalNotificationServiceExtension to communicate when a notification is received, even if your app is not active. This is required for badges and Confirmed Deliveries.

Select your **Main App Target > Signing & Capabilities > + Capability > App Groups**.

<Frame>
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/ca64b5e-flutter-appgroups1.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=04e88b94d3d6b8382342520cf794b027" width="2288" height="1176" data-path="images/docs/ca64b5e-flutter-appgroups1.png" />
</Frame>

Within **App Groups**, click the **+** button.

Set the App Groups container to be `group.YOUR_BUNDLE_IDENTIFIER.onesignal` where `YOUR_BUNDLE_IDENTIFIER` is the same as your Main Application "Bundle Identifier".

<Frame>
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a51bc81-flutter-appgroups2.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=3918fcab2795fc92ade9da8d48afafb5" width="2284" height="1228" data-path="images/docs/a51bc81-flutter-appgroups2.png" />
</Frame>

Press **OK** and repeat for the OneSignalNotificationServiceExtension Target.

Select the **OneSignalNotificationServiceExtension Target > Signing & Capabilities > + Capability > App Groups**.

<Frame>
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/98c0fa6-flutter-appgroups3.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=a90bf7c7d8c4c4e883b6a1259ab334af" width="2258" height="1272" data-path="images/docs/98c0fa6-flutter-appgroups3.png" />
</Frame>

Within **App Groups**, click the **+** button.

Set the App Groups container to be `group.YOUR_BUNDLE_IDENTIFIER.onesignal` where `YOUR_BUNDLE_IDENTIFIER` is the same as **your Main Application "Bundle Identifier"**.

**DO NOT INCLUDE** `OneSignalNotificationServiceExtension`.

<Frame caption="Do not include OneSignalNotificationServiceExtension">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/273e481-flutter-appgroups4.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=39f0adff48bce5de08f5f86782a2fdc2" width="2276" height="1238" data-path="images/docs/273e481-flutter-appgroups4.png" />
</Frame>

<Accordion title="Optional instructions to setup custom App Group Name">
  This step is only required if you **do not** want to use the default app group name (which is `group.{your_bundle_id}.onesignal`).

  Open your `Info.plist` file and add a new `OneSignal_app_groups_key` as a `String` type.

  Enter the group name you checked in the last step as it's value.

  Make sure to do the same for the `Info.plist` under the `OneSignalNotificationServiceExtension` folder.
</Accordion>

#### Add OneSignal SDK to the OneSignalNotificationServiceExtension

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

At the top of your `Podfile` make sure you have `platform :ios, '11.0'`. - Or a newer iOS version if your app requires it.

<CodeGroup>
  ```Text Podfile theme={null}
  # Uncomment this line to define a global platform for your project
  platform :ios, '11.0'
  ```
</CodeGroup>

Open terminal, `cd` to the `ios` directory, and run `pod install`.

If you see the error below, add `use_frameworks!` to the top of your podfile and try again.

```
- Runner (true) and OneSignalNotificationServiceExtension (false) do not both set use_frameworks!.
```

#### OneSignalNotificationServiceExtension Code

In the Xcode project navigator, select the **OneSignalNotificationServiceExtension folder** and open the `NotificationService.m` or `NotificationService.swift` file.

Replace the whole file's contents with the following code.

<CodeGroup>
  ```swift Swift theme={null}
  import UserNotifications

  import OneSignalExtension

  class NotificationService: UNNotificationServiceExtension {

      var contentHandler: ((UNNotificationContent) -> Void)?
      var receivedRequest: UNNotificationRequest!
      var bestAttemptContent: UNMutableNotificationContent?

      override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
          self.receivedRequest = request
          self.contentHandler = contentHandler
          self.bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)

          if let bestAttemptContent = bestAttemptContent {
              /* DEBUGGING: Uncomment the 2 lines below to check this extension is executing
                            Note, this extension only runs when mutable-content is set
                            Setting an attachment or action buttons automatically adds this */
              // print("Running NotificationServiceExtension")
              // bestAttemptContent.body = "[Modified] " + bestAttemptContent.body

              OneSignalExtension.didReceiveNotificationExtensionRequest(self.receivedRequest, with: bestAttemptContent, withContentHandler: self.contentHandler)
          }
      }

      override func serviceExtensionTimeWillExpire() {
          // Called just before the extension will be terminated by the system.
          // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.
          if let contentHandler = contentHandler, let bestAttemptContent =  bestAttemptContent {
              OneSignalExtension.serviceExtensionTimeWillExpireRequest(self.receivedRequest, with: self.bestAttemptContent)
              contentHandler(bestAttemptContent)
          }
      }
  }

  ```

  ```c objective-c theme={null}
  #import <OneSignalExtension/OneSignalExtension.h>

  #import "NotificationService.h"

  @interface NotificationService ()

  @property (nonatomic, strong) void (^contentHandler)(UNNotificationContent *contentToDeliver);
  @property (nonatomic, strong) UNNotificationRequest *receivedRequest;
  @property (nonatomic, strong) UNMutableNotificationContent *bestAttemptContent;

  @end

  @implementation NotificationService

  - (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {
      self.receivedRequest = request;
      self.contentHandler = contentHandler;
      self.bestAttemptContent = [request.content mutableCopy];

      /* DEBUGGING: Uncomment the 2 lines below and comment out the one above to ensure this extension is executing
                    Note, this extension only runs when mutable-content is set
                    Setting an attachment or action buttons automatically adds this */
      // NSLog(@"Running NotificationServiceExtension");
      // self.bestAttemptContent.body = [@"[Modified] " stringByAppendingString:self.bestAttemptContent.body];

      [OneSignalExtension didReceiveNotificationExtensionRequest:self.receivedRequest
                         withMutableNotificationContent:self.bestAttemptContent
                                     withContentHandler:self.contentHandler];
  }

  - (void)serviceExtensionTimeWillExpire {
      // Called just before the extension will be terminated by the system.
      // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.

      [OneSignalExtension serviceExtensionTimeWillExpireRequest:self.receivedRequest withMutableNotificationContent:self.bestAttemptContent];

      self.contentHandler(self.bestAttemptContent);
  }

  @end
  ```

</CodeGroup>

<Frame caption="Example of the NotificationService.swift file.">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4329841-Image_12-26-23_at_9.50_PM.jpg?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=8d397d1cc8ee523f1372d0146b3a495e" width="2126" height="1104" data-path="images/docs/4329841-Image_12-26-23_at_9.50_PM.jpg" />
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

***

Built with [Mintlify](https://mintlify.com).

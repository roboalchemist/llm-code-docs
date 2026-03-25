# Source: https://documentation.onesignal.com/docs/en/service-extensions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mobile Service Extensions

> Implement the iOS and Android notification service extensions in your app.

## Overview

Notification Service Extensions let you intercept and modify push notifications before it's displayed to the user. This enables:

* Background data handling
* Custom styles (colors, icons, vibration)
* Rich media attachments (images, videos)
* Confirmed delivery/analytics
* Action button options

<Note>
  You can access the data in your push notifications sent from OneSignal via the [OSNotification class](./osnotification-payload)
</Note>

***

## Android Notification Service Extension

Allows you to process the notification before it is shown to the user. Common use cases include:

* Receive data in the background with or without displaying a notification.
* Override specific notification settings depending on client side app logic such as custom accent color, vibration pattern, or other any other `NotificationCompat` options available.

For more details, see [Android's documentation on the NotificationCompat options.](https://developer.android.com/reference/androidx/core/app/NotificationCompat)

### 1. Create a class for the Service Extension

Create a class that extends `INotificationServiceExtension` and implement the `onNotificationReceived` method.

The method `onNotificationReceived` parameter is `event` of type [INotificationReceivedEvent](https://github.com/OneSignal/OneSignal-Android-SDK/blob/25924dc3739fbe3ae64a73efc7b504449a18cdea/OneSignalSDK/onesignal/core/src/main/java/com/onesignal/notifications/INotificationReceivedEvent.kt#L46) .

<CodeGroup>
  ```Java Java theme={null}
  package your.package.name

  import androidx.annotation.Keep;
  import com.onesignal.notifications.IActionButton;
  import com.onesignal.notifications.IDisplayableMutableNotification;
  import com.onesignal.notifications.INotificationReceivedEvent;
  import com.onesignal.notifications.INotificationServiceExtension;

  @Keep // Keep is required to prevent minification from renaming or removing your class
  public class NotificationServiceExtension implements INotificationServiceExtension {

       @Override
       public void onNotificationReceived(INotificationReceivedEvent event) {
          IDisplayableMutableNotification notification = event.getNotification();

          if (notification.getActionButtons() != null) {
             for (IActionButton button : notification.getActionButtons()) {
                // you can modify your action buttons here
             }
          }

       /* Add customizations here. See examples below for additional methods to modify the notification*/
       }
  }

  ```

  ```Kotlin Kotlin theme={null}
  class ExampleServiceExtension: INotificationServiceExtension {
      override fun onNotificationReceived(event: INotificationReceivedEvent) {
         val notification = event.notification
         val context = event.context

         notification.actionButtons?.forEach { button ->
             // You can modify your action buttons here
         }

       /* Add customizations here. See examples below for additional methods to modify the notification*/
  }
  ```

</CodeGroup>

### 2. Example use cases

The following are common examples you can implement in the template Notification Service Extension class above.

<Tabs>
  <Tab title="Prevent notification from displaying">
    <CodeGroup>
      ```Java Java theme={null}
      event.preventDefault();

      //Do some async work, then decide to show or dismiss
      new Thread(() -> {
          try {
              Thread.sleep(1000);
          } catch (InterruptedException ignored) {}

          //Manually show the notification
          event.getNotification().display();
      }).start();
      ```

      ```Kotlin Kotlin theme={null}
      event.preventDefault()

      //Do some async work, then decide to show or dismiss
      Thread{
          try {
              Thread.sleep(1000)
          } catch (ingored: InterruptedException) {}

          //Manually show the notification
          event.notification.display()
      }.start()

      ```
    </CodeGroup>
  </Tab>

  <Tab title="Add a custom field">
    <CodeGroup>
      ```Java Java theme={null}
      String promoCode = notification.getAdditionalData() != null
          ? notification.getAdditionalData().optString("promo_code", null)
          : null;

      if (promoCode != null) {
          String updatedBody = notification.getBody() + " Use code: " + promoCode;
          notification.setExtender(builder -> {
              builder.setContentText(updatedBody);
          });
      }
      ```

      ```Kotlin Kotlin theme={null}
      val promoCode = notification.additionalData?.optString("promo_code", null)

      promoCode?.let {
          val updatedBody = "${notification.body}\nUse code: $promoCode"
          notification.setExtender { builder ->
              builder.setContentText(updatedBody)
          }
      }

      ```
    </CodeGroup>
  </Tab>

  <Tab title="Change the notification color and icon">
    <CodeGroup>
      ```Java Java theme={null}
      //Note that icons referenced here must exist in the res/drawable directory
      int iconResId = R.drawable.icon_default;
      String type = notitifcation.getAdditionalData() != null
          ? notification.getAdditionalData().optString("type", "")
          : "";

      switch (type) {
          case "sale":
              iconResId = R.drawable.icon_sale;
              break;
          case "reminder":
              iconResId = R.drawable.icon_reminder;
              break;
      }

      int finalIconResId = iconResId;
      notification.setExtender(builder -> {
          builder.setColor(0xFF0000FF).setSmallIcon(finalIconResId);
      });

      ```

      ```Kotlin Kotlin theme={null}
      //Note that icons referenced here must exist in the res/drawable directory
      val type = notification.additionalData?.optString("type", "") ?: ""

      val iconResId = when (type) {
      "sale" -> R.drawable.icon_sale
          "reminder" -> R.drawable.icon_reminder
          else -> R.drawable.icon_default
      }

      notification.setExtender { builder ->
          builder.setColor(0xFF0000FF).setSmallIcon(iconResId)
      }

      ```
    </CodeGroup>
  </Tab>
</Tabs>

### 3. Add the Service Extension to your `AndroidManifest.xml`

Add the class name and value as `meta-data` within the `AndroidManifest.xml` file in the application tag. Ignore any "unused" warnings.

```XML XML theme={null}
<application> 
  <!-- Keep android:name as shown, set android:value toyour class fully name spaced-->
  <meta-data 
    android:name="com.onesignal.NotificationServiceExtension"
    android:value="com.onesignal.example.NotificationServiceExtension" />
</application>
```

***

## iOS Notification Service Extension

The [UNNotificationServiceExtension](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension) allows you to modify the content of push notifications before they are displayed to the user and is required for other important features like:

* [Images & Rich Media](./rich-media).
* [Confirmed Delivery](./confirmed-delivery)
* [Badges](./badges)
* [Action Buttons](./action-buttons)
* [Influenced Opens with Firebase Analytics](./google-analytics-for-firebase)

You likely set this up already if you followed our [Mobile SDK setup](./mobile-sdk-setup) instructions for your app, but this section will explain how to access the OneSignal notification payload data and troubleshoot any issues you might be having.

### Getting the iOS push payload

When following the [Mobile SDK setup](./mobile-sdk-setup) you will get to the section on adding the code to the OneSignalNotificationServiceExtension.

In that code, there is the method `OneSignalExtension.didReceiveNotificationExtensionRequest`. This is where we pass the `bestAttemptContent` of the notification to the app before it is displayed to the user. Before this method is called, you can get the notification payload and (if desired) update it before it is displayed to the user.

In this example, we send a notification with the following data:

```json JSON theme={null}
{
  "app_id": "YOUR_APP_ID",
  "target_channel": "push",
  "headings": {"en": "The message title"},
  "contents": {"en": "The message contents"},
  "data":{
    "additional_data_key_1":"value_1",
    "additional_data_key_2":"value_2"
    },
  "include_subscription_ids": ["SUBSCRIPTION_ID_1"]
}
```

We can access this additional `data` within the OneSignalNotificationServiceExtension via the `custom` object using the `a` parameter.

<CodeGroup>
  ```Swift Swift theme={null}
  // Check if `bestAttemptContent` exists
  if let bestAttemptContent = bestAttemptContent {

      // Try to retrieve the "custom" data from the notification payload
      if let customData = bestAttemptContent.userInfo["custom"] as? [String: Any],
         let additionalData = customData["a"] as? [String: Any] {

          // Convert the `additionalData` dictionary to a JSON string for logging
          if let jsonData = try? JSONSerialization.data(withJSONObject: additionalData, options: .prettyPrinted),
             let jsonString = String(data: jsonData, encoding: .utf8) {
              // Successfully converted to JSON; log the formatted JSON string
              print("The additionalData dictionary in JSON format:\n\(jsonString)")
          } else {
              // Failed to convert the `additionalData` dictionary to JSON
              print("Failed to convert additionalData to JSON format.")
          }
      }

      // Try to retrieve the "aps" data from the notification payload
      if let messageData = bestAttemptContent.userInfo["aps"] as? [String: Any],
         let apsData = messageData["alert"] as? [String: Any],
         let body = apsData["body"] as? String,  // Extract the "body" of the alert
         let title = apsData["title"] as? String {  // Extract the "title" of the alert
          // Successfully retrieved the body and title; log the values
          print("The message contents is: \(body), message headings is: \(title)")
      } else {
          // Failed to retrieve the "aps" data or its contents
          print("Unable to retrieve apsData")
      }

      // Pass the notification to OneSignal for further processing
      OneSignalExtension.didReceiveNotificationExtensionRequest(self.receivedRequest,
                                                                with: bestAttemptContent,
                                                                withContentHandler: self.contentHandler)
  }

  ```

  ```ObjectiveC Objective-C theme={null}
  if (bestAttemptContent) {
      // Retrieve and log customData["a"]
      NSDictionary *customData = bestAttemptContent.userInfo[@"custom"];
      if ([customData isKindOfClass:[NSDictionary class]]) {
          NSDictionary *additionalData = customData[@"a"];
          if ([additionalData isKindOfClass:[NSDictionary class]]) {
              NSError *error;
              NSData *jsonData = [NSJSONSerialization dataWithJSONObject:additionalData options:NSJSONWritingPrettyPrinted error:&error];
              if (jsonData) {
                  NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
                  NSLog(@"The additionalData dictionary in JSON format:\n%@", jsonString);
              } else {
                  NSLog(@"Failed to convert additionalData to JSON format: %@", error.localizedDescription);
              }
          }
      }

      // Retrieve and log apsData
      NSDictionary *messageData = bestAttemptContent.userInfo[@"aps"];
      if ([messageData isKindOfClass:[NSDictionary class]]) {
          NSDictionary *apsData = messageData[@"alert"];
          if ([apsData isKindOfClass:[NSDictionary class]]) {
              NSString *body = apsData[@"body"];
              NSString *title = apsData[@"title"];
              if ([body isKindOfClass:[NSString class]] && [title isKindOfClass:[NSString class]]) {
                  NSLog(@"The message content is: %@, message heading is: %@", body, title);
              }
          } else {
              NSLog(@"Unable to retrieve apsData");
          }
      }

      // Call OneSignalExtension method
      [OneSignalExtension didReceiveNotificationExtensionRequest:self.receivedRequest
                                               withNotification:bestAttemptContent
                                                withContentHandler:self.contentHandler];
  }
  ```

</CodeGroup>

**Example console output:**

```
The additionalData dictionary in JSON format:
{
  "additional_data_key_1" : "value_1",
  "additional_data_key_2" : "value_2"
}
The message contents is: The message contents, message headings is: The message title
```

### Troubleshooting the iOS Notification Service Extension

This guide is for debugging issues with Images, Action Buttons, or Confirmed Deliveries not showing on iOS mobile apps.

**Check your Xcode Settings**

In **General > Targets** make sure your **main app target** and **OneSignalNotificationServiceExtension** target have the same and correct:

* **Supported Destinations**
* **Minimum Deployment** (iOS 14.5 or higher)

<Warning>
  If you are using Cocoapods make sure these match with your main target in the Podfile to avoid build errors.
</Warning>

<Frame caption="Example Main App Target in Xcode">
  <img src="https://mintcdn.com/onesignal/RWA35uTjv8voG5iC/images/mobile/main-app-target-general-settings.png?fit=max&auto=format&n=RWA35uTjv8voG5iC&q=85&s=eb9dd4d9dbec5f2b9f351ff168087557" width="2988" height="1824" data-path="images/mobile/main-app-target-general-settings.png" />
</Frame>

<Frame caption="Example OneSignalNotificationServiceExtension Target in Xcode">
  <img src="https://mintcdn.com/onesignal/x4RdPY-EcasyyQ-o/images/mobile/onesignal-notification-service-extension-target-general-settings.png?fit=max&auto=format&n=x4RdPY-EcasyyQ-o&q=85&s=ea6f697fda7b4a338bb7e3a4dac3856f" width="2988" height="1824" data-path="images/mobile/onesignal-notification-service-extension-target-general-settings.png" />
</Frame>

Continuing in the **OneSignalNotificationServiceExtension > Info** tab, expand the `NSExtension` key. Ensure you see:

```XML XML theme={null}
 <dict>
   <key>NSExtensionPointIdentifier</key>
   <string>com.apple.usernotifications.service</string>
   <key>NSExtensionPrincipalClass</key>
   <string>$(PRODUCT_MODULE_NAME).NotificationService</string>
 </dict>
```

Example:

<Frame caption="Example NSExtension key in the Info tab">
  <img src="https://mintcdn.com/onesignal/RWA35uTjv8voG5iC/images/mobile/onesignal-notification-service-extension-info-tab.png?fit=max&auto=format&n=RWA35uTjv8voG5iC&q=85&s=06e65f878427e94127ef7391903d583e" width="3282" height="1888" data-path="images/mobile/onesignal-notification-service-extension-info-tab.png" />
</Frame>

<Warning>
  If using Objective-C, instead of `$(PRODUCT_MODULE_NAME).NotificationService` use `NotificationService`.
</Warning>

**Turn off "Copy only when installing"**

Select your **main app target > Build Phases > Embed App Extensions**. Ensure "Copy only when installing" is NOT checked. Uncheck it if it is:

<Frame caption="Main app target build phase settings">
  <img src="https://mintcdn.com/onesignal/RWA35uTjv8voG5iC/images/mobile/main-app-target-build-phases.png?fit=max&auto=format&n=RWA35uTjv8voG5iC&q=85&s=cd507862b8e5bb0934b6f6b082d0b26e" width="3282" height="1888" data-path="images/mobile/main-app-target-build-phases.png" />
</Frame>

### Debugging the iOS Notification Service Extension

Follow these steps to verify the Notification Service Extension is setup correctly.

#### 1. Update the OneSignalNotificationServiceExtension code

Open the `NotificationService.m` or `NotificationService.swift` and replace the whole file contents with the below code. (The code is the same as our original setup code, just adding some additional logging.

**Make sure to replace `YOUR_BUNDLE_ID` with your actual Bundle ID.**

<CodeGroup>
  ```Swift Swift theme={null}
  import UserNotifications
  import OneSignalExtension
  import os.log

  class NotificationService: UNNotificationServiceExtension {

      var contentHandler: ((UNNotificationContent) -> Void)?
      var receivedRequest: UNNotificationRequest!
      var bestAttemptContent: UNMutableNotificationContent?

      override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
          self.receivedRequest = request
          self.contentHandler = contentHandler
          self.bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)

          let userInfo = request.content.userInfo
          let custom = userInfo["custom"]
          print("Running NotificationServiceExtension: userInfo = \(userInfo.description)")
          print("Running NotificationServiceExtension: custom = \(custom.debugDescription)")
          //debug log types need to be enabled in Console > Action > Include Debug Messages
          //Replace YOUR_BUNDLE_ID with your actual Bundle ID
          os_log("%{public}@", log: OSLog(subsystem: "YOUR_BUNDLE_ID", category: "OneSignalNotificationServiceExtension"), type: OSLogType.debug, userInfo.debugDescription)

          if let bestAttemptContent = bestAttemptContent {
              /* DEBUGGING: Uncomment the 2 lines below to check this extension is executing
                            Note, this extension only runs when mutable-content is set
                            Setting an attachment or action buttons automatically adds this */
              print("Running NotificationServiceExtension")
              bestAttemptContent.body = "[Modified] " + bestAttemptContent.body

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

  ```objc Objective-C theme={null}
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

      //If your SDK version is < 3.5.0 uncomment and use this code:
      /*
      [OneSignal didReceiveNotificationExtensionRequest:self.receivedRequest
                         withMutableNotificationContent:self.bestAttemptContent];
      self.contentHandler(self.bestAttemptContent);
      */

      NSUserDefaults *userDefault = [[NSUserDefaults alloc] initWithSuiteName:@"group.YOUR_BUNDLE_ID.onesignal"];
      NSLog(@"NSE player_id: %@", [userDefault  stringForKey:@"GT_PLAYER_ID"]);
      NSLog(@"NSE app_id: %@", [userDefault  stringForKey:@"GT_APP_ID"]);

      /* DEBUGGING: Uncomment the 2 lines below and comment out the one above to ensure this extension is excuting
                    Note, this extension only runs when mutable-content is set
                    Setting an attachment or action buttons automatically adds this */
      NSLog(@"Running NotificationServiceExtension");
      self.bestAttemptContent.body = [@"[Modified] " stringByAppendingString:self.bestAttemptContent.body];

      [OneSignal.Debug setLogLevel:ONE_S_LL_VERBOSE];

      [OneSignal didReceiveNotificationExtensionRequest:self.receivedRequest
                         withMutableNotificationContent:self.bestAttemptContent
                                     withContentHandler:self.contentHandler];
  }

  - (void)serviceExtensionTimeWillExpire {
      // Called just before the extension will be terminated by the system.
      // Use this as an opportunity to deliver your "best attempt" at modified content, otherwise the original push payload will be used.

      [OneSignal serviceExtensionTimeWillExpireRequest:self.receivedRequest withMutableNotificationContent:self.bestAttemptContent];

      self.contentHandler(self.bestAttemptContent);
  }

  @end
  ```

</CodeGroup>

#### 2. Change your Active Scheme

Set your Active Scheme to the `OneSignalNotificationServiceExtension`.

<Frame caption="Xcode active scheme selection">
  <img src="https://mintcdn.com/onesignal/x4RdPY-EcasyyQ-o/images/mobile/xcode-active-scheme-selection.png?fit=max&auto=format&n=x4RdPY-EcasyyQ-o&q=85&s=27407135e39bc606a02e005efd3a56ff" width="3282" height="1888" data-path="images/mobile/xcode-active-scheme-selection.png" />
</Frame>

#### 3. Build and run the project

Build and run the project in Xcode on a real device.

#### 4. Open the Console

In Xcode, select **Window > Devices and Simulators**.

<Frame caption="Xcode Devices and Simulators window">
  <img src="https://mintcdn.com/onesignal/x4RdPY-EcasyyQ-o/images/mobile/xcode-devices-and-simulators-selection.png?fit=max&auto=format&n=x4RdPY-EcasyyQ-o&q=85&s=2bc1305ee0fd45087f33a078a7aeaffb" width="2518" height="1374" data-path="images/mobile/xcode-devices-and-simulators-selection.png" />
</Frame>

You should see your device connected. Select **Open Console**.

<Frame caption="Device console access button">
  <img src="https://mintcdn.com/onesignal/x4RdPY-EcasyyQ-o/images/mobile/xcode-device-console-access-button.png?fit=max&auto=format&n=x4RdPY-EcasyyQ-o&q=85&s=7ffa64afd28d452e200241ad4751c102" width="2304" height="1624" data-path="images/mobile/xcode-device-console-access-button.png" />
</Frame>

#### 5. Check the Console

In the Console:

* Select Action > Include Debug Messages
* Search for `OneSignalNotificationServiceExtension` as the CATEGORY
* Select **Start**

<Frame caption="Console debugging configuration">
  <img src="https://mintcdn.com/onesignal/x4RdPY-EcasyyQ-o/images/mobile/xcode-console-debugging-configuration.png?fit=max&auto=format&n=x4RdPY-EcasyyQ-o&q=85&s=82593a0287811e6b787cee686ab7196d" width="3368" height="1232" data-path="images/mobile/xcode-console-debugging-configuration.png" />
</Frame>

Send this device a notification with a message (use `contents` property if sending from the [Create message](/reference/create-message) API). In this example, the payload is:

```cURL cURL theme={null}
  //Replace with your own app data:
  //YOUR_API_KEY, YOUR_APP_ID, SUBSCRIPTION_ID_1

curl --request POST \
 --url 'https://api.onesignal.com/notifications' \
 --header 'Authorization: Key YOUR_API_KEY' \
 --header 'accept: application/json' \
 --header 'content-type: application/json' \
 --data '
{
"app_id": "YOUR_APP_ID",
"target_channel": "push",
"headings": {"en": "The message title"},
"contents": {"en": "The message contents"},
"data":{"additional_data_key_1":"value_1","additional_data_key_2":"value_2"},
"include_subscription_ids": [
"SUBSCRIPTION_ID_1"
]
}'
```

You should see a message logged with the app running and not running.

<Frame caption="Console debug output example">
  <img src="https://mintcdn.com/onesignal/x4RdPY-EcasyyQ-o/images/mobile/xcode-console-debug-output.png?fit=max&auto=format&n=x4RdPY-EcasyyQ-o&q=85&s=d93e3fc36610941e1c01b83abc0234b3" width="3604" height="1776" data-path="images/mobile/xcode-console-debug-output.png" />
</Frame>

If you do not see a message, then remove OneSignal from your app and follow our [Mobile SDK Setup](./mobile-sdk-setup) again to verify you setup OneSignal correctly.

***

Built with [Mintlify](https://mintlify.com).

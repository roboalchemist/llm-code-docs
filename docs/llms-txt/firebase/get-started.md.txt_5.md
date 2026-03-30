# Source: https://firebase.google.com/docs/cloud-messaging/ios/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/get-started) [Android](https://firebase.google.com/docs/cloud-messaging/android/get-started) [Web](https://firebase.google.com/docs/cloud-messaging/web/get-started) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/get-started) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/get-started) |

<br />

This guide describes how to get started with Firebase Cloud Messaging in your
Apple platform (like iOS) client apps so that you can reliably send messages.

For Apple client apps, you can receive notification and data payloads up to 4096
bytes over the Firebase Cloud Messaging APNs interface.

To write your client code in Objective-C or Swift, we recommend that you use the
[FIRMessaging
API](https://firebase.google.com/docs/reference/ios/firebasemessaging/interface_f_i_r_messaging). The
[quickstart
example](https://github.com/firebase/quickstart-ios/tree/master/messaging/)
provides sample code for both languages.

Before you get started, [add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup).

## Method swizzling in Firebase Cloud Messaging

The FCM SDK performs method swizzling in two key areas: mapping your
APNs token to the FCM registration token and
capturing analytics data during [downstream message callback
handling](https://firebase.google.com/docs/cloud-messaging/ios/receive#handle-swizzle). Developers who
prefer not to use swizzling can disable it by adding the flag
`FirebaseAppDelegateProxyEnabled` in the app's Info.plist file and setting it to
NO (boolean value). Relevant areas of the guides provide code examples, both
with and without method swizzling enabled.

> [!IMPORTANT]
> **Important:** With the Firebase Unity SDK on iOS, **do not disable method
> swizzling.** Swizzling is required by the SDK, and without it key Firebase features such as FCM token handling do not function properly.

## Upload your APNs authentication key


Upload your APNs authentication key to Firebase.
If you don't already have an APNs authentication key, make sure to create one in the
[Apple Developer Member Center](https://developer.apple.com/membercenter/index.action).

1.
   Inside your project in the Firebase console, select the
   gear icon, select
   **Project Settings** , and then select the
   **Cloud Messaging** tab.

2.
   In **APNs authentication key** under **iOS app configuration** ,
   click the **Upload** button to upload your development authentication key, or
   production authentication key, or both. At least one is required.

3.
   Browse to the location where you saved your key, select it, and click
   **Open** . Add the key ID for the key (available in the
   [Apple Developer Member Center](https://developer.apple.com/membercenter/index.action)) and click
   **Upload**.

## Register for remote notifications

Either at startup, or at the desired point in your application flow, register your app for remote notifications. Call `registerForRemoteNotifications` as shown:

> [!NOTE]
> Note: SwiftUI apps should use the `UIApplicationDelegateAdaptor` or `NSApplicationDelegateAdaptor` property wrappers to provide a type corresponding to the appropriate app delegate protocol.

#### Swift

```swift
UNUserNotificationCenter.current().delegate = self

let authOptions: UNAuthorizationOptions = [.alert, .badge, .sound]
UNUserNotificationCenter.current().requestAuthorization(
  options: authOptions,
  completionHandler: { _, _ in }
)

application.registerForRemoteNotifications()
```

#### Objective-C

```objective-c
[UNUserNotificationCenter currentNotificationCenter].delegate = self;
UNAuthorizationOptions authOptions = UNAuthorizationOptionAlert |
    UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
[[UNUserNotificationCenter currentNotificationCenter]
    requestAuthorizationWithOptions:authOptions
    completionHandler:^(BOOL granted, NSError * _Nullable error) {
      // ...
    }];

[application registerForRemoteNotifications];
```

> [!CAUTION]
> You must assign the UNUserNotificationCenter's [`delegate`](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649522-delegate) property and FIRMessaging's [`delegate`](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessaging#delegate) property. For example, in an iOS app, assign it in the `applicationWillFinishLaunchingWithOptions:` or `applicationDidFinishLaunchingWithOptions:` method of the app delegate.

## Access the registration token

> [!TIP]
> **Tip:** See [Best practices for FCM registration token
> management](https://firebase.google.com/docs/cloud-messaging/manage-tokens) for tips on managing tokens.

By default, the FCM SDK generates a
registration token for the client app instance on app launch.
Similar to the APNs device token, this token allows you to send targeted notifications
to any particular instance of your app.

In the same way that Apple platforms typically deliver an APNs device token on app start,
FCM provides a registration token via `FIRMessagingDelegate`'s
`messaging:didReceiveRegistrationToken:` method.
The FCM SDK retrieves a new or existing token during initial app launch and
whenever the token is updated or invalidated.
In all cases, the FCM SDK calls `messaging:didReceiveRegistrationToken:`
with a valid token.

> [!CAUTION]
> Apps still using deprecated Instance ID APIs for token management should update all token logic to use the FCM APIs described here.

The registration token may change when:

- The app is restored on a new device
- The user uninstalls/reinstall the app
- The user clears app data.

<br />

### Set the messaging delegate

To receive registration tokens, implement the messaging delegate
protocol and set `FIRMessaging`'s `delegate` property after calling
`[FIRApp configure]`.
For example, if your application delegate conforms to the messaging delegate
protocol, you can set the delegate on `application:didFinishLaunchingWithOptions:`
to itself.

#### Swift

```swift
Messaging.messaging().delegate = self
```

#### Objective-C

```objective-c
[FIRMessaging messaging].delegate = self;
```

### Fetching the current registration token

Registration tokens are delivered via the method
`messaging:didReceiveRegistrationToken:`. This method is called generally once per
app start with registration token. When this method is called, it is the ideal time to:

- If the registration token is new, send it to your application server.
- Subscribe the registration token to topics. This is required only for new subscriptions or for situations where the user has re-installed the app.

You can retrieve the token directly using
[token(completion:)](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#tokencompletion:).
A non null error is provided if the token retrieval failed in any way.

#### Swift

```swift
Messaging.messaging().token { token, error in
  if let error = error {
    print("Error fetching remote FCM registration token: \(error)")
  } else if let token = token {
    print("Remote instance ID token: \(token)")
  }
}
```

#### Objective-C

```objective-c
[[FIRMessaging messaging] tokenWithCompletion:^(NSString * _Nullable token, NSError * _Nullable error) {
  if (error != nil) {
    NSLog(@"Error fetching the remote FCM registration token: %@", error);
  } else {
    NSLog(@"Remote FCM registration token: %@", token);
    NSString* message =
      [NSString stringWithFormat:@"FCM registration token: %@", token];
    // display message
    NSLog(@"%@", message);
  }
}];
```

You can use this method at any time to access the token instead of storing
it.

### Monitor token refresh

To be notified whenever the token is updated, supply a delegate conforming
to the messaging delegate protocol. The following example registers
the delegate and adds the proper delegate method:

#### Swift

```swift
func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String?) {
  print("Firebase registration token: \(String(describing: fcmToken))")
  // TODO: If necessary send token to application server.
  // Note: This callback is fired at each app startup and whenever a new token is generated.
}
```

#### Objective-C

```objective-c
- (void)messaging:(FIRMessaging *)messaging didReceiveRegistrationToken:(NSString *)fcmToken {
    NSLog(@"FCM registration token: %@", fcmToken);
    // Notify about received token.
    NSDictionary *dataDict = [NSDictionary dictionaryWithObject:fcmToken forKey:@"token"];
    [[NSNotificationCenter defaultCenter] postNotificationName:
     @"FCMToken" object:nil userInfo:dataDict];
    // TODO: If necessary send token to application server.
    // Note: This callback is fired at each app startup and whenever a new token is generated.
}
```

Alternatively, you can listen for an `NSNotification` named
`kFIRMessagingRegistrationTokenRefreshNotification`
rather than supplying a delegate method. The token property always has the
current token value.

#### Swizzling disabled: mapping your APNs token and registration token

If you have disabled method swizzling, or you are building a SwiftUI app, you'll need to
explicitly map your APNs token to the FCM registration token. Implement the
`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method to
retrieve the APNs token, and then set `Messaging`'s
[`apnsToken`](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#apnstoken)
property:

#### Swift

```swift
func application(application: UIApplication,
                 didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
  Messaging.messaging().apnsToken = deviceToken
}
```

#### Objective-C

```objective-c
// With "FirebaseAppDelegateProxyEnabled": NO
- (void)application:(UIApplication *)application
    didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    [FIRMessaging messaging].APNSToken = deviceToken;
}
```

After the FCM registration token is generated, you can access it
and listen for refresh events using the same methods as with swizzling
enabled.

## Prevent auto initialization

When an FCM registration token is generated, the library uploads the
identifier and configuration data to Firebase. If you want to get an explicit
opt-in from users first, you can prevent token generation at configure time by
disabling FCM. To do this, add a metadata value to your `Info.plist` (not your
`GoogleService-Info.plist`):

`FirebaseMessagingAutoInitEnabled = NO`

To re-enable FCM, you can make a runtime call:

#### Swift

```swift
Messaging.messaging().autoInitEnabled = true
```

#### Objective-C

```objective-c
[FIRMessaging messaging].autoInitEnabled = YES;
```

This value persists across app restarts once set.

## Set up the notification service extension

To send notifications that include images to Apple devices, you must add a
notification service extension. This extension allows devices to display images
delivered in the notification payload. If you don't plan to send images in
notifications, you can skip this step.

To add a service extension, perform the required setup tasks for
[modifying and presenting notifications](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/ModifyingNotifications.html)
in APNs, and then add the FCM extension helper API in `NotificationService.m`.
Specifically, instead of completing the callback with
`self.contentHandler(self.bestAttemptContent);`,
complete it with `FIRMessaging extensionHelper` as shown:

    @interface NotificationService () <NSURLSessionDelegate>
    @property(nonatomic) void (^contentHandler)(UNNotificationContent *contentToDeliver);
    @property(nonatomic) UNMutableNotificationContent *bestAttemptContent;
    @end

    @implementation NotificationService

    - (void)didReceiveNotificationRequest:(UNNotificationRequest *)request withContentHandler:(void (^)(UNNotificationContent * _Nonnull))contentHandler {
        self.contentHandler = contentHandler;
        self.bestAttemptContent = [request.content mutableCopy];

        // Modify the notification content here as you want
        self.bestAttemptContent.title = [NSString stringWithFormat:@"%@ [modified]",
        self.bestAttemptContent.title];

      // Call FIRMessaging extension helper API.
      [[FIRMessaging extensionHelper] populateNotificationContent:self.bestAttemptContent
                                                withContentHandler:contentHandler];

    }
    ...

## Send a notification message

1. Install and run the app on the target device. On Apple devices, accept the request for permission to receive remote notifications.
2. Check that the app is in the background on the device.
3. In the Firebase console, open the [Messaging](https://console.firebase.google.com/project/_/notification) page.
4. If this is your first message, select **Create your first campaign** .
   1. Select **Firebase Notification messages** and select **Create**.
5. Otherwise, on the **Campaigns** tab, select **New campaign** and then **Notifications**.
6. Enter the message text.
7. Select **Send test message** from the right pane.
8. In the field labeled **Add an FCM registration token**, enter your registration token.
9. Select **Test**.

After you select **Test**, the targeted client device, with the app in the
background, should receive the notification.

For insight into message delivery to your app, see the [FCM reporting
dashboard](https://console.firebase.google.com/project/_/notification/reporting),
which records the number of messages sent and opened on Apple and Android
devices.

## Next steps

After you have completed the setup steps, here are a few options for moving
forward with FCM for Apple platforms:

- [Send messages to devices](https://firebase.google.com/docs/cloud-messaging/server-environment)
- [Receive messages in an Apple app](https://firebase.google.com/docs/cloud-messaging/receive-messages?platform=ios)
- [Send messages to topics](https://firebase.google.com/docs/cloud-messaging/topic-messaging)
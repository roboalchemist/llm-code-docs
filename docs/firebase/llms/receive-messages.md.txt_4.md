# Source: https://firebase.google.com/docs/cloud-messaging/ios/receive-messages.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/receive-messages) [Android](https://firebase.google.com/docs/cloud-messaging/android/receive-messages) [Web](https://firebase.google.com/docs/cloud-messaging/web/receive-messages) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/receive-messages) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/receive-messages) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/receive-messages) |

<br />

Once your client app is installed on a device, it can receive messages through
the FCM APNs interface. You can immediately start sending
notifications to user segments with the
[Notifications composer](https://console.firebase.google.com/project/_/notification),
or messages built on your application server.

## Handle alert notifications

FCM delivers all messages targeting Apple apps through APNs. To learn
more about receiving APNs notifications using `UNUserNotificationCenter`, see
Apple's documentation on
[Handling Notifications and Notification-Related Actions](https://developer.apple.com/documentation/usernotifications/handling_notifications_and_notification-related_actions?language=objc).

You must set the
[UNUserNotificationCenter delegate](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649522-delegate)
and implement the appropriate delegate methods to receive display notifications
from FCM.

### Swift

    // Receive displayed notifications for iOS 10+ devices.
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification) async
      -> UNNotificationPresentationOptions {
      let userInfo = notification.request.content.userInfo

      // With swizzling disabled you must let Messaging know about the message, for Analytics
      // Messaging.messaging().appDidReceiveMessage(userInfo)

      // ...

      // Print full message.
      print(userInfo)

      // Change this to your preferred presentation option
      // Note: UNNotificationPresentationOptions.alert has been deprecated.
      return [.list, .banner, .sound]
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse) async {
      let userInfo = response.notification.request.content.userInfo

      // ...

      // Print full message.
      print(userInfo)
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/MigratedSnippets.swift#L400-L427

### Objective-C

    // Receive displayed notifications for iOS 10+ devices.
    // Handle incoming notification messages while app is in the foreground.
    - (void)userNotificationCenter:(UNUserNotificationCenter *)center
           willPresentNotification:(UNNotification *)notification
             withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler {
      NSDictionary *userInfo = notification.request.content.userInfo;

      // With swizzling disabled you must let Messaging know about the message, for Analytics
      // [[FIRMessaging messaging] appDidReceiveMessage:userInfo];

      // Print full message.
      NSLog(@"%@", userInfo);

      // Change this to your preferred presentation option
      completionHandler(UNNotificationPresentationOptionList |
                        UNNotificationPresentationOptionBanner |
                        UNNotificationPresentationOptionSound);
    }

    - (void)messaging:(FIRMessaging *)messaging didReceiveRegistrationToken:(NSString *)fcmToken {
        NSLog(@"FCM registration token: %@", fcmToken);
        // Notify about received token.
        NSDictionary *dataDict = [NSDictionary dictionaryWithObject:fcmToken forKey:@"token"];
        [[NSNotificationCenter defaultCenter] postNotificationName:
         @"FCMToken" object:nil userInfo:dataDict];
        // TODO: If necessary send token to application server.
        // Note: This callback is fired at each app startup and whenever a new token is generated.
    }

    - (void)logFCMToken {
      NSString *fcmToken = [FIRMessaging messaging].FCMToken;
      NSLog(@"Local FCM registration token: %@", fcmToken);

      NSString* displayToken = [NSString stringWithFormat:@"Logged FCM token: %@", fcmToken];

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
      NSLog(@"%@", displayToken);
    }

    - (void)subsribeToTopic {
      [[FIRMessaging messaging] subscribeToTopic:@"weather"
                                      completion:^(NSError * _Nullable error) {
        NSLog(@"Subscribed to weather topic");
      }];
    }

    @end
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/ObjCMigratedSnippets.m#L292-L-1

If you want to add custom actions to your notifications, set the `click_action`
parameter in the
[notification payload](https://firebase.google.com/docs/cloud-messaging/http-server-ref#notification-payload-support).
Use the value that you would use for the `category` key in the APNs payload.
Custom actions must be registered before they can be used. For more
information, see Apple's
[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html#//apple_ref/doc/uid/TP40008194-CH4-SW26).

For insight into message delivery to your app, see
the [FCM reporting dashboard](https://console.firebase.google.com/project/_/notification/reporting), which records the
number of messages sent and opened on Apple and Android devices, along with
data for "impressions" (notifications seen by users) for Android apps.

## Handle silent push notifications

When sending messages with the `content-available` key (equivalent to APNs's
`content-available`), the messages will be delivered as silent notifications,
waking your app in the background for tasks like background data refresh.
Unlike foreground notifications, these notifications must be handled using the
[`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application)
method.

Implement `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`
as shown:

### Swift

    @MainActor
    func application(_ application: UIApplication,
                     didReceiveRemoteNotification userInfo: [AnyHashable: Any]) async
      -> UIBackgroundFetchResult {
      // If you are receiving a notification message while your app is in the background,
      // this callback will not be fired till the user taps on the notification launching the application.
      // TODO: Handle data of notification

      // With swizzling disabled you must let Messaging know about the message, for Analytics
      // Messaging.messaging().appDidReceiveMessage(userInfo)

      // ...

      // Print full message.
      print(userInfo)
      print("Call exportDeliveryMetricsToBigQuery() from AppDelegate")
      Messaging.serviceExtension().exportDeliveryMetricsToBigQuery(withMessageInfo: userInfo)
      return UIBackgroundFetchResult.newData
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/MigratedSnippets.swift#L378-L396

### Objective-C

    - (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo
        fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
      // If you are receiving a notification message while your app is in the background,
      // this callback will not be fired until the user taps on the notification launching the application.
      // TODO: Handle data of notification

      // With swizzling disabled you must let Messaging know about the message, for Analytics
      // [[FIRMessaging messaging] appDidReceiveMessage:userInfo];

      // Print full message.
      NSLog(@"%@", userInfo);

      completionHandler(UIBackgroundFetchResultNewData);
    }https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/qs-snippets/QSSnippets/ObjCMigratedSnippets.m#L275-L288

Apple platforms don't guarantee the delivery of background notifications. To
learn about conditions that can cause background notifications to fail, see
Apple's docs on
[Pushing Background Updates to Your App](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).

## Interpret notification message payload

The payload of notification messages is a dictionary of keys and values.
Notification messages sent through APNs has the following the APNs payload
format:

      {
        "aps" : {
          "alert" : {
            "body" : "great match!",
            "title" : "Portugal vs. Denmark",
          },
          "badge" : 1,
        },
        "customKey" : "customValue"
      }

## Handle messages with method swizzling disabled

By default, if you assign your app's app delegate class to the
`UNUserNotificationCenter` and `Messaging` delegate properties, FCM
will swizzle your app delegate class to automatically associate your
FCM token with the device's APNs token and pass notification-received
events to Analytics. If you explicitly disable method swizzling, if you are
building a SwiftUI app, or if you use a separate class for either delegate, you
will need to perform both of these tasks manually.

To associate the FCM token with the device APNs token, pass the APNs
token to the `Messaging` class in your app delegate's
[token refresh handler](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622958-application)
using the
[`apnsToken` property](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(py)APNSToken).

### Swift

    func application(_ application: UIApplication,
        didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
      Messaging.messaging().apnsToken = deviceToken;
    }

### Objective-C

    - (void)application:(UIApplication *)application
        didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
      [FIRMessaging messaging].APNSToken = deviceToken;
    }

To pass notification receipt information to Analytics, use the
[`appDidReceiveMessage(_:)` method](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging#/c:objc(cs)FIRMessaging(im)appDidReceiveMessage:).

### Swift

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification,
      withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
      let userInfo = notification.request.content.userInfo

      Messaging.messaging().appDidReceiveMessage(userInfo)

      // Change this to your preferred presentation option
      completionHandler([[.alert, .sound]])
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse,
                                withCompletionHandler completionHandler: @escaping () -> Void) {
      let userInfo = response.notification.request.content.userInfo

      Messaging.messaging().appDidReceiveMessage(userInfo)

      completionHandler()
    }

    func application(_ application: UIApplication,
    didReceiveRemoteNotification userInfo: [AnyHashable : Any],
      fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
      Messaging.messaging().appDidReceiveMessage(userInfo)
      completionHandler(.noData)
    }

### Objective-C

    - (void)userNotificationCenter:(UNUserNotificationCenter *)center
          willPresentNotification:(UNNotification *)notification
            withCompletionHandler:(void (^)(UNNotificationPresentationOptions))completionHandler {
      NSDictionary *userInfo = notification.request.content.userInfo;

      [[FIRMessaging messaging] appDidReceiveMessage:userInfo];

      // Change this to your preferred presentation option
      completionHandler(UNNotificationPresentationOptionBadge | UNNotificationPresentationOptionAlert);
    }

    - (void)userNotificationCenter:(UNUserNotificationCenter *)center
    didReceiveNotificationResponse:(UNNotificationResponse *)response
            withCompletionHandler:(void(^)(void))completionHandler {
      NSDictionary *userInfo = response.notification.request.content.userInfo;

      [[FIRMessaging messaging] appDidReceiveMessage:userInfo];

      completionHandler();
    }

    - (void)application:(UIApplication *)application
    didReceiveRemoteNotification:(NSDictionary *)userInfo
    fetchCompletionHandler:(void (^)(UIBackgroundFetchResult result))completionHandler {
      [[FIRMessaging messaging] appDidReceiveMessage:userInfo];
      completionHandler(UIBackgroundFetchResultNoData);
    }
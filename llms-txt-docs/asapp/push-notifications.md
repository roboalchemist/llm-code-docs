# Source: https://docs.asapp.com/messaging-platform/integrations/ios-sdk/push-notifications.md

# Push Notifications

## Get Started with Push Notifications

Please see Apple's documentation on the [Apple Push Notification service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview#//apple_ref/doc/uid/TP40008194-CH8-SW1) and the [User Notifications](https://developer.apple.com/documentation/usernotifications) framework.

## ASAPP Push Notifications

ASAPP's systems may trigger push notifications at certain times, such as when an agent sends a message to a customer who does not currently have the chat interface open. These push notifications are triggered by ASAPP's servers calling your company's API with data that identifies the recipient's device; ASAPP's servers do not communicate with APNs directly. Therefore, we provide methods in the SDK to register and deregister the customer's device for ASAPP push notifications.
For a deeper dive on how push notifications are handled between ASAPP and your company's API, please see our documentation on [Push Notifications and the Mobile SDKs](../push-notifications-and-the-mobile-sdks "Push Notifications and the Mobile SDKs").

### Enable Push Notifications

To enable push notifications for the current user when using the token provided by APNs in `didRegisterForRemoteNotificationsWithDeviceToken(_:)`, call `ASAPP.enablePushNotifications(with deviceToken: Data)`.
To enable push notifications using an arbitrary string that uniquely identifies the device and current user, call `ASAPP.enablePushNotifications(with uuid: String)`.

### Disable Push Notifications

To disable push notifications for the current user on the device, call `ASAPP.disablePushNotifications(failure:)`. The failure handler will be called in the event of an error. Make sure you call this function before you change or clear `ASAPP.user` to prevent the customer receiving push notifications that are not meant for them.

### Handle Push Notifications

Implement `application(_:didReceiveRemoteNotification:[fetchCompletionHandler:])` and pass the `userInfo` dictionary to `ASAPP.canHandleNotification(with:)` to determine if the push notification was triggered by ASAPP. If the function returns `true`, you can then pass `userInfo` to: `ASAPP.createChatViewControllerForPushing(fromNotificationWith:)`.

<Note>
  Your application usually won't receive push notifications from ASAPP if the user is currently connected to chat.
</Note>

### Request Permissions for Push Notifications

When a user joins a queue in the ASAPP mobile app, a prompt screen asks them to enable push notifications and provides some context on the benefits. If the user has already accepted or denied these permissions, they will not receive this prompt.
After enablement, users will receive a push notification every time there is a new message in the app chat. Users only receive push notifications if the app is not active.
You can control this feature remotely. Please contact your Integration Manager for further information. ASAPP highly recommends that you enable this feature.

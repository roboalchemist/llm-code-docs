# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes.md.txt

# FirebaseMessaging Framework Reference

# Classes

The following classes are available globally.
- `


  ### [MessagingMessageInfo](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/MessagingMessageInfo)


  ` Information about a downstream message received by the app.

  #### Declaration

  Swift

      class MessagingMessageInfo : NSObject

- `


  ### [Messaging](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/Messaging)


  ` Firebase Messaging lets you reliably deliver messages.

  To send or receive messages, the app must get a
  registration token. This token authorizes an
  app server to send messages to an app instance.

  In order to handle incoming Messaging messages, set the
  `UNUserNotificationCenter`'s `delegate` property
  and implement the appropriate methods.

  #### Declaration

  Swift

      class Messaging : NSObject

- `


  ### [FIRMessagingExtensionHelper](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper)


  ` This class is used to automatically populate a notification with an image if it is
  specified in the notification body via the `image` parameter. Images and other
  rich content can be populated manually without the use of this class. See the
  `UNNotificationServiceExtension` type for more details.

  #### Declaration

  Swift

      class FIRMessagingExtensionHelper : NSObject
# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes.md.txt

# FirebaseMessaging Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRMessaging](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessaging)


  ` Firebase Messaging lets you reliably deliver messages.

  To send or receive messages, the app must get a
  registration token. This token authorizes an
  app server to send messages to an app instance.

  In order to handle incoming Messaging messages, set the
  `UNUserNotificationCenter`'s `delegate` property
  and implement the appropriate methods.

  #### Declaration

  Objective-C


      @interface FIRMessaging : NSObject

- `


  ### [FIRMessagingMessageInfo](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessagingMessageInfo)


  ` Information about a downstream message received by the app.

  #### Declaration

  Objective-C


      @interface FIRMessagingMessageInfo : NSObject

- `


  ### [FIRMessagingExtensionHelper](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Classes/FIRMessagingExtensionHelper)


  ` This class is used to automatically populate a notification with an image if it is
  specified in the notification body via the `image` parameter. Images and other
  rich content can be populated manually without the use of this class. See the
  `UNNotificationServiceExtension` type for more details.

  #### Declaration

  Objective-C


      @interface FIRMessagingExtensionHelper : NSObject
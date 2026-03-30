# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Constants.md.txt

# FirebaseMessaging Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRMessagingRegistrationTokenRefreshedNotification](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Constants#/c:@FIRMessagingRegistrationTokenRefreshedNotification)


  ` Notification sent when the FCM registration token has been refreshed. Please use the
  FIRMessaging delegate method `messaging:didReceiveRegistrationToken:` to receive current and
  updated tokens.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME const
          NSNotificationName FIRMessagingRegistrationTokenRefreshedNotification

- `


  ### [FIRMessagingErrorDomain](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Constants#/c:@FIRMessagingErrorDomain)


  ` The domain used for all errors in Messaging.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME NSString *const FIRMessagingErrorDomain
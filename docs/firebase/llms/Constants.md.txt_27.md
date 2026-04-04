# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Constants.md.txt

# FirebaseMessaging Framework Reference

# Constants

The following constants are available globally.
- `


  ### [MessagingRegistrationTokenRefreshed](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Constants#/c:@FIRMessagingRegistrationTokenRefreshedNotification)


  ` Notification sent when the FCM registration token has been refreshed. Please use the
  FIRMessaging delegate method `messaging:didReceiveRegistrationToken:` to receive current and
  updated tokens.

  #### Declaration

  Swift

      static let MessagingRegistrationTokenRefreshed: NSNotification.Name

- `


  ### [MessagingErrorDomain](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Constants#/c:@FIRMessagingErrorDomain)


  ` The domain used for all errors in Messaging.

  #### Declaration

  Swift

      let MessagingErrorDomain: String
# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums.md.txt

# FirebaseMessaging Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [_ErrorType](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/_ErrorType)


  ` @enum FIRMessagingError

  #### Declaration

  Swift

      typealias MessagingError.Code._ErrorType = MessagingError

- `


  ### [MessagingMessageStatus](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingMessageStatus)


  ` Status for the downstream message received by the app.

  #### Declaration

  Swift

      enum MessagingMessageStatus : Int, @unchecked Sendable

- `


  ### [MessagingAPNSTokenType](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingAPNSTokenType)


  ` The APNs token type for the app. If the token type is set to `UNKNOWN`
  Firebase Messaging will implicitly try to figure out what the actual token type
  is from the provisioning profile.
  Unless you really need to specify the type, you should use the `APNSToken`
  property instead.

  #### Declaration

  Swift

      enum MessagingAPNSTokenType : Int, @unchecked Sendable
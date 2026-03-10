# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums.md.txt

# FirebaseMessaging Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRMessagingError](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError)


  ` @enum FIRMessagingError

  #### Declaration

  Objective-C

      enum FIRMessagingError : NSInteger {}

- `


  ### [FIRMessagingMessageStatus](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingMessageStatus)


  ` Status for the downstream message received by the app.

  #### Declaration

  Objective-C

      enum FIRMessagingMessageStatus : NSInteger {}

- `


  ### [FIRMessagingAPNSTokenType](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingAPNSTokenType)


  ` The APNs token type for the app. If the token type is set to `UNKNOWN`
  Firebase Messaging will implicitly try to figure out what the actual token type
  is from the provisioning profile.
  Unless you really need to specify the type, you should use the `APNSToken`
  property instead.

  #### Declaration

  Objective-C

      enum FIRMessagingAPNSTokenType : NSInteger {}
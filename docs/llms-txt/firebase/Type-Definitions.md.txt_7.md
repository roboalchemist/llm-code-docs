# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Type-Definitions.md.txt

# FirebaseMessaging Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRMessagingFCMTokenFetchCompletion](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Type-Definitions#/c:FIRMessaging.h@T@FIRMessagingFCMTokenFetchCompletion)


  ` @related FIRMessaging

  The completion handler invoked when the registration token returns.
  If the call fails we return the appropriate `error code`, described by
  `https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError`.

  #### Declaration

  Objective-C

      typedef void (^FIRMessagingFCMTokenFetchCompletion)(NSString *_Nullable,
                                                          NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` FCMToken ` | The valid registration token returned by FCM. |
  | ` error ` | The error describing why a token request failed. The error code will match a value from the FIRMessagingError enumeration. |

- `


  ### [FIRMessagingDeleteFCMTokenCompletion](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Type-Definitions#/c:FIRMessaging.h@T@FIRMessagingDeleteFCMTokenCompletion)


  ` @related FIRMessaging

  The completion handler invoked when the registration token deletion request is
  completed. If the call fails we return the appropriate `error code`, described
  by `https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingError`.

  #### Declaration

  Objective-C

      typedef void (^FIRMessagingDeleteFCMTokenCompletion)(NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` error ` | The error describing why a token deletion failed. The error code will match a value from the FIRMessagingError enumeration. |

- `


  ### [FIRMessagingTopicOperationCompletion](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Type-Definitions#/c:FIRMessaging.h@T@FIRMessagingTopicOperationCompletion)


  ` Callback to invoke once the HTTP call to FIRMessaging backend for updating
  subscription finishes.

  #### Declaration

  Objective-C

      typedef void (^FIRMessagingTopicOperationCompletion)(NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` error ` | The error which occurred while updating the subscription topic on the FIRMessaging server. This will be nil in case the operation was successful, or if the operation was cancelled. |
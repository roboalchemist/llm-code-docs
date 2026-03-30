# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions.md.txt

# FirebaseRemoteConfig Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRRemoteConfigFetchCompletion](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigFetchCompletion)


  ` Completion handler invoked by fetch methods when they get a response from the server.

  #### Declaration

  Objective-C

      typedef void (^FIRRemoteConfigFetchCompletion)(https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchStatus,
                                                     NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` status ` | Config fetching status. |
  | ` error ` | Error message on failure. |

- `


  ### [FIRRemoteConfigActivateCompletion](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigActivateCompletion)


  ` Completion handler invoked by activate method upon completion.

  #### Declaration

  Objective-C

      typedef void (^FIRRemoteConfigActivateCompletion)(NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` error ` | Error message on failure. Nil if activation was successful. |

- `


  ### [FIRRemoteConfigInitializationCompletion](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigInitializationCompletion)


  ` Completion handler invoked upon completion of Remote Config initialization.

  #### Declaration

  Objective-C

      typedef void (^FIRRemoteConfigInitializationCompletion)(NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` initializationError ` | nil if initialization succeeded. |

- `


  ### [FIRRemoteConfigFetchAndActivateCompletion](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigFetchAndActivateCompletion)


  ` Completion handler invoked by the fetchAndActivate method. Used to convey status of fetch and,
  if successful, resultant activate call

  #### Declaration

  Objective-C

      typedef void (^FIRRemoteConfigFetchAndActivateCompletion)(
          https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` status ` | Config fetching status. |
  | ` error ` | Error message on failure of config fetch |

[## FIRRemoteConfig](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/FIRRemoteConfig)

- `


  ### [FIRRemoteConfigUpdateCompletion](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Type-Definitions#/c:FIRRemoteConfig.h@T@FIRRemoteConfigUpdateCompletion)


  ` Completion handler invoked by `addOnConfigUpdateListener` when there is an update to
  the config from the backend.

  #### Declaration

  Objective-C

      typedef void (^FIRRemoteConfigUpdateCompletion)(
          https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigUpdate *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` configUpdate ` | An instance of `https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Classes/FIRRemoteConfigUpdate` that contains information on which key's values have changed. |
  | ` error ` | Error message on failure. |
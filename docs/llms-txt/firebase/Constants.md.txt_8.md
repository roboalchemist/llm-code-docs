# Source: https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Constants.md.txt

# FirebaseMLCommon Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRModelDownloadDidSucceedNotification](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadDidSucceedNotification)


  ` `Notification` name for observing model download tasks that succeed. The user info dictionary
  will contain `{ModelDownloadUserInfoKey.remoteModel : RemoteModel}`.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(firebaseMLModelDownloadDidSucceed) const NSNotificationName
          FIRModelDownloadDidSucceedNotification

- `


  ### [FIRModelDownloadDidFailNotification](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadDidFailNotification)


  ` `Notification` name for observing model download tasks that fail. The user info dictionary will
  contain `{ModelDownloadUserInfoKey.remoteModel : RemoteModel}` and
  `{ModelDownloadUserInfoKey.error : NSError}`.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(firebaseMLModelDownloadDidFail) const NSNotificationName
          FIRModelDownloadDidFailNotification

- `


  ### [FIRModelDownloadUserInfoKeyRemoteModel](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadUserInfoKeyRemoteModel)


  ` The key for retrieving the `RemoteModel` from the user info dictionary.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Type-Definitions#/c:FIRModelDownloadNotifications.h@T@FIRModelDownloadUserInfoKey _Nonnull FIRModelDownloadUserInfoKeyRemoteModel

- `


  ### [FIRModelDownloadUserInfoKeyError](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadUserInfoKeyError)


  ` The key for retrieving the `NSError` from the user info dictionary. The corresponding value is
  `nil` if the model download completed successfully.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Type-Definitions#/c:FIRModelDownloadNotifications.h@T@FIRModelDownloadUserInfoKey _Nonnull FIRModelDownloadUserInfoKeyError
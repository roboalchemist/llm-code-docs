# Source: https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants.md.txt

# FirebaseMLCommon Framework Reference

# Constants

The following constants are available globally.
- `


  ### [firebaseMLModelDownloadDidSucceed](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadDidSucceedNotification)


  ` `Notification` name for observing model download tasks that succeed. The user info dictionary
  will contain `{ModelDownloadUserInfoKey.remoteModel : RemoteModel}`.

  #### Declaration

  Swift

      static let firebaseMLModelDownloadDidSucceed: NSNotification.Name

- `


  ### [firebaseMLModelDownloadDidFail](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadDidFailNotification)


  ` `Notification` name for observing model download tasks that fail. The user info dictionary will
  contain `{ModelDownloadUserInfoKey.remoteModel : RemoteModel}` and
  `{ModelDownloadUserInfoKey.error : NSError}`.

  #### Declaration

  Swift

      static let firebaseMLModelDownloadDidFail: NSNotification.Name

- `


  ### [remoteModel](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadUserInfoKeyRemoteModel)


  ` The key for retrieving the `https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/RemoteModel` from the user info dictionary.

  #### Declaration

  Swift

      static let remoteModel: https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Type-Definitions#/c:FIRModelDownloadNotifications.h@T@FIRModelDownloadUserInfoKey

- `


  ### [error](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Constants#/c:@FIRModelDownloadUserInfoKeyError)


  ` The key for retrieving the `NSError` from the user info dictionary. The corresponding value is
  `nil` if the model download completed successfully.

  #### Declaration

  Swift

      static let error: https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Type-Definitions#/c:FIRModelDownloadNotifications.h@T@FIRModelDownloadUserInfoKey
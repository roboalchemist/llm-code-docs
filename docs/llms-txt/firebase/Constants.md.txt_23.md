# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Constants.md.txt

# FirebaseAppCheck Framework Reference

# Constants

The following constants are available globally.
- `


  ### [AppCheckTokenDidChange](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Constants#/c:@FIRAppCheckAppCheckTokenDidChangeNotification)


  ` A notification with the specified name is sent to the default notification center
  (`NotificationCenter.default`) each time a Firebase app check token is refreshed.
  The user info dictionary contains `kFIRAppCheckTokenNotificationKey` and
  `kFIRAppCheckAppNameNotificationKey` keys.

  #### Declaration

  Swift

      static let AppCheckTokenDidChange: NSNotification.Name

- `


  ### [AppCheckTokenNotificationKey](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Constants#/c:@kFIRAppCheckTokenNotificationKey)


  ` `userInfo` key for the `FirebaseApp.name` in `AppCheckTokenDidChangeNotification`.

  #### Declaration

  Swift

      let AppCheckTokenNotificationKey: String

- `


  ### [AppCheckAppNameNotificationKey](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Constants#/c:@kFIRAppCheckAppNameNotificationKey)


  ` `userInfo` key for the `https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken` in `AppCheckTokenDidChangeNotification`.

  #### Declaration

  Swift

      let AppCheckAppNameNotificationKey: String

- `


  ### [AppCheckErrorDomain](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Constants#/c:@FIRAppCheckErrorDomain)


  ` Firebase app check error domain.

  #### Declaration

  Swift

      let AppCheckErrorDomain: String
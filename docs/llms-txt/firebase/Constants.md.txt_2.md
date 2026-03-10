# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants.md.txt

# FirebaseAppCheck Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRAppCheckAppCheckTokenDidChangeNotification](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@FIRAppCheckAppCheckTokenDidChangeNotification)


  ` A notification with the specified name is sent to the default notification center
  (`NotificationCenter.default`) each time a Firebase app check token is refreshed.
  The user info dictionary contains `https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@kFIRAppCheckTokenNotificationKey` and
  `https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@kFIRAppCheckAppNameNotificationKey` keys.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AppCheckTokenDidChange) const NSNotificationName
          FIRAppCheckAppCheckTokenDidChangeNotification

- `


  ### [kFIRAppCheckTokenNotificationKey](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@kFIRAppCheckTokenNotificationKey)


  ` `userInfo` key for the `FirebaseApp.name` in `AppCheckTokenDidChangeNotification`.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AppCheckTokenNotificationKey) NSString *const
          kFIRAppCheckTokenNotificationKey

- `


  ### [kFIRAppCheckAppNameNotificationKey](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@kFIRAppCheckAppNameNotificationKey)


  ` `userInfo` key for the `AppCheckToken` in `AppCheckTokenDidChangeNotification`.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(AppCheckAppNameNotificationKey) NSString *const
          kFIRAppCheckAppNameNotificationKey

- `


  ### [FIRAppCheckErrorDomain](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@FIRAppCheckErrorDomain)


  ` Firebase app check error domain.

  #### Declaration

  Objective-C

      extern const NSErrorDomain FIRAppCheckErrorDomain
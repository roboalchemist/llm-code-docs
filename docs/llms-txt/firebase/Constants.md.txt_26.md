# Source: https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Constants.md.txt

# FirebaseInstanceID Framework Reference

# Constants


Firebase Instance ID is deprecated. Please use Firebase Installations instead.

The following constants are available globally.
- `


  ### [InstanceIDScopeFirebaseMessaging](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Constants#/c:@kFIRInstanceIDScopeFirebaseMessaging)


  ` The scope to be used when fetching/deleting a token for Firebase Messaging.

  #### Declaration

  Swift

      let InstanceIDScopeFirebaseMessaging: String

- `


  ### [InstanceIDTokenRefresh](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Constants#/c:@kFIRInstanceIDTokenRefreshNotification)


  ` Called when the system determines that tokens need to be refreshed.
  This method is also called if Instance ID has been reset in which
  case, tokens and FCM topic subscriptions also need to be refreshed.

  Instance ID service will throttle the refresh event across all devices
  to control the rate of token updates on application servers.

  #### Declaration

  Swift

      static let InstanceIDTokenRefresh: NSNotification.Name
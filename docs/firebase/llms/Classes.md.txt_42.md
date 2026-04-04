# Source: https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes.md.txt

# FirebaseInstanceID Framework Reference

# Classes


Firebase Instance ID is deprecated. Please use Firebase Installations instead.

The following classes are available globally.
- `


  ### [InstanceIDResult](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceIDResult)


  ` A class contains the results of InstanceID and token query.

  #### Declaration

  Swift

      class InstanceIDResult : NSObject, NSCopying

- `


  ### [InstanceID](https://firebase.google.com/docs/reference/swift/firebaseinstanceid/api/reference/Classes/InstanceID)


  ` Firebase Instance ID is deprecated. Please use Firebase Installations instead.

  Instance ID provides a unique identifier for each app instance and a mechanism
  to authenticate and authorize actions (for example, sending an FCM message).

  Once an InstanceID is generated, the library periodically sends information about the
  application and the device where it's running to the Firebase backend. To stop this. see
  `[FIRInstanceID deleteIDWithHandler:]`.

  Instance ID is long lived but, may be reset if the device is not used for
  a long time or the Instance ID service detects a problem.
  If Instance ID is reset, the app will be notified via
  `kFIRInstanceIDTokenRefreshNotification`.

  If the Instance ID has become invalid, the app can request a new one and
  send it to the app server.
  To prove ownership of Instance ID and to allow servers to access data or
  services associated with the app, call
  `[FIRInstanceID tokenWithAuthorizedEntity:scope:options:handler]`.

  #### Declaration

  Swift

      class InstanceID : NSObject
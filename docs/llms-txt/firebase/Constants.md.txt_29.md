# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Constants.md.txt

# FirebaseRemoteConfig Framework Reference

# Constants

The following constants are available globally.
- `


  ### [NamespaceGoogleMobilePlatform](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Constants#/c:@FIRNamespaceGoogleMobilePlatform)


  ` The Firebase Remote Config service default namespace, to be used if the API method does not
  specify a different namespace. Use the default namespace if configuring from the Google Firebase
  service.

  #### Declaration

  Swift

      let NamespaceGoogleMobilePlatform: String

- `


  ### [RemoteConfigThrottledEndTimeInSecondsKey](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigThrottledEndTimeInSecondsKey)


  ` Key used to manage throttling in NSError user info when the refreshing of Remote Config
  parameter values (data) is throttled. The value of this key is the elapsed time since 1970,
  measured in seconds.

  #### Declaration

  Swift

      let RemoteConfigThrottledEndTimeInSecondsKey: String

- `


  ### [RemoteConfigErrorDomain](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigErrorDomain)


  ` Remote Config error domain that handles errors when fetching data from the service.

  #### Declaration

  Swift

      let RemoteConfigErrorDomain: String

- `


  ### [RemoteConfigUpdateErrorDomain](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigUpdateErrorDomain)


  ` Remote Config error domain that handles errors for the real-time config update service.

  #### Declaration

  Swift

      let RemoteConfigUpdateErrorDomain: String

- `


  ### [RemoteConfigCustomSignalsErrorDomain](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigCustomSignalsErrorDomain)


  ` Error domain for custom signals errors.

  #### Declaration

  Swift

      let RemoteConfigCustomSignalsErrorDomain: String
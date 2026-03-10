# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Constants.md.txt

# FirebaseRemoteConfig Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRNamespaceGoogleMobilePlatform](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Constants#/c:@FIRNamespaceGoogleMobilePlatform)


  ` The Firebase Remote Config service default namespace, to be used if the API method does not
  specify a different namespace. Use the default namespace if configuring from the Google Firebase
  service.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME NSString *const FIRNamespaceGoogleMobilePlatform

- `


  ### [FIRRemoteConfigThrottledEndTimeInSecondsKey](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigThrottledEndTimeInSecondsKey)


  ` Key used to manage throttling in NSError user info when the refreshing of Remote Config
  parameter values (data) is throttled. The value of this key is the elapsed time since 1970,
  measured in seconds.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME NSString *const FIRRemoteConfigThrottledEndTimeInSecondsKey

- `


  ### [FIRRemoteConfigErrorDomain](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigErrorDomain)


  ` Remote Config error domain that handles errors when fetching data from the service.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME NSString *const FIRRemoteConfigErrorDomain

- `


  ### [FIRRemoteConfigUpdateErrorDomain](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigUpdateErrorDomain)


  ` Remote Config error domain that handles errors for the real-time config update service.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME NSString *const FIRRemoteConfigUpdateErrorDomain

- `


  ### [FIRRemoteConfigCustomSignalsErrorDomain](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Constants#/c:@FIRRemoteConfigCustomSignalsErrorDomain)


  ` Error domain for custom signals errors.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME NSString *const FIRRemoteConfigCustomSignalsErrorDomain
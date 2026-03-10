# Source: https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums.md.txt

# FirebaseRemoteConfig Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRRemoteConfigFetchStatus](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchStatus)


  ` Indicates whether updated data was successfully fetched.

  #### Declaration

  Objective-C

      enum FIRRemoteConfigFetchStatus : NSInteger {}

- `


  ### [FIRRemoteConfigFetchAndActivateStatus](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigFetchAndActivateStatus)


  ` Indicates whether updated data was successfully fetched and activated.

  #### Declaration

  Objective-C

      enum FIRRemoteConfigFetchAndActivateStatus : NSInteger {}

- `


  ### [FIRRemoteConfigError](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigError)


  ` Firebase Remote Config service fetch error.

  #### Declaration

  Objective-C

      enum FIRRemoteConfigError : NSInteger {}

- `


  ### [FIRRemoteConfigUpdateError](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigUpdateError)


  ` Firebase Remote Config real-time config update service error.

  #### Declaration

  Objective-C

      enum FIRRemoteConfigUpdateError : NSInteger {}

- `


  ### [FIRRemoteConfigCustomSignalsError](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigCustomSignalsError)


  ` Firebase Remote Config custom signals error.

  #### Declaration

  Objective-C

      enum FIRRemoteConfigCustomSignalsError : NSInteger {}

- `


  ### [FIRRemoteConfigSource](https://firebase.google.com/docs/reference/ios/firebaseremoteconfig/api/reference/Enums/FIRRemoteConfigSource)


  ` Enumerated value that indicates the source of Remote Config data. Data can come from
  the Remote Config service, the DefaultConfig that is available when the app is first installed,
  or a static initialized value if data is not available from the service or DefaultConfig.

  #### Declaration

  Objective-C

      enum FIRRemoteConfigSource : NSInteger {}
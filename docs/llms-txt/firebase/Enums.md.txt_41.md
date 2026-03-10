# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums.md.txt

# FirebaseRemoteConfig Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [RemoteConfigFetchStatus](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchStatus)


  ` Indicates whether updated data was successfully fetched.

  #### Declaration

  Swift

      enum RemoteConfigFetchStatus : Int, @unchecked Sendable

- `


  ### [RemoteConfigFetchAndActivateStatus](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigFetchAndActivateStatus)


  ` Indicates whether updated data was successfully fetched and activated.

  #### Declaration

  Swift

      enum RemoteConfigFetchAndActivateStatus : Int, @unchecked Sendable

- `


  ### [_ErrorType](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/_ErrorType)


  ` Firebase Remote Config service fetch error.

  #### Declaration

  Swift

      typealias RemoteConfigError.Code._ErrorType = RemoteConfigError

- `


  ### [_ErrorType](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/_ErrorType)


  ` Firebase Remote Config real-time config update service error.

  #### Declaration

  Swift

      typealias RemoteConfigUpdateError.Code._ErrorType = RemoteConfigUpdateError

- `


  ### [_ErrorType](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/_ErrorType)


  ` Firebase Remote Config custom signals error.

  #### Declaration

  Swift

      typealias RemoteConfigCustomSignalsError.Code._ErrorType = RemoteConfigCustomSignalsError

- `


  ### [RemoteConfigSource](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigSource)


  ` Enumerated value that indicates the source of Remote Config data. Data can come from
  the Remote Config service, the DefaultConfig that is available when the app is first installed,
  or a static initialized value if data is not available from the service or DefaultConfig.

  #### Declaration

  Swift

      enum RemoteConfigSource : Int, @unchecked Sendable

- `


  ### [RemoteConfigValueCodableError](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigValueCodableError)


  ` Undocumented

  #### Declaration

  Swift

      public enum RemoteConfigValueCodableError : Error

- `


  ### [RemoteConfigCodableError](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/RemoteConfigCodableError)


  ` Undocumented

  #### Declaration

  Swift

      public enum RemoteConfigCodableError : Error
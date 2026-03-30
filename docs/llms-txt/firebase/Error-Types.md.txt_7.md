# Source: https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/Error-Types.md.txt

# FirebaseRemoteConfig Framework Reference

# _ErrorType

    typealias RemoteConfigCustomSignalsError.Code._ErrorType = RemoteConfigCustomSignalsError

Firebase Remote Config custom signals error.
- `


  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/Error-Types#/c:@E@FIRRemoteConfigCustomSignalsError@FIRRemoteConfigCustomSignalsErrorUnknown)


  ` Unknown error.

  #### Declaration

  Swift

      static var unknown: RemoteConfigCustomSignalsError.Code { get }

- `


  ### [invalidValueType](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/Error-Types#/c:@E@FIRRemoteConfigCustomSignalsError@FIRRemoteConfigCustomSignalsErrorInvalidValueType)


  ` Invalid value type in the custom signals dictionary.

  #### Declaration

  Swift

      static var invalidValueType: RemoteConfigCustomSignalsError.Code { get }

- `


  ### [limitExceeded](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Enums/Error-Types#/c:@E@FIRRemoteConfigCustomSignalsError@FIRRemoteConfigCustomSignalsErrorLimitExceeded)


  ` Limit exceeded for key length, value length, or number of signals.

  #### Declaration

  Swift

      static var limitExceeded: RemoteConfigCustomSignalsError.Code { get }
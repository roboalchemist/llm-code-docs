# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Enums/Error-Types.md.txt

# FirebaseAppCheck Framework Reference

# _ErrorType

    typealias AppCheckErrorCode.Code._ErrorType = AppCheckErrorCode

Undocumented
- `


  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Enums/Error-Types#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeUnknown)


  ` An unknown or non-actionable error.

  #### Declaration

  Swift

      case unknown = 0

- `


  ### [serverUnreachable](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Enums/Error-Types#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeServerUnreachable)


  ` A network connection error.

  #### Declaration

  Swift

      case serverUnreachable = 1

- `


  ### [invalidConfiguration](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Enums/Error-Types#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeInvalidConfiguration)


  ` Invalid configuration error. Currently, an exception is thrown but this error is reserved
  for future implementations of invalid configuration detection.

  #### Declaration

  Swift

      case invalidConfiguration = 2

- `


  ### [keychain](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Enums/Error-Types#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeKeychain)


  ` System keychain access error. Ensure that the app has proper keychain access.

  #### Declaration

  Swift

      case keychain = 3

- `


  ### [unsupported](https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Enums/Error-Types#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeUnsupported)


  ` Selected app attestation provider is not supported on the current platform or OS version.

  #### Declaration

  Swift

      case unsupported = 4
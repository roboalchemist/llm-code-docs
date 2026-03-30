# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums.md.txt

# FirebaseAppCheck Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRAppCheckErrorCode](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode)


  ` Undocumented

  #### Declaration

  Objective-C

      NS_ERROR_ENUM(https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants#/c:@FIRAppCheckErrorDomain, FIRAppCheckErrorCode){
          /// An unknown or non-actionable error.
          FIRAppCheckErrorCodeUnknown = 0,

          /// A network connection error.
          FIRAppCheckErrorCodeServerUnreachable = 1,

          /// Invalid configuration error. Currently, an exception is thrown but this error is reserved
          /// for future implementations of invalid configuration detection.
          FIRAppCheckErrorCodeInvalidConfiguration = 2,

          /// System keychain access error. Ensure that the app has proper keychain access.
          FIRAppCheckErrorCodeKeychain = 3,

          /// Selected app attestation provider is not supported on the current platform or OS version.
          FIRAppCheckErrorCodeUnsupported = 4

      }
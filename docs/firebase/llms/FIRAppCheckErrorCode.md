# Source: https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode.md.txt

# FirebaseAppCheck Framework Reference

# FIRAppCheckErrorCode

    NS_ERROR_ENUM(https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Constants.html#/c:@FIRAppCheckErrorDomain, FIRAppCheckErrorCode){
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

Undocumented
- `
  ``
  ``
  `

  ### [FIRAppCheckErrorCodeUnknown](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeUnknown)

  `
  `  
  An unknown or non-actionable error.  

  #### Declaration

  Objective-C  

      FIRAppCheckErrorCodeUnknown = 0

- `
  ``
  ``
  `

  ### [FIRAppCheckErrorCodeServerUnreachable](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeServerUnreachable)

  `
  `  
  A network connection error.  

  #### Declaration

  Objective-C  

      FIRAppCheckErrorCodeServerUnreachable = 1

- `
  ``
  ``
  `

  ### [FIRAppCheckErrorCodeInvalidConfiguration](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeInvalidConfiguration)

  `
  `  
  Invalid configuration error. Currently, an exception is thrown but this error is reserved
  for future implementations of invalid configuration detection.  

  #### Declaration

  Objective-C  

      FIRAppCheckErrorCodeInvalidConfiguration = 2

- `
  ``
  ``
  `

  ### [FIRAppCheckErrorCodeKeychain](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeKeychain)

  `
  `  
  System keychain access error. Ensure that the app has proper keychain access.  

  #### Declaration

  Objective-C  

      FIRAppCheckErrorCodeKeychain = 3

- `
  ``
  ``
  `

  ### [FIRAppCheckErrorCodeUnsupported](https://firebase.google.com/docs/reference/ios/firebaseappcheck/api/reference/Enums/FIRAppCheckErrorCode#/c:@E@FIRAppCheckErrorCode@FIRAppCheckErrorCodeUnsupported)

  `
  `  
  Selected app attestation provider is not supported on the current platform or OS version.  

  #### Declaration

  Objective-C  

      FIRAppCheckErrorCodeUnsupported = 4
# Source: https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums/FIRInstallationsErrorCode.md.txt

# FirebaseInstallations Framework Reference

# FIRInstallationsErrorCode

    NS_ERROR_ENUM(https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Constants.html#/c:@kFirebaseInstallationsErrorDomain, FIRInstallationsErrorCode){
        /** Unknown error. See `userInfo` for details. */
        FIRInstallationsErrorCodeUnknown = 0,

        /** Keychain error. See `userInfo` for details. */
        FIRInstallationsErrorCodeKeychain = 1,

        /** Server unreachable. A network error or server is unavailable. See `userInfo` for details. */
        FIRInstallationsErrorCodeServerUnreachable = 2,

        /** FirebaseApp configuration issues e.g. invalid GMP-App-ID, etc. See `userInfo` for details.
         */
        FIRInstallationsErrorCodeInvalidConfiguration = 3,

    }

Undocumented
- `
  ``
  ``
  `

  ### [FIRInstallationsErrorCodeUnknown](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums/FIRInstallationsErrorCode#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeUnknown)

  `
  `  
  Unknown error. See `userInfo` for details.  

  #### Declaration

  Objective-C  

      FIRInstallationsErrorCodeUnknown = 0

- `
  ``
  ``
  `

  ### [FIRInstallationsErrorCodeKeychain](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums/FIRInstallationsErrorCode#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeKeychain)

  `
  `  
  Keychain error. See `userInfo` for details.  

  #### Declaration

  Objective-C  

      FIRInstallationsErrorCodeKeychain = 1

- `
  ``
  ``
  `

  ### [FIRInstallationsErrorCodeServerUnreachable](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums/FIRInstallationsErrorCode#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeServerUnreachable)

  `
  `  
  Server unreachable. A network error or server is unavailable. See `userInfo` for details.  

  #### Declaration

  Objective-C  

      FIRInstallationsErrorCodeServerUnreachable = 2

- `
  ``
  ``
  `

  ### [FIRInstallationsErrorCodeInvalidConfiguration](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums/FIRInstallationsErrorCode#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeInvalidConfiguration)

  `
  `  
  FirebaseApp configuration issues e.g. invalid GMP-App-ID, etc. See `userInfo` for details.  

  #### Declaration

  Objective-C  

      FIRInstallationsErrorCodeInvalidConfiguration = 3
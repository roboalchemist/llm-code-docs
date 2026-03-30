# Source: https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums.md.txt

# FirebaseInstallations Framework Reference

# Enumerations

The following enumerations are available globally.
- `


  ### [FIRInstallationsErrorCode](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Enums/FIRInstallationsErrorCode)


  ` Undocumented

  #### Declaration

  Objective-C

      NS_ERROR_ENUM(https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Constants#/c:@kFirebaseInstallationsErrorDomain, FIRInstallationsErrorCode){
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
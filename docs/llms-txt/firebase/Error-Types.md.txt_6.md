# Source: https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Enums/Error-Types.md.txt

# FirebaseInstallations Framework Reference

# _ErrorType

    typealias InstallationsErrorCode.Code._ErrorType = InstallationsErrorCode

Undocumented
- `


  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Enums/Error-Types#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeUnknown)


  ` Unknown error. See `userInfo` for details.

  #### Declaration

  Swift

      case unknown = 0

- `


  ### [keychain](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Enums/Error-Types#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeKeychain)


  ` Keychain error. See `userInfo` for details.

  #### Declaration

  Swift

      case keychain = 1

- `


  ### [serverUnreachable](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Enums/Error-Types#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeServerUnreachable)


  ` Server unreachable. A network error or server is unavailable. See `userInfo` for details.

  #### Declaration

  Swift

      case serverUnreachable = 2

- `


  ### [invalidConfiguration](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Enums/Error-Types#/c:@E@FIRInstallationsErrorCode@FIRInstallationsErrorCodeInvalidConfiguration)


  ` FirebaseApp configuration issues e.g. invalid GMP-App-ID, etc. See `userInfo` for details.

  #### Declaration

  Swift

      case invalidConfiguration = 3
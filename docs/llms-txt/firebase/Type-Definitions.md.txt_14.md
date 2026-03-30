# Source: https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Type-Definitions.md.txt

# FirebaseInstallations Framework Reference

# Type Definitions

The following type definitions are available globally.
- `


  ### [FIRInstallationsIDHandler](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Type-Definitions#/c:FIRInstallations.h@T@FIRInstallationsIDHandler)


  ` An installation ID handler block.

  #### Declaration

  Objective-C

      typedef void (^FIRInstallationsIDHandler)(NSString *_Nullable,
                                                NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` identifier ` | The installation ID string if exists or `nil` otherwise. |
  | ` error ` | The error when `identifier == nil` or `nil` otherwise. |

- `


  ### [FIRInstallationsTokenHandler](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Type-Definitions#/c:FIRInstallations.h@T@FIRInstallationsTokenHandler)


  ` An authorization token handler block.

  #### Declaration

  Objective-C

      typedef void (^FIRInstallationsTokenHandler)(
          https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes/FIRInstallationsAuthTokenResult *_Nullable, NSError *_Nullable)

  #### Parameters

  |---|---|
  | ` tokenResult ` | An instance of `InstallationsAuthTokenResult` in case of success or `nil` otherwise. |
  | ` error ` | The error when `tokenResult == nil` or `nil` otherwise. |
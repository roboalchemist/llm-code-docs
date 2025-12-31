# Source: https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations.md.txt

# FirebaseInstallations Framework Reference

# Installations

    class Installations : NSObject

The class provides API for Firebase Installations.
Each configured `FirebaseApp` has a corresponding single instance of `Installations`.
An instance of the class provides access to the installation info for the `FirebaseApp` as well
as the ability to delete it. A Firebase Installation is unique by `FirebaseApp.name` and
`FirebaseApp.options.googleAppID` .
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(im)init)

  `
  `  
  Unavailable  
  Undocumented
- `
  ``
  ``
  `

  ### [installations()](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(cm)installations)

  `
  `  
  Returns a default instance of `Installations`.  

  #### Declaration

  Swift  

      class func installations() -> Installations

  #### Return Value

  An instance of `Installations` for `FirebaseApp.defaultApp().
  @throw Throws an exception if the default app is not configured yet or required`FirebaseApp\`
  options are missing.
- `
  ``
  ``
  `

  ### [installations(app:)](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(cm)installationsWithApp:)

  `
  `  
  Returns an instance of `Installations` for an application.  

  #### Declaration

  Swift  

      class func installations(app application: FIRApp) -> Installations

  #### Parameters

  |---------------------|--------------------------------------|
  | ` `*application*` ` | A configured `FirebaseApp` instance. |

  #### Return Value

  An instance of `Installations` corresponding to the passed application.
  @throw Throws an exception if required `FirebaseApp` options are missing.
- `
  ``
  ``
  `

  ### [installationID()](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(im)installationIDWithCompletion:)

  `
  `  
  The method creates or retrieves an installation ID. The installation ID is a stable identifier
  that uniquely identifies the app instance. NOTE: If the application already has an existing
  FirebaseInstanceID then the InstanceID identifier will be used.  

  #### Declaration

  Swift  

      func installationID() async throws -> String

  #### Parameters

  |--------------------|---------------------------------------------------------------------|
  | ` `*completion*` ` | A completion handler which is invoked when the operation completes. |

- `
  ``
  ``
  `

  ### [authToken()](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(im)authTokenWithCompletion:)

  `
  `  
  Retrieves (locally if it exists or from the server) a valid installation auth token. An existing
  token may be invalidated or expired, so it is recommended to fetch the installation auth token
  before each server request. The method does the same as
  `Installations.authToken(forcingRefresh:completion:)` with forcing refresh `false`.  

  #### Declaration

  Swift  

      func authToken() async throws -> FIRInstallationsAuthTokenResult

  #### Parameters

  |--------------------|---------------------------------------------------------------------|
  | ` `*completion*` ` | A completion handler which is invoked when the operation completes. |

- `
  ``
  ``
  `

  ### [authTokenForcingRefresh(_:)](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(im)authTokenForcingRefresh:completion:)

  `
  `  
  Retrieves (locally or from the server depending on `forceRefresh` value) a valid installation
  auth token. An existing token may be invalidated or expire, so it is recommended to fetch the
  installation auth token before each server request. This method should be used with `forceRefresh
  == true` when e.g. a request with the previously fetched installation auth token failed with "Not
  Authorized" error.  

  #### Declaration

  Swift  

      func authTokenForcingRefresh(_ forceRefresh: Bool) async throws -> FIRInstallationsAuthTokenResult

  #### Parameters

  |----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*forceRefresh*` ` | If `true` then the locally cached installation auth token will be ignored and a new one will be requested from the server. If `false`, then the locally cached installation auth token will be returned if exists and has not expired yet. |
  | ` `*completion*` `   | A completion handler which is invoked when the operation completes. See `InstallationsTokenHandler` for additional details.                                                                                                                |

- `
  ``
  ``
  `

  ### [delete()](https://firebase.google.com/docs/reference/swift/firebaseinstallations/api/reference/Classes/Installations#/c:objc(cs)FIRInstallations(im)deleteWithCompletion:)

  `
  `  
  Deletes all the installation data including the unique identifier, auth tokens and
  all related data on the server side. A network connection is required for the method to
  succeed. If fails, the existing installation data remains untouched.  

  #### Declaration

  Swift  

      func delete() async throws

  #### Parameters

  |--------------------|-------------------------------------------------------------------------------------------------------|
  | ` `*completion*` ` | A completion handler which is invoked when the operation completes. `error == nil` indicates success. |
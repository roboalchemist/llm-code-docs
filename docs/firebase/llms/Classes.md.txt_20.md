# Source: https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes.md.txt

# FirebaseInstallations Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRInstallations](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes/FIRInstallations)


  ` The class provides API for Firebase Installations.
  Each configured `FirebaseApp` has a corresponding single instance of `Installations`.
  An instance of the class provides access to the installation info for the `FirebaseApp` as well
  as the ability to delete it. A Firebase Installation is unique by `FirebaseApp.name` and
  `FirebaseApp.options.googleAppID` .

  #### Declaration

  Objective-C


      @interface FIRInstallations : NSObject

- `


  ### [FIRInstallationsAuthTokenResult](https://firebase.google.com/docs/reference/ios/firebaseinstallations/api/reference/Classes/FIRInstallationsAuthTokenResult)


  ` The class represents a result of the installation auth token request.

  #### Declaration

  Objective-C


      @interface FIRInstallationsAuthTokenResult : NSObject
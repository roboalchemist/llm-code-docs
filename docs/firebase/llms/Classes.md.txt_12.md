# Source: https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes.md.txt

# FirebaseAppDistribution Framework Reference

# Classes

The following classes are available globally.
- `


  ### [FIRAppDistribution](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistribution)


  ` The Firebase App Distribution API provides methods to check for update to
  the app and returns information that enables updating the app.

  By default, Firebase App Distribution is initialized with `FirebaseApp.configure()`.

  Note: The App Distribution class cannot be subclassed. If this makes testing difficult,
  we suggest using a wrapper class or a protocol extension.

  #### Declaration

  Objective-C


      @interface FIRAppDistribution : NSObject

- `


  ### [FIRAppDistributionRelease](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease)


  ` The release information returned by the update check when a new version is available.

  #### Declaration

  Objective-C


      @interface FIRAppDistributionRelease : NSObject
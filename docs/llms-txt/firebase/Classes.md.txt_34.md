# Source: https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes.md.txt

# FirebaseAppDistribution Framework Reference

# Classes

The following classes are available globally.
- `


  ### [AppDistribution](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistribution)


  ` The Firebase App Distribution API provides methods to check for update to
  the app and returns information that enables updating the app.

  By default, Firebase App Distribution is initialized with `FirebaseApp.configure()`.

  Note: The App Distribution class cannot be subclassed. If this makes testing difficult,
  we suggest using a wrapper class or a protocol extension.

  #### Declaration

  Swift

      class AppDistribution : NSObject

- `


  ### [AppDistributionRelease](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease)


  ` The release information returned by the update check when a new version is available.

  #### Declaration

  Swift

      class AppDistributionRelease : NSObject
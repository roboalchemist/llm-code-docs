# Source: https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease.md.txt

# FirebaseAppDistribution Framework Reference

# AppDistributionRelease

    class AppDistributionRelease : NSObject

The release information returned by the update check when a new version is available.
- `


  ### [displayVersion](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)displayVersion)


  ` The short bundle version of this build (example 1.0.0).

  #### Declaration

  Swift

      var displayVersion: String { get }

- `


  ### [buildVersion](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)buildVersion)


  ` The build number of this build (example: 123).

  #### Declaration

  Swift

      var buildVersion: String { get }

- `


  ### [releaseNotes](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)releaseNotes)


  ` The release notes for this build.

  #### Declaration

  Swift

      var releaseNotes: String? { get }

- `


  ### [downloadURL](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)downloadURL)


  ` The URL for the build.

  #### Declaration

  Swift

      var downloadURL: URL { get }

- `


  ### [isExpired](https://firebase.google.com/docs/reference/swift/firebaseappdistribution/api/reference/Classes/AppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)isExpired)


  ` Whether the download URL for this release is expired.

  #### Declaration

  Swift

      var isExpired: Bool { get }
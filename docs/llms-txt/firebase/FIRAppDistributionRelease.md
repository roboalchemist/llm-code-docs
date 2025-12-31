# Source: https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease.md.txt

# FirebaseAppDistribution Framework Reference

# FIRAppDistributionRelease


    @interface FIRAppDistributionRelease : NSObject

The release information returned by the update check when a new version is available.
- `
  ``
  ``
  `

  ### [displayVersion](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)displayVersion)

  `
  `  
  The short bundle version of this build (example 1.0.0).  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull displayVersion;

- `
  ``
  ``
  `

  ### [buildVersion](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)buildVersion)

  `
  `  
  The build number of this build (example: 123).  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull buildVersion;

- `
  ``
  ``
  `

  ### [releaseNotes](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)releaseNotes)

  `
  `  
  The release notes for this build.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *releaseNotes;

- `
  ``
  ``
  `

  ### [downloadURL](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)downloadURL)

  `
  `  
  The URL for the build.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSURL *_Nonnull downloadURL;

- `
  ``
  ``
  `

  ### [isExpired](https://firebase.google.com/docs/reference/ios/firebaseappdistribution/api/reference/Classes/FIRAppDistributionRelease#/c:objc(cs)FIRAppDistributionRelease(py)isExpired)

  `
  `  
  Whether the download URL for this release is expired.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL isExpired;
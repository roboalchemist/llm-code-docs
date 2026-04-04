# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings.md.txt

# FirebaseAuth Framework Reference

# FIRActionCodeSettings


    @interface FIRActionCodeSettings : NSObject

Used to set and retrieve settings related to handling action codes.
- `
  ``
  ``
  `

  ### [URL](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)URL)

  `
  `  
  This URL represents the state/Continue URL in the form of a universal link.
  This URL can should be constructed as a universal link that would either directly open
  the app where the action code would be handled or continue to the app after the action code
  is handled by Firebase.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSURL *URL;

- `
  ``
  ``
  `

  ### [handleCodeInApp](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)handleCodeInApp)

  `
  `  
  Indicates whether the action code link will open the app directly or after being
  redirected from a Firebase owned web widget.  

  #### Declaration

  Objective-C  

      @property (nonatomic) BOOL handleCodeInApp;

- `
  ``
  ``
  `

  ### [iOSBundleID](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)iOSBundleID)

  `
  `  
  The iOS bundle ID, if available. The default value is the current app's bundle ID.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *iOSBundleID;

- `
  ``
  ``
  `

  ### [androidPackageName](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)androidPackageName)

  `
  `  
  The Android package name, if available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *androidPackageName;

- `
  ``
  ``
  `

  ### [androidMinimumVersion](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)androidMinimumVersion)

  `
  `  
  The minimum Android version supported, if available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *androidMinimumVersion;

- `
  ``
  ``
  `

  ### [androidInstallIfNotAvailable](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)androidInstallIfNotAvailable)

  `
  `  
  Indicates whether the Android app should be installed on a device where it is not
  available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL androidInstallIfNotAvailable;

- `
  ``
  ``
  `

  ### [dynamicLinkDomain](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(py)dynamicLinkDomain)

  `
  `  
  The Firebase Dynamic Link domain used for out of band code flow.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *dynamicLinkDomain;

- `
  ``
  ``
  `

  ### [-setAndroidPackageName:installIfNotAvailable:minimumVersion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRActionCodeSettings#/c:objc(cs)FIRActionCodeSettings(im)setAndroidPackageName:installIfNotAvailable:minimumVersion:)

  `
  `  
  Sets the Android package name, the flag to indicate whether or not to install the app
  and the minimum Android version supported.  

  #### Declaration

  Objective-C  

      - (void)setAndroidPackageName:(nonnull NSString *)androidPackageName
              installIfNotAvailable:(BOOL)installIfNotAvailable
                     minimumVersion:(nullable NSString *)minimumVersion;

  #### Parameters

  |-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*androidPackageName*` `    | The Android package name.                                                                                                                                                                                             |
  | ` `*installIfNotAvailable*` ` | Indicates whether or not the app should be installed if not available.                                                                                                                                                |
  | ` `*minimumVersion*` `        | The minimum version of Android supported. If installIfNotAvailable is set to YES and the link is opened on an android device, it will try to install the app if not already available. Otherwise the web URL is used. |
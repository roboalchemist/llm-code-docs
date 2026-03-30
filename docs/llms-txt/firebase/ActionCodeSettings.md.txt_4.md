# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings.md.txt

# FirebaseAuth Framework Reference

# ActionCodeSettings

    @objc(FIRActionCodeSettings)
    open class ActionCodeSettings: NSObject,
      @unchecked Sendable

Used to set and retrieve settings related to handling action codes.
- `


  ### [url](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)URL)


  ` This URL represents the state/Continue URL in the form of a universal link.

  This URL can should be constructed as a universal link that would either directly open
  the app where the action code would be handled or continue to the app after the action code
  is handled by Firebase.

  #### Declaration

  Swift

      @objc(URL)
      open var url: URL? { get set }

- `


  ### [handleCodeInApp](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)handleCodeInApp)


  ` Indicates whether the action code link will open the app directly or after being
  redirected from a Firebase owned web widget.

  #### Declaration

  Swift

      @objc
      open var handleCodeInApp: Bool { get set }

- `


  ### [iOSBundleID](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)iOSBundleID)


  ` The iOS bundle ID, if available. The default value is the current app's bundle ID.

  #### Declaration

  Swift

      @objc
      open var iOSBundleID: String? { get set }

- `


  ### [androidPackageName](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)androidPackageName)


  ` The Android package name, if available.

  #### Declaration

  Swift

      @objc
      open var androidPackageName: String? { get set }

- `


  ### [androidMinimumVersion](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)androidMinimumVersion)


  ` The minimum Android version supported, if available.

  #### Declaration

  Swift

      @objc
      open var androidMinimumVersion: String? { get set }

- `


  ### [androidInstallIfNotAvailable](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)androidInstallIfNotAvailable)


  ` Indicates whether the Android app should be installed on a device where it is not available.

  #### Declaration

  Swift

      @objc
      open var androidInstallIfNotAvailable: Bool { get set }

- `


  ### [linkDomain](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(py)linkDomain)


  ` The out of band custom domain for handling code in app.

  #### Declaration

  Swift

      @objc
      public var linkDomain: String? { get set }

- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(im)init)


  ` Sets the iOS bundle ID.

  #### Declaration

  Swift

      override public init()

- `


  ### [setAndroidPackageName(_:installIfNotAvailable:minimumVersion:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/c:@M@FirebaseAuth@objc(cs)FIRActionCodeSettings(im)setAndroidPackageName:installIfNotAvailable:minimumVersion:)


  ` Sets the Android package name, the flag to indicate whether or not to install the app,
  and the minimum Android version supported.

  If `installIfNotAvailable` is set to `true` and the link is opened on an android device, it
  will try to install the app if not already available. Otherwise the web URL is used.

  #### Declaration

  Swift

      @objc
      open func setAndroidPackageName(_ androidPackageName: String,
                                      installIfNotAvailable: Bool,
                                      minimumVersion: String?)

  #### Parameters

  |---|---|
  | ` androidPackageName ` | The Android package name. |
  | ` installIfNotAvailable ` | Indicates whether or not the app should be installed if not available. |
  | ` minimumVersion ` | The minimum version of Android supported. |

- `


  ### [setIOSBundleID(_:)](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/ActionCodeSettings#/s:12FirebaseAuth18ActionCodeSettingsC14setIOSBundleIDyySSF)


  ` Sets the iOS bundle ID.

  #### Declaration

  Swift

      open func setIOSBundleID(_ bundleID: String)
# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkIOSParameters


    @interface FIRDynamicLinkIOSParameters : NSObject

The Dynamic Link iOS parameters.
- `
  ``
  ``
  `

  ### [bundleID](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)bundleID)

  `
  `  
  The bundle ID of the iOS app to use to open the link.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *bundleID;

- `
  ``
  ``
  `

  ### [appStoreID](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)appStoreID)

  `
  `  
  The appStore ID of the iOS app in AppStore.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *appStoreID;

- `
  ``
  ``
  `

  ### [fallbackURL](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)fallbackURL)

  `
  `  
  The link to open when the app isn't installed. Specify this to do something other than
  install the app from the App Store when the app isn't installed, such as open the mobile
  web version of the content, or display a promotional page for the app.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSURL *fallbackURL;

- `
  ``
  ``
  `

  ### [customScheme](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)customScheme)

  `
  `  
  The target app's custom URL scheme, if defined to be something other than the app's
  bundle ID  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *customScheme;

- `
  ``
  ``
  `

  ### [iPadBundleID](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)iPadBundleID)

  `
  `  
  The bundle ID of the iOS app to use on iPads to open the link. This is only required if
  there are separate iPhone and iPad applications.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *iPadBundleID;

- `
  ``
  ``
  `

  ### [iPadFallbackURL](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)iPadFallbackURL)

  `
  `  
  The link to open on iPads when the app isn't installed. Specify this to do something
  other than install the app from the App Store when the app isn't installed, such as open the
  web version of the content, or display a promotional page for the app.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSURL *iPadFallbackURL;

- `
  ``
  ``
  `

  ### [minimumAppVersion](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)minimumAppVersion)

  `
  `  
  The minimum version of your app that can open the link. If the
  - installed app is an older version, the user is taken to the AppStore to upgrade the app.

  Note
  It is app's developer responsibility to open AppStore when received link declares
  - higher minimumAppVersion than currently installed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *minimumAppVersion;

- `
  ``
  ``
  `

  ### [+parametersWithBundleID:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(cm)parametersWithBundleID:)

  `
  `  
  A method for creating the iOS parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parametersWithBundleID:(nonnull NSString *)bundleID;

  #### Parameters

  |------------------|-------------------------------------------------------|
  | ` `*bundleID*` ` | The bundle ID of the iOS app to use to open the link. |

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add iOS parameters to a
  generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-initWithBundleID:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(im)initWithBundleID:)

  `
  `  
  A method for creating the iOS parameters object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithBundleID:(nonnull NSString *)bundleID;

  #### Parameters

  |------------------|-------------------------------------------------------|
  | ` `*bundleID*` ` | The bundle ID of the iOS app to use to open the link. |

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add iOS parameters to a
  generated Dynamic Link URL.
# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkIOSParameters

    class DynamicLinkIOSParameters : NSObject

The Dynamic Link iOS parameters.
- `
  ``
  ``
  `

  ### [bundleID](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)bundleID)

  `
  `  
  The bundle ID of the iOS app to use to open the link.  

  #### Declaration

  Swift  

      var bundleID: String? { get }

- `
  ``
  ``
  `

  ### [appStoreID](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)appStoreID)

  `
  `  
  The appStore ID of the iOS app in AppStore.  

  #### Declaration

  Swift  

      var appStoreID: String? { get set }

- `
  ``
  ``
  `

  ### [fallbackURL](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)fallbackURL)

  `
  `  
  The link to open when the app isn't installed. Specify this to do something other than
  install the app from the App Store when the app isn't installed, such as open the mobile
  web version of the content, or display a promotional page for the app.  

  #### Declaration

  Swift  

      var fallbackURL: URL? { get set }

- `
  ``
  ``
  `

  ### [customScheme](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)customScheme)

  `
  `  
  The target app's custom URL scheme, if defined to be something other than the app's
  bundle ID  

  #### Declaration

  Swift  

      var customScheme: String? { get set }

- `
  ``
  ``
  `

  ### [iPadBundleID](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)iPadBundleID)

  `
  `  
  The bundle ID of the iOS app to use on iPads to open the link. This is only required if
  there are separate iPhone and iPad applications.  

  #### Declaration

  Swift  

      var iPadBundleID: String? { get set }

- `
  ``
  ``
  `

  ### [iPadFallbackURL](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)iPadFallbackURL)

  `
  `  
  The link to open on iPads when the app isn't installed. Specify this to do something
  other than install the app from the App Store when the app isn't installed, such as open the
  web version of the content, or display a promotional page for the app.  

  #### Declaration

  Swift  

      var iPadFallbackURL: URL? { get set }

- `
  ``
  ``
  `

  ### [minimumAppVersion](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(py)minimumAppVersion)

  `
  `  
  The minimum version of your app that can open the link. If the
  - installed app is an older version, the user is taken to the AppStore to upgrade the app.

  Note
  It is app's developer responsibility to open AppStore when received link declares
  - higher minimumAppVersion than currently installed.  

  #### Declaration

  Swift  

      var minimumAppVersion: String? { get set }

- `
  ``
  ``
  `

  ### [+parametersWithBundleID:](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(cm)parametersWithBundleID:)

  `
  `  
  A method for creating the iOS parameters object.  

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

  ### [init(bundleID:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkIOSParameters#/c:objc(cs)FIRDynamicLinkIOSParameters(im)initWithBundleID:)

  `
  `  
  A method for creating the iOS parameters object.  

  #### Declaration

  Swift  

      init(bundleID: String)

  #### Parameters

  |------------------|-------------------------------------------------------|
  | ` `*bundleID*` ` | The bundle ID of the iOS app to use to open the link. |

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add iOS parameters to a
  generated Dynamic Link URL.
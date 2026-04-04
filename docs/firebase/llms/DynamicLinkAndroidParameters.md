# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkAndroidParameters

    class DynamicLinkAndroidParameters : NSObject

The Dynamic Link Android parameters.
- `
  ``
  ``
  `

  ### [packageName](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(py)packageName)

  `
  `  
  The Android app's package name.  

  #### Declaration

  Swift  

      var packageName: String? { get }

- `
  ``
  ``
  `

  ### [fallbackURL](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(py)fallbackURL)

  `
  `  
  The link to open when the app isn't installed. Specify this to do something other than
  install the app from the Play Store when the app isn't installed, such as open the mobile web
  version of the content, or display a promotional page for the app.  

  #### Declaration

  Swift  

      var fallbackURL: URL? { get set }

- `
  ``
  ``
  `

  ### [minimumVersion](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(py)minimumVersion)

  `
  `  
  The version code of the minimum version of your app that can open the link. If the
  - installed app is an older version, the user is taken to the Play Store to upgrade the app.  

  #### Declaration

  Swift  

      var minimumVersion: Int { get set }

- `
  ``
  ``
  `

  ### [+parametersWithPackageName:](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(cm)parametersWithPackageName:)

  `
  `  
  A method for creating the Android parameters object.  

  #### Parameters

  |---------------------|---------------------------------|
  | ` `*packageName*` ` | The Android app's package name. |

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Android parameters
  to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [init(packageName:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(im)initWithPackageName:)

  `
  `  
  A method for creating the Android parameters object.  

  #### Declaration

  Swift  

      init(packageName: String)

  #### Parameters

  |---------------------|---------------------------------|
  | ` `*packageName*` ` | The Android app's package name. |

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Android parameters
  to a generated Dynamic Link URL.
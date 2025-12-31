# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkAndroidParameters


    @interface FIRDynamicLinkAndroidParameters : NSObject

The Dynamic Link Android parameters.
- `
  ``
  ``
  `

  ### [packageName](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(py)packageName)

  `
  `  
  The Android app's package name.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *packageName;

- `
  ``
  ``
  `

  ### [fallbackURL](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(py)fallbackURL)

  `
  `  
  The link to open when the app isn't installed. Specify this to do something other than
  install the app from the Play Store when the app isn't installed, such as open the mobile web
  version of the content, or display a promotional page for the app.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSURL *fallbackURL;

- `
  ``
  ``
  `

  ### [minimumVersion](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(py)minimumVersion)

  `
  `  
  The version code of the minimum version of your app that can open the link. If the
  - installed app is an older version, the user is taken to the Play Store to upgrade the app.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSInteger minimumVersion;

- `
  ``
  ``
  `

  ### [+parametersWithPackageName:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(cm)parametersWithPackageName:)

  `
  `  
  A method for creating the Android parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parametersWithPackageName:
          (nonnull NSString *)packageName;

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

  ### [-initWithPackageName:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkAndroidParameters#/c:objc(cs)FIRDynamicLinkAndroidParameters(im)initWithPackageName:)

  `
  `  
  A method for creating the Android parameters object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithPackageName:(nonnull NSString *)packageName;

  #### Parameters

  |---------------------|---------------------------------|
  | ` `*packageName*` ` | The Android app's package name. |

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Android parameters
  to a generated Dynamic Link URL.
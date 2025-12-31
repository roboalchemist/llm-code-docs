# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLink


    @interface FIRDynamicLink : NSObject

A received Dynamic Link.
- `
  ``
  ``
  `

  ### [url](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink#/c:objc(cs)FIRDynamicLink(py)url)

  `
  `  
  The URL that was passed to the app.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSURL *url;

- `
  ``
  ``
  `

  ### [matchType](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink#/c:objc(cs)FIRDynamicLink(py)matchType)

  `
  `  
  The match type of the received Dynamic Link.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRDLMatchType.html matchType;

- `
  ``
  ``
  `

  ### [utmParametersDictionary](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink#/c:objc(cs)FIRDynamicLink(py)utmParametersDictionary)

  `
  `  
  UTM parameters associated with a Firebase Dynamic Link.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSDictionary<NSString *, id> *_Nonnull utmParametersDictionary;

- `
  ``
  ``
  `

  ### [minimumAppVersion](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink#/c:objc(cs)FIRDynamicLink(py)minimumAppVersion)

  `
  `  
  The minimum iOS application version that supports the Dynamic Link. This is retrieved
  from the imv= parameter of the Dynamic Link URL. Note: This is not the minimum iOS system
  version, but the minimum app version. If app version of the opening app is less than the
  value of this property, then app expected to open AppStore to allow user to download most
  recent version. App can notify or ask user before opening AppStore.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly, nullable) NSString *minimumAppVersion;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLink#/c:objc(cs)FIRDynamicLink(im)init)

  `
  `  
  Unavailable  
  Undocumented  

  #### Declaration

  Objective-C  

      - (instancetype)init NS_UNAVAILABLE;
# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkNavigationInfoParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkNavigationInfoParameters


    @interface FIRDynamicLinkNavigationInfoParameters : NSObject

Options class for defining navigation behavior of the Dynamic Link.
- `
  ``
  ``
  `

  ### [forcedRedirectEnabled](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkNavigationInfoParameters#/c:objc(cs)FIRDynamicLinkNavigationInfoParameters(py)forcedRedirectEnabled)

  `
  `  
  Property defines should forced non-interactive redirect be used when link is tapped on
  mobile device. Default behavior is to disable force redirect and show interstitial page where
  user tap will initiate navigation to the App (or AppStore if not installed). Disabled force
  redirect normally improves reliability of the click.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isForcedRedirectEnabled) BOOL forcedRedirectEnabled;

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkNavigationInfoParameters#/c:objc(cs)FIRDynamicLinkNavigationInfoParameters(cm)parameters)

  `
  `  
  A method for creating the Navigation Info parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parameters;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Navigation Info
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkNavigationInfoParameters#/c:objc(cs)FIRDynamicLinkNavigationInfoParameters(im)init)

  `
  `  
  A method for creating the Navigation Info parameters object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Navigation Info
  parameters to a generated Dynamic Link URL.
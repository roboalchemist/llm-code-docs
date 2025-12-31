# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkOtherPlatformParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkOtherPlatformParameters


    @interface FIRDynamicLinkOtherPlatformParameters : NSObject

Options class for defining other platform(s) parameters of the Dynamic Link.
Other here means not covered by specific parameters (not iOS and not Android).
- `
  ``
  ``
  `

  ### [fallbackUrl](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkOtherPlatformParameters#/c:objc(cs)FIRDynamicLinkOtherPlatformParameters(py)fallbackUrl)

  `
  `  
  Property defines fallback URL to navigate to when Dynamic Link is clicked on
  other platform.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSURL *fallbackUrl;

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkOtherPlatformParameters#/c:objc(cs)FIRDynamicLinkOtherPlatformParameters(cm)parameters)

  `
  `  
  A method for creating the Other platform parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parameters;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Other Platform
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkOtherPlatformParameters#/c:objc(cs)FIRDynamicLinkOtherPlatformParameters(im)init)

  `
  `  
  A method for creating the Other platform parameters object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Other Platform
  parameters to a generated Dynamic Link URL.
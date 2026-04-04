# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkItunesConnectAnalyticsParameters


    @interface FIRDynamicLinkItunesConnectAnalyticsParameters : NSObject

The Dynamic Link iTunes Connect parameters.
- `
  ``
  ``
  `

  ### [affiliateToken](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters#/c:objc(cs)FIRDynamicLinkItunesConnectAnalyticsParameters(py)affiliateToken)

  `
  `  
  The iTunes Connect affiliate token.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *affiliateToken;

- `
  ``
  ``
  `

  ### [campaignToken](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters#/c:objc(cs)FIRDynamicLinkItunesConnectAnalyticsParameters(py)campaignToken)

  `
  `  
  The iTunes Connect campaign token.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *campaignToken;

- `
  ``
  ``
  `

  ### [providerToken](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters#/c:objc(cs)FIRDynamicLinkItunesConnectAnalyticsParameters(py)providerToken)

  `
  `  
  The iTunes Connect provider token.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *providerToken;

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters#/c:objc(cs)FIRDynamicLinkItunesConnectAnalyticsParameters(cm)parameters)

  `
  `  
  A method for creating the iTunes Connect parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parameters;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add iTunes Connect
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkItunesConnectAnalyticsParameters#/c:objc(cs)FIRDynamicLinkItunesConnectAnalyticsParameters(im)init)

  `
  `  
  A method for creating the iTunes Connect parameters object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add iTunes Connect
  parameters to a generated Dynamic Link URL.
# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkGoogleAnalyticsParameters


    @interface FIRDynamicLinkGoogleAnalyticsParameters : NSObject

The Dynamic Link analytics parameters.
- `
  ``
  ``
  `

  ### [source](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)source)

  `
  `  
  The utm_source analytics parameter.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *source;

- `
  ``
  ``
  `

  ### [medium](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)medium)

  `
  `  
  The utm_medium analytics parameter.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *medium;

- `
  ``
  ``
  `

  ### [campaign](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)campaign)

  `
  `  
  The utm_campaign analytics parameter.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *campaign;

- `
  ``
  ``
  `

  ### [term](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)term)

  `
  `  
  The utm_term analytics parameter.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *term;

- `
  ``
  ``
  `

  ### [content](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)content)

  `
  `  
  The utm_content analytics parameter.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *content;

- `
  ``
  ``
  `

  ### [+parametersWithSource:medium:campaign:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(cm)parametersWithSource:medium:campaign:)

  `
  `  
  The preferred factory method for creating the analytics parameters object. It includes
  the commonly-used source, medium, and campaign fields.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parametersWithSource:(nonnull NSString *)source
                                            medium:(nonnull NSString *)medium
                                          campaign:(nonnull NSString *)campaign;

  #### Parameters

  |------------------|---------------------------------------|
  | ` `*source*` `   | The utm_source analytics parameter.   |
  | ` `*medium*` `   | The utm_medium analytics parameter.   |
  | ` `*campaign*` ` | The utm_campaign analytics parameter. |

  #### Return Value

  Returns An object to be used with FIRDynamicLinkURLComponents to add analytics parameters
  to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(cm)parameters)

  `
  `  
  A factory method for creating the analytics parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parameters;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add analytics parameters
  to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-initWithSource:medium:campaign:](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(im)initWithSource:medium:campaign:)

  `
  `  
  The preferred instance method for creating the analytics parameters object. It
  includes the commonly-used source, medium, and campaign fields.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithSource:(nonnull NSString *)source
                                      medium:(nonnull NSString *)medium
                                    campaign:(nonnull NSString *)campaign;

  #### Parameters

  |------------------|---------------------------------------|
  | ` `*source*` `   | The utm_source analytics parameter.   |
  | ` `*medium*` `   | The utm_medium analytics parameter.   |
  | ` `*campaign*` ` | The utm_campaign analytics parameter. |

  #### Return Value

  Returns An object to be used with FIRDynamicLinkURLComponents to add analytics parameters
  to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(im)init)

  `
  `  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add analytics parameters
  to a generated Dynamic Link URL.
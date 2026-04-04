# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkSocialMetaTagParameters


    @interface FIRDynamicLinkSocialMetaTagParameters : NSObject

The Dynamic Link Social Meta Tag parameters.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(py)title)

  `
  `  
  The title to use when the Dynamic Link is shared in a social post.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *title;

- `
  ``
  ``
  `

  ### [descriptionText](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(py)descriptionText)

  `
  `  
  The description to use when the Dynamic Link is shared in a social post.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *descriptionText;

- `
  ``
  ``
  `

  ### [imageURL](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(py)imageURL)

  `
  `  
  The URL to an image related to this link.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) NSURL *imageURL;

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(cm)parameters)

  `
  `  
  A method for creating the Social Meta Tag parameters object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)parameters;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Social Meta Tag
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(im)init)

  `
  `  
  A method for creating the Social Meta Tag parameters object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Social Meta Tag
  parameters to a generated Dynamic Link URL.
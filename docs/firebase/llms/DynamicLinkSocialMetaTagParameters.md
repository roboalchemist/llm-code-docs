# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkSocialMetaTagParameters

    class DynamicLinkSocialMetaTagParameters : NSObject

The Dynamic Link Social Meta Tag parameters.
- `
  ``
  ``
  `

  ### [title](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(py)title)

  `
  `  
  The title to use when the Dynamic Link is shared in a social post.  

  #### Declaration

  Swift  

      var title: String? { get set }

- `
  ``
  ``
  `

  ### [descriptionText](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(py)descriptionText)

  `
  `  
  The description to use when the Dynamic Link is shared in a social post.  

  #### Declaration

  Swift  

      var descriptionText: String? { get set }

- `
  ``
  ``
  `

  ### [imageURL](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(py)imageURL)

  `
  `  
  The URL to an image related to this link.  

  #### Declaration

  Swift  

      var imageURL: URL? { get set }

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(cm)parameters)

  `
  `  
  A method for creating the Social Meta Tag parameters object.  

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Social Meta Tag
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkSocialMetaTagParameters#/c:objc(cs)FIRDynamicLinkSocialMetaTagParameters(im)init)

  `
  `  
  A method for creating the Social Meta Tag parameters object.  

  #### Declaration

  Swift  

      init()

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Social Meta Tag
  parameters to a generated Dynamic Link URL.
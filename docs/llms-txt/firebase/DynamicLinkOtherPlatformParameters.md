# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkOtherPlatformParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkOtherPlatformParameters

    class DynamicLinkOtherPlatformParameters : NSObject

Options class for defining other platform(s) parameters of the Dynamic Link.
Other here means not covered by specific parameters (not iOS and not Android).
- `
  ``
  ``
  `

  ### [fallbackUrl](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkOtherPlatformParameters#/c:objc(cs)FIRDynamicLinkOtherPlatformParameters(py)fallbackUrl)

  `
  `  
  Property defines fallback URL to navigate to when Dynamic Link is clicked on
  other platform.  

  #### Declaration

  Swift  

      var fallbackUrl: URL? { get set }

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkOtherPlatformParameters#/c:objc(cs)FIRDynamicLinkOtherPlatformParameters(cm)parameters)

  `
  `  
  A method for creating the Other platform parameters object.  

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Other Platform
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkOtherPlatformParameters#/c:objc(cs)FIRDynamicLinkOtherPlatformParameters(im)init)

  `
  `  
  A method for creating the Other platform parameters object.  

  #### Declaration

  Swift  

      init()

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Other Platform
  parameters to a generated Dynamic Link URL.
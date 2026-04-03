# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkGoogleAnalyticsParameters

    class DynamicLinkGoogleAnalyticsParameters : NSObject

The Dynamic Link analytics parameters.
- `
  ``
  ``
  `

  ### [source](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)source)

  `
  `  
  The utm_source analytics parameter.  

  #### Declaration

  Swift  

      var source: String? { get set }

- `
  ``
  ``
  `

  ### [medium](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)medium)

  `
  `  
  The utm_medium analytics parameter.  

  #### Declaration

  Swift  

      var medium: String? { get set }

- `
  ``
  ``
  `

  ### [campaign](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)campaign)

  `
  `  
  The utm_campaign analytics parameter.  

  #### Declaration

  Swift  

      var campaign: String? { get set }

- `
  ``
  ``
  `

  ### [term](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)term)

  `
  `  
  The utm_term analytics parameter.  

  #### Declaration

  Swift  

      var term: String? { get set }

- `
  ``
  ``
  `

  ### [content](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(py)content)

  `
  `  
  The utm_content analytics parameter.  

  #### Declaration

  Swift  

      var content: String? { get set }

- `
  ``
  ``
  `

  ### [+parametersWithSource:medium:campaign:](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(cm)parametersWithSource:medium:campaign:)

  `
  `  
  The preferred factory method for creating the analytics parameters object. It includes
  the commonly-used source, medium, and campaign fields.  

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

  ### [+parameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(cm)parameters)

  `
  `  
  A factory method for creating the analytics parameters object.  

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add analytics parameters
  to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [init(source:medium:campaign:)](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(im)initWithSource:medium:campaign:)

  `
  `  
  The preferred instance method for creating the analytics parameters object. It
  includes the commonly-used source, medium, and campaign fields.  

  #### Declaration

  Swift  

      init(source: String, medium: String, campaign: String)

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

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkGoogleAnalyticsParameters#/c:objc(cs)FIRDynamicLinkGoogleAnalyticsParameters(im)init)

  `
  `  

  #### Declaration

  Swift  

      init()

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add analytics parameters
  to a generated Dynamic Link URL.
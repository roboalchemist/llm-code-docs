# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkComponentsOptions

    class DynamicLinkComponentsOptions : NSObject

Options class for defining how Dynamic Link URLs are generated.
- `
  ``
  ``
  `

  ### [pathLength](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions#/c:objc(cs)FIRDynamicLinkComponentsOptions(py)pathLength)

  `
  `  
  Specifies the length of the path component of a short Dynamic Link.  

  #### Declaration

  Swift  

      var pathLength: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/ShortDynamicLinkPathLength.html { get set }

- `
  ``
  ``
  `

  ### [+options](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions#/c:objc(cs)FIRDynamicLinkComponentsOptions(cm)options)

  `
  `  
  A method for creating the Dynamic Link components options object.  

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to specify options related
  to the generation of Dynamic Link URLs.
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkComponentsOptions#/c:objc(cs)FIRDynamicLinkComponentsOptions(im)init)

  `
  `  
  A method for creating the Dynamic Link components options object.  

  #### Declaration

  Swift  

      init()

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to specify options related
  to the generation of Dynamic Link URLs.
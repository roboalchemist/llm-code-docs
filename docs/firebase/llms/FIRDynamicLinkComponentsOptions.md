# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDynamicLinkComponentsOptions


    @interface FIRDynamicLinkComponentsOptions : NSObject

Options class for defining how Dynamic Link URLs are generated.
- `
  ``
  ``
  `

  ### [pathLength](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions#/c:objc(cs)FIRDynamicLinkComponentsOptions(py)pathLength)

  `
  `  
  Specifies the length of the path component of a short Dynamic Link.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRShortDynamicLinkPathLength.html pathLength;

- `
  ``
  ``
  `

  ### [+options](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions#/c:objc(cs)FIRDynamicLinkComponentsOptions(cm)options)

  `
  `  
  A method for creating the Dynamic Link components options object.  

  #### Declaration

  Objective-C  

      + (nonnull instancetype)options;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to specify options related
  to the generation of Dynamic Link URLs.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Classes/FIRDynamicLinkComponentsOptions#/c:objc(cs)FIRDynamicLinkComponentsOptions(im)init)

  `
  `  
  A method for creating the Dynamic Link components options object.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to specify options related
  to the generation of Dynamic Link URLs.
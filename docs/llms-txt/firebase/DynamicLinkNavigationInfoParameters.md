# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkNavigationInfoParameters.md.txt

# FirebaseDynamicLinks Framework Reference

# DynamicLinkNavigationInfoParameters

    class DynamicLinkNavigationInfoParameters : NSObject

Options class for defining navigation behavior of the Dynamic Link.
- `
  ``
  ``
  `

  ### [isForcedRedirectEnabled](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkNavigationInfoParameters#/c:objc(cs)FIRDynamicLinkNavigationInfoParameters(py)forcedRedirectEnabled)

  `
  `  
  Property defines should forced non-interactive redirect be used when link is tapped on
  mobile device. Default behavior is to disable force redirect and show interstitial page where
  user tap will initiate navigation to the App (or AppStore if not installed). Disabled force
  redirect normally improves reliability of the click.  

  #### Declaration

  Swift  

      var isForcedRedirectEnabled: Bool { get set }

- `
  ``
  ``
  `

  ### [+parameters](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkNavigationInfoParameters#/c:objc(cs)FIRDynamicLinkNavigationInfoParameters(cm)parameters)

  `
  `  
  A method for creating the Navigation Info parameters object.  

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Navigation Info
  parameters to a generated Dynamic Link URL.
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Classes/DynamicLinkNavigationInfoParameters#/c:objc(cs)FIRDynamicLinkNavigationInfoParameters(im)init)

  `
  `  
  A method for creating the Navigation Info parameters object.  

  #### Declaration

  Swift  

      init()

  #### Return Value

  Returns an object to be used with FIRDynamicLinkURLComponents to add Navigation Info
  parameters to a generated Dynamic Link URL.
# Source: https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRDLMatchType.md.txt

# FirebaseDynamicLinks Framework Reference

# FIRDLMatchType

    enum FIRDLMatchType : NSUInteger {}

The match type of the Dynamic Link.
- `
  ``
  ``
  `

  ### [FIRDLMatchTypeNone](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRDLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeNone)

  `
  `  
  The match has not been achieved.  

  #### Declaration

  Objective-C  

      FIRDLMatchTypeNone

- `
  ``
  ``
  `

  ### [FIRDLMatchTypeWeak](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRDLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeWeak)

  `
  `  
  The match between the Dynamic Link and this device may not be perfect, hence you should not
  reveal any personal information related to the Dynamic Link.  

  #### Declaration

  Objective-C  

      FIRDLMatchTypeWeak

- `
  ``
  ``
  `

  ### [FIRDLMatchTypeDefault](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRDLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeDefault)

  `
  `  
  The match between the Dynamic Link and this device has high confidence but small possibility of
  error still exist.  

  #### Declaration

  Objective-C  

      FIRDLMatchTypeDefault

- `
  ``
  ``
  `

  ### [FIRDLMatchTypeUnique](https://firebase.google.com/docs/reference/ios/firebasedynamiclinks/api/reference/Enums/FIRDLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeUnique)

  `
  `  
  The match between the Dynamic Link and this device is exact, hence you may reveal personal
  information related to the Dynamic Link.  

  #### Declaration

  Objective-C  

      FIRDLMatchTypeUnique
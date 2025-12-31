# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/DLMatchType.md.txt

# FirebaseDynamicLinks Framework Reference

# DLMatchType

    enum DLMatchType : UInt, @unchecked Sendable

The match type of the Dynamic Link.
- `
  ``
  ``
  `

  ### [none](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/DLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeNone)

  `
  `  
  The match has not been achieved.  

  #### Declaration

  Swift  

      case none = 0

- `
  ``
  ``
  `

  ### [weak](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/DLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeWeak)

  `
  `  
  The match between the Dynamic Link and this device may not be perfect, hence you should not
  reveal any personal information related to the Dynamic Link.  

  #### Declaration

  Swift  

      case weak = 1

- `
  ``
  ``
  `

  ### [default](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/DLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeDefault)

  `
  `  
  The match between the Dynamic Link and this device has high confidence but small possibility of
  error still exist.  

  #### Declaration

  Swift  

      case `default` = 2

- `
  ``
  ``
  `

  ### [unique](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/DLMatchType#/c:@E@FIRDLMatchType@FIRDLMatchTypeUnique)

  `
  `  
  The match between the Dynamic Link and this device is exact, hence you may reveal personal
  information related to the Dynamic Link.  

  #### Declaration

  Swift  

      case unique = 3
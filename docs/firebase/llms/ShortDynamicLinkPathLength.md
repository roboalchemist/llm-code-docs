# Source: https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/ShortDynamicLinkPathLength.md.txt

# FirebaseDynamicLinks Framework Reference

# ShortDynamicLinkPathLength

    enum ShortDynamicLinkPathLength : Int, @unchecked Sendable

Enum used to define the desired path length for shortened Dynamic Link URLs.
- `
  ``
  ``
  `

  ### [default](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/ShortDynamicLinkPathLength#/c:@E@FIRShortDynamicLinkPathLength@FIRShortDynamicLinkPathLengthDefault)

  `
  `  
  Uses the server-default for the path length. See <https://goo.gl/8yDAqC> for more information.  

  #### Declaration

  Swift  

      case `default` = 0

- `
  ``
  ``
  `

  ### [short](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/ShortDynamicLinkPathLength#/c:@E@FIRShortDynamicLinkPathLength@FIRShortDynamicLinkPathLengthShort)

  `
  `  
  Typical short link for non-sensitive links.  

  #### Declaration

  Swift  

      case short = 1

- `
  ``
  ``
  `

  ### [unguessable](https://firebase.google.com/docs/reference/swift/firebasedynamiclinks/api/reference/Enums/ShortDynamicLinkPathLength#/c:@E@FIRShortDynamicLinkPathLength@FIRShortDynamicLinkPathLengthUnguessable)

  `
  `  
  Short link with an extra long path for great difficulty in guessing.  

  #### Declaration

  Swift  

      case unguessable = 2
# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthAPNSTokenType.md.txt

# FirebaseAuth Framework Reference

# AuthAPNSTokenType

    @objc(FIRAuthAPNSTokenType)
    public enum AuthAPNSTokenType : Int, Sendable

The APNs token type for the app.

This enum is available on iOS, macOS Catalyst, tvOS, and watchOS only.
- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthAPNSTokenType#/c:@M@FirebaseAuth@E@FIRAuthAPNSTokenType@FIRAuthAPNSTokenTypeUnknown)

  `
  `  
  Unknown token type.

  The actual token type will be detected from the provisioning profile in the app's bundle.  

  #### Declaration

  Swift  

      case unknown

- `
  ``
  ``
  `

  ### [sandbox](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthAPNSTokenType#/c:@M@FirebaseAuth@E@FIRAuthAPNSTokenType@FIRAuthAPNSTokenTypeSandbox)

  `
  `  
  Sandbox token type.  

  #### Declaration

  Swift  

      case sandbox

- `
  ``
  ``
  `

  ### [prod](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Enums/AuthAPNSTokenType#/c:@M@FirebaseAuth@E@FIRAuthAPNSTokenType@FIRAuthAPNSTokenTypeProd)

  `
  `  
  Production token type.  

  #### Declaration

  Swift  

      case prod
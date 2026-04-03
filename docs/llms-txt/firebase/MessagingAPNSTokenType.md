# Source: https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingAPNSTokenType.md.txt

# FirebaseMessaging Framework Reference

# MessagingAPNSTokenType

    enum MessagingAPNSTokenType : Int, @unchecked Sendable

The APNs token type for the app. If the token type is set to `UNKNOWN`
Firebase Messaging will implicitly try to figure out what the actual token type
is from the provisioning profile.
Unless you really need to specify the type, you should use the `APNSToken`
property instead.
- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingAPNSTokenType#/c:@E@FIRMessagingAPNSTokenType@FIRMessagingAPNSTokenTypeUnknown)

  `
  `  
  Unknown token type.  

  #### Declaration

  Swift  

      case unknown = 0

- `
  ``
  ``
  `

  ### [sandbox](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingAPNSTokenType#/c:@E@FIRMessagingAPNSTokenType@FIRMessagingAPNSTokenTypeSandbox)

  `
  `  
  Sandbox token type.  

  #### Declaration

  Swift  

      case sandbox = 1

- `
  ``
  ``
  `

  ### [prod](https://firebase.google.com/docs/reference/swift/firebasemessaging/api/reference/Enums/MessagingAPNSTokenType#/c:@E@FIRMessagingAPNSTokenType@FIRMessagingAPNSTokenTypeProd)

  `
  `  
  Production token type.  

  #### Declaration

  Swift  

      case prod = 2
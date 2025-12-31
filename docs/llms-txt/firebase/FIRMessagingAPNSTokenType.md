# Source: https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingAPNSTokenType.md.txt

# FirebaseMessaging Framework Reference

# FIRMessagingAPNSTokenType

    enum FIRMessagingAPNSTokenType : NSInteger {}

The APNs token type for the app. If the token type is set to `UNKNOWN`
Firebase Messaging will implicitly try to figure out what the actual token type
is from the provisioning profile.
Unless you really need to specify the type, you should use the `APNSToken`
property instead.
- `
  ``
  ``
  `

  ### [FIRMessagingAPNSTokenTypeUnknown](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingAPNSTokenType#/c:@E@FIRMessagingAPNSTokenType@FIRMessagingAPNSTokenTypeUnknown)

  `
  `  
  Unknown token type.  

  #### Declaration

  Objective-C  

      FIRMessagingAPNSTokenTypeUnknown

- `
  ``
  ``
  `

  ### [FIRMessagingAPNSTokenTypeSandbox](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingAPNSTokenType#/c:@E@FIRMessagingAPNSTokenType@FIRMessagingAPNSTokenTypeSandbox)

  `
  `  
  Sandbox token type.  

  #### Declaration

  Objective-C  

      FIRMessagingAPNSTokenTypeSandbox

- `
  ``
  ``
  `

  ### [FIRMessagingAPNSTokenTypeProd](https://firebase.google.com/docs/reference/ios/firebasemessaging/api/reference/Enums/FIRMessagingAPNSTokenType#/c:@E@FIRMessagingAPNSTokenType@FIRMessagingAPNSTokenTypeProd)

  `
  `  
  Production token type.  

  #### Declaration

  Objective-C  

      FIRMessagingAPNSTokenTypeProd
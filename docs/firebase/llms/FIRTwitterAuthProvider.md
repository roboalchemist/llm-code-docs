# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTwitterAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRTwitterAuthProvider


    @interface FIRTwitterAuthProvider : NSObject

Utility class for constructing Twitter credentials.
- `
  ``
  ``
  `

  ### [+credentialWithToken:secret:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTwitterAuthProvider#/c:objc(cs)FIRTwitterAuthProvider(cm)credentialWithToken:secret:)

  `
  `  
  Creates an `AuthCredential` for a Twitter sign in.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credentialWithToken:(nonnull NSString *)token
                                                  secret:(nonnull NSString *)secret;

  #### Parameters

  |----------------|---------------------------|
  | ` `*token*` `  | The Twitter OAuth token.  |
  | ` `*secret*` ` | The Twitter OAuth secret. |

  #### Return Value

  An AuthCredential containing the Twitter credential.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRTwitterAuthProvider#/c:objc(cs)FIRTwitterAuthProvider(im)init)

  `
  `  
  This class is not meant to be initialized.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
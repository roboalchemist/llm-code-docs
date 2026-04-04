# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGoogleAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRGoogleAuthProvider


    @interface FIRGoogleAuthProvider : NSObject

Utility class for constructing Google Sign In credentials.
- `
  ``
  ``
  `

  ### [+credentialWithIDToken:accessToken:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGoogleAuthProvider#/c:objc(cs)FIRGoogleAuthProvider(cm)credentialWithIDToken:accessToken:)

  `
  `  
  Creates an `AuthCredential` for a Google sign in.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credentialWithIDToken:(nonnull NSString *)IDToken
                                               accessToken:
                                                   (nonnull NSString *)accessToken;

  #### Parameters

  |---------------------|-------------------------------|
  | ` `*IDToken*` `     | The ID Token from Google.     |
  | ` `*accessToken*` ` | The Access Token from Google. |

  #### Return Value

  An AuthCredential containing the Google credentials.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGoogleAuthProvider#/c:objc(cs)FIRGoogleAuthProvider(im)init)

  `
  `  
  This class should not be initialized.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRFacebookAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRFacebookAuthProvider


    @interface FIRFacebookAuthProvider : NSObject

Utility class for constructing Facebook credentials.
- `
  ``
  ``
  `

  ### [+credentialWithAccessToken:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRFacebookAuthProvider#/c:objc(cs)FIRFacebookAuthProvider(cm)credentialWithAccessToken:)

  `
  `  
  Creates an `AuthCredential` for a Facebook sign in.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credentialWithAccessToken:
          (nonnull NSString *)accessToken;

  #### Parameters

  |---------------------|---------------------------------|
  | ` `*accessToken*` ` | The access token from Facebook. |

  #### Return Value

  An `AuthCredential` containing the Facebook credentials.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRFacebookAuthProvider#/c:objc(cs)FIRFacebookAuthProvider(im)init)

  `
  `  
  This class should not be initialized.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
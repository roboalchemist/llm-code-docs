# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGitHubAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRGitHubAuthProvider


    @interface FIRGitHubAuthProvider : NSObject

Utility class for constructing GitHub credentials.
- `
  ``
  ``
  `

  ### [+credentialWithToken:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGitHubAuthProvider#/c:objc(cs)FIRGitHubAuthProvider(cm)credentialWithToken:)

  `
  `  
  Creates an `AuthCredential` for a GitHub sign in.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credentialWithToken:(nonnull NSString *)token;

  #### Parameters

  |---------------|--------------------------------|
  | ` `*token*` ` | The GitHub OAuth access token. |

  #### Return Value

  An AuthCredential containing the GitHub credential.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGitHubAuthProvider#/c:objc(cs)FIRGitHubAuthProvider(im)init)

  `
  `  
  This class is not meant to be initialized.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
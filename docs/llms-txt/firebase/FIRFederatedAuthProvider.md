# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRFederatedAuthProvider

    @protocol FIRFederatedAuthProvider <NSObject>

Utility type for constructing federated auth provider credentials.
- `
  ``
  ``
  `

  ### [-getCredentialWithUIDelegate:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRFederatedAuthProvider#/c:objc(pl)FIRFederatedAuthProvider(im)getCredentialWithUIDelegate:completion:)

  `
  `  
  Used to obtain an auth credential via a mobile web flow.
  This method is available on iOS only.  

  #### Declaration

  Objective-C  

      - (void)getCredentialWithUIDelegate:(nullable id<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Protocols/FIRAuthUIDelegate.html>)UIDelegate
                               completion:
                                   (nullable void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *_Nullable,
                                                      NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------|
  | ` `*UIDelegate*` ` | An optional UI delegate used to present the mobile web flow.                                                  |
  | ` `*completion*` ` | Optionally; a block which is invoked asynchronously on the main thread when the mobile web flow is completed. |
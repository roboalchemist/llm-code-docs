# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGameCenterAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIRGameCenterAuthProvider


    @interface FIRGameCenterAuthProvider : NSObject

A concrete implementation of `AuthProvider` for Game Center Sign In. Not available on
watchOS.
- `
  ``
  ``
  `

  ### [+getCredentialWithCompletion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGameCenterAuthProvider#/c:objc(cs)FIRGameCenterAuthProvider(cm)getCredentialWithCompletion:)

  `
  `  
  Creates an `AuthCredential` for a Game Center sign in.  

  #### Declaration

  Objective-C  

      + (void)getCredentialWithCompletion:
          (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *_Nullable,
                            NSError *_Nullable))completion;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRGameCenterAuthProvider#/c:objc(cs)FIRGameCenterAuthProvider(im)init)

  `
  `  
  This class is not meant to be initialized.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
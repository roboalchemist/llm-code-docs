# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorResolver.md.txt

# FirebaseAuth Framework Reference

# FIRMultiFactorResolver


    @interface FIRMultiFactorResolver : NSObject

The data structure used to help developers resolve 2nd factor requirements on users that
have opted in to 2 factor authentication.
This class is available on iOS only.
- `
  ``
  ``
  `

  ### [session](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorResolver#/c:objc(cs)FIRMultiFactorResolver(py)session)

  `
  `  
  The opaque session identifier for the current sign-in flow.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes.html#/c:objc(cs)FIRMultiFactorSession *_Nonnull session;

- `
  ``
  ``
  `

  ### [hints](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorResolver#/c:objc(cs)FIRMultiFactorResolver(py)hints)

  `
  `  
  The list of hints for the second factors needed to complete the sign-in for the current
  session.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NS_SWIFT_NAME(hints) NSArray<https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorInfo.html *> *hints;

- `
  ``
  ``
  `

  ### [auth](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorResolver#/c:objc(cs)FIRMultiFactorResolver(py)auth)

  `
  `  
  The Auth reference for the current FIRMultiResolver.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuth.html *_Nonnull auth;

- `
  ``
  ``
  `

  ### [-resolveSignInWithAssertion:completion:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorResolver#/c:objc(cs)FIRMultiFactorResolver(im)resolveSignInWithAssertion:completion:)

  `
  `  
  A helper function to help users complete sign in with a second factor using an
  FIRMultiFactorAssertion confirming the user successfully completed the second factor
  challenge.  

  #### Declaration

  Objective-C  

      - (void)resolveSignInWithAssertion:(nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRMultiFactorAssertion.html *)assertion
                              completion:
                                  (nullable https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Type-Definitions.html#/c:FIRAuth.h@T@FIRAuthDataResultCallback)completion;

  #### Parameters

  |--------------------|-----------------------------------------------------------|
  | ` `*completion*` ` | The block invoked when the request is complete, or fails. |
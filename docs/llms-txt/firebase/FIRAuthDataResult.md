# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult.md.txt

# FirebaseAuth Framework Reference

# FIRAuthDataResult


    @interface FIRAuthDataResult : NSObject

Helper object that contains the result of a successful sign-in, link and reauthenticate
action. It contains references to a `User` instance and a `AdditionalUserInfo` instance.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult#/c:objc(cs)FIRAuthDataResult(im)init)

  `
  `  
  This class should not be initialized manually. `AuthDataResult` instance is
  returned as part of `AuthDataResultCallback`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [user](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult#/c:objc(cs)FIRAuthDataResult(py)user)

  `
  `  
  The signed in user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRUser.html *_Nonnull user;

- `
  ``
  ``
  `

  ### [additionalUserInfo](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult#/c:objc(cs)FIRAuthDataResult(py)additionalUserInfo)

  `
  `  
  If available contains the additional IdP specific information about signed in user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAdditionalUserInfo.html *additionalUserInfo;

- `
  ``
  ``
  `

  ### [credential](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthDataResult#/c:objc(cs)FIRAuthDataResult(py)credential)

  `
  `  
  This property will be non-nil after a successful headful-lite sign-in via
  `signIn(with:uiDelegate:completion:)`. May be used to obtain the accessToken and/or IDToken
  pertaining to a recently signed-in user.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *credential;
# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential.md.txt

# FirebaseAuth Framework Reference

# FIROAuthCredential


    @interface FIROAuthCredential : https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html <NSSecureCoding>

Internal implementation of FIRAuthCredential for generic credentials.
- `
  ``
  ``
  `

  ### [IDToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential#/c:objc(cs)FIROAuthCredential(py)IDToken)

  `
  `  
  The ID Token associated with this credential.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *IDToken;

- `
  ``
  ``
  `

  ### [accessToken](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential#/c:objc(cs)FIROAuthCredential(py)accessToken)

  `
  `  
  The access token associated with this credential.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *accessToken;

- `
  ``
  ``
  `

  ### [secret](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential#/c:objc(cs)FIROAuthCredential(py)secret)

  `
  `  
  The secret associated with this credential. This will be nil for OAuth 2.0 providers.
  @detail OAuthCredential already exposes a providerId getter. This will help the developer
  determine whether an access token/secret pair is needed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *secret;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIROAuthCredential#/c:objc(cs)FIROAuthCredential(im)init)

  `
  `  
  This class is not supposed to be instantiated directly.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
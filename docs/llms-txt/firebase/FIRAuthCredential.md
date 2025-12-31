# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.md.txt

# FirebaseAuth Framework Reference

# FIRAuthCredential


    @interface FIRAuthCredential : NSObject

Represents a credential.
- `
  ``
  ``
  `

  ### [provider](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential#/c:objc(cs)FIRAuthCredential(py)provider)

  `
  `  
  Gets the name of the identity provider for the credential.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull provider;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential#/c:objc(cs)FIRAuthCredential(im)init)

  `
  `  
  This is an abstract base class. Concrete instances should be created via factory
  methods available in the various authentication provider libraries (like the Facebook
  provider or the Google provider libraries.)  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;
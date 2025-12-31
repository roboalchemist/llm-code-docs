# Source: https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIREmailAuthProvider.md.txt

# FirebaseAuth Framework Reference

# FIREmailAuthProvider


    @interface FIREmailAuthProvider : NSObject

A concrete implementation of `AuthProvider` for Email \& Password Sign In.
- `
  ``
  ``
  `

  ### [+credentialWithEmail:password:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIREmailAuthProvider#/c:objc(cs)FIREmailAuthProvider(cm)credentialWithEmail:password:)

  `
  `  
  Creates an `AuthCredential` for an email \& password sign in.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credentialWithEmail:(nonnull NSString *)email
                                                password:(nonnull NSString *)password;

  #### Parameters

  |------------------|---------------------------|
  | ` `*email*` `    | The user's email address. |
  | ` `*password*` ` | The user's password.      |

  #### Return Value

  An `AuthCredential` containing the email \& password credential.
- `
  ``
  ``
  `

  ### [+credentialWithEmail:link:](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIREmailAuthProvider#/c:objc(cs)FIREmailAuthProvider(cm)credentialWithEmail:link:)

  `
  `  
  Creates an `AuthCredential` for an email \& link sign in.  

  #### Declaration

  Objective-C  

      + (nonnull https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIRAuthCredential.html *)credentialWithEmail:(nonnull NSString *)email
                                                    link:(nonnull NSString *)link;

  #### Parameters

  |---------------|---------------------------|
  | ` `*email*` ` | The user's email address. |
  | ` `*link*` `  | The email sign-in link.   |

  #### Return Value

  An `AuthCredential` containing the email \& link credential.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseauth/api/reference/Classes/FIREmailAuthProvider#/c:objc(cs)FIREmailAuthProvider(im)init)

  `
  `  
  This class is not meant to be initialized directly.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;